# NorthStar Technologies – Current-State Security Assessment

## 1. Assessment Overview

This assessment examines the assumed identity and access management environment of NorthStar Technologies.

The purpose is to identify potential security weaknesses and establish the requirements for the proposed Enterprise IAM and Zero Trust architecture.

**Important:** This is a hypothetical assessment based on the fictional project scenario. It is not an assessment of a real organization's infrastructure.

## 2. Assumed Current Environment

| Component | Assumed Current State |
|---|---|
| Workforce | Approximately 200 employees |
| Work locations | Office and remote |
| Cloud platforms | AWS and Microsoft Azure |
| Identity management | Separate or inconsistently managed cloud identities |
| Authentication | Basic authentication controls with inconsistent MFA enforcement |
| Access management | Permissions assigned with limited standardization |
| Privileged accounts | Administrative access requires stronger governance |
| Monitoring | Cloud and authentication logs are not centrally reviewed consistently |
| Access reviews | No standardized periodic access certification process |

## 3. Identified Security Gaps

| ID | Identified Gap | Potential Security Impact | Priority |
|---|---|---|---|
| GAP-01 | Inconsistent MFA enforcement | Increased risk of account compromise | Critical |
| GAP-02 | Fragmented identity management | Reduced visibility and inconsistent access control | High |
| GAP-03 | Excessive user permissions | Unauthorized access to sensitive resources | Critical |
| GAP-04 | Insufficient privileged account controls | Increased risk of administrative account misuse | Critical |
| GAP-05 | Limited access review procedures | Former or transferred employees may retain unnecessary access | High |
| GAP-06 | Inconsistent cloud access policies | Different security standards across AWS and Azure | High |
| GAP-07 | Limited centralized identity monitoring | Delayed identification of suspicious authentication activity | High |
| GAP-08 | Limited device-based access evaluation | Potential access from untrusted or unmanaged devices | High |

## 4. Risk Analysis

### Risk 1 – Compromised User Accounts

**Scenario:** An attacker obtains an employee's password through phishing or credential reuse.

**Potential impact:** Unauthorized access to business applications and cloud resources.

**Recommended controls:**
- Enforce MFA.
- Apply risk-based or contextual access policies where supported.
- Monitor suspicious authentication activity.
- Implement account protection and recovery procedures.

### Risk 2 – Excessive Privileges

**Scenario:** An employee has permissions beyond those required for their responsibilities.

**Potential impact:** Unauthorized changes, exposure of sensitive data or misuse of cloud resources.

**Recommended controls:**
- Implement RBAC.
- Apply least privilege.
- Conduct periodic access reviews.
- Separate standard and administrative accounts.

### Risk 3 – Privileged Account Compromise

**Scenario:** An attacker compromises a cloud administrator account.

**Potential impact:** Unauthorized infrastructure changes, data exposure or disruption of services.

**Recommended controls:**
- Use dedicated privileged accounts.
- Require strong MFA.
- Apply just-in-time administrative access where supported.
- Monitor privileged activity.
- Maintain emergency access procedures.

### Risk 4 – Inconsistent Cloud Security

**Scenario:** AWS and Azure resources use inconsistent identity and access policies.

**Potential impact:** Security gaps and excessive permissions across cloud environments.

**Recommended controls:**
- Establish common identity governance standards.
- Define cloud-specific RBAC policies.
- Review trust relationships and federated access.
- Centralize relevant audit and security logs.

## 5. Recommended Security Improvements

| Improvement | Proposed Control |
|---|---|
| Centralized identity | Establish a defined identity governance model |
| Strong authentication | Enforce MFA |
| Access governance | Standardize RBAC |
| Privileged access | Introduce PAM and just-in-time access |
| Cloud security | Standardize AWS and Azure identity controls |
| Device security | Introduce device compliance requirements |
| Monitoring | Centralize identity and access logs |
| Governance | Establish periodic access reviews |

## 6. Assessment Summary

The assumed current environment presents identity-related risks involving inconsistent authentication, excessive permissions, privileged access and limited monitoring.

The proposed architecture will address these gaps through centralized identity governance, Zero Trust principles, least-privilege access, stronger privileged account controls and improved security monitoring.

## 7. Document Status

Status: Initial hypothetical assessment  
Project: Enterprise IAM and Zero Trust Architecture  
Organization: NorthStar Technologies (fictional)