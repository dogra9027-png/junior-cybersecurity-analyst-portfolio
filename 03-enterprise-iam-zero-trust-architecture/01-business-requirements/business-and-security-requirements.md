# NorthStar Technologies – Business and Security Requirements

## 1. Organization Overview

NorthStar Technologies is a fictional mid-sized organization with approximately 200 employees.

The organization operates through a combination of office-based and remote work arrangements. Its business applications and workloads are hosted across Microsoft Azure and Amazon Web Services (AWS).

The organization requires a centralized and secure identity management approach to protect access to business applications, cloud resources and sensitive information.

## 2. Business Requirements

The proposed IAM and Zero Trust architecture must support the following business requirements:

| ID | Business Requirement |
|---|---|
| BR-01 | Support secure access for approximately 200 employees. |
| BR-02 | Provide secure access for both office-based and remote employees. |
| BR-03 | Support access to applications and resources hosted in AWS and Azure. |
| BR-04 | Simplify identity administration through centralized identity management. |
| BR-05 | Support different access privileges based on employee responsibilities. |
| BR-06 | Protect administrative accounts and sensitive business resources. |
| BR-07 | Provide visibility into user authentication and access activities. |
| BR-08 | Support future organizational growth and additional cloud services. |

## 3. Security Requirements

| ID | Security Requirement | Priority |
|---|---|---|
| SR-01 | Enforce Multi-Factor Authentication (MFA) for user access. | Critical |
| SR-02 | Implement Role-Based Access Control (RBAC). | High |
| SR-03 | Apply least-privilege access principles. | Critical |
| SR-04 | Protect privileged accounts using dedicated administrative controls. | Critical |
| SR-05 | Apply Conditional Access policies based on identity and access context. | High |
| SR-06 | Maintain centralized authentication and access logs. | High |
| SR-07 | Review and revoke access when employees change roles or leave. | High |
| SR-08 | Apply Zero Trust principles to access decisions. | Critical |
| SR-09 | Protect cloud resources through appropriate identity and network controls. | High |
| SR-10 | Monitor suspicious authentication and access activities. | High |

## 4. User Categories

The organization will use the following initial identity categories:

| User Category | Description |
|---|---|
| Standard Employees | Access business applications and approved organizational resources. |
| IT Support | Perform approved IT support and account administration tasks. |
| Cloud Administrators | Manage designated AWS and Azure cloud resources. |
| Security Analysts | Monitor security events and investigate suspicious activity. |
| Senior Management | Access approved management applications and business information. |

## 5. Proposed Security Principles

The architecture will follow these principles:

### Least Privilege
Users receive only the permissions required to perform their assigned responsibilities.

### Zero Trust
Access is not automatically trusted based on network location. Identity, device and access context must be evaluated.

### Defense in Depth
Multiple security controls protect identities, applications, cloud infrastructure and organizational data.

### Separation of Duties
Sensitive administrative and business activities should be separated to reduce unauthorized access and misuse.

### Continuous Monitoring
Authentication, authorization and privileged access activities should be logged and monitored.

## 6. Assumptions and Scope

This project is a conceptual architecture case study based on a fictional organization.

Assumptions:
- Approximately 200 employees.
- AWS and Azure are both used.
- Employees work remotely and from an office.
- A centralized identity provider will be selected during architecture design.
- Existing identity and access processes require improvement.

Out of scope:
- Production deployment.
- Live integration with company identity systems.
- Real employee information or credentials.
- Actual cloud subscription configuration.

## 7. Expected Outcomes

The proposed architecture should provide:

- Centralized identity governance.
- Strong authentication and access management.
- Reduced risk of unauthorized access.
- Improved privileged account protection.
- Secure access to cloud resources.
- Better visibility into identity-related security events.

## 8. Document Status

Status: Initial requirements baseline  
Project: Enterprise IAM and Zero Trust Architecture  
Organization: NorthStar Technologies (fictional)