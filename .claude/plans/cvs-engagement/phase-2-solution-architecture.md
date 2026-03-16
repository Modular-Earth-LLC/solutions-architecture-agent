# Phase 2: Solution Architecture and Technical Design

Use ultrathink for this phase. Engage extended reasoning before every major output.

Perform deep web research using WebSearch before making any technical claims. Cite all sources with URLs. Cross-validate across multiple sources. This is the most technically dense phase — it produces the core architecture that all subsequent phases build on.

## Objective

Design the complete solution architecture for CVS Health's Legacy System Transformation. This phase produces:
1. `knowledge_base/integration_plan.json` via `/integration-plan` — legacy integration strategy
2. `knowledge_base/architecture.json` via `/architecture` — system architecture with 3 solution options
3. `knowledge_base/data_model.json` via `/data-model` — data model for the modernized system
4. Mermaid architecture diagrams
5. Quality reviews of all artifacts

This phase addresses two key considerations: **Legacy System Integration** and **Technology Stack**. It also incorporates the **GenAI/ML pipeline layer** (dual competency thread) showing how the modernized system supports the data science team's workflows.

## Input Dependencies

- `knowledge_base/requirements.json` — Phase 0 requirements
- `outputs/cvs-legacy-transformation/research-findings.md` — Phase 0 research (all clusters)
- `outputs/cvs-legacy-transformation/honesty-map.md` — Paul's experience mapping
- `outputs/cvs-legacy-transformation/ux-design-document.md` — Phase 1 UX design (personas, patterns, accessibility)

## Prior Phase Context

Read ALL completed phase context summaries before executing:
- `.claude/plans/cvs-engagement/context/phase-*-context.md`

Adapt this plan based on findings, corrections, and insights from prior phases. Pay special attention to:
- Phase 0's IBMi modernization research (Cluster 1) — what tools and approaches are viable?
- Phase 0's GCP services research (Cluster 3) — which GCP services are best fit?
- Phase 0's CVS technology context (Cluster 2) — what is CVS already using?
- Phase 1's UX patterns — what does the architecture need to support?
- Phase 1's performance requirements per persona (e.g., claims processor < 200ms)
- Any assumption corrections from Phase 0 or 1

## Context Files

**Paul's Architecture Experience** (base: `C:\dev\paulprae-com`):
- `docs/technical-design-document.md` — Paul's technical design patterns
- `docs/ai-architecture.md` — Paul's AI architecture experience
- `docs/devops.md` — Paul's DevOps and CI/CD patterns
- `data/generated/career-data.json` — for architecture-relevant experience

**Paloist Architecture** (base: `C:\dev\paloist-core`):
- `docs/solution-architecture.md` — example solution architecture Paul has produced

**Agent Config**:
- `.claude/rules/guiding-principles.md` — principles 9-17 (Architecture & Design), 28-32 (Operations & Infrastructure)
- `knowledge_base/system_config.json` — Well-Architected Framework definitions (READ-ONLY)
- `.claude/plans/references/sa-best-practices-research-2026.md` — SA frameworks research

**Assignment**:
- `.claude/plans/references/solution-architect-case-study-and-interview.md` — key considerations 1 (Legacy Integration) and 4 (Technology Stack)
- `.claude/plans/references/CVS - GenAI Data Scientist Job Description .pdf` — for AI/ML pipeline layer

## Research Directives

### Cluster 1: IBMi Integration Middleware (Deep Dive)
- `IBMi data queue API integration middleware 2025 2026`
- `IBM Rational Host Access Transformation Services HATS alternatives`
- `Profound Logic Profound.js Node.js IBMi integration`
- `AS/400 DB2 for i SQL access remote JDBC ODBC`
- `IBMi ILE RPG free format REST API web services`

### Cluster 2: GCP Architecture for Legacy Modernization
- `GCP Apigee X API gateway legacy mainframe integration`
- `Google Cloud Run vs GKE vs App Engine enterprise application 2026`
- `GCP Cloud Interconnect hybrid connectivity on-premise IBMi`
- `Firebase vs GCP Identity Platform enterprise authentication`
- `GCP Pub/Sub event-driven architecture legacy system integration`

### Cluster 3: Strangler Fig Pattern Implementation
- `strangler fig pattern legacy modernization implementation guide`
- `anti-corruption layer domain driven design legacy integration`
- `parallel run strategy legacy modernization risk mitigation`
- `feature toggle legacy to modern UI gradual migration`

### Cluster 4: Frontend Architecture for Enterprise Migration
- `React vs Angular enterprise legacy modernization 2025 2026`
- `micro frontend architecture module federation legacy migration`
- `web component design system enterprise healthcare`
- `server-side rendering SSR enterprise application performance`

### Cluster 5: GenAI/ML Pipeline Architecture
- `GCP Vertex AI pipeline architecture production healthcare`
- `BigQuery ML healthcare data analytics pipeline`
- `LLM inference pipeline GCP Cloud Run serverless`
- `clinical NLP pipeline architecture unstructured to structured healthcare`

### Cluster 6: Data Layer Architecture
- `CQRS event sourcing legacy modernization pattern`
- `API gateway BFF pattern legacy system integration`
- `data mesh domain-oriented data architecture enterprise`
- `change data capture CDC legacy database synchronization`

## Execution Steps

### Step 1: Read All Context and Input Files
Read Phase 0 and Phase 1 outputs, Paul's architecture docs, and the assignment. Focus on:
- Requirements that constrain architecture choices
- UX patterns that require specific technical support
- Paul's demonstrated architecture patterns (for authentic voice)
- GCP service capabilities vs. requirements

### Step 2: Execute Web Research
Run all 6 research clusters. Focus on:
- Viable IBMi integration approaches with current tooling
- GCP services that fit the modernization pattern
- Frontend frameworks that support the dual-mode UX from Phase 1
- GenAI pipeline patterns that integrate with the modernized system

### Step 3: Run `/integration-plan`
Invoke the `/integration-plan` skill with context:
- Legacy system: IBMi (AS/400) green screen applications
- Integration pattern: Strangler Fig with anti-corruption layer
- Target platform: GCP-based modern architecture
- Key constraints from requirements.json
- Data synchronization strategy (CDC, event-driven)
- API contract design between legacy and modern layers

The integration plan should cover:
- Legacy system access patterns (DB2 for i, data queues, program calls)
- API gateway layer (Apigee X)
- Anti-corruption layer design
- Data synchronization strategy
- Migration phases (parallel run → gradual cutover)
- Rollback strategy

### Step 4: Run `/architecture`
Invoke the `/architecture` skill with context:
- All requirements from requirements.json
- Integration plan from Step 3
- UX design requirements from Phase 1
- GenAI DS JD requirements (AI/ML pipeline layer)

**Three solution options** (as required by the case study — "explore and present multiple options"):

**Option A: Screen Transformation (Tactical)**
- IBMi screen scraping / HATS-like approach
- Minimal backend changes, new frontend overlay
- Fastest to deploy, lowest risk, limited modernization depth
- GCP: Cloud Run for frontend, Apigee for API management

**Option B: API-First Strangler Fig (Recommended)**
- Extract IBMi business logic into REST/gRPC APIs
- Modern React/Angular frontend consuming APIs
- Gradual migration with anti-corruption layer
- GCP: Cloud Run/GKE, Apigee X, Pub/Sub, BigQuery, Vertex AI
- Includes GenAI/ML pipeline layer for clinical data processing

**Option C: Full Platform Rewrite (Strategic)**
- Complete rewrite on cloud-native platform
- Domain-driven microservices architecture
- Maximum modernization, highest risk, longest timeline
- GCP: Full managed services stack

For each option: architecture diagram (Mermaid), pros/cons, risk assessment, timeline estimate, Well-Architected scoring.

The architecture MUST include a dedicated **AI/ML Pipeline Layer** showing:
- How unstructured clinical notes flow into the system
- LLM processing pipeline (Vertex AI)
- Structured output generation (referral processing)
- Evaluation and guardrails layer
- Integration with Salesforce and care platforms
- This demonstrates Paul's capability to lead the GenAI DS team

### Step 5: Run `/data-model`
Invoke the `/data-model` skill with context:
- Architecture from Step 4 (recommended option)
- Integration plan from Step 3
- Requirements for data access patterns
- GenAI pipeline data requirements

The data model should cover:
- Core PBM entities (members, claims, pharmacies, formularies, prior authorizations)
- User and access management entities
- Audit and compliance tracking
- GenAI pipeline data (clinical notes, referral outputs, evaluation results)
- Data synchronization entities (CDC tracking)

### Step 6: Validate KB and Update Engagement
After producing all KB files:
1. Run `python tests/validate_knowledge_base.py` to validate all three KB files against schemas
2. Update `knowledge_base/engagement.json`: set `lifecycle_state` for `integration_plan`, `architecture`, and `data_model` to `complete`

### Step 7: Create Mermaid Diagrams
Create these Mermaid diagrams:
1. **System Context Diagram** — high-level showing all system boundaries
2. **Container Diagram** — for the recommended option (Option B)
3. **Integration Flow Diagram** — showing legacy-to-modern data flow
4. **GenAI Pipeline Diagram** — showing the AI/ML processing pipeline
5. **Deployment Diagram** — GCP infrastructure layout

### Step 8: Run `/review` on All Artifacts
Review each artifact:
- `knowledge_base/integration_plan.json`
- `knowledge_base/architecture.json`
- `knowledge_base/data_model.json`

Target >= 7.5/10 across all dimensions. Iterate if below threshold.

## Honesty Rules

1. **Architecture patterns** → map to Paul's actual architecture experience from paulprae-com docs and paloist-core docs. "In my experience designing [system], I applied [pattern]..."
2. **GCP specifics** → researched for this engagement. "For CVS's GCP-primary environment, I recommend [service] based on [research finding]..."
3. **IBMi integration** → entirely researched. "Based on current IBMi modernization tooling from [vendor/source]..."
4. **AI/ML pipeline** → map to Paul's actual AI/ML experience, augmented with GCP-specific research
5. **Three options** → be genuinely balanced. Don't strawman options A or C to make B look good.
6. **Well-Architected scores** → justify every score with specific evidence
7. **Performance claims** → cite sources or flag as estimates with assumptions

## Quality Gate

- Run `/review` on `integration_plan.json`, `architecture.json`, `data_model.json`
- Minimum score: >= 7.5/10 across all 5 dimensions (completeness, technical soundness, well-architected, clarity, feasibility) for each artifact
- Note: `/architecture` uses `parallel-wa-reviewer` sub-agents for Well-Architected pillar scoring
- All three solution options must have genuine pros and cons
- Mermaid diagrams must render correctly (validate syntax)
- GenAI/ML pipeline layer must be present in recommended architecture
- GCP services must be accurately described (verify against current GCP docs)
- Well-Architected scoring must be justified per pillar

## Exit Criteria

Before proceeding to Phase 3:
- [ ] `knowledge_base/integration_plan.json` produced and reviewed
- [ ] `knowledge_base/architecture.json` produced with 3 options and reviewed
- [ ] `knowledge_base/data_model.json` produced and reviewed
- [ ] All `/review` scores >= 7.5/10
- [ ] 5 Mermaid diagrams created and syntax-validated
- [ ] GenAI/ML pipeline layer documented in architecture
- [ ] Three solution options with balanced pros/cons
- [ ] GCP services accurately described with current capabilities
- [ ] All assumptions numbered (A-2-NNN series)
- [ ] `engagement.json` lifecycle_state updated for integration_plan, architecture, data_model
- [ ] KB validation passes: `python tests/validate_knowledge_base.py`

## Context Handoff

After execution completes, save context for future phases:

1. **Write context summary** to `.claude/plans/cvs-engagement/context/phase-2-context.md` using the Context Summary Template (see master-plan.md)

2. **Update ALL remaining phase plan files** with:
   - Architecture artifacts and file paths for Phase 3 (threat modeling needs architecture.json)
   - Technology stack decisions for Phase 4 (estimation needs to know what to estimate)
   - GCP service selections for Phase 3 (IAM strategy depends on chosen GCP services)
   - GenAI pipeline details for Phase 5 (methodology section needs to describe the pipeline)
   - Diagram references for Phase 6 (assembly needs to embed diagrams)
   - Data model details for Phase 3 (data classification for security review)
   - Integration patterns for Phase 4 (migration timeline depends on integration approach)
   - Any new assumptions or corrected assumptions

3. **Update master-plan.md** if any structural changes to the engagement

4. **Commit** all context and plan updates to git with message: `docs(plans): complete Phase 2 solution architecture, update future plans`

## Human Checkpoint

Paul: review the following before proceeding to Phase 3:
- Integration plan: `knowledge_base/integration_plan.json`
  - Is the strangler fig approach appropriate?
  - Are the IBMi integration patterns technically sound?
- Architecture: `knowledge_base/architecture.json`
  - Are the 3 solution options genuinely differentiated?
  - Does Option B (recommended) feel right?
  - Is the GCP service selection appropriate?
  - Does the GenAI/ML pipeline layer accurately represent the team's work?
- Data model: `knowledge_base/data_model.json`
  - Are the PBM domain entities reasonable?
- Mermaid diagrams: do they render correctly and tell the right story?
- Is the architecture authentically Paul's? (not generic template)
- Updated future phase plans (review changes from this phase's learnings)
- Context summary accuracy
