# Study Guide -- Night Before / Morning Of
## AI-Driven Prior Authorization — Autonomize AI Interview

> Study this to build confidence. For the presentation itself, use [speaker-script.md](../speaker-script.md) alongside [presentation.md](../presentation.md).

---

## 1. Azure to AWS Service Mapping

### Complete Service Mapping Table

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

### Key Azure Services to Review

These are Azure-specific. You can't fully substitute with "same as AWS" on these:

**1. Azure AI Foundry**
- What it is: Microsoft's unified AI development platform -- model catalog (Claude, GPT-4, Llama), Agent Service, Prompt Flow, evals
- Why it's in the architecture: Hosts the AI models PA Copilot calls; Agent Service provides the agentic runtime
- 5-minute review: [Azure AI Foundry overview](https://learn.microsoft.com/en-us/azure/foundry/)
- Key fact: Agent Service is in free preview until April 2026 -- mention this as a Phase 0 cost advantage

**2. Azure Health Data Services**
- What it is: Managed FHIR R4 server + DICOM + MedTech services in one Azure resource
- Why it's in the architecture: Clinical Data Aggregation component -- normalizes and stores FHIR data
- AWS equivalent: AWS HealthLake (less feature-rich; no DICOM)
- Key fact: HIPAA and HITRUST certified out of the box

**3. Azure Service Bus (Premium tier)**
- What it is: Enterprise message broker -- queues and topics, similar to SQS/SNS hybrid
- Why it's in the architecture: Async decoupling between ingestion and AI engine
- Critical detail: Premium tier is required for HIPAA BAA coverage; Standard tier is not eligible
- Key fact: Sessions feature enables message ordering -- useful if PA requests have sequence dependencies

**4. Azure API Management (APIM)**
- What it is: Full-lifecycle API gateway -- rate limiting, auth, developer portal, analytics
- Why it's in the architecture: PA Ingestion Gateway front door; handles all three intake channels
- AWS equivalent: Amazon API Gateway + custom developer portal
- Key fact: APIM has native Azure Active Directory integration for OAuth 2.0

**5. Azure Container Apps**
- What it is: Serverless container platform built on Kubernetes -- no K8s control plane to manage
- Why it's in the architecture: Deployment platform for all custom services (aggregation, routing, response)
- AWS equivalent: Amazon ECS on Fargate (managed compute) or App Runner (higher abstraction)
- Key fact: Native support for KEDA (event-driven autoscaling) -- scales based on Service Bus queue depth

**6. Microsoft Entra ID (formerly Azure Active Directory)**
- What it is: Microsoft's cloud identity platform -- SSO, RBAC, conditional access
- Why it's in the architecture: RBAC for clinical reviewers; service account management; SMART on FHIR
- Key healthcare fact: Native SMART on FHIR support for OAuth 2.0 flows with FHIR APIs -- this is a significant advantage over Cognito

### How Your AWS Experience Translates

**5 AWS Certifications -- What They Signal**

| Cert | What It Demonstrates for This Role |
|---|---|
| AWS Solutions Architect (Associate + Professional) | Deep understanding of distributed systems, cloud-native architecture, well-architected principles -- all transfer directly to Azure |
| AWS Machine Learning Specialty | ML system design: data pipelines, model deployment, monitoring, inference optimization -- directly applicable to LLMOps pipeline |
| AWS SysOps / DevOps (if held) | Operational excellence: IaC, CI/CD, monitoring, incident response -- cloud-agnostic principles |

**3 Years as AWS Solutions Architect -- Healthcare Focus**

"In my AWS SA role, I designed architectures for healthcare customers at scale -- eligibility APIs, clinical data platforms, PHI handling in the cloud. The patterns I built in AWS translate directly: SQS to Service Bus, CloudWatch to Azure Monitor, Textract to Document Intelligence, Bedrock to Azure AI Foundry. The healthcare compliance layer -- HIPAA, HITRUST, minimum necessary access -- is identical on both clouds."

**The Honest Framing**

Paul has not deployed production systems on Azure. He has designed Azure architectures using Microsoft documentation and first-principles translation from AWS. That's an honest position and a defensible one for a Principal Architect candidate:

"I designed this architecture using Azure because Autonomize is Azure-native. I validated every service choice. I haven't operated an Azure production environment the way I've operated AWS -- but the architectural decision-making is the same discipline. I'd accelerate quickly on Azure specifics; the design fundamentals are already there."

### Azure Terminology Quick Reference

| Term Ujjwal Might Use | What It Means | AWS Analog |
|---|---|---|
| Azure Resource Group | Logical container for related resources -- billing, access, lifecycle | CloudFormation Stack |
| Azure Subscription | Billing and resource boundary -- like an AWS Account | AWS Account |
| Management Group | Hierarchy above subscriptions -- enterprise governance | AWS Organizations OU |
| Azure Policy | Guardrails that enforce compliance on resources | AWS Config + SCPs |
| Log Analytics Workspace | Centralized log store -- uses KQL query language | CloudWatch Logs + Insights |
| KQL (Kusto Query Language) | Azure's log query language | CloudWatch Insights syntax |
| Managed Identity | Service principal without credentials -- automatic auth | IAM Role for EC2/Lambda |
| Azure Arc | Extend Azure management to on-prem / multi-cloud | AWS Outposts / Systems Manager hybrid |
| Azure Monitor Workbook | Dashboard/visualization for metrics + logs | CloudWatch Dashboard |
| Bicep | Azure IaC language (ARM replacement) | CloudFormation YAML or CDK |

---

## 2. Per-Diagram Talking Points

### Diagram 1: System Context (Slide 3)

**What it shows**: Four external actors, one AI platform in the middle. The executive view.

**Talking Points:**
1. **"Four actors, one platform in the middle."** Providers submit PA requests through existing channels -- fax, portal, EDI. The health plan's core systems provide eligibility and clinical data. Autonomize's PA Copilot sits in the middle. Regulators receive compliance reporting. This is the non-technical stakeholder view.
2. **"Nothing new in the process -- everything new in the execution."** The PA business process is standardized by AMA and CAQH. This architecture doesn't reinvent the process. It automates steps 3, 4, and 5 using AI. That framing matters for a COO audience.
3. **"Bidirectional integration with the Payer Core."** PA Copilot reads from the Payer Core (eligibility, benefits) and writes to it (determinations). That bidirectional relationship is the most critical integration -- and the one with the most unknowns until we see the actual API specification.
4. **"Compliance reporting flows to regulators as output, not as an afterthought."** CMS-0057-F metrics are a first-class output, not a reporting bolt-on. That's an architectural decision showing regulators this isn't a last-minute compliance patch.

**If asked to go deeper:**
- "What's the data flow for a single PA request?" -- "Let me take you to slide 5 -- the PA processing flow is the detailed view of that."
- "How does the PA Copilot actually connect to the health plan's systems?" -- "That's the integration detail on slide 7 -- three specific integration points, each with the protocol and auth model."

### Diagram 2: Component Architecture (Slide 4)

**What it shows**: 10 components across 5 layers, with data flow arrows and Azure service labels.

**Talking Points:**
1. **"Five layers, each with a clear responsibility boundary."** Ingestion layer receives and normalizes. Integration layer connects to external systems. AI engine reviews and routes. Human review handles exception cases. Response layer closes the loop back to the Payer Core and notifies providers. Clean separation of concerns.
2. **"The AI engine is Autonomize's PA Copilot -- I'm integrating it, not rebuilding it."** PA Copilot and Genesis Platform are Autonomize's product. My job is to wire it correctly into the health plan's ecosystem with the right auth, data contracts, and safety controls.
3. **"Azure Service Bus is the decoupling mechanism."** The message queue sits between ingestion and the AI engine. Nothing calls the AI engine synchronously except what has to be synchronous. That queue is why the system is resilient to Autonomize platform outages and traffic spikes.
4. **"Every path ends at the audit and compliance store."** Follow any data flow arrow -- it terminates at immutable Blob Storage. All paths write to the audit trail. CMS-0057-F and HIPAA require tamper-proof decision records; the immutable storage designation is the architectural response.

**If asked to go deeper:**
- "How does the Document Processing pipeline handle different file types?" -- "OCR for faxes is Azure AI Document Intelligence. PDFs from the portal go through the same pipeline. EDI bypasses OCR entirely -- it's already structured. The output in all cases is a canonical JSON PA record on Service Bus."
- "Why Azure Container Apps over AKS?" -- "Container Apps is managed Kubernetes -- autoscaling and container orchestration without managing control plane infrastructure. AKS is the right choice if you need deep Kubernetes customization. At PA volumes of 1-3M/month, Container Apps handles it. AKS is a Phase 3 consideration."

### Diagram 3: PA Processing Flow (Slide 5)

**What it shows**: The 6-step PA lifecycle from provider submission to determination, with three routing outcomes.

**Talking Points:**
1. **"This is the AMA/CAQH standard PA process -- we're not inventing steps, we're automating them."** Receive, validate eligibility, retrieve clinical data, review, determine, respond. The innovation is in the speed and consistency of steps 4 and 5.
2. **"Three determination outcomes, configured by clinical governance -- not hardcoded."** Auto-approve fires when confidence is above the threshold. Human review fires when confidence is below. Pend fires when data is insufficient. The threshold is a parameter, not a constant.
3. **"Auto-denial is explicitly not on this diagram."** That's intentional. Phase 1 has no auto-denial path. If the AI is confident it should be denied, it still goes to a human reviewer. That's a safety and regulatory position -- not a technical limitation.

**If asked to go deeper:**
- "What happens to the PA request that gets pended?" -- "The system notifies the provider with a specific request for additional clinical information needed. It's queued for reprocessing when the provider responds. CMS-0057-F mandates the response timing, so the pend state has a clock attached."
- "What about urgent PA requests -- different flow?" -- "Same steps, different SLA clock. CMS-0057-F requires 24-hour turnaround for urgent vs. 72 hours for standard. The system tags urgency at ingestion and the confidence threshold for auto-routing can be adjusted for urgent cases."

### Diagram 4: Clinical Data Integration (Slide 7)

**What it shows**: Two-source clinical data architecture -- FHIR R4 for modern EMRs, legacy DB connectors for older systems.

**Talking Points:**
1. **"Two worlds, one aggregation layer."** Modern EMRs -- Epic, Oracle Health, Cerner -- expose FHIR R4 endpoints natively. Older systems don't. The aggregation service handles both, normalizing to FHIR-compatible format before the AI engine sees it.
2. **"FHIR R4 is the interoperability label, not a deep implementation commitment."** I use FHIR R4 as the standard because it's the CMS-mandated baseline and modern EMRs speak it natively. What I haven't done is design a full FHIR server with Da Vinci Implementation Guide conformance -- that's a clinical informatics project.
3. **"PHI tokenization happens at this boundary."** Before any clinical data crosses into the AI engine, PHI is tokenized. The AI sees clinical facts without patient identity. The de-identified clinical context is sufficient for coverage matching.

**If asked to go deeper:**
- "What specific FHIR resources does the AI receive?" -- "Patient (tokenized), Encounter, Observation, DiagnosticReport, Condition, MedicationRequest. Those six resources give the AI the clinical narrative for coverage matching. Additional resources -- CarePlan, Procedure history -- are Phase 2 additions."
- "How does SMART on FHIR auth work in this architecture?" -- "The aggregation service authenticates to each FHIR endpoint using a service account with read-only scope. Entra ID manages the credentials and enforces conditional access. Minimum necessary access -- it can read clinical resources for the specific member in the PA request, nothing broader."

### Diagram 5: LLMOps Pipeline (Slide 8)

**What it shows**: The four-step feedback loop for monitoring and maintaining AI output quality over time.

**Talking Points:**
1. **"This is LLMOps, not MLOps -- the monitoring approach is fundamentally different."** We're not retraining models. LLMOps monitors output quality: are the determinations correct? Are the reasoning chains valid? Are human reviewers overturning AI recommendations at an acceptable rate? The signal is behavioral, not statistical.
2. **"Human reviewer corrections are the most valuable signal in the system."** When a reviewer overturns an AI recommendation, that correction is captured and feeds into the eval dataset. Over time, human-validated cases become the benchmark against which new model versions are tested.
3. **"Guardrails are always active -- they don't turn off during blue-green deployment."** Input filtering, output validation, and citation requirements are enforced regardless of what model version is running. They're infrastructure, not application logic.

**If asked to go deeper:**
- "How do you decide when to trigger model revalidation?" -- "Three triggers: overturn rate exceeds baseline by more than X% over a rolling window; confidence distribution shifts detectably; or eval pass rate drops below acceptance threshold. Specific thresholds are business parameters set by clinical governance."
- "What if a new model version is worse -- rollback?" -- "Blue-green deployment means the previous version is still running. Traffic shift is incremental -- 10%, then 25%, then 100%. If metrics degrade at any shift point, we shift traffic back. Rollback time is under a minute."

### Diagram 6: Security & Zero Trust (Slide 6)

**What it shows**: Three top security risks with architectural mitigations. Table format rather than flow diagram.

**Talking Points:**
1. **"I led with AI-specific risks, not generic cloud security."** PHI exposure through the AI pipeline and prompt injection are novel attack surfaces in healthcare AI. Leading with AI-specific risks signals security-informed AI architecture.
2. **"PHI tokenization is the key AI safety control."** The AI engine never sees patient identity. Even if the AI is compromised or an adversarial clinical document attempts extraction, there's no PHI to exfiltrate.
3. **"The audit trail is the regulatory defense artifact."** Every determination record contains: model version, input document hash, clinical context hash, reasoning chain, evidence citations, confidence score, and reviewer identity if applicable. Immutable 7-year retention.
4. **"Human review for all denials is a safety principle, not a Phase 1 limitation."** The principle that auto-denial requires stronger governance than auto-approval is permanent. The asymmetry exists because denying access to care has higher stakes than approving it.

**If asked to go deeper:**
- "What about HIPAA BAA coverage for Azure services?" -- "All Azure services in this architecture are covered by Microsoft's HIPAA BAA. Service Bus Premium tier specifically requires the Premium SKU for BAA coverage. Standard tier is not BAA-eligible."
- "What about SOC 2 / HITRUST for the deployment?" -- "Azure Health Data Services and the core services are HITRUST-certified. Autonomize AI has HIPAA BAA and SOC 2 Type 2. The application layer we write needs to go through a HITRUST assessment -- that's scoped in Phase 3."

---

## 3. Assumptions & Discovery Questions

Every assumption in the architecture is a question you couldn't answer without a real client engagement. Knowing these questions -- and being able to articulate why they matter -- demonstrates the thoroughness of a Principal Architect.

**Opening frame**: "Every architecture starts with assumptions. A good SA makes them explicit, states which design decisions they support, and knows which questions to ask first. Here are mine."

### Ask Early -- These Impact the Overall Architecture

**A-1: PA Volume and Channel Distribution**
- Assumption: Top-5 US health plan scale -- approximately 1 to 3 million PA requests per month, with fax as the dominant channel.
- Design decision it supports: Service Bus Premium tier sizing; Document Processing pipeline as a core component; OCR capacity planning; Redis cache TTL calibration.
- Discovery question: "What is the actual monthly PA volume, and what percentage arrives via fax, web portal, and X12 278 EDI? Is volume seasonal or event-driven?"
- Why it matters: If 90% of volume is already via portal (structured input), the Document Processing pipeline is far simpler -- no OCR, no handwriting challenges. If volume is 10M/month, Service Bus and Container Apps sizing changes significantly.

**A-2: Payer Core System Interface**
- Assumption: The Payer Core System exposes a synchronous REST API for eligibility lookups and determination writes.
- Design decision it supports: Synchronous eligibility check as a blocking step in the PA flow; real-time determination write-back; Redis caching to reduce API load.
- Discovery question: "What is the Payer Core System? (TriZetto Facets, QNXT, Amisys, custom?) What does its API interface look like -- REST, SOAP, batch file, database connector? What are the rate limits and SLA guarantees?"
- Why it matters: If the Payer Core API is SOAP, integration is harder but not impossible. If it's batch-only (no real-time), the eligibility step can't be synchronous -- the architecture needs a pre-fetched eligibility cache or a redesigned flow.

**A-3: FHIR R4 Adoption Percentage**
- Assumption: A mix of FHIR R4-capable EMRs and legacy systems -- roughly 50/50 in Phase 1 scope.
- Design decision it supports: Clinical Data Aggregation service with both FHIR R4 connectors and legacy DB adapters; Phase 1 FHIR-only, Phase 2 legacy connector build.
- Discovery question: "Which EMR systems are deployed across the health plan's provider network? What percentage of those systems have live FHIR R4 endpoints? What are the legacy systems -- HL7 v2, flat files, direct DB access?"
- Why it matters: If 90% of clinical sources are FHIR R4-capable today, Phase 1 scope is much richer. If 90% are legacy, Phase 1 is very limited clinical context, and the AI's accuracy depends heavily on what's available from the FHIR minority.

**A-4: Autonomize Platform Components Available**
- Assumption: PA Copilot, Genesis Platform, and AI Studio are available to deploy for this engagement.
- Design decision it supports: The entire AI engine is Autonomize's product, not custom-built. Clinical Review Dashboard is AI Studio. Multi-tenant LOB config uses Genesis capabilities.
- Discovery question: "What Autonomize platform components are currently licensed or available under the engagement? Is this a net-new deployment or integration into an existing Autonomize deployment? What's the relationship with the Pegasus Program?"
- Why it matters: If only a subset of Genesis Platform is licensed, the architecture needs custom components for what's missing. If there's an existing Autonomize deployment at the health plan, integration patterns change.

**A-5: Cloud Commitment and Multi-Cloud Constraints**
- Assumption: Azure is the correct cloud platform with no conflicting commitments or regulatory restrictions.
- Design decision it supports: All service choices are Azure-native; no hybrid or multi-cloud routing.
- Discovery question: "Does the health plan have existing cloud commitments -- Enterprise Agreement discounts, Reserved Instance pools, compliance certifications in a specific cloud? Are there regulatory restrictions on cloud deployment for this data classification?"
- Why it matters: If there's a major AWS spend commitment and no Azure EA, the cost model changes. If a state regulator requires on-premises for certain data, the architecture needs a hybrid layer.

### Ask During Design -- These Impact Integration Specifics

**A-6: Clinical Guidelines Source**
- Assumption: The health plan uses a standard clinical guideline system (InterQual or MCG) that the AI engine can be configured against.
- Design decision it supports: AI engine coverage criteria configuration; eval dataset construction; human reviewer workflow design.
- Discovery question: "Which clinical guidelines does the health plan use for PA determinations -- InterQual, MCG, custom payer criteria, or a mix by LOB? How frequently are they updated, and what is the change management process?"
- Why it matters: If the health plan uses custom payer-specific criteria, that's a more complex configuration and knowledge base build than standard InterQual. Quarterly updates mean the LLMOps pipeline needs a guidelines change management workflow.

**A-7: Acceptable Confidence Threshold**
- Assumption: The health plan's clinical governance team will define an acceptable confidence threshold for auto-determination.
- Design decision it supports: Determination Router configuration; expected auto-determination rate; clinical reviewer queue sizing.
- Discovery question: "What is the current manual auto-approval rate -- PA requests that reviewers approve immediately without extended review? That's the baseline target for AI auto-determination. What confidence level would clinical governance require before auto-determination goes live?"
- Why it matters: If clinical governance wants 95% confidence before auto-determination, the auto-approval rate will be conservative -- maybe 20-30%. If they accept 80% confidence, auto-determination rate could reach Altais levels (50%).

**A-8: Fax Gateway Infrastructure**
- Assumption: The health plan has an existing fax gateway that can be integrated via SFTP file drop to Azure Blob Storage.
- Design decision it supports: Fax ingestion path -- SFTP to Blob to Document Processing -- is the correct pattern.
- Discovery question: "How is fax currently handled -- physical fax machines, virtual fax service (eFax, RightFax), or a clearinghouse? What format do fax files land in -- TIFF, PDF? Is there an existing fax API or is it SFTP file drop?"
- Why it matters: If there's a virtual fax service with an API (eFax has one), the integration is push-based and real-time. If it's SFTP file drop, we need a polling job and there's inherent latency.

**A-9: PA Denial Appeal Workflow**
- Assumption: The existing denial appeal workflow is out of scope for Phase 1 -- the system produces determinations, humans handle appeals.
- Design decision it supports: No appeals automation in Phase 1 scope. Audit trail is the appeals support mechanism.
- Discovery question: "What is the current PA denial appeal process? How many appeals are filed per month? Do clinicians manually pull the PA record to support appeals, or is there a workflow system? Is appeal automation on the roadmap?"
- Why it matters: If appeals are a major administrative burden, there's a Phase 2 opportunity to surface the AI's reasoning chain and evidence citations in the appeals workflow.

**A-10: LOB Rule Complexity**
- Assumption: 20 LOBs with different administrative rules, manageable with per-LOB configuration rather than separate deployments.
- Design decision it supports: Multi-tenant architecture with per-LOB config is sufficient; separate instances only where regulatory isolation is required.
- Discovery question: "What are the 20 lines of business? What are the key rule differences between them -- commercial vs. Medicare Advantage vs. Medicaid vs. Exchange? Are there LOBs with contractual data isolation requirements?"
- Why it matters: If commercial and Medicare Advantage share most coverage criteria, per-LOB config handles the differences easily. If Medicaid requires state-specific rules that differ significantly from commercial, the configuration model gets complex.

### Ask Before Go-Live -- These Impact Operations

**A-11: Clinical Reviewer Team Size and Workflow**
- Assumption: The health plan has an existing clinical reviewer team that will be onboarded to the Autonomize AI Studio dashboard.
- Discovery question: "How large is the current PA clinical reviewer team? Are reviewers generalists or specialists by LOB or clinical area? What is the current PA review workflow -- queue management, escalation paths, peer review? Are reviewers employed or contracted?"
- Why it matters: The Clinical Review Dashboard needs to match the existing workflow, not replace it. If reviewers specialize by clinical area, the routing logic should route to the right reviewer.

**A-12: State-Specific PA Requirements**
- Assumption: CMS-0057-F federal requirements are the primary compliance driver.
- Discovery question: "In which states does the health plan operate? What are the state-specific PA requirements that go beyond federal baseline -- some states have stricter PA timeframe requirements, specific denial reason codes, or gold-carding provisions. Has the compliance team completed a state-by-state mapping?"
- Why it matters: Several states (California AB 352, Texas HB 3459, New York) have additional requirements on PA timeframes, denial reasons, and AI-use disclosure.

**A-13: Legal Position on AI-Assisted Determination**
- Assumption: Legal has reviewed and approved AI-assisted auto-approval. Auto-denial requires additional legal review before Phase 2.
- Discovery question: "Has the health plan's legal team reviewed the use of AI in PA determination? What documentation is required for regulatory defense of an AI-assisted determination? Has the plan obtained legal opinion on CMS-0057-F AI disclosure requirements?"
- Why it matters: In February 2024, a federal judge ruled against UnitedHealth for using AI (NaviHealth) to deny claims without adequate oversight. The legal landscape for AI-assisted healthcare decisions is active.

**A-14: Payer Core SLA During PA Processing**
- Assumption: The Payer Core API can support the synchronous eligibility call within the PA processing latency budget (target: under 5 seconds).
- Discovery question: "What SLA does the Payer Core System API guarantee for eligibility lookups? What is the current P95 and P99 latency? Are there maintenance windows or known peak-load degradation periods?"
- Why it matters: If the Payer Core API SLA is 2 seconds P95 but 15 seconds P99, the Redis cache design becomes more important. If there are daily maintenance windows, the PA processing flow needs a graceful degradation path.

**A-15: Business Continuity and Regulatory Defense During Outage**
- Assumption: During Autonomize platform outages, PA requests queue and process on restoration within CMS-0057-F SLA windows.
- Discovery question: "What is the health plan's current business continuity plan for PA processing? During system outages, how are CMS-0057-F timeframe commitments maintained? What is the escalation path if Autonomize has an extended outage during high-volume periods?"
- Why it matters: CMS-0057-F has hard timeframe requirements -- 72 hours standard, 24 hours urgent. If Autonomize has a 4-hour outage during a high-volume period, can the queue drain fast enough on restoration to meet SLAs?

### Assumption Dependency Map

```
Architecture Shape          -> A-1 (volume), A-3 (FHIR %)
Integration Specifications  -> A-2 (Payer Core API), A-8 (fax gateway)
AI Engine Configuration     -> A-4 (Autonomize components), A-6 (guidelines), A-7 (threshold)
Deployment Platform         -> A-5 (cloud commitment)
Multi-tenant vs Multi-inst  -> A-10 (LOB complexity)
Phase 1 Scope               -> A-3 (FHIR %), A-9 (appeals)
Compliance Reporting        -> A-12 (state requirements), A-13 (legal position)
Operational Procedures      -> A-11 (reviewer workflow), A-14 (Payer Core SLA), A-15 (BCP)
```

### Interview Framing

**When Suresh asks a deep integration question you can't fully answer**:
"That's exactly the question I'd ask during discovery. I've designed around [assumption], but the actual answer determines [specific design decision]. Here's what I'd want to find out and why it matters."

**When Ujjwal asks about a design trade-off**:
"The architecture is designed around [assumption]. If the discovery finding is different -- for example, [alternative] -- the design pivots to [alternative approach]. I've documented both paths."

**When Kris asks about risk**:
"The top assumptions that could change the architecture are [A-1, A-2, A-4]. The first thing I'd do in a real engagement is validate those three. Everything else is integration detail that adjusts without reshaping the architecture."

---

## 4. Key Numbers to Know

| Metric | Value | Source |
|---|---|---|
| Manual PA cost (provider) | $10.97 | CAQH 2024 Index |
| Manual PA cost (payer) | $3.52 | CAQH 2024 Index |
| Automated PA cost | ~$0.05 | CAQH 2024 Index |
| Manual PA time (phone/fax) | 24 minutes per transaction | CAQH 2024 Index |
| Manual PA time (portal) | 16 minutes per transaction | CAQH 2024 Index |
| Electronic PA adoption rate | 35% of medical PAs | CAQH 2024 Index |
| Potential annual savings (full electronic) | $494 million | CAQH 2024 Index |
| Altais review time reduction | 45% | BusinessWire Feb 2026 |
| Altais error reduction | 54% | BusinessWire Feb 2026 |
| Altais auto-determination | 50% | BusinessWire Feb 2026 |
| Altais staff productivity increase | 50% | BusinessWire Feb 2026 |
| Altais turnaround compliance improvement | 63% | BusinessWire Feb 2026 |
| Physician PA burden | 12-13 hr/week | AMA 2024 Survey |
| PA requests per physician/week | 39 | AMA 2024 Survey |
| PA causes care delays | 93% of physicians | AMA 2024 Survey |
| PA increases burnout | 89% of physicians | AMA 2024 Survey |
| Serious adverse events from PA | 23% of physicians report | AMA 2024 Survey |
| Medicare Advantage PA denial rate | 6.4% | AMA 2024 Survey |
| CMS-0057-F Phase 1 | Live Jan 1, 2026 | CMS Fact Sheet |
| CMS-0057-F Phase 2 | Jan 1, 2027 | CMS Fact Sheet |
| CMS-0057-F first metrics reporting | Due March 31, 2026 | CMS Fact Sheet |
| Autonomize customers | 3 of top 5 US plans | autonomize.ai |
| Autonomize agents | 100+ in marketplace | BusinessWire Oct 2025 |
| Autonomize funding | $32M total ($28M Series A) | BusinessWire Jun 2025 |
| Autonomize PA Copilot deployment time | 45-60 days to production | GlobeNewswire Apr 2025 |
| PA Copilot processing time | 35 min to under 15 min | GlobeNewswire Apr 2025 |
| PA Copilot accuracy | 95%+ on complex cases | GlobeNewswire Apr 2025 |
| Cohere Health PA volume | 12M+ PAs/year | Cohere Health |
| Industry electronic PA pledge | 80% real-time by 2027 | MedCity Dec 2025 |
