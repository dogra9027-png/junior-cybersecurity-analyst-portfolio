
# Junior Cybersecurity Analyst Portfolio

Welcome to my cybersecurity portfolio. This repository showcases practical projects and structured security exercises focused on security monitoring, threat detection, SOC investigations, identity and access management, and Zero Trust security design.

My goal is to demonstrate developing cybersecurity skills through Python scripting, SIEM analysis, detection logic, investigation workflows, access reviews, security documentation, and architecture design.

## Projects

### 1. Security Monitoring and Triage

**Status:** Initial implementation completed

A Python-based security alert analysis project that evaluates simulated authentication and network events using detection rules.

**Key capabilities:**
- Detects possible brute-force login activity.
- Identifies possible port scanning.
- Flags high-severity security alerts.
- Correlates failed login attempts with subsequent successful logins.
- Generates Markdown security findings and investigation reports.
- Includes automated unit tests using Python's `unittest` framework.

**Technologies:** Python, CSV, PowerShell, Markdown, unittest.

[View Project: Security Monitoring and Triage](./01-security-monitoring-and-triage/)

### 2. SOC Investigation Lab

**Status:** Practical lab completed

A simulated Security Operations Centre (SOC) investigation lab using Python and Splunk to analyze authentication events and investigate suspicious login activity.

**Key capabilities:**
- Analyzes simulated authentication logs.
- Identifies repeated failed login attempts.
- Detects successful logins following repeated failures.
- Highlights potentially suspicious privileged account activity.
- Uses Python to support detection and investigation workflows.
- Uses Splunk dashboards to visualize authentication activity.
- Includes investigation findings and incident response documentation.
- Includes example KQL queries for Microsoft Sentinel-style investigations.

**Technologies:** Python, Splunk, CSV, KQL, PowerShell, SIEM, Markdown.

**Note:** The authentication data is simulated. Splunk was used for log analysis and dashboard creation. Microsoft Sentinel queries are documented examples and were not executed in a live Sentinel workspace.

[View Project: SOC Investigation Lab](./02-soc-investigation-lab/)

### 3. Enterprise IAM and Zero Trust Architecture

**Status:** Security design case study and practical simulated IAM exercise completed

An enterprise security architecture case study based on a fictional 200-employee organization. The project explores identity and access management, least-privilege access, Zero Trust principles, cloud security, threat modelling, and implementation planning.

**Key capabilities:**
- Develops a conceptual enterprise IAM architecture using Microsoft Entra ID, AWS IAM Identity Center, and Azure RBAC.
- Defines role-based access controls and least-privilege principles.
- Documents identity lifecycle processes, including Joiner, Mover, and Leaver workflows.
- Designs Zero Trust controls covering MFA, Conditional Access, device compliance, and privileged access.
- Conducts hypothetical threat modelling and qualitative risk assessment.
- Develops a phased IAM and Zero Trust implementation roadmap.
- Includes a Python-based access review exercise using fictional employee permission records.
- Identifies permission mismatches and privileged access requiring further review.
- Documents analyst decisions and generates a consolidated IAM audit report.

**Practical IAM exercise results:**
- 10 permission records analyzed.
- 6 permission records matched stated role requirements.
- 2 permission mismatches flagged for review.
- 2 privileged permission assignments flagged for additional review.
- 4 analyst decisions documented.

**Technologies:** Python, CSV, PowerShell, Microsoft Entra ID (architecture design), AWS IAM (architecture design), Azure RBAC (architecture design), Markdown.

**Note:** The architecture is a conceptual design case study, not a live cloud deployment. The Python exercise uses fictional records and simulated analyst decisions. No actual cloud permissions were changed or revoked.

[View Project: Enterprise IAM and Zero Trust Architecture](./03-enterprise-iam-zero-trust-architecture/)

## Skills Demonstrated

- Security alert analysis and initial triage
- Python scripting and automation
- Detection logic and event correlation
- SOC investigation workflows
- SIEM monitoring and dashboard analysis
- Authentication log analysis
- Incident investigation and reporting
- MITRE ATT&CK mapping
- Identity and access management fundamentals
- Role-based access control and least privilege
- Privileged access review
- Access governance and audit documentation
- Zero Trust security principles
- Cloud security concepts across AWS and Microsoft Azure
- Threat modelling and qualitative risk assessment
- Technical documentation and security reporting

## Tools and Technologies

- **Programming:** Python
- **SIEM:** Splunk
- **Query and analysis:** KQL examples, CSV
- **Cloud and identity concepts:** AWS IAM, Microsoft Entra ID, Azure RBAC
- **Security frameworks and concepts:** MITRE ATT&CK, Zero Trust, least privilege
- **Development environment:** Visual Studio Code, PowerShell
- **Documentation:** Markdown

## About This Portfolio

This portfolio is a practical learning and professional development project. It demonstrates my approach to analyzing security events, documenting investigation findings, reviewing access permissions, and designing security controls.

The projects use simulated datasets and clearly documented case-study assumptions where applicable. They are intended to demonstrate practical learning and developing technical capabilities rather than claim production enterprise security deployments.

Additional projects and improvements will be added as I continue developing my skills in security operations, cloud security, vulnerability management, identity security, and incident response.

## Portfolio Website

Visit the portfolio website to explore the project case studies:

[Cybersecurity Portfolio – Dimple Dogra](https://dogra9027-png.github.io/junior-cybersecurity-analyst-portfolio/)

## Author

**Dimple Dogra**

GitHub: [dogra9027-png](https://github.com/dogra9027-png)

LinkedIn: [Dimple Dogra](https://www.linkedin.com/in/dimple-dogra-8771b41a8/)
