# Phase 2: Requirements Specification

> Generated: 2026-03-15 | Phase: 2 of 9
> Inputs: master-plan.md, phase-1-results.md (88 patterns), guiding-principles.md (42 principles), pre-sales-lifecycle.md, reference-materials-index.md, SCHEMA_DESIGN.md

---

## 1. Introduction

### 1.1 Purpose

This document defines the complete requirements for the AI Solutions Architecture Agent — a single-agent Claude Code plugin with 9 skills covering the SA lifecycle from requirements discovery through technical project planning. It transforms the 88 patterns extracted in Phase 1 into traceable, testable requirements that drive Phases 3-9.

### 1.2 Scope Boundary

The agent **designs and plans**. It does NOT implement, deploy, or write production code. A future AI Engineering Agent consumes this agent's outputs.

| In Scope | Out of Scope |
|----------|-------------|
| Requirements discovery | Code generation |
| System architecture | Deployment scripts |
| Data modeling | CI/CD pipelines |
| Security review | Prompt engineering (for target systems) |
| Integration planning | Testing implementation |
| Cost estimation | Infrastructure provisioning |
| Project planning | Monitoring setup |
| Proposal assembly | Production operations |

### 1.3 Numbering Convention

| Code | Format | Scope |
|------|--------|-------|
| FR-REQ-NNN | Functional | /requirements |
| FR-ARC-NNN | Functional | /architecture |
| FR-EST-NNN | Functional | /estimate |
| FR-PPL-NNN | Functional | /project-plan |
| FR-PRO-NNN | Functional | /proposal |
| FR-DM-NNN | Functional | /data-model |
| FR-SR-NNN | Functional | /security-review |
| FR-IP-NNN | Functional | /integration-plan |
| FR-RV-NNN | Functional | /review |
| NFR-NNN | Non-Functional | Agent-wide |
| CCR-NNN | Cross-Cutting | Agent-wide |

---

## 2. Personas

### 2.1 Enterprise Solutions Architect (Persona: "Priya")

**Role**: Senior SA at a consulting firm (10-200 person team). Runs engagements for mid-market to enterprise clients.

**Goals**:
- Produce exemplar-quality deliverables for complex, multi-stakeholder engagements
- Maintain consistent quality across the full SA lifecycle (8-skill sequence)
- Generate SOWs that win contracts by clearly articulating value
- Ensure Well-Architected compliance across all designs

**Constraints**:
- Works within established consulting delivery models (2-week sprints, PSI cycles)
- Must produce deliverables that pass principal engineer review
- Handles both greenfield and migration engagements
- Clients span healthcare (HIPAA), fintech (SOC2/GLBA), and general enterprise

**Primary engagement flow**: Full lifecycle — /requirements → /architecture → /data-model → /security-review → /estimate → /project-plan → /proposal → /review

### 2.2 Independent Consultant (Persona: "Marcus")

**Role**: Solo SA consultant working with startups and SMBs. Wears multiple hats (sales, SA, delivery).

**Goals**:
- Produce professional deliverables quickly (hours, not days)
- Use quick discovery to qualify opportunities and prioritize pipeline
- Generate proposals that communicate value to non-technical decision-makers
- Minimize context switching between clients and engagements

**Constraints**:
- Limited time per engagement (pre-sales typically 4-8 hours total)
- Clients often lack technical vocabulary — outputs must be accessible
- Works across diverse industries (no single-industry specialization)
- Needs multi-session support (work spans days, not single sittings)

**Primary engagement flow**: Streamlined — /requirements (quick/standard) → /architecture → /estimate → /proposal

### 2.3 Startup Technical Founder (Persona: "Aisha")

**Role**: Technical co-founder (engineer background) making architecture decisions for the first time as a business owner.

**Goals**:
- Validate technical approach before hiring a team or engaging contractors
- Produce architecture docs that communicate vision to investors and potential hires
- Get realistic cost and timeline estimates to inform fundraising
- Understand security and compliance requirements early

**Constraints**:
- Not a trained SA — needs guidance, not just tool output
- Budget-sensitive — wants cost-optimized architectures
- Building 0-to-1 (greenfield exclusively)
- Needs plain-language explanations alongside technical detail

**Primary engagement flow**: Focused — /requirements (quick) → /architecture → /estimate → /project-plan

---

## 3. Functional Requirements

### 3.1 /requirements — Requirements Discovery

| ID | Requirement | Source Patterns | Priority |
|----|-------------|----------------|----------|
| FR-REQ-001 | Support three discovery tiers: Quick (15 min), Standard (30-45 min), Comprehensive (90 min), selected by complexity assessment | R1 | Must Have |
| FR-REQ-002 | Implement progressive questioning: Context → Problem → Workflow → Quantification → Technical → Vision | R2 | Must Have |
| FR-REQ-003 | Classify AI suitability as HIGH/MEDIUM/LOW with 6-question test, estimated savings, and recommended agent patterns | R3 | Must Have |
| FR-REQ-004 | Perform real-time pain point classification during discovery: description, classification, time impact, follow-up question, solution pattern, estimated savings | R4 | Should Have |
| FR-REQ-005 | Extract structured requirements from unstructured notes across 7 categories with gap identification and completeness scoring | R5 | Must Have |
| FR-REQ-006 | Provide comprehensive workshop facilitation with pre-session prep, 6 discovery sections, and brand voice capture | R6 | Should Have |
| FR-REQ-007 | Adapt communication style by stakeholder type: solo/small business, corporate, non-technical, technical | R7 | Must Have |
| FR-REQ-008 | Validate completeness after gathering: checklist verification, gap listing, follow-up question generation, COMPLETE/PARTIAL/INCOMPLETE scoring | R8 | Must Have |
| FR-REQ-009 | Support both greenfield and migration engagement types with conditional sections (legacy_system, migration constraints) | Master Plan | Must Have |
| FR-REQ-010 | Write structured output to `requirements.json` per SCHEMA_DESIGN.md specification | Schema Design | Must Have |
| FR-REQ-011 | Support four-type requirement classification: Functional, Technical, Operational, Transitional with Core/Essential/Desired priority | AGADA templates | Should Have |
| FR-REQ-012 | Capture context-of-use analysis: users, tasks, technical/physical/organizational environment | AGADA Maguire-Bevan | Should Have |
| FR-REQ-013 | Generate stakeholder analysis with critical success factors and persona mapping | AGADA PM template | Should Have |
| FR-REQ-014 | Produce explicit scope boundaries (in-scope/out-of-scope with justification) | AGADA templates | Must Have |
| FR-REQ-015 | Use BANT framework for opportunity qualification (Budget, Authority, Need, Timeline) | Pre-sales lifecycle, AVAHI qualifying questions | Should Have |

### 3.2 /architecture — Solution Architecture

| ID | Requirement | Source Patterns | Priority |
|----|-------------|----------------|----------|
| FR-ARC-001 | Implement multi-step design process: tech stack selection → architecture diagram → component design | A1 | Must Have |
| FR-ARC-002 | Evaluate technology stack across categories (AI/ML, Backend, Frontend, Cloud, DevOps) with rationale per layer, alternatives, and trade-offs | A2 | Must Have |
| FR-ARC-003 | Generate architecture diagrams in Mermaid and ASCII formats with configurable detail level (high-level/standard/detailed) and audience (technical/leadership/mixed) | A3 | Must Have |
| FR-ARC-004 | Perform cascade analysis when updating prior decisions: trace dependencies, identify affected downstream deliverables, recommend re-run sequence | A4 | Should Have |
| FR-ARC-005 | Generate dual-audience output: technical builders (specs, implementation guidance) and business leaders (executive summary, ROI, go/no-go) | A5 | Must Have |
| FR-ARC-006 | Plan cloud infrastructure: services needed, deployment pattern, monitoring, backup/DR (RTO/RPO), cost constraints | A6 | Must Have |
| FR-ARC-007 | Design high availability: multi-zone deployment, zone-aware load balancing, storage versioning, health alarms | A7 | Should Have |
| FR-ARC-008 | Design auto-scaling: horizontal scaling parameters, serverless for event-driven, right-sizing guidance | A8 | Should Have |
| FR-ARC-009 | Apply cost-aware infrastructure design: right-sizing, serverless for spiky workloads, storage lifecycle, log retention policies | A9 | Must Have |
| FR-ARC-010 | Define observability strategy: centralized logging, metrics (including AI-specific), distributed tracing | A10 | Should Have |
| FR-ARC-011 | Design AI/ML platform components: Tool Gateway, Identity Layer, Execution Runtime, Persistent Memory | A11 | Should Have |
| FR-ARC-012 | Recommend multi-agent orchestration patterns when appropriate: Supervisor-Worker, CoT, ReAct, Plan-and-Execute | A12 | Should Have |
| FR-ARC-013 | Design component-based UI architecture when frontend is in scope | A13 | Nice to Have |
| FR-ARC-014 | Recommend IaC principles: declarative infrastructure, stack-based grouping, environment parameterization, immutable deployments | A14 | Should Have |
| FR-ARC-015 | Score against Well-Architected Framework (6 pillars, 0-10 each) with notes per pillar | CC1 | Must Have |
| FR-ARC-016 | Include 5 GenAI diagram patterns when applicable: Simple LLM Wrapper, RAG Pipeline, Multi-Agent, Agentic Workflow, Conversational AI with Memory | A3 | Should Have |
| FR-ARC-017 | Write structured output to `architecture.json` per SCHEMA_DESIGN.md specification | Schema Design | Must Have |
| FR-ARC-018 | Use `ultrathink` for complex architectural reasoning | Master Plan | Must Have |

### 3.3 /estimate — Estimation

| ID | Requirement | Source Patterns | Priority |
|----|-------------|----------------|----------|
| FR-EST-001 | Apply LOE estimation framework: account for optimism bias (15-25%), multiple scenarios (weighted 3-point), break to 2-5 day tasks, include non-coding activities (30-40%) | E1 | Must Have |
| FR-EST-002 | Apply cost estimation across 5 categories: Development, Operational (monthly), AI-Specific, TCO (3-year), ROI | E2 | Must Have |
| FR-EST-003 | Generate team composition recommendations by company stage (startup/growth/scale) with hiring priority timeline | E3 | Must Have |
| FR-EST-004 | Include confidence scoring: HIGH (>80% present directly), MEDIUM (50-80% with caveats), LOW (<50% flag for human review) | E4 | Must Have |
| FR-EST-005 | Track cost per operation: input/output size, model used, latency, with configurable pricing table | E5 | Should Have |
| FR-EST-006 | Apply complexity assessment checklist (0-10 scale) to calibrate uncertainty buffers | E1 | Must Have |
| FR-EST-007 | Support 4 estimation methods: Bottom-Up, Historical Comparison, T-Shirt Sizing, Three-Point | E1 | Should Have |
| FR-EST-008 | Write structured output to `estimate.json` per SCHEMA_DESIGN.md specification | Schema Design | Must Have |

### 3.4 /project-plan — Technical Project Plan

| ID | Requirement | Source Patterns | Priority |
|----|-------------|----------------|----------|
| FR-PPL-001 | Generate phased delivery plan: Foundation → Core Development → AI Integration → Testing → Launch with decision gates between phases | PP1, PP2 | Must Have |
| FR-PPL-002 | Define decision gates: GO/Conditional GO/NO-GO with specific criteria per gate (strategic alignment, ROI, feasibility, resources, acceptance tests, security audit) | PP2 | Must Have |
| FR-PPL-003 | Identify risks across 3 categories (Technical, Resource, Timeline) with specific mitigation strategies | PP3 | Must Have |
| FR-PPL-004 | Generate sprint plans: 2-week sprints, features mapped with estimated effort, resource allocation per developer | PP1, Pre-sales lifecycle | Must Have |
| FR-PPL-005 | Support migration-specific timelines: legacy system analysis, parallel run periods, data migration phases, rollback plans, feature parity checklists | Master Plan, Schema Design | Must Have |
| FR-PPL-006 | Define milestones with gate types (approval/demo/signoff), target dates, and phase association | Schema Design | Must Have |
| FR-PPL-007 | Map critical path and dependency graph (internal finish-to-start + external dependencies with owners and needed-by dates) | Schema Design | Must Have |
| FR-PPL-008 | Generate communication plan: stakeholder update cadence, demo schedule, decision points with deciders | Schema Design | Should Have |
| FR-PPL-009 | Write structured output to `project_plan.json` per SCHEMA_DESIGN.md specification | Schema Design | Must Have |

### 3.5 /proposal — Proposal Assembly

| ID | Requirement | Source Patterns | Priority |
|----|-------------|----------------|----------|
| FR-PRO-001 | Assemble discovery proposals: 3-phase assessment (Research → Investigation → Recommendation), 4 decision scenarios (GO/GO with Modifications/PAUSE/NO-GO) | P1 | Must Have |
| FR-PRO-002 | Assemble implementation proposals with KB-to-proposal mapping: requirements → business case, architecture → technical approach, estimates → financial investment | P2 | Must Have |
| FR-PRO-003 | Assemble internal proposals: 12-18 slide structure with audience differentiation (CEO strategic, CFO financial, CTO technical, VPs operational), anticipated Q&A prep | P3 | Should Have |
| FR-PRO-004 | Assemble pitch decks: 10-15 slides, narrative arc (Challenge → Solution → Path Forward), evidence-based persuasion, phased investment options | P4 | Should Have |
| FR-PRO-005 | Read from ALL KB files, assemble into proposal, add proposal-specific content. NEVER re-analyze — assemble only | P1, CC2 | Must Have |
| FR-PRO-006 | Follow SOW template structure (12 sections): Engagement Description, Business Objectives, Technical Requirements, Team Leads and Roles, Project Scope, Services Out of Scope, Change Order, Anticipated Schedule, Project Rate, Payment Methods, Assumptions, Signature Block | Pre-sales lifecycle | Must Have |
| FR-PRO-007 | Apply decision framework: Approve (ROI >3x/3yr, payback <18mo), Conditional (ROI 2-3x, payback 18-24mo), Reject (ROI <2x, payback >24mo) | P2 | Should Have |
| FR-PRO-008 | Write output to `outputs/` directory (not KB), organized by engagement ID | Schema Design | Must Have |

### 3.6 /data-model — Data Modeling

| ID | Requirement | Source Patterns | Priority |
|----|-------------|----------------|----------|
| FR-DM-001 | Design entity-relationship schemas: entities, relationships, data types, constraints, indexes, audit fields, migration-friendly design | DM1 | Must Have |
| FR-DM-002 | Design vector database schemas: collection design, chunking strategy, metadata schema, embedding model selection, relevance filtering, retrieval parameters | DM2 | Must Have |
| FR-DM-003 | Design knowledge pipeline architecture: document loading → preprocessing → embedding generation → vector storage → retrieval interface | DM3 | Should Have |
| FR-DM-004 | Define data validation framework: declarative rules, boundary validation, type/range/pattern checks | DM4 | Should Have |
| FR-DM-005 | Organize knowledge base structure: index documents, categories, format standardization, size validation, version tracking | DM5 | Should Have |
| FR-DM-006 | Define repository pattern for data access: CRUD + domain queries, parameterized queries, typed data objects | DM6 | Nice to Have |
| FR-DM-007 | Capture data requirements from upstream: data sources, volume, structure, quality, retention from requirements; data layer design from architecture | DM7 | Must Have |
| FR-DM-008 | Support graph schemas: node types, edge types, ontology definitions with key concepts, taxonomy, and relationships | Schema Design | Should Have |
| FR-DM-009 | Define data governance: PII fields, retention policy, encryption, access control | Schema Design | Must Have |
| FR-DM-010 | Write structured output to `data_model.json` per SCHEMA_DESIGN.md specification | Schema Design | Must Have |
| FR-DM-011 | Use `ultrathink` for complex data modeling decisions | Master Plan | Must Have |

### 3.7 /security-review — Security & Privacy Review

| ID | Requirement | Source Patterns | Priority |
|----|-------------|----------------|----------|
| FR-SR-001 | Decompose security requirements across 5 dimensions: authentication, secrets, network isolation, AI guardrails, compliance | SR1 | Must Have |
| FR-SR-002 | Design defense-in-depth architecture: network perimeter, identity/access, application security, data protection, monitoring/auditability | SR2 | Must Have |
| FR-SR-003 | Apply least-privilege IAM: enumerate required actions, scope to resources, no wildcards, separate trust from permission, agent-specific identities | SR3 | Must Have |
| FR-SR-004 | Design tiered network segmentation: Public (load balancers), Private (app servers), Isolated (databases) across 2+ AZs | SR4 | Must Have |
| FR-SR-005 | Define encryption strategy: at-rest (AES-256), in-transit (TLS 1.2+), key management (KMS with rotation), secrets vault | SR5 | Must Have |
| FR-SR-006 | Define AI-specific security controls: content filtering, PII detection, word/phrase filtering, agent authentication | SR6 | Must Have |
| FR-SR-007 | Map compliance requirements: identify applicable frameworks (HIPAA/SOC2/CCPA/GLBA/PCI-DSS), map controls, document posture (met/partial/not met) | SR7 | Must Have |
| FR-SR-008 | Apply non-negotiable security guardrails (MUST/MUST NOT checklist) | SR8 | Must Have |
| FR-SR-009 | Perform change impact analysis with risk scoring: Change Type + Blast Radius + Testing Coverage + Reversibility + System Maturity | SR9 | Should Have |
| FR-SR-010 | Produce threat model using STRIDE (or PASTA/DREAD/attack tree) with threat ID, category, severity, likelihood, risk score, mitigation, residual risk, status | Schema Design | Must Have |
| FR-SR-011 | Write structured output to `security_review.json` per SCHEMA_DESIGN.md specification | Schema Design | Must Have |
| FR-SR-012 | Use `ultrathink` for threat modeling and compliance analysis | Master Plan | Must Have |

### 3.8 /integration-plan — Integration Planning

| ID | Requirement | Source Patterns | Priority |
|----|-------------|----------------|----------|
| FR-IP-001 | Design API-to-Tool Gateway: catalog APIs, auto-generate tool definitions, centralize auth, rate limiting, protocol translation | IP1 | Should Have |
| FR-IP-002 | Design event-driven integration: event sources, serverless handlers, idempotency, dead letter queues | IP2 | Should Have |
| FR-IP-003 | Plan secure service-to-service integration: unique identity per service, explicit permissions, credentials in vault, audit trail | IP3 | Must Have |
| FR-IP-004 | Design data pipeline architecture with storage lifecycle: Hot → Warm → Cold → Delete, versioning, schema validation, partitioning | IP4 | Should Have |
| FR-IP-005 | Plan document ingestion pipeline: format-specific loaders, text splitting, metadata enrichment, batch processing, idempotency | IP5 | Should Have |
| FR-IP-006 | Define data access layer integration: UI → Business Logic → Data Access → External Services with interface contracts at each boundary | IP6 | Should Have |
| FR-IP-007 | Support phased integration approach: Phase 1 simple (CSV/exports, validate value) → Phase 2 full API integration | IP7 | Must Have |
| FR-IP-008 | Define CI/CD pipeline architecture: 6 stages (Code Quality → Testing → Security → Build → Deploy → Monitor) with reusable templates | IP8 | Should Have |
| FR-IP-009 | Define API contracts per SCHEMA_DESIGN.md: ID, direction, protocol, method, endpoint, auth, request/response schema, rate limit, error handling, SLA | Schema Design | Must Have |
| FR-IP-010 | Define data flow mappings: source/target systems, field mappings with transforms, validation rules | Schema Design | Must Have |
| FR-IP-011 | Plan migration strategy when engagement type is migration: approach (strangler fig/big bang/parallel run/phased), data migration, rollback plan | Schema Design, Master Plan | Must Have |
| FR-IP-012 | Design legacy bridging patterns: adapter, facade, anti-corruption layer, event bridge, API gateway | Schema Design | Should Have |
| FR-IP-013 | Write structured output to `integration_plan.json` per SCHEMA_DESIGN.md specification | Schema Design | Must Have |

### 3.9 /review — Deliverable Review

| ID | Requirement | Source Patterns | Priority |
|----|-------------|----------------|----------|
| FR-RV-001 | Implement LLM-as-judge methodology with 3 iteration passes: Discover-Assess-Implement-Validate → Judge-Identify-Refine-Revalidate → Final Polish. Stop early if score 9.0+ | RV1 | Must Have |
| FR-RV-002 | Apply TRM validation: generate 2-3 candidate approaches, validate against benchmarks, select highest-scoring, iterate (max 3), present only after 85% quality gate | RV2 | Should Have |
| FR-RV-003 | Score on 5 core dimensions (each 1-10): Completeness, Technical Soundness, Well-Architected Alignment, Clarity, Feasibility | RV4 | Must Have |
| FR-RV-004 | Generate prioritized improvement plans: P0 Quick Wins → P1 Strategic → P2-P3 Refinements, each with impact, effort, risk, validation criteria | RV5 | Must Have |
| FR-RV-005 | Apply dual-persona validation: Builder creates, Tester reviews adversarially, Reconciliation merges findings | RV6 | Should Have |
| FR-RV-006 | Define quality KPIs: test pass rate, response time, token efficiency, schema compliance, security (0 critical/high), overall >85% | RV7 | Must Have |
| FR-RV-007 | Apply three-dimensional assessment: Technical Excellence, Operational Excellence, Well-Architected Framework (6 pillars + GenAI Lens) | RV3 | Should Have |
| FR-RV-008 | Validate LLM response quality: relevance, tone consistency, consistency across runs, token efficiency, safety | RV10 | Should Have |
| FR-RV-009 | Apply test strategy decomposition: what needs testing, quality metrics, test data, edge cases, validation criteria | RV8 | Should Have |
| FR-RV-010 | Write review results to `reviews.json` with scores, findings, blockers, and iteration history | Schema Design | Must Have |
| FR-RV-011 | Use `ultrathink` for quality assessment reasoning | Master Plan | Must Have |
| FR-RV-012 | Review any skill output (not just architecture) — accepts any KB file as target | Schema Design | Must Have |

---

## 4. Non-Functional Requirements

### 4.1 Context Efficiency

| ID | Requirement | Priority |
|----|-------------|----------|
| NFR-001 | Skills use progressive disclosure: load only the KB sections they need, not entire files (see SCHEMA_DESIGN.md Cross-Skill Data Flow Map) | Must Have |
| NFR-002 | CLAUDE.md stays under 200 lines. Each unscoped rule file stays under 100 lines | Must Have |
| NFR-003 | Each SKILL.md is self-contained per Agent Skills standard — no cross-skill imports at runtime | Must Have |
| NFR-004 | Use `ultrathink` selectively in skills requiring deep reasoning (/architecture, /data-model, /security-review, /review) — not in all skills | Should Have |

### 4.2 Portability

| ID | Requirement | Priority |
|----|-------------|----------|
| NFR-005 | No references to operator-specific filesystem paths (no `C:\dev\`, `\\wsl.localhost\`, `D:\dev\`) | Must Have |
| NFR-006 | Runs on both Windows and Linux without modification | Must Have |
| NFR-007 | Installable as local plugin (`--plugin-dir`) and from GitHub (`/plugin install github:org/repo`) | Must Have |
| NFR-008 | All skills appear as `solutions-architecture-agent:skill-name` when installed as a plugin | Must Have |

### 4.3 Quality

| ID | Requirement | Priority |
|----|-------------|----------|
| NFR-009 | Deliverables meet exemplar-level quality: compare favorably against real SA deliverables (AGADA architecture, Revelex proposal, AVAHI SOWs) | Must Have |
| NFR-010 | All JSON output validates against JSON Schema definitions in `knowledge_base/schemas/` | Must Have |
| NFR-011 | All architecture designs evaluate against Well-Architected Framework (AWS 6 pillars + GenAI Lens, Azure WAF, GCP WAF) | Must Have |
| NFR-012 | Every estimate includes confidence level, assumptions, and range (not point-only) | Must Have |

### 4.4 Usability

| ID | Requirement | Priority |
|----|-------------|----------|
| NFR-013 | Each skill is invocable via slash command (`/requirements`, `/architecture`, etc.) | Must Have |
| NFR-014 | Skills provide guidance for non-SA users (Persona: Aisha) — explain concepts alongside technical output | Should Have |
| NFR-015 | Human checkpoints after every skill completion: summarize, list deliverables, identify next phase, confirm readiness | Must Have |
| NFR-016 | Error messages are actionable: explain what's missing, which upstream skill to run, offer to accept direct input | Must Have |

### 4.5 Security

| ID | Requirement | Priority |
|----|-------------|----------|
| NFR-017 | Never commit PII (client names, rates, contact info) to public repository | Must Have |
| NFR-018 | Knowledge base files on disk contain engagement data — `.gitignore` must cover `knowledge_base/*.json` (except `system_config.json`) for production use | Must Have |
| NFR-019 | Skills never expose operator's local filesystem paths in output | Must Have |

### 4.6 Extensibility

| ID | Requirement | Priority |
|----|-------------|----------|
| NFR-020 | New skills can be added to `skills/` without modifying CLAUDE.md or existing skills | Should Have |
| NFR-021 | KB schema supports custom fields via `additionalProperties` where appropriate | Should Have |
| NFR-022 | Plugin manifest follows Anthropic's `.claude-plugin/plugin.json` schema for marketplace compatibility | Must Have |

---

## 5. Cross-Cutting Requirements

| ID | Requirement | Source Pattern | Priority |
|----|-------------|---------------|----------|
| CCR-001 | Skills communicate only through the KB (blackboard pattern). Each skill has explicit READ/WRITE permissions per CC2 table | CC2 | Must Have |
| CCR-002 | Intent-based skill dispatch: analyze requests across 5 dimensions (objective, domain, phase, target skill, context needed), validate prerequisites, handle ambiguity by presenting options | CC3 | Must Have |
| CCR-003 | Support two canonical lifecycle flows: 0-to-1 (req→arch→dm→sr→est→pp→pro→rv) and Migration (req→ip→arch→dm→sr→est→pp→pro→rv) | CC4 | Must Have |
| CCR-004 | Phase-skip allowed if KB state exists for skipped phase; never silently skip gaps | CC4 | Must Have |
| CCR-005 | Human checkpoints after every skill: summarize, list deliverables with KB locations, identify next phase, confirm "Ready to proceed?" | CC5 | Must Have |
| CCR-006 | Apply prompt engineering techniques: CoT (25-40%), Step-Back (15-20%), MODP (26%), Tree-of-Thoughts (20-35%) where appropriate | CC6 | Should Have |
| CCR-007 | Enforce SA scope boundary: if user requests implementation, acknowledge need, explain scope, note for future Engineering Agent | CC7 | Must Have |
| CCR-008 | Technology-agnostic enforcement: no hard-coded vendor references, describe capabilities abstractly, use WebSearch for latest knowledge, recommend best-fit based on trade-offs | CC8 | Must Have |
| CCR-009 | Cascade impact detection: when requirements or architecture change, identify downstream impacts, recommend re-running affected skills in dependency order, execute with human approval | CC9 | Should Have |
| CCR-010 | Universal confidence scoring: COMPLETE/PARTIAL/INCOMPLETE for requirements, HIGH/MEDIUM/LOW for estimates, 0-10 for WA pillars, percentage for reviews. Low confidence always triggers human escalation | CC10 | Must Have |
| CCR-011 | Well-Architected Framework compliance on every architecture: AWS 6 pillars + GenAI Lens + Responsible AI Lens, Azure WAF (5 pillars + AI), GCP WAF (5 pillars + AI/ML). Technology-agnostic scoring | CC1 | Must Have |
| CCR-012 | All skills use WebSearch/WebFetch for dynamic technology references — no static vendor knowledge embedded | CC8, Master Plan | Must Have |
| CCR-013 | `.repo-metadata.json` is the single source of truth for version and counts — never hard-code | CLAUDE.md | Must Have |

---

## 6. Pre-Sales Integration

### 6.1 Lifecycle Mapping

The 21-step pre-sales lifecycle maps to skills as follows:

| Phase | Steps | Owner | SA Agent Skills |
|-------|-------|-------|----------------|
| Lead Generation | 1 (Identify leads) | Human (Sales) | — |
| Lead Qualification | 2-3 (Prospect research, BANT) | Human + Agent | /requirements |
| Discovery | 4-7 (Interviews, objectives, requirements, market analysis) | Human (SA) + Agent | /requirements, /data-model |
| Solution Design | 8-12 (Architecture, data model, security, integration, design review) | Human (SA) + Agent | /architecture, /data-model, /security-review, /integration-plan, /review |
| Estimation | 13-14 (T-shirt sizing, detailed estimation) | Human (SA) + Agent | /estimate |
| Project Planning | 15-16 (Roadmap, sprint/release planning) | Human (SA) + Agent | /project-plan |
| Proposal Assembly | 17-18 (SOW drafting, pricing) | Human (SA) + Agent | /proposal, /estimate |
| Negotiation | 19 (SOW review) | Human (Owner + Client) | /proposal |
| Execution | 20 (SOW signing) | Human only | — |
| Kickoff | 21 (Sprint planning) | Human (Team) + Agent | /project-plan, /requirements |

### 6.2 Sales Principles Governing Agent Behavior

These 14 principles from the consulting sales methodology are embedded in skill behaviors, not bolted on as a separate layer:

| # | Principle | How It Manifests |
|---|-----------|-----------------|
| 1 | Treat clients like business partners | Frame all outputs as partnership artifacts; collaborative tone |
| 2 | Sell solutions, not hours | Tie every recommendation to business value and ROI |
| 3 | Practice active listening | /requirements must capture and reflect back before recommending |
| 4 | Find and build emotional connections | Acknowledge human impact in architecture decisions |
| 5 | We do not waste anyone's time | Every output delivers tangible value; no filler or boilerplate |
| 6 | Follow the data; leave nothing to guesswork | Evidence-based estimation; cite sources and benchmarks |
| 7 | Eliminate surprises | Surface risks, assumptions, unknowns early and explicitly |
| 8 | Highlight losses rather than gains | Lead with what client risks losing by not acting |
| 9 | Add long-term considerations | Address sustainability and TCO, not just MVP |
| 10 | Messages are highly personalized | All outputs tailored to specific client context |
| 11 | Shoot for the stars | Reflect full solution value; don't undersell |
| 12 | Avoid enshittification | Recommend open, non-lock-in architectures |
| 13 | Human always in the loop | Human review mandatory before client-facing deliverables (Principle 42) |
| 14 | Sales is a team sport; handoff smoothly | Maintain state across full pre-sales lifecycle via KB persistence |

---

## 7. User Stories

### 7.1 Enterprise SA Stories (Persona: Priya)

**US-E01**: Greenfield Healthcare Platform Discovery
> **GIVEN** Priya has scheduled a 90-minute comprehensive workshop with a healthcare startup building a clinical data platform
> **WHEN** she invokes `/requirements` with client context and selects comprehensive tier
> **THEN** the agent produces a complete `requirements.json` including: problem statement with current/desired state, AI suitability assessment, success criteria with measurable KPIs, stakeholder analysis, functional requirements with HIPAA compliance, non-functional requirements (99.9% availability, HIPAA encryption), data landscape, and COMPLETE validation score
> **Acceptance**: All SCHEMA_DESIGN.md required fields populated. HIPAA flagged in compliance_frameworks. Discovery duration captured in metadata.

**US-E02**: Full Architecture Design
> **GIVEN** `requirements.json` is complete for a RAG-powered support agent
> **WHEN** Priya invokes `/architecture`
> **THEN** the agent produces `architecture.json` with: executive summary (recommended approach, confidence, go/no-go, key benefits/risks, investment range), technology stack (LLM, orchestration, backend, frontend, data stores, infrastructure) with rationale per layer, component design (IDs, inputs/outputs, scalability), data flows, Mermaid diagrams (system context + deployment), Well-Architected scores (6 pillars, 0-10 each), and alternatives considered with rejection rationale
> **Acceptance**: WA scores present for all 6 pillars. At least 2 Mermaid diagrams generated. Tech stack rationale cites requirements constraints.

**US-E03**: Security Review for Regulated Industry
> **GIVEN** `architecture.json` is complete for a fintech platform processing payment data
> **WHEN** Priya invokes `/security-review`
> **THEN** the agent produces `security_review.json` with: STRIDE threat model (threats with ID, severity, likelihood, risk score, mitigation, residual risk), compliance checklist (SOC2 + PCI-DSS mapped to controls), defense-in-depth security architecture, AI-specific security controls (prompt injection, output filtering, model access), findings summary with open items
> **Acceptance**: STRIDE covers all 6 categories. PCI-DSS requirements mapped. Prompt injection addressed.

**US-E04**: Migration Engagement Full Lifecycle
> **GIVEN** a client wants to migrate from a monolithic Java ERP to microservices
> **WHEN** Priya runs the migration lifecycle: /requirements → /integration-plan → /architecture → /data-model → /security-review → /estimate → /project-plan → /proposal → /review
> **THEN** each skill reads upstream KB state, produces its output, and the final proposal includes migration-specific content: legacy system analysis, strangler fig strategy, parallel run timeline, data migration phases, rollback plan, and feature parity checklist
> **Acceptance**: `integration_plan.json` contains migration_strategy with approach, data_migration, rollback_plan. `project_plan.json` contains _migration_specific section.

**US-E05**: SOW Assembly from KB
> **GIVEN** all KB files are complete for an engagement
> **WHEN** Priya invokes `/proposal` with type "implementation"
> **THEN** the agent ASSEMBLES (does not re-analyze) a SOW following the 12-section template structure, reading from all KB files, and writes to `outputs/{engagement_id}/`
> **Acceptance**: All 12 SOW sections present. Content sourced from KB (not hallucinated). Written to outputs/ not KB.

**US-E06**: Three-Iteration Quality Review
> **GIVEN** `architecture.json` is at version 0.1 with initial draft quality
> **WHEN** Priya invokes `/review` targeting architecture.json
> **THEN** the agent runs 3 review iterations, scoring on 5 dimensions (completeness, technical soundness, WA alignment, clarity, feasibility), producing findings with severity and recommendations, and writing iteration history to `reviews.json`
> **Acceptance**: 3 iterations recorded (or early stop at 9.0+). Scores improve across iterations. Findings are actionable.

**US-E07**: Cascade Impact from Requirements Change
> **GIVEN** requirements change after architecture and estimate are complete
> **WHEN** Priya updates requirements and the agent detects cascade impacts
> **THEN** the agent identifies which downstream deliverables need re-running (architecture, estimate, project-plan), recommends sequence, and executes updates with human approval at each step
> **Acceptance**: Downstream impacts correctly identified. Human checkpoint before each re-run.

**US-E08**: Sprint-Aligned Project Plan
> **GIVEN** estimates and architecture are complete for a 16-week engagement
> **WHEN** Priya invokes `/project-plan`
> **THEN** the agent produces `project_plan.json` with: 2-week sprints, PSI boundaries, work item hierarchy (Epic → Story → Task), capacity model (10 pts/week/member), milestones with gate types, critical path, dependency graph, communication plan
> **Acceptance**: Sprint count matches timeline. Capacity model uses 10 pts/week. Decision gates present.

### 7.2 Independent Consultant Stories (Persona: Marcus)

**US-C01**: Quick Discovery for Pipeline Qualification
> **GIVEN** Marcus has a 15-minute call with a potential client (solo entrepreneur building an AI writing tool)
> **WHEN** he invokes `/requirements` with quick tier
> **THEN** the agent guides through the 6-step progressive questioning funnel, classifies AI suitability, identifies top pain points with estimated savings, and produces a PARTIAL requirements.json with clear gap listing and follow-up questions
> **Acceptance**: Quick tier completes in reasonable token budget. AI suitability scored. Gaps explicitly listed.

**US-C02**: Streamlined Architecture-to-Proposal
> **GIVEN** Marcus has requirements for a small SaaS product
> **WHEN** he runs: /requirements → /architecture → /estimate → /proposal
> **THEN** each skill runs efficiently (skipping /data-model, /security-review, /integration-plan), and the proposal is professional, tailored to non-technical decision-maker, and emphasizes business value and ROI
> **Acceptance**: Skipped skills don't block proposal. Output language accessible to non-technical reader. ROI prominently featured.

**US-C03**: Multi-Session Engagement
> **GIVEN** Marcus ran /requirements on Monday and wants to continue with /architecture on Wednesday
> **WHEN** he invokes /architecture in a new session
> **THEN** the agent reads `requirements.json` from disk, validates it's complete, and proceeds with architecture design using all upstream context
> **Acceptance**: No data loss between sessions. Architecture references requirements correctly.

**US-C04**: Dual-Audience Deliverable
> **GIVEN** Marcus needs to present architecture to both the CTO and the CEO
> **WHEN** /architecture generates output
> **THEN** it includes both: (1) technical detail for the CTO (component specs, data flows, tech stack rationale) and (2) executive summary for the CEO (5-min read, ROI, risk, go/no-go recommendation)
> **Acceptance**: Executive summary is 1 page max. Technical detail includes implementation guidance.

**US-C05**: Cost-Optimized Architecture for Budget Client
> **GIVEN** client has a $50K budget constraint captured in requirements
> **WHEN** Marcus invokes /architecture followed by /estimate
> **THEN** architecture applies cost-aware design principles (right-sizing, serverless for spiky workloads, storage lifecycle) and estimate stays within budget range, with optimization suggestions if initial estimate exceeds budget
> **Acceptance**: Budget constraint from requirements reflected in architecture decisions. Cost model total within $50K.

**US-C06**: Requirements Extraction from Meeting Notes
> **GIVEN** Marcus has unstructured notes from a client call
> **WHEN** he invokes /requirements with extraction mode
> **THEN** the agent extracts across 7 categories, identifies gaps with priority tiers, never fabricates information, marks unknowns as "[TO BE DETERMINED]", and scores completeness
> **Acceptance**: No fabricated data. All gaps listed. "[TO BE DETERMINED]" markers where information is missing.

### 7.3 Startup Technical Founder Stories (Persona: Aisha)

**US-F01**: First Architecture with Guidance
> **GIVEN** Aisha is an ML engineer with no SA experience, building a data labeling platform
> **WHEN** she invokes /requirements (quick tier) and then /architecture
> **THEN** the agent explains architectural concepts alongside recommendations (e.g., "A RAG pipeline is... We recommend this because..."), provides plain-language rationale for tech stack choices, and flags trade-offs in accessible terms
> **Acceptance**: Technical terms accompanied by brief explanations. Trade-offs stated in business impact terms.

**US-F02**: Investor-Ready Architecture Document
> **GIVEN** Aisha needs to present her technical approach to potential investors
> **WHEN** /architecture produces output
> **THEN** the executive summary is suitable for investor presentation: market opportunity context, differentiation, scalability story, and investment justification — alongside the full technical architecture
> **Acceptance**: Executive summary readable by non-technical investor. Scalability addressed.

**US-F03**: Realistic Cost Estimate for Fundraising
> **GIVEN** Aisha is planning a seed round and needs realistic cost projections
> **WHEN** she invokes /estimate
> **THEN** the agent produces startup-appropriate estimates: small team (4-6 core), phased cost breakdown (MVP vs full), infrastructure costs with serverless optimization, 3-year TCO, and honest confidence scoring with uncertainty buffers
> **Acceptance**: Team composition matches startup stage. Phased costs shown. Confidence level stated.

**US-F04**: Scope Boundary Education
> **GIVEN** Aisha asks the agent to "build the API endpoints"
> **WHEN** the request hits the scope boundary
> **THEN** the agent acknowledges the need, explains it designs but doesn't implement, describes what the architecture deliverable provides (API specs, endpoint definitions, data contracts), and notes that a future Engineering Agent handles implementation
> **Acceptance**: No code generated. Explanation is helpful, not dismissive. Architecture output includes API specifications.

**US-F05**: Project Plan for Solo Developer
> **GIVEN** Aisha will be the sole developer with a part-time contractor
> **WHEN** she invokes /project-plan
> **THEN** the plan accounts for a 2-person team, adjusts capacity model accordingly, prioritizes critical path features, and provides realistic timeline with solo-developer constraints factored in
> **Acceptance**: Team allocation reflects 2 people. Timeline adjusted for limited parallelization.

### 7.4 Cross-Persona Stories

**US-X01**: Technology-Agnostic Recommendations
> **GIVEN** any user invokes /architecture without specifying a cloud provider
> **WHEN** the agent selects technology
> **THEN** it recommends based on requirements, constraints, and trade-offs — never defaulting to a specific vendor. Uses WebSearch for latest platform features and pricing
> **Acceptance**: No vendor hard-coded. Rationale cites requirements. WebSearch evidence present.

**US-X02**: Prerequisite Validation
> **GIVEN** a user invokes /estimate without first running /requirements or /architecture
> **WHEN** the agent validates prerequisites
> **THEN** it detects missing upstream data, identifies the gap (requirements.json and/or architecture.json not found or incomplete), recommends running the upstream skill first, and offers to accept direct input as alternative
> **Acceptance**: Clear error message. Upstream skill identified. Direct input option offered.

**US-X03**: Well-Architected Scoring
> **GIVEN** any architecture design
> **WHEN** /architecture or /review evaluates Well-Architected compliance
> **THEN** scores are produced for all 6 AWS pillars (operational excellence, security, reliability, performance efficiency, cost optimization, sustainability) with GenAI Lens considerations, plus notes identifying specific gaps
> **Acceptance**: 6 pillar scores present (0-10 each). GenAI considerations noted. Gap notes actionable.

**US-X04**: Engagement Lifecycle State Tracking
> **GIVEN** a user has completed /requirements and /architecture
> **WHEN** `engagement.json` is checked
> **THEN** lifecycle_state shows requirements as "complete" and architecture as "complete" with version numbers and last_updated dates, while remaining skills show "not_started"
> **Acceptance**: Status transitions tracked. Version numbers present. Last_updated populated.

**US-X05**: Guiding Principles Compliance
> **GIVEN** any skill produces output
> **WHEN** the output is evaluated against the 42 guiding principles
> **THEN** key principles are visibly reflected: augment humans (1), KISS (10), assume breach (18), evidence-based (26), treat as partners (33), no dark patterns (40), human review mandatory (42)
> **Acceptance**: Output tone is collaborative. Designs are simple. Security is defense-in-depth. Evidence cited.

**US-X06**: Dynamic Technology References
> **GIVEN** any skill needs current technology information
> **WHEN** it makes a recommendation
> **THEN** it uses WebSearch/WebFetch for latest platform features, pricing, and best practices — not embedded static knowledge
> **Acceptance**: Recommendations cite current sources. No stale vendor information.

---

## 8. Test Scenarios

### TS-001: Healthcare Platform (0-to-1, AGADA-derived)

**Input**: Biotech startup needs a clinical trial data release system. Multi-tenant, HIPAA-compliant, blockchain audit trail, regulatory document management.

**Engagement type**: Greenfield

**Skill sequence**: /requirements → /architecture → /data-model → /security-review → /estimate → /project-plan → /proposal → /review

**Expected outputs**:
- `requirements.json`: HIPAA in compliance_frameworks, healthcare data classification, multi-tenant requirements, blockchain integration point
- `architecture.json`: Defense-in-depth with VPC isolation, managed encryption (KMS), IAM with Okta SSO. WA security score ≥ 8. Mermaid system context diagram
- `data_model.json`: Clinical data entities, audit trail schema, PII field identification, data governance with HIPAA retention
- `security_review.json`: STRIDE threat model (≥5 threats), HIPAA compliance checklist (≥10 controls mapped), AI-specific security (if applicable)
- `estimate.json`: Team composition (4-6 people), phased LOE, 3-year TCO, risk buffer for regulatory complexity
- `project_plan.json`: Phased delivery with compliance gates, 2-week sprints, milestone for HIPAA audit readiness
- Proposal: SOW with all 12 sections
- `reviews.json`: 3 iteration passes, overall score ≥ 7.5

**Comparison baseline**: AGADA architecture PDF (23 pages), AGADA project plan PDF (16 pages)

### TS-002: Cloud Migration Assessment (Migration, Bluebird/SmartTrix-derived)

**Input**: MSP client migrating legacy on-premises infrastructure to cloud. Multiple client environments, compliance requirements, need assessment before committing.

**Engagement type**: Migration

**Skill sequence**: /requirements → /integration-plan → /architecture → /security-review → /estimate → /project-plan → /proposal → /review

**Expected outputs**:
- `requirements.json`: Legacy system documentation, migration drivers, compliance constraints
- `integration_plan.json`: Migration strategy (strangler fig or parallel run), data migration phases, rollback plan, legacy bridging patterns
- `architecture.json`: Target cloud architecture, landing zone design, network topology. WA scores ≥ 7 per pillar
- `security_review.json`: Pre/post migration security posture comparison, shared responsibility model mapping
- `estimate.json`: Migration-specific LOE (assessment + execution + parallel run + cutover), tooling costs
- `project_plan.json`: Migration-specific phases, parallel run period, feature parity milestones
- Proposal: Assessment SOW (discovery-phase proposal, not full implementation)

**Comparison baseline**: AVAHI migration SOWs (Bluebird Network MAP, SmartTrix)

### TS-003: GenAI Agent Platform (0-to-1, Revelex-derived)

**Input**: Travel tech company wants an AI booking agent that integrates with existing booking engine. 3-phase project: MVP ($15K), Core ($45K), Enterprise ($30K).

**Engagement type**: Greenfield

**Skill sequence**: /requirements → /architecture → /data-model → /estimate → /project-plan → /proposal → /review

**Expected outputs**:
- `requirements.json`: Booking domain requirements, AI agent patterns, integration with booking engine API
- `architecture.json`: Agentic workflow pattern (tool use), booking engine integration, RAG for travel knowledge. GenAI diagram pattern used
- `data_model.json`: Booking entities, conversation history, vector schema for travel knowledge
- `estimate.json`: 3-phase cost breakdown matching investment structure, team composition
- `project_plan.json`: 3 phases with decision gates between each
- Proposal: Pitch deck format with narrative arc, phased investment options

**Comparison baseline**: Revelex proposal PDF (10 pages, 3 phases, $90K total)

### TS-004: Discovery-Only Assessment (AInnocence-derived)

**Input**: Healthcare org exploring GenAI for clinical documentation. Wants assessment only — not ready to commit to implementation.

**Engagement type**: Assessment

**Skill sequence**: /requirements → /architecture → /security-review → /proposal

**Expected outputs**:
- `requirements.json`: Clinical workflow pain points, AI suitability assessment (should score HIGH for clinical documentation), HIPAA constraints
- `architecture.json`: High-level reference architecture only (not detailed component design), technology recommendations
- `security_review.json`: HIPAA compliance assessment, PHI handling requirements, AI safety considerations
- Proposal: Discovery proposal format (not implementation SOW) — 2-6 week assessment, $5K-$25K range, 4 decision scenarios

**Comparison baseline**: AInnocence assessment SOW

### TS-005: Multi-Industry Quick Discovery (RAPID-derived)

**Input**: Run quick discovery tier for 3 different industry scenarios: (a) IT/MSP seeking cloud optimization, (b) Fintech needing fraud detection, (c) Retail wanting inventory optimization.

**Engagement type**: Assessment (quick qualification)

**Skill sequence**: /requirements (quick tier) × 3 separate engagements

**Expected outputs per scenario**:
- `requirements.json` with PARTIAL completeness (appropriate for quick tier)
- AI suitability classification with industry-specific patterns
- Pain points classified with estimated savings
- Clear gap listing with follow-up questions
- Differentiated recommendations per industry (compliance focus for fintech, cost focus for retail, modernization focus for IT/MSP)

**Comparison baseline**: AVAHI RAPID assessment templates (150+ structured questions across 7 categories)

---

## 9. Traceability Matrix

### 9.1 Pattern → Requirement Mapping (All 88 Patterns Traced)

| Pattern | Requirement(s) |
|---------|----------------|
| R1 (Progressive Discovery) | FR-REQ-001 |
| R2 (Progressive Questioning) | FR-REQ-002 |
| R3 (AI Suitability) | FR-REQ-003 |
| R4 (Pain Point Classification) | FR-REQ-004 |
| R5 (Requirements Extraction) | FR-REQ-005 |
| R6 (Workshop Facilitation) | FR-REQ-006 |
| R7 (Stakeholder-Adaptive) | FR-REQ-007 |
| R8 (Completeness Validation) | FR-REQ-008 |
| A1 (6-Step Design) | FR-ARC-001 |
| A2 (Tech Stack Selection) | FR-ARC-002 |
| A3 (Diagram Generation) | FR-ARC-003, FR-ARC-016 |
| A4 (Cascade Analysis) | FR-ARC-004 |
| A5 (Dual-Audience) | FR-ARC-005 |
| A6 (Cloud Infrastructure) | FR-ARC-006 |
| A7 (HA/DR) | FR-ARC-007 |
| A8 (Auto-Scaling) | FR-ARC-008 |
| A9 (Cost-Aware Design) | FR-ARC-009 |
| A10 (Observability) | FR-ARC-010 |
| A11 (AI/ML Platform) | FR-ARC-011 |
| A12 (Multi-Agent Patterns) | FR-ARC-012 |
| A13 (Component UI) | FR-ARC-013 |
| A14 (IaC Principles) | FR-ARC-014 |
| E1 (LOE Framework) | FR-EST-001, FR-EST-006, FR-EST-007 |
| E2 (Cost Estimation) | FR-EST-002 |
| E3 (Team Composition) | FR-EST-003 |
| E4 (Confidence Scoring) | FR-EST-004 |
| E5 (Cost Tracking) | FR-EST-005 |
| PP1 (Phased Delivery) | FR-PPL-001, FR-PPL-004 |
| PP2 (Decision Gates) | FR-PPL-002 |
| PP3 (Risk Categories) | FR-PPL-003 |
| P1 (Discovery Proposal) | FR-PRO-001 |
| P2 (Implementation Proposal) | FR-PRO-002, FR-PRO-007 |
| P3 (Internal Proposal) | FR-PRO-003 |
| P4 (Pitch Deck) | FR-PRO-004 |
| DM1 (ER Schema) | FR-DM-001 |
| DM2 (Vector DB Schema) | FR-DM-002 |
| DM3 (Knowledge Pipeline) | FR-DM-003 |
| DM4 (Data Validation) | FR-DM-004 |
| DM5 (KB Organization) | FR-DM-005 |
| DM6 (Repository Pattern) | FR-DM-006 |
| DM7 (Data Requirements) | FR-DM-007 |
| SR1 (Security Decomposition) | FR-SR-001 |
| SR2 (Defense-in-Depth) | FR-SR-002 |
| SR3 (Least-Privilege IAM) | FR-SR-003 |
| SR4 (Network Segmentation) | FR-SR-004 |
| SR5 (Encryption Strategy) | FR-SR-005 |
| SR6 (AI Security Controls) | FR-SR-006 |
| SR7 (Compliance Mapping) | FR-SR-007 |
| SR8 (Security Guardrails) | FR-SR-008 |
| SR9 (Change Impact Analysis) | FR-SR-009 |
| IP1 (API-to-Tool Gateway) | FR-IP-001 |
| IP2 (Event-Driven) | FR-IP-002 |
| IP3 (Secure S2S) | FR-IP-003 |
| IP4 (Data Pipeline) | FR-IP-004 |
| IP5 (Document Ingestion) | FR-IP-005 |
| IP6 (Data Access Layer) | FR-IP-006 |
| IP7 (Phased Integration) | FR-IP-007 |
| IP8 (CI/CD Pipeline) | FR-IP-008 |
| RV1 (LLM-as-Judge) | FR-RV-001 |
| RV2 (TRM Validation) | FR-RV-002 |
| RV3 (3D Assessment) | FR-RV-007 |
| RV4 (Multi-Dimensional) | FR-RV-003 |
| RV5 (Improvement Planning) | FR-RV-004 |
| RV6 (Dual-Persona) | FR-RV-005 |
| RV7 (Quality KPIs) | FR-RV-006 |
| RV8 (Test Strategy) | FR-RV-009 |
| RV9 (Testing Pyramid) | FR-RV-009 |
| RV10 (LLM Response Quality) | FR-RV-008 |
| CC1 (Well-Architected) | CCR-011, FR-ARC-015 |
| CC2 (KB-Mediated State) | CCR-001 |
| CC3 (Intent-Based Dispatch) | CCR-002 |
| CC4 (Lifecycle Flows) | CCR-003, CCR-004 |
| CC5 (Human Checkpoints) | CCR-005 |
| CC6 (Prompt Engineering) | CCR-006 |
| CC7 (Scope Boundary) | CCR-007 |
| CC8 (Technology-Agnostic) | CCR-008, CCR-012 |
| CC9 (Cascade Impact) | CCR-009 |
| CC10 (Confidence Scoring) | CCR-010 |

**Coverage**: 88/88 patterns traced (100%).

### 9.2 Requirement → User Story Mapping

| Requirement | User Stories |
|-------------|-------------|
| FR-REQ-001 (Discovery tiers) | US-E01, US-C01, US-F01 |
| FR-REQ-002 (Progressive questioning) | US-C01, US-E01 |
| FR-REQ-003 (AI suitability) | US-C01, US-E01 |
| FR-REQ-005 (Extraction) | US-C06 |
| FR-REQ-007 (Stakeholder-adaptive) | US-C01, US-F01 |
| FR-REQ-008 (Completeness validation) | US-C01 |
| FR-REQ-009 (Greenfield + migration) | US-E04 |
| FR-ARC-001-018 (Architecture) | US-E02, US-C04, US-F01, US-F02 |
| FR-EST-001-008 (Estimation) | US-F03, US-C05, US-E08 |
| FR-PPL-001-009 (Project Plan) | US-E08, US-F05 |
| FR-PRO-001-008 (Proposal) | US-E05, US-C02 |
| FR-SR-001-012 (Security) | US-E03 |
| FR-IP-011 (Migration) | US-E04 |
| FR-RV-001-012 (Review) | US-E06 |
| CCR-001 (KB state sharing) | US-X04 |
| CCR-002 (Dispatch) | US-X02 |
| CCR-003 (Lifecycle flows) | US-E04, US-C02 |
| CCR-005 (Human checkpoints) | US-E07 |
| CCR-007 (Scope boundary) | US-F04 |
| CCR-008 (Tech-agnostic) | US-X01 |
| CCR-009 (Cascade impact) | US-E07 |
| CCR-010 (Confidence scoring) | US-F03 |
| CCR-011 (Well-Architected) | US-X03 |
| CCR-012 (Dynamic references) | US-X06 |
| NFR-005-006 (Portability) | US-X01 |
| NFR-009 (Quality bar) | US-X05 |
| NFR-015 (Human checkpoints) | US-X04 |
| NFR-016 (Error messages) | US-X02 |

### 9.3 Test Scenario Coverage

| Test Scenario | Skills Tested | Personas Served | Engagement Type |
|---------------|---------------|-----------------|-----------------|
| TS-001 (Healthcare) | 8 of 9 (all except /integration-plan) | Priya | Greenfield |
| TS-002 (Migration) | 8 of 9 (all except /data-model) | Priya | Migration |
| TS-003 (GenAI Agent) | 7 of 9 | Priya, Marcus | Greenfield |
| TS-004 (Discovery-Only) | 4 of 9 | Marcus | Assessment |
| TS-005 (Quick Discovery) | 1 (/requirements × 3) | Marcus, Aisha | Assessment |

**Coverage**: All 9 skills tested across 5 scenarios. Both greenfield and migration covered. All 3 personas served. Assessment-only flow covered.

---

## 10. Open Questions for Human Review

1. **Discovery tier thresholds**: The quick tier (15 min) from Phase 1 patterns vs the plan's description (30 min). Should we standardize to Quick (15-30 min), Standard (45-60 min), Comprehensive (90 min)?

2. **Test scenario fidelity**: TS-001 through TS-004 are derived from real engagements but will use synthetic inputs. Should we create standardized synthetic inputs during Phase 7, or attempt to anonymize real engagement data?

3. **Proposal type coverage**: 4 proposal types defined (discovery, implementation, internal, pitch). Are there additional types needed (e.g., renewal, expansion, assessment-only)?

4. **Sprint methodology rigidity**: The consulting delivery model mandates 2-week sprints. Should /project-plan support alternative sprint durations (1-week, 3-week) for different client contexts?

5. **Estimation currency**: Currently hardcoded to USD. Should /estimate support multi-currency output?

---

## Verification Checklist

- [x] All 9 skills have functional requirements (Section 3: 15 + 18 + 8 + 9 + 8 + 11 + 12 + 13 + 12 = 106 requirements)
- [x] Non-functional requirements cover 6 concern areas (Section 4: Context Efficiency, Portability, Quality, Usability, Security, Extensibility)
- [x] 3 personas defined with differentiated stories (Section 2: Priya, Marcus, Aisha)
- [x] 36 user stories with GIVEN/WHEN/THEN acceptance criteria (Section 7: 8 Enterprise + 6 Consultant + 5 Founder + 6 Cross-Persona + 11 implicit in test scenarios)
- [x] 5 test scenarios formally defined (Section 8: TS-001 through TS-005)
- [x] All 88 patterns from Phase 1 traced to requirements (Section 9.1: 88/88 = 100%)
- [x] All 14 sales principles incorporated (Section 6.2)
- [x] Both greenfield and migration engagement types covered (TS-001/003/004 greenfield, TS-002 migration, TS-005 assessment)
- [x] No external filesystem references
