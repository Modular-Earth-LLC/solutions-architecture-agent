# Azure ↔ AWS Service Mapping
## AI-Driven Prior Authorization | Autonomize AI Interview
### Paul Prae | Principal AI Engineer & Architect

> **How to use this file**: This is your translation layer. When Ujjwal or Suresh asks about an Azure service you don't know deeply, anchor on the AWS equivalent you do know deeply. The patterns are identical — the vendor APIs are the easy part.

---

## Complete Service Mapping Table

| Generic Function | Azure Service | AWS Equivalent | Paul's Depth | Key Difference |
|---|---|---|---|---|
| AI Model Access | Azure AI Foundry (model catalog) | Amazon Bedrock | AWS deep | Azure is only cloud with Claude + GPT in same env |
| Agent Runtime | Azure AI Foundry Agent Service | Amazon Bedrock Agents | AWS deep | Both support MCP protocol; Azure in free preview until Apr 2026 |
| AI Search / RAG | Azure AI Search | Amazon OpenSearch (AOSS) | AWS familiar | Azure supports hybrid vector + keyword natively |
| Document OCR / Extraction | Azure AI Document Intelligence | Amazon Textract | AWS deep | Functionally equivalent; form extraction, clinical docs |
| Container Compute | Azure Container Apps | Amazon ECS (Fargate) | AWS deep | Container Apps = managed K8s; ECS Fargate = serverless containers |
| Kubernetes (advanced) | AKS (Azure Kubernetes Service) | Amazon EKS | AWS deep | Same underlying K8s; different managed plane implementations |
| Message Queue (standard) | Azure Service Bus | Amazon SQS | AWS deep | Service Bus Premium = HIPAA BAA eligible; SQS is BAA-eligible by default |
| Event Streaming (future) | Azure Event Hubs | Amazon Kinesis Data Streams | AWS familiar | Both are Kafka-compatible; Kinesis has tighter AWS integration |
| Serverless Functions | Azure Functions | AWS Lambda | AWS deep | Functionally equivalent; different cold-start characteristics |
| API Gateway | Azure API Management (APIM) | Amazon API Gateway | AWS deep | APIM has richer developer portal; both support WAF integration |
| Healthcare FHIR | Azure Health Data Services | AWS HealthLake | AWS familiar | Both HIPAA/HITRUST; Azure includes DICOM natively |
| Relational Database | Azure Database for PostgreSQL | Amazon RDS for PostgreSQL | AWS deep | Both managed Postgres; different HA/failover configurations |
| Object Storage | Azure Blob Storage | Amazon S3 | AWS deep | Functionally equivalent; both support immutable storage policies |
| Cache | Azure Cache for Redis | Amazon ElastiCache (Redis) | AWS deep | Same Redis protocol; managed service on both sides |
| CDN / Edge | Azure Front Door | Amazon CloudFront | AWS familiar | Front Door includes WAF; CloudFront requires separate WAF config |
| Identity / AuthN | Microsoft Entra ID | AWS IAM + Amazon Cognito | AWS deep | Entra ID has native SMART on FHIR support; Cognito requires custom |
| Secrets Management | Azure Key Vault | AWS Secrets Manager + KMS | AWS deep | Functionally equivalent; Key Vault unifies key + secret management |
| Monitoring / Observability | Azure Monitor + App Insights | Amazon CloudWatch + X-Ray | AWS deep | Both support OpenTelemetry; App Insights has richer APM defaults |
| Log Management | Log Analytics Workspace | CloudWatch Logs + Athena | AWS deep | Log Analytics uses KQL; CloudWatch uses CloudWatch Insights |
| Network / VNet | Azure Virtual Network (VNet) | Amazon VPC | AWS deep | Same concepts; different subnet/peering syntax |
| Private Connectivity | Azure Private Endpoint | AWS PrivateLink | AWS deep | Functionally equivalent; both prevent public internet exposure |
| WAF | Azure Web Application Firewall | AWS WAF | AWS deep | Both support OWASP Top 10; different rule syntax |
| Data Encryption at Rest | Azure Disk Encryption + ADE | AWS KMS + EBS encryption | AWS deep | Same underlying principle; customer-managed keys available in both |
| Infrastructure as Code | Azure Bicep / ARM Templates | AWS CloudFormation / CDK | AWS deep (CDK) | Bicep is ARM's improvement; CDK equivalent is Pulumi or Bicep |
| CI/CD | Azure DevOps / GitHub Actions | AWS CodePipeline / GitHub Actions | Both | GitHub Actions is cloud-agnostic; both use it |

---

## When to Mention AWS in the Interview

**Frame**: "My AWS experience gives me deep pattern familiarity — the same architecture on Azure uses different service names but identical design principles."

**Use this when**:
- Ujjwal asks "have you used Azure before?" → "I'm AWS-certified at the Solutions Architect and specialty levels. Every service in this architecture has a direct AWS equivalent I know deeply — the patterns are identical. The Azure-specific APIs are the learning curve, not the architecture."
- Someone questions your Azure depth → "I designed this architecture with Azure because Autonomize is Azure-native. I validated each service choice against Microsoft's own documentation. And I can map every decision back to AWS patterns I've implemented in production."

**Do NOT volunteer your AWS background unprompted** — they're an Azure-native shop. Lead with Azure; have AWS as a credibility anchor when challenged.

---

## Key Azure Services to Review Before the Interview

These are Azure-specific. You can't fully substitute with "same as AWS" on these:

### 1. Azure AI Foundry
- What it is: Microsoft's unified AI development platform — model catalog (Claude, GPT-4, Llama), Agent Service, Prompt Flow, evals
- Why it's in the architecture: Hosts the AI models Paul's PA Copilot calls; Agent Service provides the agentic runtime
- 5-minute review: [Azure AI Foundry overview](https://learn.microsoft.com/en-us/azure/foundry/)
- Key fact: Agent Service is in free preview until April 2026 — mention this as a Phase 0 cost advantage

### 2. Azure Health Data Services
- What it is: Managed FHIR R4 server + DICOM + MedTech services in one Azure resource
- Why it's in the architecture: Clinical Data Aggregation component — normalizes and stores FHIR data
- AWS equivalent: AWS HealthLake (less feature-rich; no DICOM)
- Key fact: HIPAA and HITRUST certified out of the box

### 3. Azure Service Bus (Premium tier)
- What it is: Enterprise message broker — queues and topics, similar to SQS/SNS hybrid
- Why it's in the architecture: Async decoupling between ingestion and AI engine
- Critical detail: Premium tier is required for HIPAA BAA coverage; Standard tier is not eligible
- Key fact: Sessions feature enables message ordering — useful if PA requests have sequence dependencies

### 4. Azure API Management (APIM)
- What it is: Full-lifecycle API gateway — rate limiting, auth, developer portal, analytics
- Why it's in the architecture: PA Ingestion Gateway front door; handles all three intake channels
- AWS equivalent: Amazon API Gateway + custom developer portal
- Key fact: APIM has native Azure Active Directory integration for OAuth 2.0

### 5. Azure Container Apps
- What it is: Serverless container platform built on Kubernetes — no K8s control plane to manage
- Why it's in the architecture: Deployment platform for all custom services (aggregation, routing, response)
- AWS equivalent: Amazon ECS on Fargate (managed compute) or App Runner (higher abstraction)
- Key fact: Native support for KEDA (event-driven autoscaling) — scales based on Service Bus queue depth

### 6. Microsoft Entra ID (formerly Azure Active Directory)
- What it is: Microsoft's cloud identity platform — SSO, RBAC, conditional access
- Why it's in the architecture: RBAC for clinical reviewers; service account management; SMART on FHIR
- Key healthcare fact: Native SMART on FHIR support for OAuth 2.0 flows with FHIR APIs — this is a significant advantage over Cognito

---

## How Paul's AWS Experience Translates

### 5 AWS Certifications — What They Signal

| Cert | What It Demonstrates for This Role |
|---|---|
| AWS Solutions Architect (Associate + Professional) | Deep understanding of distributed systems, cloud-native architecture, well-architected principles — all transfer directly to Azure |
| AWS Machine Learning Specialty | ML system design: data pipelines, model deployment, monitoring, inference optimization — directly applicable to LLMOps pipeline |
| AWS SysOps / DevOps (if held) | Operational excellence: IaC, CI/CD, monitoring, incident response — cloud-agnostic principles |

### 3 Years as AWS Solutions Architect — Healthcare Focus

"In my AWS SA role, I designed architectures for healthcare customers at scale — eligibility APIs, clinical data platforms, PHI handling in the cloud. The patterns I built in AWS translate directly: SQS → Service Bus, CloudWatch → Azure Monitor, Textract → Document Intelligence, Bedrock → Azure AI Foundry. The healthcare compliance layer — HIPAA, HITRUST, minimum necessary access — is identical on both clouds."

### The Honest Framing

Paul has not deployed production systems on Azure. He has designed Azure architectures using Microsoft documentation and first-principles translation from AWS. That's an honest position and a defensible one for a Principal Architect candidate:

"I designed this architecture using Azure because Autonomize is Azure-native. I validated every service choice. I haven't operated an Azure production environment the way I've operated AWS — but the architectural decision-making is the same discipline. I'd accelerate quickly on Azure specifics; the design fundamentals are already there."

---

## Quick-Reference: "What Is That?" for Common Azure Terms

| Term Ujjwal Might Use | What It Means | AWS Analog |
|---|---|---|
| Azure Resource Group | Logical container for related resources — billing, access, lifecycle | CloudFormation Stack |
| Azure Subscription | Billing and resource boundary — like an AWS Account | AWS Account |
| Management Group | Hierarchy above subscriptions — enterprise governance | AWS Organizations OU |
| Azure Policy | Guardrails that enforce compliance on resources | AWS Config + SCPs |
| Log Analytics Workspace | Centralized log store — uses KQL query language | CloudWatch Logs + Insights |
| KQL (Kusto Query Language) | Azure's log query language | CloudWatch Insights syntax |
| Managed Identity | Service principal without credentials — automatic auth | IAM Role for EC2/Lambda |
| Azure Arc | Extend Azure management to on-prem / multi-cloud | AWS Outposts / Systems Manager hybrid |
| Azure Monitor Workbook | Dashboard/visualization for metrics + logs | CloudWatch Dashboard |
| Bicep | Azure IaC language (ARM replacement) | CloudFormation YAML or CDK |
