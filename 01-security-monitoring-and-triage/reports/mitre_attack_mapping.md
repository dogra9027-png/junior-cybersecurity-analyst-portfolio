
# MITRE ATT&CK Detection Mapping

## Project
Security Monitoring and Alert Triage

## 1. Purpose

This document maps simulated security detection findings
to relevant MITRE ATT&CK Enterprise techniques.

The mapping helps analysts describe observed behaviour
using a recognized adversary behaviour framework.

## 2. Detection Mapping

| Rule ID | Detection | MITRE Technique | Technique ID |
|---|---|---|---|
| DET-001 | Possible Brute-Force Activity | Brute Force | T1110 |
| DET-002 | Possible Port Scanning | Network Service Discovery | T1046 |
| DET-003 | High-Severity Alert | No direct mapping | N/A |

## 3. Technique Details

### T1110 - Brute Force

Tactic: Credential Access

Description:

Adversaries may repeatedly attempt authentication
using different passwords or credentials to gain
unauthorized account access.

Project evidence:

- Alert ID: 1002
- Alert ID: 1004
- Alert ID: 1006
- Failed login attempts: 35, 52 and 27 respectively.

Analyst interpretation:

The repeated authentication failures are consistent
with possible brute-force activity.

Additional evidence is required to determine whether
the behaviour represents password guessing,
password spraying or another cause.

Official reference:
https://attack.mitre.org/techniques/T1110/

### T1046 - Network Service Discovery

Tactic: Discovery

Description:

Adversaries may scan network hosts and services
to identify available services and potential
attack opportunities.

Project evidence:

- Alert ID: 1005
- Event Type: Port Scan
- Source IP: 192.168.1.30

Analyst interpretation:

The event is consistent with possible network
service discovery activity.

Additional firewall, network flow or packet
capture evidence would help validate the activity.

Official reference:
https://attack.mitre.org/techniques/T1046/

## 4. Detection Rule Without Direct ATT&CK Mapping

### DET-003 - High-Severity Alert

This rule prioritizes alerts based on their assigned
severity.

Severity classification is not itself an adversary
technique. Therefore, no direct MITRE ATT&CK
technique is assigned.

## 5. Analyst Recommendations

1. Review authentication logs for repeated failures.
2. Identify affected user accounts.
3. Check for successful logins following failed attempts.
4. Review network traffic associated with port scans.
5. Correlate findings with other security events.
6. Document confirmed evidence before escalating.

## 6. Conclusion

The project demonstrates how simulated security
alerts can be mapped to MITRE ATT&CK techniques.

The mappings represent possible adversary behaviours,
not confirmation of successful attacks.

Further investigation is necessary to establish
whether the activity is malicious.

## 7. References

- MITRE ATT&CK - Brute Force (T1110)
  https://attack.mitre.org/techniques/T1110/

- MITRE ATT&CK - Network Service Discovery (T1046)
  https://attack.mitre.org/techniques/T1046/
