
import csv
from pathlib import Path

# Locate project directories
project_dir = Path(__file__).resolve().parents[1]
data_dir = project_dir / "data"
report_dir = project_dir / "reports"

access_file = data_dir / "employee_access.csv"
decisions_file = data_dir / "access_review_decisions.csv"
report_file = report_dir / "consolidated_iam_audit_report.csv"

# Permissions requiring additional scrutiny
privileged_permissions = {
    "Azure Contributor",
    "AWS Administrator"
}

# Load employee access records
with access_file.open("r", newline="", encoding="utf-8-sig") as file:
    access_records = list(csv.DictReader(file))

# Load analyst review decisions
with decisions_file.open("r", newline="", encoding="utf-8-sig") as file:
    decision_records = list(csv.DictReader(file))

# Match decisions to access records
decision_lookup = {
    (
        record["user_id"],
        record["resource"],
        record["assigned_permission"]
    ): record
    for record in decision_records
}

audit_results = []

for record in access_records:
    assigned = record["assigned_permission"].strip()
    required = record["required_permission"].strip()

    if assigned != required:
        status = "REVIEW_REQUIRED"
        reason = "Assigned permission does not match the stated business requirement."

    elif assigned in privileged_permissions:
        status = "PRIVILEGED_ACCESS_REVIEW"
        reason = "Privileged permission requires additional approval and scope validation."

    else:
        status = "MATCH"
        reason = "Assigned permission matches the stated business requirement."

    key = (
        record["user_id"],
        record["resource"],
        assigned
    )

    decision = decision_lookup.get(key, {})

    audit_results.append({
        "user_id": record["user_id"],
        "employee_name": record["employee_name"],
        "job_role": record["job_role"],
        "resource": record["resource"],
        "assigned_permission": assigned,
        "required_permission": required,
        "access_scope": record["access_scope"],
        "review_status": status,
        "review_reason": reason,
        "analyst_decision": decision.get(
            "analyst_decision", "PENDING_REVIEW"
        ),
        "justification": decision.get("justification", "Not yet documented"),
        "next_action": decision.get("next_action", "Analyst review required")
    })

# Create consolidated audit report
report_dir.mkdir(parents=True, exist_ok=True)

with report_file.open("w", newline="", encoding="utf-8") as file:
    fieldnames = audit_results[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(audit_results)

# Display summary
print("CONSOLIDATED IAM AUDIT REPORT")
print("=" * 40)

print(f"Total permission records: {len(audit_results)}")

for status in [
    "MATCH",
    "REVIEW_REQUIRED",
    "PRIVILEGED_ACCESS_REVIEW"
]:
    count = sum(
        record["review_status"] == status
        for record in audit_results
    )
    print(f"{status}: {count}")

print("\nANALYST DECISION SUMMARY")

for decision in [
    "REVOKE_PENDING_APPROVAL",
    "RETAIN_PENDING_VALIDATION",
    "PENDING_REVIEW"
]:
    count = sum(
        record["analyst_decision"] == decision
        for record in audit_results
    )
    print(f"{decision}: {count}")

print(f"\nReport saved to: {report_file}")

print("\nNote: This is a simulated IAM exercise.")
print("No permissions were actually changed or revoked.")
