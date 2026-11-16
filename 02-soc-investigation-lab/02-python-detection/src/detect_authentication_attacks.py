
import csv
from collections import defaultdict
from pathlib import Path


# Locate the authentication dataset relative to this script.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASET_PATH = PROJECT_ROOT / "01-datasets" / "authentication_logs.csv"


def load_authentication_logs(file_path):
    """Load authentication events from a CSV file."""

    with open(file_path, mode="r", newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))


def detect_repeated_failures(logs, threshold=3):
    """Detect consecutive failed logins from the same user and source IP."""

    events_by_user_ip = defaultdict(list)

    for event in logs:
        key = (event["username"], event["source_ip"])
        events_by_user_ip[key].append(event)

    findings = []

    for (username, source_ip), events in events_by_user_ip.items():

        events.sort(key=lambda event: event["timestamp"])

        failure_streak = []

        for event in events:
            status = event["authentication_status"].strip().upper()

            if status == "FAILED":
                failure_streak.append(event)

            else:
                if len(failure_streak) >= threshold:
                    findings.append({
                        "detection": "Repeated Consecutive Failed Logins",
                        "username": username,
                        "source_ip": source_ip,
                        "failed_attempts": len(failure_streak),
                        "first_seen": failure_streak[0]["timestamp"],
                        "last_seen": failure_streak[-1]["timestamp"],
                        "severity": "HIGH"
                    })

                failure_streak = []

        # Check for consecutive failures at the end of the sequence.
        if len(failure_streak) >= threshold:
            findings.append({
                "detection": "Repeated Consecutive Failed Logins",
                "username": username,
                "source_ip": source_ip,
                "failed_attempts": len(failure_streak),
                "first_seen": failure_streak[0]["timestamp"],
                "last_seen": failure_streak[-1]["timestamp"],
                "severity": "HIGH"
            })

    return findings


def detect_success_after_failures(logs, threshold=3):
    """Detect successful logins following repeated failed attempts."""

    events_by_user_ip = defaultdict(list)

    for event in logs:
        key = (event["username"], event["source_ip"])
        events_by_user_ip[key].append(event)

    findings = []

    for (username, source_ip), events in events_by_user_ip.items():

        events.sort(key=lambda event: event["timestamp"])

        consecutive_failures = 0

        for event in events:
            status = event["authentication_status"].strip().upper()

            if status == "FAILED":
                consecutive_failures += 1

            elif status == "SUCCESS":

                if consecutive_failures >= threshold:
                    findings.append({
                        "detection": "Successful Login After Repeated Failures",
                        "username": username,
                        "source_ip": source_ip,
                        "failed_attempts_before_success": consecutive_failures,
                        "success_time": event["timestamp"],
                        "severity": "CRITICAL"
                    })

                consecutive_failures = 0

    return findings


def detect_privileged_account_activity(logs):
    """Detect failed authentication attempts involving privileged accounts."""

    privileged_accounts = {"admin", "administrator"}

    findings = []

    for event in logs:

        username = event["username"].strip().lower()
        status = event["authentication_status"].strip().upper()

        if username in privileged_accounts and status == "FAILED":

            findings.append({
                "detection": "Failed Privileged Account Login",
                "username": event["username"],
                "source_ip": event["source_ip"],
                "timestamp": event["timestamp"],
                "severity": "HIGH"
            })

    return findings


def main():

    logs = load_authentication_logs(DATASET_PATH)

    repeated_failures = detect_repeated_failures(logs)
    successful_after_failures = detect_success_after_failures(logs)
    privileged_activity = detect_privileged_account_activity(logs)

    print("=" * 65)
    print("SOC AUTHENTICATION SECURITY DETECTION REPORT")
    print("=" * 65)

    print(f"\nTotal authentication events analyzed: {len(logs)}")

    print("\n[1] REPEATED CONSECUTIVE FAILED LOGIN DETECTIONS")

    for finding in repeated_failures:
        print(finding)

    print("\n[2] SUCCESSFUL LOGIN AFTER REPEATED FAILURES")

    for finding in successful_after_failures:
        print(finding)

    print("\n[3] FAILED PRIVILEGED ACCOUNT LOGINS")

    for finding in privileged_activity:
        print(finding)

    print("\n" + "=" * 65)
    print("DETECTION ANALYSIS COMPLETED")
    print("=" * 65)


if __name__ == "__main__":
    main()
