
# Junior Cybersecurity Analyst Portfolio

Welcome to my cybersecurity portfolio. This repository showcases practical cybersecurity projects, technical investigations, security architecture designs, and hands-on exercises focused on security monitoring, threat detection, identity and access management, and incident response.

My goal is to demonstrate developing cybersecurity skills through Python scripting, SIEM investigations, detection logic, access reviews, security documentation, and structured analysis.

## Projects

### 1. Security Monitoring and Triage

**Status:** Initial implementation completed

A Python-based security alert analysis project that evaluates simulated authentication and network events using detection rules.

**Key capabilities:**
- Detects possible brute-force login activity.
- Identifies possible port scanning.
- Flags high-severity security alerts.
- Correlates failed login attempts with subsequent successful logins.
- Generates security findings and investigation reports.
- Includes automated unit tests using Python's `unittest` framework.
- Maps selected findings to MITRE ATT&CK techniques.

**Technologies:** Python, CSV, PowerShell, Markdown, unittest, MITRE ATT&CK.

[View Project: Security Monitoring and Triage](./01-security-monitoring-and-triage/)

[View Project Case Study](./projects/security-monitoring.html)

---

### 2. SOC Investigation Lab

**Status:** Initial implementation completed

A simulated Security Operations Centre (SOC) investigation lab focused on authentication monitoring, suspicious login activity, detection development, and investigation workflows.

**Key capabilities:**
- Analyses simulated authentication events.
- Identifies repeated failed login attempts.
- Detects successful logins following repeated failures.
- Investigates suspicious privileged account activity.
- Uses Splunk Cloud to create authentication monitoring dashboards.
- Includes Sentinel-style KQL detection queries.
- Documents investigation findings and incident response procedures.

**Technologies:** Python, Splunk Cloud, SPL, KQL, CSV, Markdown.

**Environment note:** Splunk dashboards were created using uploaded simulated data. Sentinel-style queries were documented and locally validated but were not executed in a live Microsoft Sentinel workspace.

[View Project: SOC Investigation Lab](./02-soc-investigation-lab/)

[View Project Case Study](./projects/soc-investigation.html)

---

### 3. Enterprise IAM and Zero Trust Architecture

**Status:** Architecture design and practical IAM exercise completed

A security architecture design case study for a fictional 200-employee organization operating across AWS and Microsoft Azure environments.

The project explores identity governance, role-based access control, least privilege, privileged access management, Zero Trust principles, and cloud security.

**Key capabilities:**
- Designs a conceptual enterprise IAM architecture.
- Proposes centralized identity management using Microsoft Entra ID.
- Documents AWS IAM Identity Center and Azure RBAC integration concepts.
- Develops role-based access control and identity lifecycle workflows.
- Designs MFA, Conditional Access, and Zero Trust security controls.
- Conducts hypothetical threat modelling and qualitative risk assessment.
- Develops a phased IAM and Zero Trust implementation roadmap.
- Builds a Python-based simulated IAM access review exercise.
- Identifies permission mismatches and privileged access requiring review.
- Generates consolidated IAM audit reports with analyst decisions and recommendations.

**Practical IAM exercise results:**
- 10 fictional permission records analysed.
- 6 permission matches.
- 2 records requiring investigation.
- 2 privileged access records flagged for review.
- 4 analyst decisions documented.

**Technologies:** Python, CSV, PowerShell, Visual Studio Code, AWS IAM concepts, Microsoft Entra ID concepts, Azure RBAC concepts.

**Environment note:** The architecture is a conceptual design, and the access review uses fictional records processed locally with Python. No live cloud identity configuration or permission changes were performed.

[View Project: Enterprise IAM and Zero Trust Architecture](./03-enterprise-iam-zero-trust-architecture/)

[View Project Case Study](./projects/enterprise-iam-zero-trust.html)

---

## Technical Skills Demonstrated

- Security monitoring and alert triage
- Python scripting and security automation
- Authentication log analysis
- Detection logic and event correlation
- SIEM dashboards and investigations
- Splunk and SPL
- KQL query development and validation
- Identity and Access Management (IAM)
- Role-Based Access Control (RBAC)
- Least-privilege access and privileged access review
- Zero Trust security principles
- Threat modelling and risk assessment
- MITRE ATT&CK mapping
- Incident investigation and response documentation
- Technical documentation and security reporting

## About This Portfolio

This portfolio is continuously evolving as I develop practical cybersecurity knowledge and skills through structured projects and exercises.

The projects distinguish between simulated exercises, conceptual architecture designs, and tools or platforms used in practical lab environments. Project descriptions identify their scope and limitations transparently.

## Portfolio Website

Explore the project case studies and supporting information:

[Cybersecurity Portfolio – Dimple Dogra](https://dogra9027-png.github.io/junior-cybersecurity-analyst-portfolio/)

## Author

**Dimple Dogra**

Cybersecurity | SOC Analysis | Security Monitoring | IAM | Technical Documentation

[GitHub](https://github.com/dogra9027-png) | [LinkedIn](https://www.linkedin.com/in/dimple-dogra-8771b41a8/)
