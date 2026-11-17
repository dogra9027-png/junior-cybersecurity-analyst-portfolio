# Enterprise IAM and Zero Trust Architecture

## Project Overview

This project presents an enterprise Identity and Access Management (IAM) and Zero Trust security architecture for a fictional organization, NorthStar Technologies.

The organization has approximately 200 employees working across office and remote environments, with workloads hosted across Amazon Web Services (AWS) and Microsoft Azure.

The objective is to design a secure, scalable identity and access management approach that protects organizational resources through centralized identity governance, strong authentication, least-privilege access and continuous security verification.

## Business Scenario

NorthStar Technologies requires a modern identity security architecture to support:

- Centralized identity management for employees and administrators.
- Secure access for remote and office-based employees.
- Multi-Factor Authentication (MFA).
- Role-Based Access Control (RBAC).
- Privileged Access Management (PAM).
- Secure access to AWS and Azure resources.
- Least-privilege access policies.
- Continuous monitoring and security logging.

## Project Objectives

1. Assess the organization's identity and access management requirements.
2. Develop an enterprise IAM architecture.
3. Apply Zero Trust security principles.
4. Define employee and administrator access models.
5. Design secure access to AWS and Azure resources.
6. Identify identity-related threats and security risks.
7. Recommend appropriate security controls.
8. Develop a phased implementation roadmap.

## Planned Deliverables

| Area | Deliverable |
|---|---|
| Business requirements | Business and security requirements document |
| Current-state assessment | Identity security gap assessment |
| Architecture design | Enterprise IAM architecture diagram |
| IAM | Identity roles and access control matrix |
| Zero Trust | Zero Trust security design |
| Threat modelling | Threat model and risk register |
| Implementation | Phased implementation roadmap |
| Practical IAM exercise | Python-based employee access review and permission analysis |
| Access governance | Simulated analyst decisions, approval tracking and least-privilege review |
| Audit reporting | Consolidated IAM access review report |

## Practical IAM Access Review Exercise

A Python-based practical exercise was developed to demonstrate employee permission analysis and access governance.

The exercise uses simulated employee records to:

- Compare assigned permissions against stated job requirements.
- Identify potentially excessive access.
- Flag privileged AWS and Azure permissions for additional review.
- Document analyst decisions, justifications and recommended next actions.
- Generate consolidated CSV-based IAM audit reports.

**Tools:** Python 3, CSV, PowerShell and Visual Studio Code.

**Exercise location:** `08-evidence/iam-practical-exercise/`

The exercise uses fictional data and does not modify permissions in live cloud environments.

## Technologies and Concepts

- Microsoft Entra ID
- AWS Identity and Access Management (IAM)
- Role-Based Access Control (RBAC)
- Multi-Factor Authentication (MFA)
- Single Sign-On (SSO)
- Privileged Access Management (PAM)
- Conditional Access
- Zero Trust Architecture
- AWS and Azure security controls
- Security monitoring and logging

## Project Approach

The architecture will be developed as a documented design case study using a fictional business scenario.

Cloud configurations and architecture recommendations will be clearly distinguished from controls implemented and tested in live environments.

## Project Status

In progress.

## Learning Outcomes

This project aims to demonstrate practical understanding of enterprise IAM design, Zero Trust principles, cloud identity security, access governance, threat modelling and security architecture documentation.