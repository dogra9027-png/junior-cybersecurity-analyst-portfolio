
import csv
from pathlib import Path
from collections import Counter
from datetime import datetime, timedelta


# --------------------------------------------------
# PROJECT CONFIGURATION
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = PROJECT_DIR / "data" / "security_alerts.csv"
REPORT_DIR = PROJECT_DIR / "reports"

BRUTE_FORCE_THRESHOLD = 20
CORRELATION_WINDOW_MINUTES = 30


# --------------------------------------------------
# DETECTION RULES DET-001, DET-002, DET-003
# --------------------------------------------------

def evaluate_alert(alert):
    """Evaluate one security alert against detection rules."""

    findings = []

    source_ip = alert["source_ip"].strip()
    event_type = alert["event_type"].strip()
    severity = alert["severity"].strip()
    failed_attempts = int(alert["failed_attempts"])

    # DET-001: Possible brute-force activity
    if (
        event_type == "Failed Login"
        and failed_attempts >= BRUTE_FORCE_THRESHOLD
    ):
        findings.append({
            "rule_id": "DET-001",
            "alert_id": alert["alert_id"],
            "source_ip": source_ip,
            "severity": "High",
            "detection": "Possible Brute-Force Activity",
            "evidence": f"{failed_attempts} failed login attempts",
            "action": (
                "Investigate authentication logs, "
                "review account activity, and check for "
                "successful logins following failed attempts."
            )
        })

    # DET-002: Possible port scanning
    if event_type == "Port Scan":
        findings.append({
            "rule_id": "DET-002",
            "alert_id": alert["alert_id"],
            "source_ip": source_ip,
            "severity": "Medium",
            "detection": "Possible Port Scanning",
            "evidence": "Port Scan event detected",
            "action": (
                "Review firewall logs, identify targeted ports, "
                "and investigate the source IP."
            )
        })

    # DET-003: High-severity security alert
    if severity == "High":
        findings.append({
            "rule_id": "DET-003",
            "alert_id": alert["alert_id"],
            "source_ip": source_ip,
            "severity": "High",
            "detection": "High-Severity Security Alert",
            "evidence": "Original alert classified as High",
            "action": (
                "Prioritize investigation and review related "
                "security events."
            )
        })

    return findings


# --------------------------------------------------
# DETECTION RULE DET-004: EVENT CORRELATION
# --------------------------------------------------

def detect_success_after_brute_force(alerts):
    """Detect successful logins following brute-force activity."""

    findings = []

    for failed_alert in alerts:

        if (
            failed_alert["event_type"].strip() != "Failed Login"
            or int(failed_alert["failed_attempts"]) < BRUTE_FORCE_THRESHOLD
        ):
            continue

        source_ip = failed_alert["source_ip"].strip()

        failed_time = datetime.strptime(
            failed_alert["timestamp"],
            "%Y-%m-%d %H:%M:%S"
        )

        for successful_alert in alerts:

            if (
                successful_alert["event_type"].strip() != "Successful Login"
                or successful_alert["source_ip"].strip() != source_ip
            ):
                continue

            successful_time = datetime.strptime(
                successful_alert["timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )

            time_difference = successful_time - failed_time

            if (
                timedelta(0) < time_difference
                <= timedelta(minutes=CORRELATION_WINDOW_MINUTES)
            ):
                findings.append({
                    "rule_id": "DET-004",
                    "alert_id": successful_alert["alert_id"],
                    "source_ip": source_ip,
                    "severity": "Critical",
                    "detection": (
                        "Possible Successful Login Following "
                        "Brute-Force Activity"
                    ),
                    "evidence": (
                        f"{failed_alert['failed_attempts']} failed login attempts "
                        f"followed by a successful login after "
                        f"{int(time_difference.total_seconds() / 60)} minutes"
                    ),
                    "action": (
                        "Investigate the affected account, verify the login, "
                        "review authentication logs, and assess possible "
                        "unauthorized access."
                    )
                })

    return findings


# --------------------------------------------------
# MAIN ANALYSIS AND REPORT GENERATION
# --------------------------------------------------

def main():

    REPORT_DIR.mkdir(exist_ok=True)

    findings = []
    alert_ids = set()
    alerts = []

    # Load alerts and run individual detection rules
    with open(
        DATA_FILE,
        "r",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        for alert in reader:

            alert_ids.add(alert["alert_id"])
            alerts.append(alert)

            findings.extend(evaluate_alert(alert))

    # DET-004: Correlate failed and successful login events
    findings.extend(detect_success_after_brute_force(alerts))

    # Calculate unique alerts that triggered detections
    flagged_alert_ids = {
        finding["alert_id"] for finding in findings
    }

    # Count findings by severity and detection rule
    severity_counts = Counter(
        finding["severity"] for finding in findings
    )

    rule_counts = Counter(
        finding["rule_id"] for finding in findings
    )

    # Build the Markdown report
    report = [
        "# Security Detection Findings",
        "",
        "## Executive Summary",
        "",
        f"- Total unique alerts analyzed: {len(alert_ids)}",
        f"- Total detection rule matches: {len(findings)}",
        f"- Unique alerts requiring investigation: {len(flagged_alert_ids)}",
        "",
        "## Findings by Severity",
        "",
    ]

    for severity in ["Critical", "High", "Medium", "Low"]:
        report.append(
            f"- {severity}: {severity_counts.get(severity, 0)}"
        )

    report.extend([
        "",
        "## Findings by Detection Rule",
        ""
    ])

    rule_names = {
        "DET-001": "Possible Brute-Force Activity",
        "DET-002": "Possible Port Scanning",
        "DET-003": "High-Severity Security Alert",
        "DET-004": (
            "Possible Successful Login Following Brute-Force Activity"
        )
    }

    for rule_id, count in sorted(rule_counts.items()):
        report.append(
            f"- {rule_id} ({rule_names[rule_id]}): {count}"
        )

    report.extend([
        "",
        "## Detection Results",
        ""
    ])

    for finding in findings:

        report.extend([
            f"### {finding['rule_id']} - {finding['detection']}",
            f"- Alert ID: {finding['alert_id']}",
            f"- Source IP: {finding['source_ip']}",
            f"- Severity: {finding['severity']}",
            f"- Evidence: {finding['evidence']}",
            f"- Recommended Action: {finding['action']}",
            ""
        ])

    report.extend([
        "## Analyst Notes",
        "",
        "Multiple detection rules may trigger from the same alert.",
        "Detection rule matches are therefore not equivalent to "
        "unique alerts or confirmed security incidents.",
        "",
        "Findings represent indicators requiring further investigation.",
        "They do not independently confirm malicious activity.",
        "",
        "The recommended actions are initial investigation steps. "
        "Analysts should correlate findings with additional logs "
        "and available security telemetry."
    ])

    # Save Markdown report
    report_file = REPORT_DIR / "detection_findings.md"

    report_file.write_text(
        "\n".join(report),
        encoding="utf-8"
    )

    # Display execution summary
    print("Detection analysis completed.")
    print(f"Unique alerts analyzed: {len(alert_ids)}")
    print(f"Total detection rule matches: {len(findings)}")
    print(
        f"Unique alerts requiring investigation: "
        f"{len(flagged_alert_ids)}"
    )
    print(f"Report saved to: {report_file}")


# --------------------------------------------------
# SCRIPT ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":
    main()
