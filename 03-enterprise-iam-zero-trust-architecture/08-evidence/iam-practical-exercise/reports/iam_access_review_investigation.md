# IAM Access Review – Practical Investigation Report

## 1. Project Overview

This practical exercise demonstrates an Identity and Access Management (IAM) access review process for a fictional organization.

The objective was to evaluate employee permissions against their stated job requirements, identify potentially excessive or privileged access, document analyst review decisions, and generate an audit report.

The exercise uses simulated employee access records and a Python-based analysis tool.

## 2. Environment and Tools

- **Programming Language:** Python 3
- **Data Format:** CSV
- **Development Environment:** Visual Studio Code
- **Operating System:** Windows 11
- **Concepts:** IAM, Role-Based Access Control (RBAC), Least Privilege, Privileged Access Management (PAM), Access Governance

## 3. Investigation Methodology

The following activities were performed:

1. Created a simulated employee access dataset containing five fictional employees and ten permission assignments.
2. Compared assigned permissions against stated business requirements.
3. Identified permission mismatches requiring investigation.
4. Flagged privileged permissions for additional approval and scope validation.
5. Documented analyst decisions, justifications, and recommended next actions.
6. Developed a Python script to combine access findings and analyst decisions.
7. Generated a consolidated IAM audit report in CSV format.

## 4. Investigation Results

| Finding | Records |
|---|---:|
| Total permission records analysed | 10 |
| Permissions matching stated requirements | 6 |
| Permissions requiring investigation | 2 |
| Privileged permissions requiring review | 2 |
| Analyst decisions documented | 4 |
| Records awaiting analyst review | 6 |

## 5. Key Findings

### Finding 1 – Potentially Excessive Azure Access

- Employee: Sarah
- Job role: HR Specialist
- Assigned permission: Azure Contributor
- Stated requirement: No Azure Admin Access
- Review status: REVIEW_REQUIRED

**Recommendation:** Validate the assignment with the employee's manager and Azure resource owner. If access is confirmed to be unnecessary, obtain authorization before revocation.

### Finding 2 – Potentially Excessive AWS Access

- Employee: Maria
- Job role: Finance Analyst
- Assigned permission: AWS Administrator
- Stated requirement: No AWS Admin Access
- Review status: REVIEW_REQUIRED

**Recommendation:** Confirm the business requirement and approval history with the manager and AWS account owner. Consider removing unnecessary administrative access following authorization.

### Finding 3 – Privileged AWS Access

- Employee: Alex
- Job role: Cloud Administrator
- Assigned permission: AWS Administrator
- Review status: PRIVILEGED_ACCESS_REVIEW

**Recommendation:** Validate business justification, approval, account scope, and whether a more restrictive permission would be sufficient.

### Finding 4 – Privileged Azure Access

- Employee: Alex
- Job role: Cloud Administrator
- Assigned permission: Azure Contributor
- Review status: PRIVILEGED_ACCESS_REVIEW

**Recommendation:** Validate approval and subscription scope. Review whether the assigned access follows least-privilege principles.

## 6. Analyst Decision Tracking

Four analyst decisions were documented:

- Two potentially excessive permissions were marked REVOKE_PENDING_APPROVAL.
- Two privileged permissions were marked RETAIN_PENDING_VALIDATION.

These decisions are proposed actions within the simulated exercise. No actual access was changed or revoked.

Six remaining records were retained as PENDING_REVIEW because no separate analyst decision had been documented for them.

## 7. Deliverables

The practical exercise produced:

- `employee_access.csv` – Simulated employee permissions.
- `access_review_decisions.csv` – Documented analyst decisions.
- `analyze_access.py` – Python access review and reporting script.
- `access_review_report.csv` – Initial permission analysis.
- `consolidated_iam_audit_report.csv` – Combined findings and analyst decisions.

## 8. Security Principles Demonstrated

- Least Privilege
- Role-Based Access Control (RBAC)
- Privileged Access Review
- Access Governance
- Separation of Duties
- Access Approval and Accountability
- Audit Documentation

## 9. Limitations

This is a simulated learning exercise using fictional employee records.

No live Microsoft Entra ID, Azure subscription, or AWS account was connected. No production permissions were retrieved, modified, or revoked.

The stated business requirements and analyst decisions are simulated. In a real organization, access changes would require validation against authoritative role requirements, approval records, resource ownership, and organizational procedures.

## 10. Conclusion

This exercise demonstrates a structured IAM access review workflow using Python and CSV-based evidence.

It shows how an analyst can identify potential excessive permissions, flag privileged access, document review decisions, and generate an audit-friendly report.

The project provides practical evidence of IAM analysis, access governance, least-privilege assessment, and security documentation skills.