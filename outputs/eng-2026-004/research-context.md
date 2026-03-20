# eng-2026-004: Research Context
## AI-Driven Prior Authorization — Autonomize AI Interview

### Paul Prae — Key Background (from career-data.json + paulprae.com)

#### Current Role
- **Staff AI DataOps Engineer** at Arine — healthcare AI platform serving 45+ health plans, 50M members
- Designed HIPAA-compliant coding assistants, AI observability pipelines (DynamoDB → Snowflake → dbt → QuickSight)
- Manages enterprise data platform on Snowflake + AWS processing petabytes of healthcare data

#### Relevant Prior Roles
- **Chief AI Architect, Senior Manager** — Booz Allen Hamilton (healthcare/life science AI)
- **Enterprise AI/ML Solutions Architect** — Amazon Web Services (3 years, national ML SME)
- **Neuroinformatics Data Platform Architect** — TReNDS Center (COINSTAC, federated learning, PHI)
- **Founder** — Hyperbloom (healthcare AI consulting), Modular Earth (open-source AI agents)
- **Senior AI Engineer** — NeuroLex Labs (voice computing for healthcare, ML pipelines)

#### AWS Certifications
- AWS Certified Solutions Architect
- AWS Certified Machine Learning — Specialty
- AWS Certified Machine Learning Engineer
- AWS Certified AI Practitioner
- AWS Certified Cloud Practitioner

#### Technical Skills (from career data)
**Languages**: Python, SQL, Bash, JavaScript, C#, C++, Java, PHP, PowerShell, Prolog
**AI/ML**: Amazon Bedrock, SageMaker, Deep Learning, MLOps, NLP, Prompt Engineering, Generative AI, LLMs, Multi-agent Systems
**Data**: Snowflake, PostgreSQL, DynamoDB, dbt, Apache Kafka, Data Engineering, DataOps
**Cloud**: AWS (Bedrock, SageMaker, ECS, EKS, Lambda, Step Functions, S3, SNS, SQS, EventBridge, IAM, QuickSight, RDS)
**Healthcare**: HIPAA, EHR, Clinical Decision Support, Healthcare Analytics, Neuroinformatics, Genomics
**Infrastructure**: Docker, Distributed Systems, Edge Computing, System Architecture

#### Compliance Experience (verified from projects/skills)
- **HIPAA** — multiple projects (Arine, COINSTAC, blockchain data platform)
- **CCPA** — blockchain-based life science data platform
- **GDPR** — blockchain-based life science data platform
- **HL7** — blockchain-based life science data platform (interoperability standards)
- **FAIR data principles** — life science data governance
- **CDISC/SDTM/ADaM** — clinical data standards
- **PHI protection** — differential privacy (COINSTAC), data governance

#### Relevant Healthcare Projects
1. **Arine** — 50M members, 45+ health plans, medication optimization AI
2. **COINSTAC** — federated neuroimaging analysis, differential privacy for PHI
3. **NeuroLex** — ML for mental health detection from audio data
4. **Clinical trials DR** — 10,000+ research sites, 45 countries
5. **Blockchain life science data platform** — HIPAA/CCPA/GDPR/HL7 compliant
6. **Behavioral healthcare service review app** — $2M+ revenue
7. **Healthcare demand forecasting** — predictive analytics for facility capacity
8. **Genomics data lake** — AWS-based, VCF→Parquet, Glue Data Catalog

---

### Autonomize AI — Platform Research (verified from web research)

#### Company Profile
- **Live with 3 of the 5 largest US health plans** (names not publicly disclosed)
- **ServiceNow partnership** announced March 2026 (BusinessWire press release)
- **Molina Healthcare** confirmed as customer
- **ACAP member** (Association for Community Affiliated Plans)
- Recent leadership hires in healthcare marketing and regulatory (Feb 2026)

#### Five Largest US Health Plans (by revenue, 2024)
1. UnitedHealthcare (UnitedHealth Group) — ~$224B revenue
2. Elevance Health (formerly Anthem)
3. Kaiser Permanente — highest enrollment
4. Centene — largest individual marketplace insurer (4.5M+ members)
5. HCSC (Health Care Service Corporation) — ~5.6M customers

#### Platform Components (verified)
- **Genesis Platform** — compound AI substrate, foundation layer
- **Compound AI Agents** — multi-agent orchestration
- **Prior Auth Copilot** — document processing, clinical review, decision support
- **AI Studio** — low-code orchestration for workflow customization
- **Agents Marketplace** — 100+ pre-built healthcare agents
- **Security**: HIPAA compliant, SOC 2 Type 2 certified
- **Encryption**: AES-256 + TLS 1.2+

#### Key Use Cases
- Prior Authorization
- Care Gaps Review
- Medical Record Review
- Care Management
- Complex Document Processing
- Clinical Research

#### Deployment
- Azure-based deployments (confirmed from TipRanks article)
- Emphasis on specialized healthcare agents

---

### Questionnaire Answers — Complete Synthesis

#### Section A: Client Scenario Assumptions

**A1. Client Scale & Volume**
Based on Autonomize AI's actual customer profile (3 of top 5 US health plans):
- **Client model**: Composite based on Elevance Health-scale payer
- **Members**: ~45M covered lives across multiple LOBs (Commercial, Medicare Advantage, Medicaid)
- **PA requests/month**: ~2.5M (industry average for top-5 payer scale)
- **Provider network**: 1.2M+ contracted providers
- **Geographic coverage**: National, 50-state operations

**A2. Current State Pain Points — Interview Personas**
- **Dr. Sarah Chen, CMO** — Frustrated by 5-day avg PA turnaround, clinical staff spending 40% of time on PA paperwork
- **Marcus Williams, VP of Operations** — Managing 450 FTEs in PA processing, 60% fax-based intake, 15% auto-approval rate
- **Priya Patel, CIO** — Legacy Facets core system, fragmented clinical data across 12+ EMR systems, partial FHIR adoption
- **James Morrison, Director of Compliance** — CMS-0057-F deadline approaching, NCQA accreditation renewal, state-level mandates in CA and NY

**A3. Clinical Guidelines** — Based on Paul's background:
- InterQual (evidence-based clinical decision support — aligns with Paul's Clinical Decision Support skill)
- MCG Health (for secondary validation)
- Custom payer-specific criteria (digitized, stored in knowledge graph — aligns with Paul's Neo4j/knowledge graph experience)
- Change frequency: quarterly updates with annual major revisions

**A4. Technology Landscape** — Based on Paul's skills (compatible, commonly co-deployed stack):
- **Payer Core**: TriZetto Facets (modern enterprise, widely adopted)
- **Cloud**: AWS primary (Paul's strongest platform)
- **Data Platform**: Snowflake (Paul's current stack at Arine) + PostgreSQL + DynamoDB
- **Integration**: Apache Kafka (Paul has direct experience) for event streaming
- **ML Platform**: Amazon SageMaker + Amazon Bedrock (Paul's AWS ML certifications)
- **Orchestration**: Amazon ECS/EKS (containerized services)
- **Serverless**: Lambda, Step Functions, EventBridge (Paul's current stack)
- **Monitoring**: QuickSight dashboards + CloudWatch
- **Data Processing**: dbt for transformations, AWS Glue for ETL
- **FHIR**: Partial adoption — R4 compliant for newer systems, legacy connectors for older DBs

**A5. Compliance** — From Paul's verified experience only:
- HIPAA (Privacy Rule, Security Rule, Breach Notification)
- CCPA (California Consumer Privacy Act)
- GDPR (General Data Protection Regulation)
- HL7/FHIR interoperability standards
- CMS-0057-F (Prior Authorization Final Rule — regulatory driver for this solution)

#### Section B: Solution Strategy Decisions

**B1. Automation Targets**
- Phase 1 auto-determination target: **60%** (conservative, clinically validated)
- Human-in-the-loop threshold: confidence score < 0.85 triggers clinical review
- Auto-approval only in Phase 1; auto-denial introduced Phase 2 with additional clinical validation safeguards (regulatory sensitivity)

**B2. Deployment & Infrastructure**
- **Cloud**: AWS (Paul's strongest, 5 AWS certs; Autonomize deploys on Azure but integration layer on AWS)
- **On-prem**: PHI data stays in payer's VPC; Autonomize AI accesses via VPC peering or PrivateLink
- **Deployment model**: Dedicated tenant (Autonomize AI deployed in payer's cloud account for data sovereignty)

**B3. Integration Priority**
- **First**: Fax ingestion (60% of volume, highest ROI impact)
- **Second**: Web portal API (growing channel, easy to standardize)
- **Third**: EDI X12 278 (already structured, lowest transformation cost)
- Clinical data: Real-time for eligibility checks, near-real-time (streaming) for clinical data enrichment
- FHIR facade over legacy DBs (future-proofs for CMS-0057-F compliance)

**B4. AI/ML Architecture**
- Full retraining pipeline with fine-tuning as the primary update mechanism
- Drift monitoring: Both statistical (PSI, KS test) + outcome-based (approval overturn rate, appeal rate)
- Feedback loop: Async batch (daily aggregation of reviewer corrections → weekly model evaluation → monthly fine-tuning cycle)

**B5. Multi-Tenancy**: Multi-tenant for full architecture (Paul's explicit choice)
- Multi-tenant platform with LOB-specific configuration isolation (rules engine per LOB)
- Shared base model + LOB-specific fine-tuning for high-volume LOBs (Commercial, Medicare Advantage)
- Shared model + rules-only for lower-volume LOBs
- Cost optimization priority over strict data isolation (data is all within same payer organization)

**B6. Differentiation**: Business outcome-focused, automating operations, saving operational overhead, automating tedious tasks, patient outcomes. Speed-to-value + clinical accuracy.
- Lead angle: **Business outcomes** — operational cost reduction, patient experience, regulatory readiness
- Technologies to showcase: Multi-agent AI orchestration, FHIR R4, event-driven architecture, MLOps
- Reference CMS-0057-F as regulatory driver (Jan 1, 2027 deadline creates urgency)

#### Section C: Presentation Strategy — CONFIRMED
- C1: 12-slide structure approved
- C2: Both Mermaid diagrams + detailed descriptions
- C3: Speaker notes per slide, 1-hour panel presentation

---

### Prior Authorization Industry Data (from research)

- **Average PA turnaround**: 3-5 business days (manual), target < 72 hours (CMS-0057-F requirement for urgent)
- **Cost per PA transaction**: $11-15 per manual review (CAQH Index)
- **Volume**: Large payers process 1-3M PA requests/month
- **Auto-approval industry average**: 15-25% (without AI), 50-70% (with AI-assisted automation)
- **FTE requirements**: ~1 FTE per 3,000-4,000 PA requests/month for manual processing
- **PA denial rate**: ~6-7% of all requests (AMA 2024 survey)
- **Physician time burden**: Average 14 hours/week on PA per physician (AMA)
