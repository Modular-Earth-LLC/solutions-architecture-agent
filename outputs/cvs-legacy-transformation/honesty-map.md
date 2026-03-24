# Experience Honesty Map — CVS Health Legacy Transformation Engagement

> **Purpose**: Transparent self-assessment of Paul Prae's expertise mapped to the 5 key considerations in the CVS case study, plus 3 additional competency areas required by the role. Drives honest positioning in the solution architecture presentation and identifies where to lean on research vs. direct experience.
>
> **Status**: FINAL (Step 9) — Refined with Phase 0 research insights
>
> **Date**: 2026-03-16

## Confidence Rating Scale

| Rating | Label | Meaning |
|--------|-------|---------|
| 5/5 | Expert | Deep hands-on experience; can speak with authority and cite own projects |
| 4/5 | Strong | Significant experience; may need to refresh specific frameworks/tools |
| 3/5 | Moderate | Adjacent experience; understands concepts but limited direct application |
| 2/5 | Foundational | General awareness; needs research to speak credibly |
| 1/5 | Novice | No direct experience; requires comprehensive research before presenting |

## Evidence Type Labels

| Label | Meaning |
|-------|---------|
| **DIRECT** | Hands-on project experience from career |
| **RESEARCHED** | Knowledge acquired through Phase 0 web research (54 sources) |
| **INDUSTRY** | Industry standard frameworks/patterns applied through adjacent experience |
| **ASSUMPTION** | Inferred from case study context; flagged in assumption register |

---

## Honesty Map (Final)

### Area 1: Legacy System Integration (IBMi/AS/400)
- **Final Rating**: 2/5 (upgraded from 1/5)
- **Upgrade Rationale**: Deep research produced comprehensive knowledge of modernization patterns, vendor landscape, API layers, and the sidecar strategy. Paul can now speak credibly about IBMi modernization approaches, but has zero hands-on IBMi experience.
- **Direct Experience**: None with IBMi/AS/400 specifically.
- **Researched Knowledge**: 11 IBMi-specific sources. Comprehensive understanding of: 5 modernization patterns (rehost/replatform/refactor/rearchitect/replace), 7 vendors (Rocket, Profound Logic, Fresche, LANSA, Replay, m-Power, Infinite i), IBM IWS for native REST API exposure, Db2 REST Services, .NET wrapper approach, NCPDP claims processing standards, sidecar architecture pattern, and the 70% big-bang failure rate statistic.
- **Interview Strategy**: Lead with architectural patterns and vendor options; be transparent about no hands-on IBMi; frame through general enterprise modernization experience (Arine data platform migration, genomics data lake at Hyperbloom).
- **Evidence Types**: RESEARCHED (patterns, vendors, API layers), INDUSTRY (modernization best practices from AWS SA role)

### Area 2: IAM Strategy (Healthcare)
- **Final Rating**: 2.5/5 (upgraded from 2/5)
- **Upgrade Rationale**: Research filled specific healthcare IAM gaps (SMART on FHIR, NIST 800-207 zero trust, GCP Cloud Identity). AWS IAM experience transfers well conceptually.
- **Direct Experience**: AWS IAM architecture guidance (3 years as SA), HIPAA compliance at Arine and Hyperbloom, data privacy in blockchain life science project (CCPA, GDPR, HIPAA, FAIR). **No IAM systems built from scratch.**
- **Researched Knowledge**: 5 IAM sources. SMART on FHIR authorization framework (OAuth 2.0-based for healthcare), NIST SP 800-207 zero trust architecture (identity-centric, continuous verification), GCP Cloud Identity Platform HIPAA implementation, hybrid RBAC/ABAC model for healthcare (pharmacist vs nurse vs admin roles).
- **Interview Strategy**: Frame through AWS IAM expertise; present GCP Cloud Identity through service mapping; cite NIST 800-207 and SMART on FHIR as authoritative frameworks; be transparent that IAM architecture design is a strength at conceptual level but no healthcare-specific IAM builds.
- **Evidence Types**: DIRECT (AWS IAM, HIPAA compliance), RESEARCHED (SMART on FHIR, zero trust, GCP Cloud Identity), INDUSTRY (NIST 800-207)

### Area 3: HCD Design Principles
- **Final Rating**: 4/5 (unchanged)
- **Direct Experience**: BA in Cognitive Science (AI focus) from UGA with formal HCI coursework. 6+ UX projects: Tempus Fugit (HCI course), Fortune 100 conversational UI design (Azure vs Lex bot assessment at Slalom), behavioral healthcare review app with nurse/staff user research ($2M revenue), Neona chatbot design, Knowledge Transfer Module (React UX), FitBloc wireframing.
- **Researched Knowledge**: 5 HCD sources. NIST health IT usability framework, ONC Safety-Enhanced Design (SED) — mandated for certified health IT, NIST GCR 15-996 (technical basis for health IT UI design), WCAG 2.1 AA requirements for healthcare, Integrated Patient Journey Map (IPJM) framework.
- **Interview Strategy**: **Lead with direct experience.** BA in Cognitive Science is a differentiator. Cite healthcare-specific frameworks (NIST, ONC SED) to show awareness of regulatory requirements. Reference the behavioral healthcare review app as direct HCD-in-healthcare experience.
- **Evidence Types**: DIRECT (Cognitive Science degree, HCI coursework, 6+ UX projects, healthcare UX), RESEARCHED (NIST/ONC frameworks), INDUSTRY (WCAG, ADA)

### Area 4: Technology Stack
- **Final Rating**: 3/5 (unchanged overall; GCP upgraded from 1/5 to 2/5)
- **Direct Experience**: AWS Certified Solutions Architect (3 years as Enterprise SA, serving Fortune 500). Azure (Microsoft support engineer + Slalom consulting: Azure ML, Azure Bot Service). Full-stack: Python, JavaScript/TypeScript, React, Node.js, .NET/C#, Java. Data engineering: Snowflake, PostgreSQL, Kafka, Spark, S3, Glue, DynamoDB. **Zero GCP experience.**
- **Researched Knowledge**: 18-service AWS→GCP translation table (S3→Cloud Storage, Redshift→BigQuery, SageMaker→Vertex AI, Bedrock→Vertex AI Model Garden, ECS/EKS→Cloud Run/GKE, SNS/SQS→Pub/Sub, Lambda→Cloud Functions, API Gateway→Apigee, IAM→Cloud IAM, etc.). GCP Dual Run for parallel production validation. CVS tech stack inferred from job postings: Java, Python, React, Angular, Spring Boot, Kafka, Kubernetes, Docker.
- **Interview Strategy**: Present GCP through AWS-equivalent lens using translation table. Emphasize architectural patterns (strangler fig, BFF, event-driven) which are cloud-agnostic. Never claim GCP experience; frame as "I've architected equivalent solutions on AWS, and here's how they map to GCP services."
- **Evidence Types**: DIRECT (AWS certification, Azure experience, full-stack development), RESEARCHED (GCP service mapping, CVS tech stack), INDUSTRY (architectural patterns)

### Area 5: Change Management
- **Final Rating**: 3.5/5 (upgraded from 3/5)
- **Upgrade Rationale**: Research provided formal frameworks (Prosci ADKAR, Kotter 8-step) that complement Paul's practical coaching and training experience. Key statistic: 85% of digital transformation failures are people/process issues.
- **Direct Experience**: Executive coaching at Mento (100% leadership improvement, 93% performance improvement). AI enablement workshops at Arine (trained 100 engineers). Knowledge transfer sessions at Slalom, AWS, Microsoft. Led cultural change at Decooda ("radical transparency with a passion for people").
- **Researched Knowledge**: 5 change management sources. Prosci ADKAR model (Awareness→Desire→Knowledge→Ability→Reinforcement), Kotter 8-step model (create urgency→build coalition→..→anchor in culture), adoption metrics (login frequency, feature usage, task completion), 85% digital transformation failure statistic, 40% higher sustained adoption with performance management integration.
- **Interview Strategy**: Frame Mento coaching and Arine workshops as practical change management. Apply ADKAR stages to green-screen-to-web transition (awareness of why, desire through demos, knowledge through training, ability through sandbox, reinforcement through metrics). Cite 85% failure statistic to position change management as critical path.
- **Evidence Types**: DIRECT (coaching, training, workshops), RESEARCHED (ADKAR, Kotter, metrics), INDUSTRY (change management best practices)

### Area 6: GenAI/ML Leadership
- **Final Rating**: 4.5/5 (upgraded from 4/5)
- **Upgrade Rationale**: Research confirmed CVS's March 2026 Google Cloud partnership with Health100 agentic AI platform — Paul's AI agent experience at Arine is directly relevant. MedGemma launch, HIMSS 2026 agentic AI announcements, and GCP Vertex AI healthcare capabilities provide current context.
- **Direct Experience**: Chief AI Architect at Booz Allen (healthcare & life science AI). Enterprise AI/ML SA at AWS (3 years, SageMaker/Bedrock specialization). Staff AI DataOps Engineer at Arine (HIPAA-compliant AI agents, observability for autonomous pharmacist agent, trained 100 engineers). Chief AI Officer at Hyperbloom ($1.4M ARR AI consulting). NeuroLex (voice computing ML platform). Decooda (NLP/behavior prediction). 15+ ML projects across career.
- **Researched Knowledge**: 6 GenAI sources. GCP Vertex AI healthcare capabilities, Gemini multimodal models, MedGemma (open-source healthcare AI model), Health100 platform agentic AI, CVS/Humana/Highmark AI agent deployments, GenAI DS team structure (AI/ML Engineers, Data Scientists, Data Engineers, MLOps, Domain Specialists). Pharmacy-specific GenAI use cases: PA automation, clinical decision support, formulary optimization, claims acceleration.
- **Interview Strategy**: **Lead with depth.** This is Paul's strongest area. Reference Arine's autonomous pharmacist agent observability pipeline as directly analogous to CVS's needs. Present GenAI DS team structure from both hiring and management perspectives. Show how Vertex AI maps to Paul's SageMaker/Bedrock expertise. Demonstrate thought leadership through pharmacy-specific GenAI use cases.
- **Evidence Types**: DIRECT (15+ ML projects, 3 healthcare AI roles, AI agent development), RESEARCHED (Vertex AI, Health100, MedGemma), INDUSTRY (GenAI team structure, evaluation frameworks)

### Area 7: GCP (Google Cloud Platform)
- **Final Rating**: 2/5 (upgraded from 1/5)
- **Upgrade Rationale**: Research produced comprehensive AWS→GCP service translation table (18 services mapped). Understanding of GCP-unique services (Dual Run, Apigee, Cloud Healthcare API) adds real value. The March 2026 CVS-Google partnership makes GCP knowledge immediately actionable.
- **Direct Experience**: **Zero GCP experience.** AWS-primary throughout career. Azure through Microsoft and Slalom roles.
- **Researched Knowledge**: 5 GCP sources. Complete service mapping table, Dual Run (unique to GCP — parallel production for migration), Apigee (enterprise API management), Cloud Healthcare API (FHIR R4, HL7v2, DICOM), GKE/Cloud Run for container orchestration, BigQuery (serverless analytics), Vertex AI + Model Garden (Gemini), Cloud Identity Platform (HIPAA-capable), Pub/Sub + Eventarc (event-driven architecture).
- **Interview Strategy**: **Never claim GCP experience.** Always frame as: "In my AWS architecture practice, I solved [problem] using [AWS service]. The GCP equivalent is [service], which offers [differentiator]." Use the translation table as a visual aid. Highlight GCP-unique capabilities (Dual Run, Apigee, Cloud Healthcare API) that have no direct AWS equivalent.
- **Evidence Types**: RESEARCHED (service mapping, Dual Run, Cloud Healthcare API), DIRECT (AWS architectural equivalent experience), ASSUMPTION (A-0-005: GCP is primary platform per partnership)

### Area 8: Healthcare Domain
- **Final Rating**: 4/5 (unchanged)
- **Direct Experience**: Arine — healthcare AI platform serving 45+ health plans, 2 national PBMs, covering 50M members. Booz Allen — clinical, behavioral, genomic data AI solutions for healthcare & life science clients. Hyperbloom — disaster recovery for clinical trials (10K+ sites, 45 countries), blockchain data platform for life science (HIPAA, HL7). Slalom — behavioral health demand forecasting, healthcare service review app ($2M revenue). TReNDS — neuroinformatics platform (COINSTAC, differential privacy for PHI).
- **Researched Knowledge**: 5 PBM-specific sources. Claims adjudication architecture (NCPDP B1 transactions, real-time at POS), PBM workflows (eligibility → DUR → UM → pricing → adjudication), CVS Caremark platform (myPBM on Azure, 130+ APIs), formulary management process, 99%+ electronic adjudication rate, 70% of PBM market on legacy systems.
- **Interview Strategy**: **Lead with healthcare depth.** Arine's work with national PBMs is directly relevant. Acknowledge PBM claims adjudication as a learning area but frame through adjacent healthcare expertise. Use the Arine autonomous pharmacist agent as a bridge to CVS's GenAI ambitions.
- **Evidence Types**: DIRECT (5 healthcare/life science employers, HIPAA compliance, HL7 interoperability), RESEARCHED (PBM workflows, claims adjudication, NCPDP), INDUSTRY (healthcare compliance frameworks)

---

## Summary — Final Confidence Profile

| Area | Draft Rating | Final Rating | Change | Strongest Evidence |
|------|-------------|-------------|--------|-------------------|
| Legacy System Integration | 1/5 | **2/5** | +1 | RESEARCHED: 11 IBMi sources, 5 patterns, 7 vendors |
| IAM Strategy | 2/5 | **2.5/5** | +0.5 | DIRECT: AWS IAM + HIPAA; RESEARCHED: SMART on FHIR, zero trust |
| HCD Design Principles | 4/5 | **4/5** | — | DIRECT: Cognitive Science BA, 6+ UX projects, healthcare UX |
| Technology Stack | 3/5 | **3/5** | — | DIRECT: AWS SA certified; RESEARCHED: 18-service GCP mapping |
| Change Management | 3/5 | **3.5/5** | +0.5 | DIRECT: coaching, workshops; RESEARCHED: ADKAR, Kotter |
| GenAI/ML Leadership | 4/5 | **4.5/5** | +0.5 | DIRECT: 15+ ML projects, 3 healthcare AI roles, AI agents |
| GCP | 1/5 | **2/5** | +1 | RESEARCHED: translation table, Dual Run, Cloud Healthcare API |
| Healthcare Domain | 4/5 | **4/5** | — | DIRECT: 5 healthcare employers; RESEARCHED: PBM workflows |

**Weighted Average**: 3.2/5 → Moderate-to-strong overall. Strongest in GenAI/ML (4.5), HCD (4.0), and Healthcare (4.0). Weakest in IBMi (2.0) and GCP (2.0) — both addressable through research-backed presentation strategy.

## Interview Positioning Strategy

1. **Lead with strengths**: Open with GenAI/ML leadership and healthcare domain expertise — Paul's differentiators
2. **Bridge to gaps**: Use AWS→GCP translation table for technology stack; use modernization patterns for IBMi
3. **Be transparent**: "My cloud architecture experience is AWS-primary. Here's how these solutions translate to GCP..."
4. **Cite frameworks**: NIST, SMART on FHIR, ADKAR, WCAG — shows awareness beyond just technology
5. **Show research depth**: Demonstrate understanding of CVS's March 2026 Google Cloud partnership and Health100 platform
6. **Dual competency**: Weave GenAI DS team leadership throughout the architecture presentation, not as a separate section
