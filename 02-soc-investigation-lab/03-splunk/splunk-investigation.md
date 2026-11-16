# Splunk Authentication Log Investigation

## 1. Investigation Overview

**Platform:** Splunk Cloud  
**Data source:** authentication_logs.csv  
**Source type:** csv  
**Host:** soc-lab  
**Index:** main  
**Total events analyzed:** 15

## 2. Investigation Objective

Analyze authentication events to identify suspicious login activity, including repeated failed login attempts and successful authentication following multiple failures.

## 3. Detection 1 – Repeated Failed Login Attempts

**Detection logic:** Identify usernames and source IP addresses with three or more failed authentication attempts.

**Findings:**

| Username | Source IP | Failed Attempts | Severity |
|---|---|---:|---|
| jdoe | 203.0.113.45 | 5 | High |
| admin | 198.51.100.77 | 3 | High |

**Analysis:** Both accounts experienced repeated failed authentication attempts. These patterns may indicate password guessing or brute-force activity.

## 4. Detection 2 – Successful Login After Repeated Failures

**Detection logic:** Identify successful authentication events following at least three failed attempts from the same username and source IP.

**Finding:**

- Username: jdoe
- Source IP: 203.0.113.45
- Failed attempts before success: 5
- Successful event: AUTH008
- Successful login time: 08:11:10

**Analysis:** The successful login occurred shortly after five failed attempts from the same source IP. This activity warrants investigation for possible account compromise.

## 5. Detection 3 – Failed Privileged Account Login Attempts

**Detection logic:** Identify failed authentication attempts involving privileged accounts such as `admin` and `administrator`.

**Finding:**

- Username: admin
- Source IP: 198.51.100.77
- Destination host: SERVER-01
- Failed attempts: 3
- Severity: High

**Analysis:** Three failed login attempts targeting the administrator account were observed from the same source IP. This activity may indicate password guessing or an unauthorized access attempt against a privileged account.

**Recommended actions:**
1. Review administrator authentication history.
2. Validate whether the source IP is expected.
3. Check for successful authentication attempts from the same source.
4. Review relevant server logs for additional suspicious activity.

## 6. Detection 4 – Successful Privileged Account Login

**Detection logic:** Identify successful authentication events involving privileged accounts.

**Finding:**

- Username: admin
- Event ID: AUTH015
- Source IP: 192.168.1.10
- Destination host: SERVER-01
- Authentication status: SUCCESS

**Analysis:** A successful administrator login was observed from an internal IP address. The same account had earlier experienced three failed login attempts from a different source IP.

This activity warrants contextual review, but the available evidence does not establish a connection between the two sources or confirm account compromise.

**Recommended actions:**
1. Verify whether the administrator login was authorized.
2. Review the administrator's recent authentication history.
3. Correlate the event with server and endpoint logs.
4. Investigate any unexpected privileged activity.


## 5. Recommended SOC Investigation Actions

1. Review the affected account's authentication history.
2. Validate the login with the account owner.
3. Check whether the source IP is associated with known infrastructure.
4. Review endpoint and network activity around the authentication time.
5. Escalate and follow incident response procedures if compromise is suspected.

## 6. Limitations

- The dataset contains simulated authentication events.
- No real user accounts or production systems were investigated.
- Detection results indicate suspicious patterns, not confirmed compromise.
- The SPL queries demonstrate basic event aggregation and sequence analysis.

## 7. Conclusion

Splunk Cloud was used to ingest and analyze authentication logs. Two detection searches identified repeated failed logins and a successful login following repeated failures.

The investigation demonstrates practical experience with CSV ingestion, SPL searches, authentication monitoring, suspicious activity identification, and preliminary SOC triage.

## 8. SOC Authentication Monitoring Dashboard

A Splunk Dashboard Studio dashboard was created to provide a visual overview of authentication activity and suspicious login patterns using simulated authentication logs.

### Dashboard Panels

1. Authentication Events by Status
2. Repeated Failed Login Attempts
3. Successful Login After Repeated Failures
4. Failed Privileged Account Logins
5. Successful Privileged Account Logins

### Dashboard Configuration

- Platform: Splunk Cloud
- Dashboard: SOC Authentication Monitoring Dashboard
- Index: main
- Data source: authentication_logs.csv
- Host: soc-lab
- Visualization: Table and Column Chart

### Evidence

Dashboard screenshots are available in:

`07-evidence/screenshots/`

### Outcome

The dashboard provides a centralized view of authentication events, repeated login failures, successful logins following repeated failures, and privileged-account activity.

All events used in this lab are simulated and do not represent a real security incident.