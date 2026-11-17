# NorthStar Technologies – IAM Roles and Access Control Matrix

## 1. Purpose

This document defines the proposed Identity and Access Management (IAM) role structure for NorthStar Technologies.

The objective is to ensure that employees receive access based on their responsibilities, with permissions restricted according to the principle of least privilege.

## 2. User Roles

The architecture defines five primary user categories.

| Role ID | User Category | Primary Responsibility |
|---|---|---|
| ROLE-01 | Standard Employee | Access business applications and approved resources |
| ROLE-02 | IT Support | Provide approved IT support and account administration |
| ROLE-03 | Cloud Administrator | Manage assigned AWS and Azure resources |
| ROLE-04 | Security Analyst | Monitor security events and investigate alerts |
| ROLE-05 | Senior Management | Access approved management applications and reports |

## 3. Access Control Matrix

Legend:
- **Read:** View permitted information.
- **Manage:** Perform approved administrative actions.
- **Assigned:** Access only to specifically assigned resources.
- **No access:** Access is not granted by default.

| Resource | Employee | IT Support | Cloud Admin | Security Analyst | Management |
|---|---|---|---|---|---|
| Business applications | Assigned | Support access | Assigned | Assigned | Assigned |
| Employee directory | Limited | Manage | No access by default | Read | Limited |
| AWS resources | No access by default | No access by default | Manage assigned accounts | Read assigned security data | No access by default |
| Azure resources | No access by default | Limited support | Manage assigned resources | Read assigned security data | No access by default |
| Security logs | No access by default | Limited | Assigned | Read and investigate | Summary reports |
| User access requests | Submit | Process assigned requests | Submit | Submit | Submit |
| Privileged administration | No access | Limited and approved | Elevated access | No access by default | No access |

## 4. Role-Based Access Control Design

### Standard Employees
- Access only approved business applications.
- No direct cloud administrative permissions.
- MFA required.
- Access removed when employment ends.

### IT Support
- Access limited to assigned support responsibilities.
- No unrestricted cloud administration.
- Administrative activities logged.
- Elevated permissions require approval.

### Cloud Administrators
- Separate standard and administrative identities.
- Access limited to assigned AWS accounts and Azure scopes.
- Strong MFA required.
- Privileged access granted through approved elevation procedures.
- Administrative activities monitored.

### Security Analysts
- Read access to approved security logs and monitoring tools.
- Permission to investigate and document security incidents.
- No unrestricted production infrastructure administration.
- Response actions require appropriate authorization.

### Senior Management
- Access to approved business applications and security reports.
- No direct cloud administrative privileges.
- Access limited to management responsibilities.

## 5. Privileged Access Management

Privileged accounts present an elevated security risk.

The following controls are proposed:

1. Separate everyday user accounts from administrative accounts.
2. Require MFA for privileged access.
3. Use time-limited elevation where supported.
4. Require approval for sensitive administrative activities.
5. Record privileged access events.
6. Review administrative role assignments regularly.
7. Maintain controlled emergency access accounts.

## 6. Joiner, Mover and Leaver (JML) Process

### Joiner – New Employee
- Create an identity through an approved onboarding process.
- Assign a role based on job responsibilities.
- Grant access to approved applications and resources.
- Enforce MFA.
- Record the access assignment.

### Mover – Employee Changes Role
- Review existing permissions.
- Remove permissions no longer required.
- Assign permissions for the new responsibilities.
- Obtain approval for sensitive access.
- Record changes for auditing.

### Leaver – Employee Leaves
- Disable the employee identity promptly.
- Revoke active sessions and credentials where supported.
- Remove AWS and Azure access assignments.
- Recover organizational devices.
- Retain required audit records according to policy.

## 7. Access Review and Governance

Proposed governance controls:

| Control | Proposed Frequency |
|---|---|
| Privileged access review | Monthly |
| Standard employee access review | Quarterly |
| Cloud role assignment review | Quarterly |
| Inactive account review | Monthly |
| Emergency access review | After every use |
| Joiner/Mover/Leaver verification | At each relevant event |

## 8. Security Recommendations

- Use groups and role assignments instead of unnecessary individual permissions.
- Avoid shared administrator accounts.
- Review inherited and excessive permissions.
- Use dedicated service identities for applications.
- Protect credentials and secrets.
- Maintain an auditable access approval process.

## 9. Design Limitations

This matrix is a conceptual access model for a fictional organization.

Actual permissions must be mapped to platform-specific roles, policies and resource scopes before implementation. Access assignments should be tested and approved by the organization's security and business owners.

## 10. Document Status

Status: Proposed IAM access control design  
Project: Enterprise IAM and Zero Trust Architecture  
Organization: NorthStar Technologies (fictional)