# SOC Investigation Lab

## Project Overview

This project demonstrates practical Security Operations Center (SOC) activities using simulated authentication logs, Python-based detection scripts, Splunk Cloud, and Microsoft Sentinel-style KQL detection queries.

The objective is to identify suspicious authentication patterns, investigate potential security events, develop detection logic, and document incident response procedures.

## Tools and Technologies

- Python 3
- CSV authentication log analysis
- Splunk Cloud
- SPL (Search Processing Language)
- Kusto Query Language (KQL)
- Microsoft Sentinel detection concepts
- MITRE ATT&CK Framework
- Markdown documentation

## Project Structure

- `01-datasets/` – Simulated authentication logs
- `02-python-detection/` – Python authentication detection scripts
- `03-splunk/` – SPL queries, investigation documentation, and dashboard materials
- `04-microsoft-sentinel/` – KQL detection queries and local Python validation
- `05-investigation/` – Authentication investigation findings
- `06-incident-response/` – Incident response playbook
- `07-evidence/` – Screenshots and lab evidence

## Detection Scenarios

1. Repeated failed login attempts
2. Successful login following repeated failures
3. Failed privileged account login attempts
4. Successful privileged account login monitoring

## Key Findings

The simulated dataset contains 15 authentication events:

- 9 failed login events
- 6 successful login events
- Repeated failed login activity involving `jdoe` and `admin`
- A successful login by `jdoe` following five failed attempts
- Three failed privileged account login attempts involving `admin`

## Python Detection

Python scripts analyze the authentication dataset and identify suspicious login patterns.

The detection logic includes:

- Repeated failed authentication attempts
- Successful authentication following repeated failures
- Failed privileged account authentication attempts

## Splunk Monitoring

A Splunk Dashboard Studio dashboard was created with five panels:

1. Authentication Events by Status
2. Repeated Failed Login Attempts
3. Successful Login After Repeated Failures
4. Failed Privileged Account Logins
5. Successful Privileged Account Logins

SPL queries and investigation documentation are included in `03-splunk/`.

## Microsoft Sentinel and KQL

Four Sentinel-style KQL detection queries were developed for the authentication scenarios.

The detection logic was validated locally using Python against the simulated dataset.

**Lab limitation:** No live Microsoft Sentinel workspace was configured. KQL queries are portfolio examples and have not been executed in a live Sentinel environment. The Python validation checks the underlying detection logic, not KQL runtime syntax.

## Investigation and Incident Response

The investigation report documents the suspicious authentication patterns, findings, recommendations, and preliminary MITRE ATT&CK mappings.

An incident response playbook outlines:

- Identification
- Initial analysis
- Containment
- Eradication
- Recovery
- Lessons learned

## Important Notes and Limitations

- All authentication events are simulated for educational and portfolio purposes.
- The IP addresses are reserved documentation addresses.
- No real users, attackers, or compromised systems are involved.
- Detection findings represent suspicious patterns, not confirmed security breaches.
- No actual containment or recovery actions were performed.

## Project Objective

This lab demonstrates foundational SOC analyst skills in log analysis, security detection, investigation, SIEM monitoring, detection documentation, and incident response.