# Security Monitoring and Alert Triage

## Project Overview

A Python-based security monitoring project demonstrating foundational SOC analyst skills through security alert analysis, rule-based detection, event correlation, and investigation reporting.

The project analyzes a sample dataset of authentication and network events, identifies potentially suspicious activity, and generates structured Markdown reports with recommended investigation actions.

## Objectives

- Analyze security alerts using Python.
- Identify possible brute-force login activity.
- Detect possible port scanning.
- Prioritize high-severity alerts.
- Correlate failed login attempts with subsequent successful logins.
- Document investigation findings and recommended actions.
- Validate detection logic through automated unit tests.

## Project Structure

```text
01-security-monitoring-and-triage/
├── data/
│   └── security_alerts.csv
├── reports/
│   ├── alert_analysis_report.md
│   ├── detection_findings.md
│   ├── incident_investigation.md
│   └── mitre_attack_mapping.md
├── src/
│   ├── analyze_alerts.py
│   └── detect_suspicious_activity.py
├── tests/
│   └── test_detection_rules.py
└── README.md
```

## Detection Rules

| Rule | Description |
|---|---|
| DET-001 | Possible brute-force activity: 20 or more failed login attempts |
| DET-002 | Possible port scanning: Port Scan event |
| DET-003 | High-severity security alert |
| DET-004 | Successful login following qualifying failed login activity from the same source IP within 30 minutes |

## Sample Detection Results

| Metric | Result |
|---|---:|
| Unique alerts analyzed | 7 |
| Detection rule matches | 8 |
| Unique alerts requiring investigation | 5 |

DET-004 identified a successful login from the same source IP two minutes after 35 failed login attempts.

This is a potential indicator requiring investigation, not confirmation of unauthorized access.

## Reports

The project generates and maintains the following investigation documentation:

- `alert_analysis_report.md` — alert statistics and suspicious IP activity.
- `detection_findings.md` — detection rule results, evidence, severity, and recommended actions.
- `incident_investigation.md` — incident investigation documentation.
- `mitre_attack_mapping.md` — mapping of observed activity to relevant MITRE ATT&CK techniques.

## Technologies

- Python 3
- CSV processing
- Python standard library
- unittest
- PowerShell
- Visual Studio Code
- Markdown

## How to Run

Run commands from the portfolio root directory.

### Alert analysis

```powershell
python .\01-security-monitoring-and-triage\src\analyze_alerts.py
```

### Security detection

```powershell
python .\01-security-monitoring-and-triage\src\detect_suspicious_activity.py
```

### Automated tests

```powershell
python -m unittest discover -s ".\01-security-monitoring-and-triage\tests" -p "test_*.py" -v
```

## Limitations

- Uses a sample CSV dataset rather than live SIEM telemetry.
- Event correlation is based on source IP and timestamps; account-level correlation is not available because the dataset does not contain account identifiers.
- Detection thresholds are predefined and require tuning for real-world environments.
- Findings require analyst validation and additional supporting evidence.

## Project Status

Initial detection implementation, alert analysis, investigation documentation, MITRE ATT&CK mapping, and automated unit tests completed.