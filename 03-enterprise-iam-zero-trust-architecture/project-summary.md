# Enterprise IAM and Zero Trust Architecture

## Project Overview

**Project type:** Enterprise Security Architecture Case Study  
**Organization:** NorthStar Technologies (Fictional)  
**Focus areas:** Identity and Access Management (IAM), Zero Trust, Cloud Security, Risk Assessment, Security Governance  
**Status:** Architecture design completed; proposed implementation not deployed.

## 1. Business Scenario

NorthStar Technologies is a fictional organization with approximately 200 employees working remotely and from an office environment.

The organization uses Microsoft Azure and Amazon Web Services (AWS) and requires a more consistent approach to identity management, privileged access, cloud security, and monitoring.

This project develops a proposed enterprise IAM and Zero Trust architecture to address these requirements.

## 2. Project Objectives

- Design centralized identity management.
- Establish role-based access control and least privilege.
- Define MFA and Conditional Access requirements.
- Develop privileged access management procedures.
- Propose secure workforce access to AWS and Azure.
- Apply Zero Trust security principles.
- Identify threats and assess security risks.
- Develop a phased implementation roadmap.

## 3. Architecture Overview

The proposed architecture uses:

- **Microsoft Entra ID:** Central workforce identity provider.
- **Microsoft Entra MFA and Conditional Access:** Authentication and contextual access controls.
- **AWS IAM Identity Center:** Federated workforce access to AWS.
- **Azure RBAC:** Role-based access to Azure resources.
- **Privileged access controls:** Separate administrative accounts and controlled elevation.
- **Microsoft Sentinel:** Proposed centralized security monitoring.
- **AWS CloudTrail and Azure Activity Logs:** Cloud activity auditing.

## 4. Project Deliverables

| Document / Exercise | Description |
|---|---|
| Business and Security Requirements | Defines organizational needs and security objectives |
| Current-State Security Assessment | Identifies hypothetical security gaps |
| Enterprise IAM Architecture | Describes the proposed identity architecture |
| IAM Access Control Matrix | Defines roles, permissions, and access governance |
| Zero Trust Security Design | Maps Zero Trust principles to practical controls |
| Threat Model and Risk Register | Identifies threats, evaluates risks, and recommends mitigations |
| Implementation Roadmap | Defines phased implementation priorities |
| Python IAM Access Review Exercise | Analyses simulated employee permissions against stated job requirements |
| Analyst Decision Tracking | Documents simulated access review decisions, justifications, and recommended actions |
| Consolidated IAM Audit Report | Combines permission findings and analyst decisions into an audit-friendly CSV report |

## 5. Skills Demonstrated

- Enterprise IAM architecture design
- Identity lifecycle management
- Role-Based Access Control (RBAC)
- Least-privilege access assessment
- Multifactor authentication (MFA)
- Conditional Access concepts
- Privileged Access Management (PAM)
- Zero Trust security principles
- AWS and Azure identity integration concepts
- Python-based access analysis
- CSV data processing and audit reporting
- Permission mismatch identification
- Privileged access review
- Access governance and analyst decision documentation
- Threat modelling and risk assessment
- Security governance and technical documentation

## 6. Frameworks and Technologies

**Technologies and platforms considered:**
- Microsoft Entra ID
- Microsoft Azure
- Amazon Web Services (AWS)
- AWS IAM Identity Center
- Azure RBAC
- Microsoft Sentinel

**Security concepts and frameworks:**
- Zero Trust Architecture
- NIST SP 800-207
- Identity and Access Management
- Least Privilege
- Defence in Depth
- Risk-Based Access Control

## 7. Project Limitations

The practical IAM access review exercise uses fictional employee records and simulated analyst decisions. Python-based analysis and CSV report generation were performed locally. No live identity provider, AWS account, or Azure subscription was connected, and no actual user permissions were changed or revoked.

## 8. Conclusion

This project demonstrates how IAM and Zero Trust principles can be applied to design a secure enterprise identity and cloud access model.

It brings together identity governance, privileged access, cloud security, threat modelling, risk management, and implementation planning into a single architecture case study.