# eng-2026-004 v2: Autonomize AI Prior Authorization — Solution Architecture Iteration

> **Engagement**: eng-2026-004 | **Iteration**: v2 | **Date**: 2026-03-23
> **Plugin required**: Solutions Architecture Agent (all skills via `solutions-architecture-agent:{skill}`)
> **Base deliverables**: `outputs/eng-2026-004/` (v1 — do NOT overwrite)

---

## Execution Protocol

```
1. Paste this prompt into Claude Code with SA Agent plugin loaded
2. Claude executes Phase 0 INTERACTIVELY (requirements validation)
3. You confirm all decisions
4. Enter plan mode: /plan
5. Claude writes execution plan from Phases 1–8
6. You approve the plan
7. Claude executes autonomously, stopping at HUMAN CHECKPOINT gates
8. After each SA skill: validate KB → git commit → push
```

**Context engineering**: Load files just-in-time per phase — do NOT read all files upfront.
**Excluded**: Do NOT read anything under `.claude/plans/archive/` or `knowledge_base/archive/`.

---

## Phase 0: Requirements Validation [INTERACTIVE — BEFORE PLAN MODE]

> Execute this phase NOW. Do NOT enter plan mode until every decision below is confirmed.

### 0.1 Context Loading

Read these files to understand the current v1 state:

```
knowledge_base/engagement.json
outputs/eng-2026-004/proposal.md
outputs/eng-2026-004/research-context.md
outputs/eng-2026-004/plans/backlog.md
outputs/eng-2026-004/plans/uat-checklist.md
inputs/autonomize-solutions-architect-job-description.md
```

Remember, always ground yourself in the original assignment document. It was transformed to markdown for easy parsing here: `C:\dev\solutions-architecture-agent\inputs\Solution Architect Interview Assignment_ AI-Driven Prior Authorization.md`.

Defer reading KB JSON files (architecture.json, requirements.json, etc.) until their respective phases.

### 0.2 Critical Decisions — Present Each to User

**Technical Architecture:**

| ID | Decision | v1 Assumption | Question |
|----|----------|---------------|----------|
| TD-1 | **Cloud platform** | AWS primary (Paul's certs) | Autonomize deploys on Azure. Should production architecture target (a) Azure-primary, (b) AWS-primary, (c) cloud-agnostic with Azure for Autonomize components? |
| TD-2 | **Agent design scope** | Assumes custom PA agent on Genesis | Does the assignment expect us to (a) integrate Autonomize's existing PA Copilot into a customer environment, or (b) design a PA agent from scratch to demonstrate AI agent architecture skills? This changes the entire architecture. |
| TD-3 | **Event streaming** | Apache Kafka (MSK) | Kafka is powerful but complex. Keep for production? Or simplify to managed queue (SQS/Azure Service Bus) since the assignment doesn't require streaming? |
| TD-4 | **FHIR depth** | FHIR R4 Facade, SMART on FHIR, Da Vinci PAS | You flagged difficulty speaking to these. Simplify to (a) "Healthcare Interoperability API" with footnote, (b) keep FHIR but remove SMART/Da Vinci details, or (c) keep as-is? |
| TD-5 | **MLOps scope** | Dual drift detection (PSI/KS + outcome-based) | You flagged statistics avoidance and LLM-ops preference. Simplify to (a) LLM evals + human feedback + guardrails only, (b) keep light traditional ML monitoring, or (c) keep full dual approach? |
| TD-6 | **Auto-determination target** | 60% Phase 1 | Altais achieved 50%. Is 60% right, or should we cite Altais benchmark and say "targeting Altais-level or better"? |
| TD-7 | **Remove estimates** | $1.2M Year 1, hourly rates, timeline numbers | Per your guardrail: remove ALL financial/time estimates, or keep industry-sourced benchmarks (CAQH per-transaction costs)? |

**Demo:**

| ID | Decision | v1 Assumption | Question |
|----|----------|---------------|----------|
| DM-1 | **Demo platform** | FastAPI + Kafka + Docker Compose | Fastest path: (a) Claude Code plugin with PA skills on Vercel, (b) single FastAPI app with Anthropic SDK (no Kafka), (c) Streamlit app, (d) other? |
| DM-2 | **Demo timeline** | 12-16 hours | Is 48 hours still the constraint? More? Less? |
| DM-3 | **Demo data** | Synthetic clinical data, mock FHIR APIs | Use (a) mock APIs only, (b) public health datasets (Azure Open Datasets, CMS public files), (c) something else? |
| DM-4 | **Demo hosting** | Local Docker only | Deploy to (a) Vercel, (b) local only, (c) Anthropic-hosted? |

**Presentation:**

| ID | Decision | v1 Assumption | Question |
|----|----------|---------------|----------|
| PD-1 | **PowerPoint method** | Not yet decided | (a) Manual SVG paste, (b) md-to-docx pipeline, (c) Marp CLI, (d) Claude Code PowerPoint plugin, (e) other? |
| PD-2 | **Diagram variants** | 6 single-version diagrams | Produce (a) 1 version per diagram, (b) 2-3 variants of key diagrams (business/tech/progressive), (c) single progressive set? |
| PD-3 | **Interview timing** | "Later this week" | Exact date? This determines time budget for remaining work. |

### 0.3 New Information

Ask: "Since the v1 deliverables were produced on 2026-03-20, do you have any new information from Autonomize AI contacts, additional research, feedback from reviewers, or changes to interview format/timing?"

### 0.4 Scope Confirmation

Summarize all decisions in a table and confirm:
- **Depth**: STANDARD for most skills, COMPREHENSIVE for architecture and proposal
- **Versioning**: KB files update in place (v1.0 → v2.0), new outputs in `outputs/eng-2026-004-v2/`
- **Deliverables**: (1) slide generation prompts, (2) demo implementation plan, (3) email draft, (4) interview prep materials

> **GATE**: Document all confirmed decisions. Do NOT proceed to plan mode until user explicitly confirms.

---

## Constraints

### Non-Negotiable Guardrails (HIGHEST PRIORITY)

1. **No fabricated numbers** — Never generate statistics, percentages, costs, or timelines. Only cite authoritative sources with working URLs.
2. **No hallucinated citations** — Every URL must be verified. Every claim must trace to a source. Triple-check.
3. **No assumptions about Autonomize AI** — Speak in generalities about their platform unless you can cite their public documentation.
4. **Preserve v1 outputs** — Never overwrite files in `outputs/eng-2026-004/`. Create `outputs/eng-2026-004-v2/` for all new outputs.
5. **Human checkpoint compliance** — MANDATORY STOP after each phase marked with HUMAN CHECKPOINT. Do NOT auto-invoke the next skill.
6. **No overengineering** — Meet the assignment requirements with the simplest solution that earns trust. Every component must be justified.
7. **Validate after every KB write** — Run `python tests/validate_knowledge_base.py` and fix errors before committing.
8. **Iterative commits** — Git add, commit, and push after each logical change. Do not batch work.

### Quality Standards

1. **Single source of truth** — Create one master document (`solution-architecture-source-of-truth.md`) that all other deliverables reference. Every fact in the slide deck must trace back to it.
2. **Cross-deliverable consistency** — Technology decisions, component names, and data flows must be identical across all KB files, diagrams, and slides.
3. **Progressive disclosure** — Initial diagrams: 3-4 components. Each subsequent diagram adds complexity. The audience builds understanding incrementally.
4. **Citation-linked claims** — Every technology recommendation, design pattern, or industry statistic must link directly to its authoritative source. Include the exact section or page when possible.
5. **Self-contained slide deck** — The deck + original assignment document are the only things the audience has. No references to internal KB files, SA workflow artifacts, or generated research.
6. **Read-aloud speaker notes** — Every speaker note must sound natural when Paul reads it aloud. Target ~5 min/slide. No sentences Paul cannot confidently speak to.
7. **Mermaid diagram rules** — Follow `.claude/rules/mermaid-diagrams.md` strictly.

### Persona & Voice

**Role**: Principal AI Solutions Architect at Autonomize AI, presenting a technical design to an interview panel of senior engineers and architects.

**Paul's Technology Inventory** — organized by depth. Prefer technologies from the top tiers for architecture and especially for the demo. Read `inputs/career-data.json` for full context on each skill.

**Tier 1 — Core Expertise (10+ years, daily use across multiple employers)**:
- **Python** — primary language throughout career (AI/ML, data engineering, web services, automation)
- **SQL** — used at every role from Microsoft through Arine
- **AI/ML foundations** — BS in Computer Science (AI emphasis) + BA in Cognitive Science (AI focus), 15 years applied AI
- **NLP / Natural Language Processing** — nationally recognized SME (Decooda, NeuroLex, IBM Watson, chatbots)
- **System Architecture / Solutions Architecture** — career-defining skill across AWS, Booz Allen, Slalom, Hyperbloom
- **Healthcare domain** — HIPAA, clinical decision support, PHI protection, EHR, behavioral health, clinical trials, genomics, neuroinformatics
- **Full-stack web development** — JavaScript, Node.js, React, Express, .NET/C#, LAMP stack (PHP/MySQL), HTML/CSS
- **Agile / Scrum** — practitioner and Scrum master across multiple organizations
- **Data engineering / ETL pipelines** — from LAMP stacks through AWS Glue through Snowflake

**Tier 2 — Strong Production Experience (3-10 years, enterprise-scale)**:
- **AWS (3 years as Solutions Architect + continued heavy use, 5 certs)**:
  - Bedrock (LLM integration), SageMaker (ML platform), Comprehend (NLP)
  - ECS/EKS (containers), Lambda/Step Functions/EventBridge (serverless)
  - S3, RDS, DynamoDB, SNS, SQS (storage + messaging)
  - IAM, VPC, PrivateLink, CloudWatch (security + observability)
  - Glue / Data Catalog (ETL), QuickSight (BI)
  - Deep Learning AMIs, GPU infrastructure
- **Microsoft Azure** — 2+ years at Slalom: Azure ML, Azure Bot Service, Cognitive Services, Azure Search, DocumentDB
- **C# / .NET** — Microsoft (2 years), Slalom (2.5 years), Red Ventures: UWP, ASP.NET, PowerShell, SharePoint
- **Docker / containerization** — used across Arine, COINSTAC, Hyperbloom, personal projects
- **Apache Kafka** — production microservices at Decooda, data pipelines at Arine
- **PostgreSQL** — production databases across Arine, COINSTAC, open-source projects
- **Deep Learning / neural networks** — SageMaker, Deep Learning AMIs, model training pipelines
- **MLOps** — model lifecycle, drift monitoring, deployment automation, observability pipelines
- **Conversational AI / chatbots** — Amazon Lex, Azure Bot Service, Neona chatbot, conversational interface design
- **Distributed systems** — federated computing (COINSTAC), decentralized architectures, microservices
- **Git / GitHub** — active open-source contributor, team workflows across all roles
- **PowerShell** — extensive automation at Microsoft, infrastructure scripting
- **Predictive analytics / classification** — demand forecasting, behavior prediction, clinical prediction

**Tier 3 — Active Current Use (1-3 years, production or daily)**:
- **Anthropic Claude / Claude Code** — daily driver, building plugins and skills, prompt engineering
- **Cursor AI / GitHub Copilot** — daily AI-augmented development
- **MCP Tools / protocol** — building MCP integrations for Claude Code
- **Prompt engineering / context engineering** — active project: AI Engineering Assistant
- **Multi-agent systems** — Modular Earth AI agents, SA Agent plugin architecture
- **Generative AI / LLMs** — Claude, Mistral, Qwen, Llama, DeepSeek families
- **Ollama** — local LLM hosting for open-source stack
- **LangChain** — current open-source AI stack (familiar, not preferred for production)
- **n8n** — workflow automation in open-source stack
- **Neo4j** — knowledge graphs in current AI stack
- **DynamoDB** — production at Arine (observability pipeline)
- **Snowflake** — recent (~6 months at Arine, production enterprise data platform)
- **dbt** — recent (~6 months at Arine, data transformations)
- **Bash scripting** — daily use for automation
- **Differential privacy / federated learning** — COINSTAC (published research in Frontiers in Neuroinformatics)
- **Blockchain / Web3 / smart contracts** — life science data platform, decentralized architectures

**Tier 4 — Foundational Knowledge (used in past, can ramp quickly)**:
- **Java** — university CS coursework, web programming
- **C/C++** — university systems programming
- **Prolog / Lisp** — university symbolic programming and AI
- **PHP** — Red Ventures LAMP stack
- **MySQL, Microsoft SQL Server, MongoDB** — various projects
- **React** — Decooda Knowledge Transfer Module
- **Rust, TypeScript** — mentioned in current open-source stack
- **Tauri** — local-first desktop app framework
- **Apache Spark** — hackathon data processing (140M+ rows)
- **Jupyter** — research environments (COINSTAC, neuroinformatics)
- **Power BI** — Slalom healthcare project
- **SharePoint** — Microsoft SME (2 years)
- **WordPress** — web development consulting

**Academic Foundations (shapes architectural thinking)**:
- Cognitive Science (BA) — human-computer interaction, theory of knowledge, linguistics
- Computer Science (BS, AI emphasis) — data structures, algorithms, evolutionary computation, symbolic AI, deductive systems
- Published researcher — Frontiers in Neuroinformatics (federated neuroimaging analysis)

**Key Project References for Demo/Architecture Alignment**:
| Project | Scale | Relevance |
|---------|-------|-----------|
| Arine | 50M members, 45+ health plans | Healthcare AI platform, data pipelines, HIPAA |
| AWS SA | Fortune 500 customers, 3 years | Enterprise architecture, ML solutions, pre-sales |
| COINSTAC | Published research, multi-site | Federated learning, differential privacy, PHI |
| NeuroLex | ML platform | Automated ML workflows, audio/text data, healthcare |
| Booz Allen | Healthcare & life science AI | Clinical, behavioral, genomic data, AI governance |
| Decooda | NLP platform, Kafka microservices | Behavior prediction, text analytics, real-time processing |
| Slalom | Azure ML, chatbots, healthcare analytics | Predictive analytics, demand forecasting, $2M+ app |
| Microsoft | Fortune 100, SharePoint SME | Enterprise support, PowerShell automation, disaster recovery |
| Hyperbloom | Healthcare AI consulting | Solutions architecture, go-to-market, team leadership |
| Modular Earth | Open-source AI agents | Claude Code plugins, multi-agent systems, local-first |
| Genomics Data Lake | AWS, S3/Glue/VPC | Data lake architecture, VCF→Parquet, security |
| Clinical Trials DR | 10K+ sites, 45 countries | Disaster recovery, data governance, global scale |
| Blockchain Life Science | HIPAA/CCPA/GDPR/HL7 | Compliance, smart contracts, data lifecycle |

**For the DEMO — prioritize these (Paul's fastest path to impressive output)**:
1. Python + Anthropic SDK (native, no frameworks) — deepest skill + best LLM
2. Claude Code + MCP tools — daily driver, can build plugins/skills rapidly
3. FastAPI or similar lightweight Python web framework
4. Docker — knows well, quick local setup
5. PostgreSQL — years of production experience
6. Simple HTML/JS frontend or Streamlit — fast visual results
7. Vercel for hosting — familiar deployment target

**Paul's gaps (design around — simplify or avoid depth)**:
- FHIR R4 deep internals, SMART on FHIR, Da Vinci PAS specifics
- Statistics (KS test, PSI calculations, Wasserstein Distance)
- SageMaker (known but not well-liked in industry — minimize mentions)
- EDI X12 278 transaction parsing
- Specific NIST framework numbers, compliance control IDs
- LOB terminology in healthcare payer context (verify accuracy before using)
- Snowflake/dbt (only ~6 months experience — don't lean heavily on these)

**Voice calibration**: Informed by `inputs/career-data.json`. Paul is a 15-year AI/ML veteran with deep CS and cognitive science foundations, enterprise architecture experience across AWS and Azure, and a passion for healthcare AI and open-source. Speaker notes should sound like a senior engineer who has built ML platforms, led architecture for Fortune 500 customers, and shipped production healthcare AI — confident on architecture and AI, collaborative on clinical details, honest about what requires discovery.

---

## Phase 1: Research & Discovery Update

> **Skill**: Web research (WebSearch, WebFetch) — no SA skill
> **Entry**: Phase 0 decisions confirmed
> **Exit**: Updated research document with verified citations
> **Parallel**: Yes — launch research agents concurrently for independent topics

### Tasks

1.1 **Autonomize AI Platform (March 2026)**
- Latest product releases, partnerships, marketplace updates
- Verify Genesis Platform architecture, PA Copilot workflow, AI Studio capabilities
- ServiceNow partnership details (announced March 2026)
- Azure Marketplace presence and deployment model
- Agents Marketplace: what's available, how agents are deployed to customers
- Extract PA workflow details from `inputs/PA-with-graphics.mp4`

1.2 **AI Agent Architecture Best Practices (2026)**
- Single agent + tools/skills vs multi-agent orchestration — current consensus
- MCP protocol adoption status and healthcare use cases
- Native SDKs vs frameworks (LangChain/CrewAI) — industry direction
- Open source vs proprietary models: cost, latency, accuracy trade-offs for healthcare
- Context engineering: how production AI agents manage context windows effectively
- Agentic design patterns: ReAct, tool-use, reflection, planning — which apply to PA?

1.3 **Cloud Platform Comparison** (informed by TD-1 decision)
- Azure AI services relevant to PA: Azure OpenAI, Azure AI Search, Azure Health APIs
- AWS AI services relevant to PA: Bedrock, HealthLake, Comprehend Medical
- Cross-platform technologies Paul knows: Python, Kafka, PostgreSQL, Docker, Node.js, Neo4j, Anthropic SDK
- Which cloud has better healthcare-specific managed services?

1.4 **Prior Authorization Industry (March 2026)**
- CMS regulatory updates since January 2026
- Updated CAQH Index per-transaction cost data
- Published reference architectures for healthcare AI agents
- Standard PA business process documentation (cite authoritative sources like AMA, CAQH, CMS)
- Autonomize AI's published case studies (Altais metrics, other references)

### Deliverable
- `outputs/eng-2026-004-v2/research-context.md`

### Verification
- [ ] Every URL verified working (click-test)
- [ ] No claims without a cited source
- [ ] Technology decisions are grounded in verifiable sources, not opinion
- [ ] Git commit and push

---

## Phase 2: Requirements Revision

> **Skill**: `solutions-architecture-agent:requirements` | `--depth STANDARD`
> **Entry**: Research complete
> **Exit**: Updated requirements with full assignment traceability
> **Read now**: `inputs/Solution Architect Interview Assignment_ AI-Driven Prior Authorization.pdf`, `knowledge_base/requirements.json`

### Tasks

2.1 **Re-read assignment document line by line.** Extract:
- Every explicit requirement (slide topics, diagram types, questions to answer)
- Every implicit requirement (hints in parentheses, italics, end-of-paragraph)
- Key phrases: "Consider the balance of cost, isolation, and complexity", "poor integrations", payer = health plan, long turnaround = labor overhead

2.2 **Build requirements traceability matrix:**

| Assignment Question/Requirement | Slide # | KB Source | Status |
Each row maps an assignment requirement to where it's answered.

2.3 **Resolve requirement tensions** (using Phase 0 decisions):
- "10-12 slides" vs detailed questions per slide → prioritize conciseness
- "Architect for Autonomize" vs "architect for Paul's expertise" → per TD-1
- "Don't overengineer" vs "impress senior executives" → meet requirements precisely, no more
- "Design for their tech stack" vs "design for what I can build quickly" → separate production and demo

2.4 **Incorporate feedback:**
- Strict adherence to assignment requirements ONLY — strip any added requirements
- Generic-first architecture, then technology selection (separate concerns)
- Clear separation: production architecture vs demo vs interview prep vs study materials
- Three integration focus areas: (1) member eligibility check API, (2) secure PA request ingestion (one format), (3) clinical data source for AI processing
- Do NOT add requirements from the SA workflow that aren't in the assignment

### Deliverable
- Updated `knowledge_base/requirements.json` (v2.0)
- `outputs/eng-2026-004-v2/requirements-traceability.md`

### Verification
- [ ] Every assignment question mapped to a slide
- [ ] No requirements that aren't in the assignment document
- [ ] Requirement conflicts resolved and documented
- [ ] `python tests/validate_knowledge_base.py` passes
- [ ] Git commit and push

**HUMAN CHECKPOINT**: Review requirements traceability before architecture work.

---

## Phase 3: Architecture Redesign

> **Skill**: `solutions-architecture-agent:architecture` | `--depth COMPREHENSIVE`
> **Entry**: Requirements v2.0 confirmed
> **Exit**: Generic-first architecture + technology mapping + diagram variants
> **Read now**: `knowledge_base/architecture.json`, `knowledge_base/requirements.json`
> **Parallel**: Launch WA reviewer agents alongside architecture work (backlog #1)

### Tasks

3.1 **Generic Architecture Design**
Design using technology-agnostic names FIRST:
- "Cloud Computing Environment" → then map to Azure/AWS
- "Event Stream / Message Queue" → then map to Kafka/SQS/Service Bus
- "LLM Provider" → then map to Claude/GPT/open-source
- "Healthcare Interoperability Layer" → then map to FHIR/HL7/custom API
- "Vector Store" → then map to pgvector/Azure AI Search/etc.
- "Agent Orchestration Platform" → then map to Autonomize Genesis

3.2 **Technology Selection Table**
After generic design, create:

| Generic Component | Production Choice | Demo Choice | Justification | Verified URL |
Every row must have a working URL and a reason grounded in research or Paul's expertise.

3.3 **Diagram Design** (iterative per-diagram workflow)

For each diagram: draft Mermaid → validate rendering → review content → refine → render SVG+PNG.

**Diagram 1 — High-Level System Architecture** (MOST IMPORTANT)
- Progressive variants if PD-2 confirmed:
  - (A) Business stakeholder view: 3-4 boxes — Health Plan, Autonomize Platform, Data Sources, Regulatory
  - (B) Component view: expand each box into internal components
  - (C) Data flow view: show how a PA request traverses the system
- Follow progressive disclosure: slides present A → B → C

**Diagram 2 — PA Request Ingestion**
- Focus on ONE intake channel (the simplest, most modern — likely web portal API)
- Show: submission → validation → AI processing → determination → response
- Highlight the AI determination step prominently

**Diagram 3 — Clinical Data Access**
- Simplify per TD-4 decision (avoid deep FHIR internals if Paul prefers)
- Focus on ONE critical data source for the PA decision
- Show security boundaries clearly (where PHI flows, where it's encrypted)

**Diagram 4 — Security & Zero Trust**
- Visual security layers (identity → network → data → application → AI)
- AI-specific controls front and center (prompt injection defense, output validation, agent boundaries)
- Align to Autonomize's SOC 2 / HIPAA attestation

**Diagram 5 — MLOps / LLMOps** (per TD-5 decision)
- Focus on: LLM evaluation pipeline, automated guardrails, human-in-the-loop feedback
- Clearly distinguish: agent capabilities (tools, skills, orchestration) vs model capabilities (prediction, generation)
- Clearly distinguish: models we control (fine-tuned classifiers) vs proprietary models (Claude, GPT)
- Show the feedback loop: human review → eval dataset update → regression test → model update
- Minimize traditional ML complexity unless justified by ensemble architecture

3.4 **Single Source of Truth Document**
Create `outputs/eng-2026-004-v2/solution-architecture-source-of-truth.md`:
- Master system diagram (most detailed — all other diagrams are views of this)
- Complete technology decision table with URLs
- All assumptions in one table
- Open questions we'd ask in real discovery (map to assumptions)
- PA business process reference (standard flow, cited)
- This document grounds ALL other deliverables — if something isn't here, it shouldn't be in the slides

3.5 **Architecture Feedback to Incorporate:**

<architecture_feedback>
- Autonomize AI platform at the center — not a custom-built greenfield system
- Align agent workflow directly to how Autonomize's PA Copilot works (from research)
- AI governance and LLM-specific risks at the forefront of design
- Use technologies Paul knows that work across Azure AND AWS (Python, Kafka, PostgreSQL, Snowflake)
- Do NOT use Kafka in demo (too complex for 48 hours) — production only if justified
- Focus on shared services, tools, and APIs over complex multi-agent protocols
- Do NOT design more agents than needed — if one agent with skills works, prefer it
- Use traditional ML (classifiers, predictors) where appropriate — not everything needs an LLM
- Every component in a diagram must be interesting, important, required, and easy for Paul to discuss
- Follow standard PA business processes exactly — cite authoritative sources (AMA, CAQH, CMS)
- Innovate the technology, not the business process
- Do NOT specify more specific names/versions than necessary (avoid "FHIR R4.0.1", just "FHIR R4")
- Do NOT address legacy systems unless the assignment explicitly mentions them
- Do NOT make up data flow percentages unless cited
- Do NOT design for every integration — go deep on 3, summarize others
- Leverage pre-built solutions (Autonomize marketplace, cloud managed services) over custom-build
- Only custom-build what makes business sense (cost savings, data sovereignty, reduced dependencies)
</architecture_feedback>

### Deliverable
- Updated `knowledge_base/architecture.json` (v2.0)
- `outputs/eng-2026-004-v2/solution-architecture-source-of-truth.md`
- `outputs/eng-2026-004-v2/diagrams/` — Mermaid sources, SVG, PNG (white background)

### Verification
- [ ] Generic-first design with separate technology mapping table
- [ ] Progressive disclosure: diagrams increase in complexity
- [ ] All technology choices justified with verified URLs
- [ ] Source of truth document is complete and internally consistent
- [ ] Mermaid diagrams render without errors via `mmdc`
- [ ] `python tests/validate_knowledge_base.py` passes
- [ ] Git commit and push

**HUMAN CHECKPOINT**: Review architecture, diagrams, and source of truth before proceeding.

---

## Phase 4: Security & Compliance Review

> **Skill**: `solutions-architecture-agent:security-review` | `--depth STANDARD`
> **Entry**: Architecture v2.0 confirmed
> **Exit**: Security review focused on AI-specific controls and healthcare compliance
> **Read now**: `knowledge_base/security_review.json`, `knowledge_base/architecture.json`

### Tasks

4.1 **AI-Specific Security Controls** (HIGHEST PRIORITY for this assignment)
- LLM prompt injection defense (input validation, output filtering, sandboxing)
- AI agent authorization boundaries (least privilege, capability restrictions)
- Model output validation and automated guardrails
- Data poisoning prevention in fine-tuning pipelines
- AI governance framework (model cards, decision audit trails, explainability)
- Human-in-the-loop safeguards (when AI cannot make autonomous decisions)

4.2 **Zero Trust Architecture**
- Identity-centric security model (not network-perimeter)
- Continuous verification of all actors (users, agents, services)
- Least privilege for AI agents accessing clinical data
- Microsegmentation between components

4.3 **Healthcare Compliance Mapping**
- HIPAA: Privacy Rule, Security Rule, Breach Notification — architectural controls only
- Audit trail: tamper-proof logging for all AI decisions (backlog #5)
- PHI handling: encryption at rest and in transit, de-identification for analytics
- Brief mention of state-level PA regulations as awareness item (backlog #11)

4.4 **Simplification Rules:**
- Do NOT cite specific NIST control numbers or framework IDs
- Summarize each compliance program in 1-2 sentences (what it is, why it matters)
- Focus on architectural patterns: "mutual TLS between services" not "use encryption"
- Make every security concept something Paul can explain confidently
- Do NOT include compliance controls Paul hasn't worked with directly

### Deliverable
- Updated `knowledge_base/security_review.json` (v2.0)

### Verification
- [ ] AI-specific controls are the most prominent section
- [ ] No memorization-heavy compliance IDs or framework numbers
- [ ] Security measures are architectural patterns, not generic advice
- [ ] Aligns with architecture v2.0 components
- [ ] `python tests/validate_knowledge_base.py` passes
- [ ] Git commit and push

---

## Phase 5: Project Planning & Demo Scope

> **Skill**: `solutions-architecture-agent:project-plan` | `--depth STANDARD`
> **Entry**: Architecture and security confirmed
> **Exit**: Phased roadmap with demo as Phase 0 of implementation
> **Read now**: `knowledge_base/project_plan.json`, `knowledge_base/estimate.json`

### Tasks

5.1 **Restructure Roadmap as Progressive Delivery**
- **Phase 0 — Demo** (built by Paul with Claude Code, per DM-2 timeline)
- **Phase 1 — Production MVP** (core PA automation, single integration, single LOB)
- **Phase 2 — Scale** (additional integrations, multi-LOB, advanced MLOps)
- **Phase 3 — Enterprise** (multi-tenant scaling, advanced analytics, marketplace agents)
- AI/killer features front-loaded — NOT waterfall data integrations first
- Agile: working product every sprint, demos every 1-2 weeks, releases after each phase
- Each phase ends with a deployable, demonstrable system

5.2 **Demo Implementation Plan**
Create `outputs/eng-2026-004-v2/plans/demo-implementation-prompt.md`:
- Self-contained prompt for Claude Code plan mode
- Tightly scoped to Paul's skills and timeline from DM-1/DM-2 decisions
- Single agent with PA determination capability
- Minimal dependencies: native Anthropic SDK, no frameworks
- Mock data integrations (clinical data, eligibility)
- Designed for rapid iteration: working demo every hour of development
- Script for walking through the demo aligned to user stories
- Focus on killer AI features that map to the job role

5.3 **Future State Vision** (for final slide)
- Scaling considerations: multi-tenancy vs multi-instance trade-offs
- Performance vs privacy balance
- Marketplace agent deployment model
- Honest about unknowns: "these decisions require discovery with the customer"

5.4 **REMOVE from v2:**
- All financial estimates (no dollar amounts from LLM)
- All hourly rate assumptions
- All FTE counts unless cited from industry sources
- All made-up percentages (keep only cited industry benchmarks like CAQH)
- All specific timeline numbers that Paul would struggle to defend

### Deliverable
- Updated `knowledge_base/project_plan.json` (v2.0)
- `outputs/eng-2026-004-v2/plans/demo-implementation-prompt.md`

### Verification
- [ ] Demo scope achievable within confirmed timeline
- [ ] No fabricated estimates of any kind
- [ ] Phased approach shows clear progression from demo → production → scale
- [ ] `python tests/validate_knowledge_base.py` passes
- [ ] Git commit and push

**HUMAN CHECKPOINT**: Review roadmap and demo plan before proposal assembly.

---

## Phase 6: Proposal Assembly — Slide Deck & Supporting Materials

> **Skill**: `solutions-architecture-agent:proposal` | `--depth COMPREHENSIVE` | `--type custom`
> **Entry**: All upstream KB files at v2.0
> **Exit**: Complete slide content, per-slide generation prompts, supporting materials
> **Read now**: All KB files, `outputs/eng-2026-004/proposal.md` (v1 for reference)

### Tasks

6.1 **Slide Deck Structure** (10-12 slides, per assignment)

Recommended flow (adjust based on Phase 0 decisions):
1. **Title & Introduction** — Paul's credibility: Arine (50M members), AWS (5 certs), healthcare AI
2. **Executive Summary** — Business benefits of Paul's TECHNICAL DECISIONS (not the AI agent itself)
3. **High-Level Architecture** — Business stakeholder view (3-4 components)
4. **System Architecture Detail** — Component view with technology labels
5. **PA Ingestion & Processing** — How a PA request flows through the system
6. **Clinical Data Integration** — Secure access to clinical data for AI processing
7. **Security & Zero Trust** — Layered security with AI-specific controls (Paul's favorite)
8. **Healthcare Compliance** — HIPAA, audit trails, AI governance
9. **MLOps / LLMOps** — Eval pipeline, guardrails, feedback loops, model lifecycle
10. **Implementation Roadmap** — Demo → MVP → Scale → Enterprise (progressive phases)
11. **Future State & Scaling** — Multi-tenant, marketplace, advanced capabilities
12. **Discussion & Q&A Topics** — Guided discussion starters for the panel

6.2 **Per-Slide Generation Prompts**
For each slide, create a self-contained prompt file in `outputs/eng-2026-004-v2/slide-generation-prompts/`:
- Slide title and subtitle
- Key content (3-5 bullet points max per slide)
- Tables or diagram references (SVG/PNG paths)
- Speaker notes (natural speech, ~5 min per slide when read aloud)
- Design guidance (layout, color, emphasis areas)
- Assignment question(s) this slide answers (traceability)

6.3 **Presentation Feedback to Incorporate:**

<presentation_feedback>
ORDER & FLOW:
- Executive summary FIRST, implementation phases LAST
- Logical progression: overview → architecture → security → compliance → MLOps → roadmap → future
- Each slide builds on the previous — the audience never sees something they can't yet contextualize

EXECUTIVE SUMMARY (Slide 2):
- Sells Paul and his SA skills, NOT the AI agent itself
- Business benefits of his specific technical decisions
- Altais case study as strongest proof point (backlog #3: 45% review time reduction, verified)
- CAQH per-transaction cost benchmarks if we kept industry-cited numbers (backlog #4)
- Do NOT focus on what PA automation does in general — the audience already knows

SPEAKER NOTES:
- Must sound like Paul — use career-data.json to calibrate voice
- Remove any sentence Paul cannot confidently speak to (test: would Paul say this in an interview?)
- No: "For EDI, we parse the X12 278 transaction against the ASC X12 grammar" — Paul cannot speak to this
- No: Kolmogorov-Smirnov test details, SageMaker internals, LOB terminology if inaccurate
- Yes: AWS architecture patterns, Kafka operational experience, Snowflake data pipelines, HIPAA controls

DIAGRAMS:
- Follow progressive disclosure across slides
- Initial diagrams: 3-4 components, clean, easy to explain
- Later diagrams: add technical detail progressively
- Every component drawn must be interesting, important, required, and easy to discuss
- Do not draw standard/obvious components unless the assignment calls them out

MLOps / LLMOps (Slide 9):
- Think and speak like a data scientist with LLM research background
- Explain model drift and performance degradation so business leaders understand
- Distinguish: agent capabilities vs model capabilities
- Distinguish: custom models we control vs proprietary models we don't
- Focus on LLM ops (evals, guardrails, human feedback) over traditional ML ops
- Do NOT overcomplicate — bare minimum to address assignment-specific issues
- Do NOT use statistical terminology Paul can't explain

IMPLEMENTATION ROADMAP (Slide 10):
- Better visualization than v1 — no cryptic P-001/G-001 labels
- Show clear progression: demo → Phase 1 → Phase 2 → future
- AI features front-loaded, not behind waterfall data integrations
- Every phase produces a working, demonstrable product

FUTURE STATE (Slide 11):
- Grounded in the core problem/solution — do NOT drift
- Multi-tenant vs multi-instance: present as a trade-off to discuss, not a decided answer
- Performance vs data privacy balance
- Be honest about what requires customer discovery
- Do NOT use LOB unless verified accurate for this context

SELF-CONTAINED DECK:
- No references to internal SA workflow artifacts (KB files, reviews.json, etc.)
- No citations of requirements that were generated, not from the assignment (e.g., CMS-0057-F if not in assignment)
- The deck + original assignment = everything the audience needs
- Designed as email attachment for interview panel
</presentation_feedback>

6.4 **Email Draft**
Create `outputs/eng-2026-004-v2/email-draft.md`:
- Professional response to the assignment email
- Acknowledge AI tool usage: "I used my Solutions Architecture Agent — a Claude Code plugin I built — to iteratively develop and validate this architecture"
- Position Paul as an AI engineer using best-in-class tools
- Attach slide deck reference
- Express enthusiasm and readiness for the presentation
- Tone: confident, collaborative, honest — earning trust

6.5 **Format for Claude CoWork**
Organize all assets so Claude CoWork for Windows can ingest them into context:
- Clear file naming
- Index file listing all deliverables
- Logical directory structure

### Deliverable
- `outputs/eng-2026-004-v2/proposal.md` — full slide content with speaker notes
- `outputs/eng-2026-004-v2/slide-generation-prompts/slide-{NN}-{title}.md` — per-slide prompts
- `outputs/eng-2026-004-v2/email-draft.md`

### Verification
- [ ] 10-12 slides (no more)
- [ ] Every assignment question explicitly answered (cross-check traceability matrix)
- [ ] No uncited claims, fabricated numbers, or hallucinated references
- [ ] Speaker notes pass "read aloud" test — natural speech, Paul's voice
- [ ] Slide deck is self-contained (no internal artifact references)
- [ ] All diagram references point to existing rendered files
- [ ] Git commit and push

**HUMAN CHECKPOINT**: Review ALL slide content and speaker notes before final review phase.

---

## Phase 7: Comprehensive Review

> **Skill**: `solutions-architecture-agent:review` | `--depth COMPREHENSIVE`
> **Entry**: All v2.0 deliverables complete and human-approved
> **Exit**: Review score ≥ 9.0/10, 0 blocking findings
> **Read now**: All KB files, all output files

### Tasks

7.1 **Cross-Deliverable Consistency Audit**
- Every fact in slide deck traces to source-of-truth document
- Technology names, component names, data flows identical across all files
- Diagrams match the architecture description exactly
- Speaker notes align with slide bullet points

7.2 **Assignment Compliance Check**
- Requirements traceability matrix: 100% coverage (every question answered)
- Slide count: 10-12
- All required diagram types present and rendered
- Demo plan is achievable and aligned to full architecture

7.3 **Anti-Hallucination Audit** (CRITICAL)
- Click-test every URL in every document
- Verify every statistic has a cited, authoritative source
- Verify every technology claim matches current documentation
- Verify Autonomize AI claims against their actual public materials
- Flag any claim that cannot be independently verified

7.4 **Paul-Readiness Audit**
- For each slide: can Paul speak to every bullet point with confidence?
- Flag concepts Paul identified as difficult (FHIR, statistics, X12)
- Verify speaker notes are in Paul's voice (calibrated to career-data.json)
- Verify no memorization-heavy content (specific numbers, control IDs)

7.5 **Autonomous Fix Cycle**
Per feedback_autonomous_review_cycle: if review finds SA agent skill/schema bugs, fix them autonomously without stopping for approval. Run up to 3 fix-QA cycles.

### Deliverable
- Updated `knowledge_base/reviews.json` (v2.0)
- Fix list applied to all affected files

### Verification
- [ ] Review score ≥ 9.0/10
- [ ] 0 blocking findings
- [ ] All URLs verified working
- [ ] All cross-references consistent
- [ ] `python tests/validate_knowledge_base.py` passes
- [ ] Git commit and push

**HUMAN CHECKPOINT**: Review findings. Proceed to final assembly only if review passes.

---

## Phase 8: Final Output Assembly

> **Skill**: None (assembly, rendering, organization)
> **Entry**: Review passed (≥ 9.0/10)
> **Exit**: All deliverables organized, cross-referenced, and ready for Paul

### Tasks

8.1 **Interview Prep Materials**
Create `outputs/eng-2026-004-v2/interview-prep/`:

- **qa-prep.md** — 15+ anticipated panel questions with detailed answers:
  - Architecture decisions: "Why this cloud?", "Why this event streaming approach?"
  - AI/ML: "How do you handle model drift?", "What if AI accuracy drops?", "Prompt injection defense?"
  - Healthcare: "How does the interoperability layer work?", "What about auto-denial?"
  - Operational: "What's the deployment model?", "How does monitoring work?"
  - Skepticism: "Autonomize platform goes down?", "Why multi-tenant?", "What about vendor lock-in?"

- **technical-deep-dive.md** — Study guide for each diagram:
  - Talking points organized by diagram (separate from speaker notes)
  - "If asked to go deeper" sections for each slide topic
  - Technical concepts explained at Paul's level (not memorization, understanding)

- **assumptions-and-questions.md** — What we'd still ask in real discovery:
  - Map each assumption to the design decision it supports
  - Frame as "great questions to ask in the interview" — shows thoroughness

8.2 **Render Final Diagrams**
- All Mermaid → SVG via `mmdc`
- All Mermaid → PNG with `-b white` for PowerPoint
- Verify every diagram renders cleanly at presentation size

8.3 **Organize Output Directory**

```
outputs/eng-2026-004-v2/
├── README.md                                  # Index of all deliverables
├── proposal.md                                # Slide content + speaker notes
├── solution-architecture-source-of-truth.md   # Master reference document
├── research-context.md                        # Research findings with citations
├── requirements-traceability.md               # Assignment → slide mapping
├── email-draft.md                             # Interview response email
├── slide-generation-prompts/                  # Per-slide PowerPoint prompts
│   ├── slide-01-introduction.md
│   ├── slide-02-executive-summary.md
│   ├── ...
│   └── slide-12-discussion.md
├── interview-prep/
│   ├── qa-prep.md                             # Anticipated Q&A (15+ questions)
│   ├── technical-deep-dive.md                 # Per-diagram study guide
│   └── assumptions-and-questions.md           # Discovery questions + assumption map
├── diagrams/
│   ├── 01-system-context.mmd                  # Mermaid source
│   ├── 01-system-context.svg                  # SVG render
│   ├── 01-system-context.png                  # PNG for PowerPoint
│   ├── ...
│   └── {variant diagrams if PD-2 confirmed}
└── plans/
    ├── demo-implementation-prompt.md          # Claude Code plan mode prompt for demo build
    └── backlog-v2.md                          # Remaining improvements (post-interview)
```

8.4 **Update Engagement State**
- Update `knowledge_base/engagement.json`: all lifecycle_state entries to v2.0
- Update session context: `.claude/plans/eng-2026-004-session-context.md`

### Final Verification Checklist
- [ ] All files present per directory structure above
- [ ] All internal file references/links are valid
- [ ] All external URLs verified working
- [ ] All diagrams render without errors
- [ ] KB validation passes: `python tests/validate_knowledge_base.py`
- [ ] Cross-deliverable consistency: no contradictions between any two documents
- [ ] Slide deck self-contained: no references to internal artifacts
- [ ] Speaker notes natural: passes "read aloud" test
- [ ] Requirements traceability: 100% assignment coverage
- [ ] Git commit with descriptive message → push

---

## Appendix A: Backlog Items to Incorporate

From `outputs/eng-2026-004/plans/backlog.md`:

| # | Item | Phase | Action |
|---|------|-------|--------|
| 1 | Re-run WA reviewers | 3 | Launch parallel `solutions-architecture-agent:parallel-wa-reviewer` agents |
| 2 | Correct SageMaker PSI claim | 3 | Fix if SageMaker is still in architecture; otherwise remove |
| 3 | Add Altais case study | 6 | Add to executive summary slide — strongest verified proof point |
| 4 | Add CAQH cost benchmarks | 6 | Add per-transaction savings if keeping cited industry numbers |
| 5 | External audit trail | 4 | Add tamper-proof audit anchoring to security review |
| 8 | FDA PCCP framework | 3 | Add only if relevant to LLMOps discussion — don't force it |
| 10 | Q&A prep document | 8 | Create comprehensive Q&A prep |
| 11 | State PA regulations | 4 | Brief awareness mention in security/compliance |

**Skip**: #6 (Kafka topics — depends on TD-3), #7 (Snowflake DDM — out of scope), #9 (Wasserstein — Paul avoids statistics), #12 (PNG — included in Phase 8), #13-14 (post-interview).

## Appendix B: Key Principles for This Iteration

These principles synthesize Paul's feedback and latest best practices (March 2026):

1. **Assignment fidelity over comprehensiveness** — Answer exactly what's asked. Don't add.
2. **Generic-first architecture** — Design the system, then choose the vendors. Reduces bias.
3. **Progressive disclosure** — Every visual builds on the previous one. Never overwhelm.
4. **Single source of truth** — One document grounds all others. Contradictions are bugs.
5. **Paul-speakable content only** — If Paul can't confidently explain it, remove it.
6. **Cited or removed** — Every claim, statistic, and technology recommendation has a source, or it doesn't exist.
7. **AI-first, not AI-only** — Use traditional ML, simple web services, and managed solutions where they're the right tool.
8. **Earn trust through honesty** — Acknowledge unknowns. Frame discovery questions as strengths.
9. **Simplicity is sophistication** — The best architecture is the one with the fewest components that meets all requirements.
10. **Demo proves the vision** — The demo is the first phase of implementation, not a throwaway prototype.
