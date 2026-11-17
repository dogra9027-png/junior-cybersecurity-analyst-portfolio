# Threat Model and Risk Register

## 1. Purpose

This document identifies potential security threats affecting the proposed NorthStar Technologies enterprise IAM and Zero Trust architecture.

The assessment considers workforce identities, privileged accounts, cloud infrastructure, endpoints, and authentication systems.

The threats and scenarios are hypothetical and are used for architecture design and risk analysis.

## 2. Assets Requiring Protection

| Asset | Security importance |
|---|---|
| Employee identities | Prevent unauthorized account access |
| Privileged accounts | Protect administrative capabilities |
| Microsoft Entra ID | Protect centralized identity services |
| AWS resources | Protect cloud infrastructure and data |
| Azure resources | Protect cloud workloads and configurations |
| Endpoints | Prevent compromised devices from accessing resources |
| Authentication logs | Support detection and investigation |
| Business applications | Protect sensitive business information |

## 3. Threat Identification

| ID | Threat | Potential impact |
|---|---|---|
| T-01 | Credential theft | Unauthorized access to employee accounts |
| T-02 | Brute-force attacks | Account compromise through repeated password attempts |
| T-03 | Privilege escalation | Unauthorized administrative access |
| T-04 | Excessive permissions | Increased impact of compromised accounts |
| T-05 | Unmanaged device access | Sensitive information exposed through insecure devices |
| T-06 | Cloud misconfiguration | Unauthorized access to cloud resources |
| T-07 | Inadequate access reviews | Former or unauthorized users retain access |
| T-08 | Insufficient monitoring | Delayed detection of suspicious activity |

## 4. Risk Assessment Method

Risks are assessed using a simple qualitative model.

**Risk score = Likelihood × Impact**

Likelihood and impact are rated from 1 to 5.

| Score | Rating |
|---|---|
| 1 | Very Low |
| 2 | Low |
| 3 | Moderate |
| 4 | High |
| 5 | Very High |

Risk classification:

| Score | Risk level |
|---|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–16 | High |
| 17–25 | Critical |

These ratings are illustrative and would need validation against an organization's actual environment.

## 5. Risk Register

| Risk ID | Threat | Likelihood | Impact | Score | Level |
|---|---|---:|---:|---:|---|
| R-01 | Stolen employee credentials | 4 | 5 | 20 | Critical |
| R-02 | Repeated password attacks | 4 | 4 | 16 | High |
| R-03 | Excessive administrator privileges | 3 | 5 | 15 | High |
| R-04 | Unmanaged endpoint access | 3 | 4 | 12 | High |
| R-05 | Cloud configuration errors | 3 | 5 | 15 | High |
| R-06 | Inactive accounts retaining access | 3 | 4 | 12 | High |
| R-07 | Insufficient security monitoring | 3 | 4 | 12 | High |

## 6. Recommended Mitigation Controls

| Risk ID | Recommended controls |
|---|---|
| R-01 | MFA, Conditional Access, sign-in risk monitoring, account recovery controls |
| R-02 | Account lockout or throttling protections, MFA, authentication monitoring |
| R-03 | Least privilege, separate admin accounts, privileged access management |
| R-04 | Device compliance checks, endpoint protection, restricted access |
| R-05 | Cloud security policies, RBAC, configuration reviews, audit logging |
| R-06 | Joiner-Mover-Leaver process, prompt account deactivation, periodic access reviews |
| R-07 | Centralized logging, SIEM alerts, investigation procedures |

## 7. Threat Scenarios

### Scenario 1: Compromised Employee Account

**Threat:** An attacker obtains an employee's credentials through phishing.

**Potential impact:**
- Unauthorized application access.
- Exposure of business information.
- Attempts to access additional cloud resources.

**Recommended response:**
1. Review the suspicious sign-in.
2. Require additional verification or block access.
3. Revoke active sessions where appropriate.
4. Reset compromised credentials.
5. Investigate activity performed by the account.
6. Review whether other accounts or resources were affected.

### Scenario 2: Privileged Account Misuse

**Threat:** An administrator account is compromised or misused.

**Potential impact:**
- Unauthorized changes to cloud resources.
- Exposure or modification of sensitive data.
- Creation of additional privileged accounts.

**Recommended response:**
1. Restrict or disable the affected account.
2. Review privileged activity logs.
3. Identify unauthorized changes.
4. Restore approved configurations where necessary.
5. Rotate affected credentials and review permissions.

### Scenario 3: Cloud Misconfiguration

**Threat:** A cloud storage resource is configured with excessive or unintended access.

**Potential impact:**
- Unauthorized data exposure.
- Data modification or deletion.
- Compliance and reputational consequences.

**Recommended response:**
1. Identify the affected resource.
2. Restrict unintended access.
3. Review access policies and permissions.
4. Examine available audit logs.
5. Document findings and corrective actions.

## 8. Monitoring and Detection Recommendations

The proposed security monitoring approach should identify:

- Repeated failed authentication attempts.
- Successful logins following multiple failures.
- Unusual administrator activity.
- Unexpected role or permission changes.
- Access from non-compliant devices.
- Unusual cloud resource configuration changes.

Relevant log sources include Microsoft Entra ID sign-in logs, AWS CloudTrail, and Azure Activity Logs.

Microsoft Sentinel is proposed as a centralized SIEM platform.

## 9. Residual Risk and Review

Implementing security controls reduces risk but does not eliminate it.

NorthStar Technologies should:
- Review risks periodically.
- Reassess risks after significant infrastructure changes.
- Test security controls.
- Track unresolved findings.
- Assign risk owners.
- Update mitigation plans as threats evolve.

## 10. Limitations

- NorthStar Technologies is fictional.
- Threat scenarios and risk ratings are illustrative.
- No production environment or live security assessment was conducted.
- The effectiveness of proposed controls has not been tested in a live cloud environment.

## 11. Conclusion

This threat model identifies key risks associated with identity management, privileged access, endpoint security, and cloud infrastructure.

The proposed mitigations align with the IAM and Zero Trust architecture and provide a foundation for a structured security implementation roadmap.