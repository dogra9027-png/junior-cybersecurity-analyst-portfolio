# Authentication Security Investigation

## 1. Investigation Overview

**Investigation Type:** Authentication Anomaly Detection  
**Environment:** Simulated enterprise environment  
**Data Source:** Authentication event logs (CSV)  
**Analysis Tool:** Python 3.10.2  
**Investigation Date:** November 12, 2026  
**Status:** Investigation required

## 2. Executive Summary

A review of 15 simulated authentication events identified suspicious login activity involving two accounts: `jdoe` and `admin`.

The analysis identified repeated consecutive authentication failures from external-looking source IP addresses. One account, `jdoe`, subsequently recorded a successful login following five consecutive failures from the same source IP.

These events may indicate a brute-force attempt followed by successful authentication. Further investigation would be required to determine whether the account was compromised.

## 3. Detection Summary

| Detection | Account | Source IP | Findings |
|---|---|---|---|
| Repeated consecutive failed logins | jdoe | 203.0.113.45 | 5 failures |
| Repeated consecutive failed logins | admin | 198.51.100.77 | 3 failures |
| Successful login after repeated failures | jdoe | 203.0.113.45 | Success after 5 failures |
| Failed privileged account logins | admin | 198.51.100.77 | 3 failures |

## 4. Detailed Findings

### Finding 1: Repeated Authentication Failures — jdoe

- **Username:** jdoe
- **Source IP:** 203.0.113.45
- **Destination Host:** WORKSTATION-01
- **Failed Attempts:** 5 consecutive failures
- **First Failed Attempt:** 08:10:15
- **Last Failed Attempt:** 08:10:55
- **Severity:** High

Five consecutive authentication failures were recorded for the same account and source IP within approximately 40 seconds.

**Assessment:** This pattern is consistent with a possible brute-force attempt.

### Finding 2: Successful Authentication Following Repeated Failures — jdoe

- **Username:** jdoe
- **Source IP:** 203.0.113.45
- **Destination Host:** WORKSTATION-01
- **Failed Attempts Before Success:** 5
- **Successful Login:** 08:11:10
- **Severity:** Critical

A successful authentication occurred 15 seconds after the fifth consecutive failure from the same source IP.

**Assessment:** This sequence raises concern about possible unauthorized account access. The successful authentication should be investigated further.

### Finding 3: Repeated Authentication Failures — admin

- **Username:** admin
- **Source IP:** 198.51.100.77
- **Destination Host:** SERVER-01
- **Failed Attempts:** 3 consecutive failures
- **First Failed Attempt:** 08:15:20
- **Last Failed Attempt:** 08:15:40
- **Severity:** High

Three consecutive failed authentication attempts were recorded against a privileged account.

**Assessment:** Repeated attempts against a privileged account warrant investigation and review of administrative authentication activity.

## 5. Recommended Investigation Actions

1. Review authentication logs surrounding the suspicious login timestamps.
2. Verify whether the successful login for `jdoe` was legitimate.
3. Examine endpoint activity on WORKSTATION-01 after the successful authentication.
4. Review account activity for unexpected processes, privilege changes, or unusual access.
5. Investigate the failed administrative login attempts against SERVER-01.
6. Check whether the source IP addresses appear in other available security telemetry.
7. Preserve relevant authentication and endpoint evidence for further analysis.

## 6. MITRE ATT&CK Mapping

| Technique | Technique ID | Relevance |
|---|---|---|
| Brute Force | T1110 | Repeated failed authentication attempts |
| Valid Accounts | T1078 | Successful authentication following repeated failures |

These are preliminary mappings based on observed patterns, not confirmation that either technique was successfully used by an attacker.

## 7. Conclusion

The simulated authentication dataset contains multiple suspicious login patterns requiring further investigation.

The highest-priority finding is the successful authentication of `jdoe` following five consecutive failures from the same source IP.

Additional endpoint, identity, and network telemetry would be required to establish whether unauthorized access occurred and determine the scope and impact.

## 8. Data and Testing Limitations

- The dataset contains simulated authentication events.
- The source IP addresses `203.0.113.45` and `198.51.100.77` belong to documentation-only address ranges and do not represent real attacker infrastructure.
- No actual account compromise or security incident has been established.
- Detection results depend on the fields and events available in the CSV dataset.
- Severity levels are preliminary classifications for this lab exercise.
