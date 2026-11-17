# Enterprise IAM Architecture Diagram

## Project Context

This diagram represents the proposed identity and access architecture for NorthStar Technologies, a fictional organization.

## Architecture

```mermaid
flowchart TD
    A["Employees and Administrators"] --> B["Microsoft Entra ID"]
    B --> C["Identity Verification and MFA"]
    C --> D["Conditional Access Evaluation"]

    D --> E["Access Decision"]

    E -->|Approved| F["Authorized Access"]
    E -->|Denied| G["Block or Restrict Access"]

    F --> H["Business Applications"]
    F --> I["AWS IAM Identity Center"]
    F --> J["Microsoft Azure RBAC"]

    I --> K["AWS Cloud Resources"]
    J --> L["Azure Cloud Resources"]

    H --> M["Application Activity Logs"]
    I --> N["AWS CloudTrail"]
    J --> O["Azure Activity Logs"]
    B --> P["Entra Sign-in and Audit Logs"]

    M --> Q["Centralized Security Monitoring"]
    N --> Q
    O --> Q
    P --> Q

    Q --> R["Proposed Microsoft Sentinel SIEM"]
    R --> S["Security Alerts and Investigation"]
```

## Architecture Components

| Component | Purpose |
|---|---|
| Microsoft Entra ID | Central workforce identity management |
| MFA | Additional authentication verification |
| Conditional Access | Context-based access decisions |
| AWS IAM Identity Center | Federated workforce access to AWS |
| Azure RBAC | Controls permissions to Azure resources |
| AWS CloudTrail | Records AWS account activity |
| Azure Activity Logs | Records Azure resource and subscription activity |
| Microsoft Sentinel | Proposed centralized security monitoring |

## Important Note

This is a conceptual architecture diagram for a fictional organization. It has not been deployed or validated in a live cloud environment.