
import csv
from pathlib import Path
from collections import Counter, defaultdict

# Locate project directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "security_alerts.csv"
REPORT_DIR = PROJECT_DIR / "reports"

REPORT_DIR.mkdir(exist_ok=True)

# Store alert information
alerts = []

# Read CSV data
with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        alerts.append(row)

# Analyze alerts
severity_counts = Counter()
event_counts = Counter()
ip_activity = defaultdict(int)

for alert in alerts:
    severity = alert["severity"].strip()
    event_type = alert["event_type"].strip()
    source_ip = alert["source_ip"].strip()
    failed_attempts = int(alert["failed_attempts"])

    severity_counts[severity] += 1
    event_counts[event_type] += 1
    ip_activity[source_ip] += failed_attempts

# Identify suspicious IP addresses
suspicious_ips = {
    ip: attempts
    for ip, attempts in ip_activity.items()
    if attempts >= 20
}

# Generate report
report = []

report.append("# Security Alert Analysis Report\n")
report.append(f"Total alerts analyzed: {len(alerts)}\n")

report.append("\n## Alerts by Severity\n")

for severity, count in severity_counts.items():
    report.append(f"- {severity}: {count}")

report.append("\n## Alerts by Event Type\n")

for event, count in event_counts.items():
    report.append(f"- {event}: {count}")

report.append("\n## Suspicious IP Addresses\n")

if suspicious_ips:
    for ip, attempts in suspicious_ips.items():
        report.append(
            f"- {ip}: {attempts} failed login attempts"
        )
else:
    report.append("No suspicious IP addresses identified.")

report.append(
    "\n## Analyst Summary\n"
    "IP addresses generating 20 or more failed login "
    "attempts have been flagged for further investigation."
)

# Save report
report_file = REPORT_DIR / "alert_analysis_report.md"

report_file.write_text(
    "\n".join(report),
    encoding="utf-8"
)

print("Security alert analysis completed.")
print(f"Total alerts analyzed: {len(alerts)}")
print(f"Suspicious IP addresses: {len(suspicious_ips)}")
print(f"Report saved to: {report_file}")
