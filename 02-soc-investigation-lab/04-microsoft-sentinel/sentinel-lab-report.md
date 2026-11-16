
# Microsoft Sentinel - Authentication Detection Lab

## 1. Project Overview

This lab demonstrates Microsoft Sentinel-style authentication threat detection using Kusto Query Language (KQL).

The objective was to develop detection queries for suspicious authentication patterns and validate the underlying detection logic against a simulated authentication dataset.

## 2. Tools and Technologies

- Kusto Query Language (KQL)
- Python 3
- CSV authentication logs
- MITRE ATT&CK Framework
- Visual Studio Code

## 3. Dataset

File: `authentication_logs.csv`

Total authentication events analyzed: 15

- Successful logins: 6
- Failed logins: 9

All authentication events and IP addresses are simulated for educational purposes.

## 4. Detection Scenarios

Four KQL detection scenarios were developed:

### Detection 1: Repeated Failed Login Attempts

Identifies accounts with three or more failed authentication attempts from the same source IP address.

Findings:
- jdoe: 6 failed attempts from 203.0.113.45
- admin: 3 failed attempts from 198.51.100.77

### Detection 2: Successful Login After Repeated Failures

Identifies successful authentication events occurring after at least three earlier failed login attempts from the same username and source IP.

Finding:
- Account: jdoe
- Event ID: AUTH008
- Source IP: 203.0.113.45
- Failed attempts before success: 5

### Detection 3: Failed Privileged Account Logins

Monitors failed authentication attempts involving privileged account names such as admin and administrator.

Finding:
- Account: admin
- Source IP: 198.51.100.77
- Failed attempts: 3
- Severity: High

### Detection 4: Successful Privileged Account Logins

Identifies successful authentication events involving privileged account names.

Finding:
- Account: admin
- Event ID: AUTH015
- Source IP: 192.168.1.10
- Destination: SERVER-01

## 5. Local Validation

A Python validation script was developed:

`validate_kql_detections.py`

The script independently checked the four detection scenarios against the simulated CSV dataset.

Validation results:
- Repeated failed login detection: Successful
- Successful login after repeated failures: Successful
- Failed privileged account detection: Successful
- Successful privileged account monitoring: Successful

All four detection scenarios returned the expected findings.

## 6. Limitations

- No live Microsoft Sentinel workspace was deployed.
- KQL queries were written but not executed in a live Sentinel environment.
- Python was used to validate the underlying detection logic, not to execute KQL.
- The AuthenticationLogs table represents the intended table schema and would need to be mapped to an actual Sentinel data table during deployment.
- All events are simulated and do not represent a confirmed security incident.

## 7. Conclusion

This lab demonstrates the ability to develop KQL-based authentication detection logic, analyze suspicious login patterns, validate detection scenarios using Python, and document security findings.

The work complements the Python detection and Splunk investigation components of the SOC Investigation Lab.
