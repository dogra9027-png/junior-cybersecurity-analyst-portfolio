
import csv
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_ROOT / "01-datasets" / "authentication_logs.csv"


def load_logs():
    with open(DATA_FILE, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def validate_repeated_failures(logs, threshold=3):
    grouped = defaultdict(list)

    for log in logs:
        if log["authentication_status"] == "FAILED":
            key = (log["username"], log["source_ip"])
            grouped[key].append(log)

    print("\n[1] REPEATED FAILED LOGIN VALIDATION")

    for (username, source_ip), events in grouped.items():
        if len(events) >= threshold:
            print(
                f"{username} | {source_ip} | "
                f"{len(events)} failed attempts | HIGH"
            )


def validate_success_after_failures(logs, threshold=3):
    grouped = defaultdict(list)

    for log in logs:
        key = (log["username"], log["source_ip"])
        grouped[key].append(log)

    print("\n[2] SUCCESS AFTER REPEATED FAILURES VALIDATION")

    for (username, source_ip), events in grouped.items():
        events.sort(key=lambda event: event["timestamp"])
        failures = 0

        for event in events:
            if event["authentication_status"] == "FAILED":
                failures += 1

            elif (
                event["authentication_status"] == "SUCCESS"
                and failures >= threshold
            ):
                print(
                    f"{username} | {source_ip} | "
                    f"{event['event_id']} | "
                    f"{failures} failures before success"
                )


def validate_privileged_failures(logs):
    print("\n[3] FAILED PRIVILEGED ACCOUNT VALIDATION")

    for username in ("admin", "administrator"):
        grouped = defaultdict(list)

        for log in logs:
            if (
                log["username"].lower() == username
                and log["authentication_status"] == "FAILED"
            ):
                grouped[log["source_ip"]].append(log)

        for source_ip, events in grouped.items():
            print(
                f"{username} | {source_ip} | "
                f"{len(events)} failures | HIGH"
            )


def validate_privileged_success(logs):
    print("\n[4] SUCCESSFUL PRIVILEGED ACCOUNT VALIDATION")

    for log in logs:
        if (
            log["username"].lower() in ("admin", "administrator")
            and log["authentication_status"] == "SUCCESS"
        ):
            print(
                f"{log['event_id']} | {log['username']} | "
                f"{log['source_ip']} | {log['destination_host']}"
            )


def main():
    logs = load_logs()

    print("=" * 65)
    print("KQL DETECTION LOGIC - LOCAL PYTHON VALIDATION")
    print("=" * 65)
    print(f"Authentication events analyzed: {len(logs)}")

    validate_repeated_failures(logs)
    validate_success_after_failures(logs)
    validate_privileged_failures(logs)
    validate_privileged_success(logs)

    print("\nVALIDATION COMPLETED")
    print("Note: Python validation, not live Microsoft Sentinel execution.")


if __name__ == "__main__":
    main()
