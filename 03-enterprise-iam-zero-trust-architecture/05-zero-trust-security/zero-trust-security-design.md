# Zero Trust Security Design

## 1. Purpose

This document defines a proposed Zero Trust security model for NorthStar Technologies, a fictional organization with approximately 200 employees working remotely and from an office environment.

The design applies Zero Trust principles to workforce identities, devices, applications, cloud resources, and administrative access.

The objective is to ensure that access decisions are based on verified identity, device security, contextual risk, and authorization rather than automatically trusting users because they are inside a corporate network.

## 2. Zero Trust Principles

The proposed architecture follows these principles:

### 2.1 Verify Explicitly
- Authenticate users before granting access.
- Require multifactor authentication (MFA).
- Evaluate sign-in risk and access context.
- Apply additional verification for sensitive applications and administrative activities.

### 2.2 Use Least-Privilege Access
- Grant only the permissions required for a user's responsibilities.
- Separate standard user accounts from administrative accounts.
- Use role-based access control (RBAC).
- Review permissions regularly and remove unnecessary access.

### 2.3 Assume Breach
- Do not automatically trust users, devices, or network locations.
- Monitor authentication and administrative activity.
- Centralize relevant security logs.
- Investigate unusual access patterns.
- Restrict the potential impact of compromised accounts.

## 3. Proposed Zero Trust Access Decision Model

Every access request should be evaluated using the following factors:

| Factor | Security consideration |
|---|---|
| Identity | Is the user's identity verified? |
| Authentication | Has MFA been completed? |
| Device | Is the device managed and compliant? |
| Context | Is the access request consistent with expected activity? |
| Risk | Does the sign-in or activity indicate elevated risk? |
| Authorization | Does the user have permission to access the resource? |
| Session | Should the session continue, require reauthentication, or be revoked? |

Access should be granted only when the applicable requirements are satisfied.

## 4. Proposed Security Controls

### 4.1 Identity Verification
- Use Microsoft Entra ID as the proposed central identity provider.
- Require MFA for workforce accounts.
- Apply stronger authentication requirements to privileged accounts.
- Disable accounts promptly when employees leave the organization.

### 4.2 Device Security
- Prefer organization-managed devices for access to sensitive resources.
- Require device compliance checks where supported.
- Apply operating system and security update requirements.
- Restrict access from devices that fail defined security requirements.

### 4.3 Conditional Access
Proposed access policies include:

| Policy | Proposed control |
|---|---|
| Standard employee access | Require MFA |
| Administrative access | Require MFA and stronger authentication |
| Untrusted device | Block or restrict sensitive access |
| High-risk sign-in | Require additional verification or block access |
| Sensitive cloud resources | Require approved identity and authorized role |
| Inactive or terminated account | Disable access |

Actual policy configuration must be validated against platform capabilities, licensing, and organizational requirements.

### 4.4 Privileged Access
- Maintain separate administrative accounts.
- Avoid using privileged accounts for everyday activities.
- Grant administrative permissions only when required.
- Use time-limited privileged access where supported.
- Record and review privileged activities.

### 4.5 Cloud Access
**Microsoft Azure**
- Use Microsoft Entra ID for identity management.
- Apply Azure RBAC to control resource permissions.
- Use least-privilege role assignments.
- Monitor Azure Activity Logs.

**Amazon Web Services (AWS)**
- Use federated workforce access through AWS IAM Identity Center.
- Assign permission sets based on job responsibilities.
- Avoid unnecessary long-term access keys.
- Monitor activity through AWS CloudTrail.

## 5. Example Zero Trust Scenarios

### Scenario 1: Employee Access from a New Device

**Situation:** An employee attempts to access a company application from an unfamiliar device.

**Proposed response:**
1. Verify the employee's identity.
2. Require MFA.
3. Evaluate device compliance.
4. Apply access restrictions if the device does not meet security requirements.
5. Record the sign-in activity for monitoring.

**Security objective:** Prevent unauthorized access through compromised credentials or unmanaged devices.

### Scenario 2: Cloud Administrator Access

**Situation:** A cloud administrator attempts to modify production resources.

**Proposed response:**
1. Verify the administrator's identity.
2. Require strong MFA.
3. Confirm the administrator has the required role.
4. Grant only the permissions needed for the task.
5. Log the administrative activity.
6. Review unusual or high-impact changes.

**Security objective:** Reduce the risk of privilege misuse and unauthorized cloud changes.

### Scenario 3: Suspicious Sign-in Activity

**Situation:** A user account generates repeated failed sign-in attempts followed by a successful login.

**Proposed response:**
1. Generate an alert for the unusual authentication pattern.
2. Review the source IP address and sign-in history.
3. Assess whether the successful login is legitimate.
4. Require additional verification or restrict access when appropriate.
5. Escalate suspected account compromise for investigation.

**Security objective:** Detect and respond to possible credential attacks.

## 6. Security Monitoring and Logging

The proposed monitoring approach collects relevant identity and cloud activity:

| Source | Example events |
|---|---|
| Microsoft Entra ID | Sign-in and audit events |
| AWS CloudTrail | API and administrative activity |
| Azure Activity Logs | Resource and subscription changes |
| Endpoint security tools | Device and threat alerts |

Microsoft Sentinel is proposed as a centralized SIEM platform for collecting and analyzing relevant security events.

Monitoring should focus on:
- Repeated authentication failures.
- Successful logins following repeated failures.
- Unusual administrative activity.
- Unexpected privilege changes.
- Access from non-compliant devices.
- Suspicious cloud resource modifications.

## 7. Implementation Priorities

1. Establish centralized identity management.
2. Enforce MFA for all workforce accounts.
3. Review existing roles and permissions.
4. Separate standard and privileged accounts.
5. Introduce device compliance requirements.
6. Apply Conditional Access policies.
7. Centralize identity and cloud audit logs.
8. Establish ongoing access reviews and security monitoring.

## 8. Limitations and Assumptions

- NorthStar Technologies is a fictional organization.
- The existing security environment described in this project is hypothetical.
- This document represents a proposed security architecture, not a deployed environment.
- No live Microsoft Entra ID, Azure, or AWS federation has been configured or tested.
- Platform licensing, technical requirements, and integration capabilities require validation before implementation.
- The proposed controls must be tested before production deployment.

## 9. Conclusion

The proposed Zero Trust model reduces reliance on implicit trust and introduces stronger identity verification, device evaluation, least-privilege access, and continuous monitoring.

By applying these controls across workforce identities and cloud environments, NorthStar Technologies can establish a more consistent security model and reduce the potential impact of compromised accounts and unauthorized access.