# Phase 4: Estimation, Team Composition, and Project Plan

Use ultrathink for this phase. Engage extended reasoning before every major output.

Perform deep web research using WebSearch before making any cost or pricing claims. Cite all sources with URLs. All cost estimates MUST reference authoritative pricing sources — never use LLM-generated estimates without cited backing.

## Objective

Produce comprehensive estimation, team composition, and phased project plan for CVS Health's Legacy System Transformation. This phase produces:
1. `knowledge_base/estimate.json` via `/estimate` — LOE, cost modeling, team composition, confidence scoring
2. `knowledge_base/project_plan.json` via `/project-plan` — phased roadmap, sprints, milestones, dependencies
3. Change management integration within the project plan (key consideration 5)
4. Quality reviews of all artifacts

This phase addresses the **Change Management** key consideration by embedding it within the project plan rather than treating it as a separate workstream. It also includes cloud infrastructure cost modeling with verified GCP pricing.

**Interview depth target**: Change Management may be the focus of one 45-minute interview (likely paired with HCD). Cost estimates with cited authoritative sources gain importance for deep questioning — interviewers may probe specific cost assumptions and confidence levels.

## Input Dependencies

- `knowledge_base/architecture.json` — Phase 2 architecture (what to estimate)
- `knowledge_base/integration_plan.json` — Phase 2 integration plan (migration complexity)
- `knowledge_base/data_model.json` — Phase 2 data model (data migration scope)
- `knowledge_base/security_review.json` — Phase 3 security review (security infrastructure costs)
- `knowledge_base/requirements.json` — Phase 0 requirements (scope definition)
- `outputs/cvs-legacy-transformation/research-findings.md` — Phase 0 research (Cluster 6: Change Management)
- `outputs/cvs-legacy-transformation/ux-design-document.md` — Phase 1 UX design (training needs)
- `outputs/cvs-legacy-transformation/iam-strategy.md` — Phase 3 IAM strategy (migration phases)
- `outputs/cvs-legacy-transformation/honesty-map.md` — Paul's experience mapping

## Prior Phase Context

Read ALL completed phase context summaries before executing:
- `.claude/plans/cvs-engagement/context/phase-*-context.md`

Adapt this plan based on findings, corrections, and insights from prior phases. Pay special attention to:
- Phase 2's architecture choices — what services need cost modeling?
- Phase 2's integration approach — how complex is the migration?
- Phase 3's security infrastructure — what security tooling needs budgeting?
- Phase 3's IAM migration phases — how does this affect the timeline?
- Phase 1's training needs — what does change management require?
- Phase 0's change management research (Cluster 6)
- Any assumption corrections from prior phases

**Phase 2 Insights for Estimation & Planning**:
- Three architecture options need cost comparison: GCP (Apigee Enterprise ~$100K/yr, Partner Interconnect ~$600-1,500/mo, Cloud Run, Vertex AI), AWS (API Gateway pay-per-request, Direct Connect, HealthLake $0.27/hr, Bedrock), Modern Cloud (Vercel Pro+HIPAA $370/mo, Supabase Team+HIPAA ~$950/mo)
- CDC tooling: Precisely Connect or Striim licensing needed on all platforms — neither DMS nor Datastream support Db2 for i
- Strangler fig migration phases: Phase 1 (member eligibility, 8 weeks), Phase 2 (claims, 16 weeks), Phase 3 (formulary+PA+GenAI, 12 weeks), Phase 4 (remaining+Health100, 12 weeks) = ~48 weeks total
- Team needs: RPG/CL developers (scarce — avg age 50+) for IWS API layer, React+TypeScript for frontend, Python for GenAI pipeline, platform engineers for multi-cloud
- GenAI pipeline costs: Vertex AI inference (Gemini for complex, MedGemma for routine — tiered inference reduces per-call cost), Vertex AI Pipelines for batch processing
- Cloud Run: ~$8/mo per min-instance for cold-start mitigation, auto-scaling 0-100
- BigQuery: serverless (start on-demand, evaluate flat-rate if >$10K/mo)
- Partner Interconnect: 1-2 Gbps via carrier CVS already uses (~$600-1,500/mo including HA VPN overlay)
- Estimated row counts from review finding RF-017: members ~50M, claims ~500M/yr, pharmacies ~70K, drug_products ~200K, formulary_entries ~1M
- Dual Run validation costs: doubles compute during validation periods (temporary)
- HIPAA audit log storage: 6-year retention in Cloud Logging + BigQuery — significant storage cost at CVS scale

**Phase 3 Insights for Estimation & Planning**:
- Security infrastructure costs per option: GCP (Cloud Armor Enterprise ~$3K/mo, VPC-SC included, Cloud DLP pay-per-scan ~$1-3/GB, Secret Manager $0.06/version/mo), AWS (Shield Advanced $3K/mo, WAF per-rule pricing), Modern Cloud (Cloudflare Enterprise, Supabase Team+HIPAA $599+$350/mo)
- IAM migration effort: 3 phases over 18 months — Phase 1 SSO Bridge (months 1-6), Phase 2 Identity Consolidation (months 7-12), Phase 3 Full Zero Trust (months 13-18). Requires IBM i-side developer time for journal bridge and IWS modifications.
- Compliance audit costs: SOC 2 Type II audit $10-25K, penetration testing $15-35K (Paloist reference), DEA EPCS third-party audit every 2 years per §1311.300
- IGA tool licensing: SailPoint/Saviynt/ConductorOne evaluation needed — budget $50-150K/yr for enterprise IGA
- 8 open security findings need implementation effort budgeted: IBM i journal bridge (high effort — RPG/CL dev needed), break-glass workflow (medium), EPCS CSP integration (medium), cross-cloud audit bridge (medium), IWS authority audit (medium), DLP custom info types (low), DR drill procedure (low), IGA tool selection (medium)
- SIEM procurement or integration: Chronicle, Splunk, or existing CVS SIEM — budget for integration if not existing
- FIDO2 hardware key deployment for ~100K users: $25-50/key for high-privilege roles initially, phased rollout

**Phase 1 Insights for Estimation & Planning**:
- Change management costs must include: F-key mapping laminated cards, training sandbox environment, champion network setup, monthly NPS surveys, dual-UI maintenance during transition
- 5 personas with mapped change resistance levels: Claims Processor (HIGH), Clinical Pharmacist (MODERATE), Benefits Analyst (LOW), IT Admin (LOW), New Hire (NONE)
- Member Eligibility Lookup recommended as first strangler fig migration target — lowest risk
- Claims Adjudication is highest risk migration — requires extensive performance validation
- Green screen escape hatch adds temporary dual-UI development cost — budget accordingly
- Onboarding time target: 42 days → 10 days (SC-001) — training program must be costed

## Context Files

**Paul's Estimation Experience** (base: `C:\dev\paulprae-com`):
- `data/generated/career-data.json` — for estimation and project management experience (include Mento coaching for change management)
- `data/sources/knowledge/career/projects.json` — project portfolio (for comparable estimation)

**Agent Config**:
- `.claude/rules/guiding-principles.md` — principles 15 (small reversible changes), 16 (anticipate failure), 17 (ship), 28-32 (Operations)
- `knowledge_base/system_config.json` — team and constraint configuration reference (READ-ONLY)
- `.claude/plans/references/sa-best-practices-research-2026.md` — estimation frameworks section

**Assignment**:
- `.claude/plans/references/solution-architect-case-study-and-interview.md` — key consideration 5 (Change Management)

## Research Directives

### Cluster 1: GCP Pricing (Current — Must Be Verified)
- `GCP Cloud Run pricing calculator 2026`
- `GCP Apigee X pricing enterprise tier 2026`
- `GCP Vertex AI pricing inference training 2026`
- `Google Cloud Identity Platform pricing enterprise 2026`
- `GCP BigQuery pricing storage query 2026`
- `GCP Pub/Sub Cloud Interconnect pricing 2026`

### Cluster 2: Enterprise Modernization Cost Benchmarks
- `IBMi AS/400 modernization project cost benchmarks enterprise`
- `legacy modernization total cost ownership TCO healthcare`
- `enterprise UI transformation project duration team size benchmarks`
- `pharmacy benefits management system modernization cost case study`

### Cluster 3: Change Management Frameworks
- `Prosci ADKAR model change management technology transformation`
- `Kotter 8-step change management enterprise IT`
- `change management ROI measurement enterprise technology`
- `green screen to web UI user adoption resistance strategies`
- `organizational change management healthcare pharmacy technology`

### Cluster 4: Team Composition for Enterprise Modernization
- `enterprise modernization team composition roles responsibilities`
- `IBMi modernization team skills required staffing`
- `GenAI data science team composition healthcare`
- `change management team staffing enterprise technology transformation`

## Execution Steps

### Step 1: Read All Context and Input Files
Read all prior phase outputs, Paul's career data, and the assignment. Focus on:
- Architecture components that need estimation
- Migration complexity from integration plan
- Security infrastructure from security review
- Paul's experience with estimation and project management
- Change management research from Phase 0

### Step 2: Execute Web Research
Run all 4 research clusters. Focus on:
- **Current GCP pricing** — must have source URLs for every price point
- **Comparable project benchmarks** — for three-point estimation validation
- **Change management frameworks** — for embedding in project plan
- **Team composition** — for realistic staffing model

### Step 3: Run `/estimate`
Invoke the `/estimate` skill with context:
- Architecture from architecture.json (recommended option — Option B)
- Integration plan complexity from integration_plan.json
- Security infrastructure from security_review.json
- All requirements from requirements.json

The estimate should cover:

**LOE Breakdown** (by workstream):
- Frontend development (modern UI, component library, accessibility)
- Backend/API development (IBMi integration layer, REST/gRPC APIs)
- IAM implementation (identity migration, SSO, zero trust)
- Data migration (DB2 for i to cloud, CDC setup)
- GenAI/ML pipeline (Vertex AI, NLP pipeline, evaluation framework)
- Security implementation (WAF, encryption, monitoring, compliance)
- Infrastructure/DevOps (GCP setup, CI/CD, observability)
- Change management (training, communication, support)
- Testing and QA (integration, performance, security, UAT)
- Project management and architecture oversight

**Cost Modeling** (with cited sources):
- Team costs (by role, blended rates — range, not point estimate)
- GCP infrastructure costs (monthly run rate — cite GCP pricing calculator)
- Third-party tooling costs (IBMi middleware, monitoring, etc.)
- Training and change management costs
- Contingency (15-20% based on confidence level)

**Confidence Scoring**:
- HIGH confidence items: well-understood scope, comparable projects
- MEDIUM confidence items: reasonable estimates with assumptions
- LOW confidence items: significant unknowns, need further discovery

**Three-Point Estimates**:
- Optimistic (P10) / Most Likely (P50) / Pessimistic (P90) for total engagement

### Step 4: Run `/project-plan`
Invoke the `/project-plan` skill with context:
- Estimate from Step 3
- Architecture from architecture.json
- Integration plan from integration_plan.json
- IAM migration phases from iam-strategy.md
- Change management framework research

The project plan should cover:

**Phased Roadmap** (aligned with strangler fig migration):

**Phase 1: Foundation (Months 1-3)**
- GCP infrastructure setup
- CI/CD pipeline establishment
- IAM foundation (SSO bridge, identity federation)
- Design system and component library
- IBMi integration middleware POC
- Change management: stakeholder analysis, communication plan launch
- **Decision Gate**: Go/no-go on IBMi integration approach

**Phase 2: Pilot (Months 4-6)**
- First workflow migration (lowest-risk, highest-visibility)
- Parallel run with green screen
- User testing with pilot group
- IAM: MFA rollout to pilot users
- GenAI pipeline: POC for clinical note processing
- Change management: pilot user training, feedback loops
- **Decision Gate**: Pilot success criteria met?

**Phase 3: Expansion (Months 7-12)**
- Additional workflow migrations
- Full IAM migration (identity consolidation)
- GenAI pipeline: production deployment
- Performance optimization
- Change management: broad training, champion network
- **Decision Gate**: Scale-out readiness

**Phase 4: Completion (Months 13-18)**
- Remaining workflow migrations
- Legacy decommission preparation
- Zero trust implementation completion
- Change management: adoption measurement, continuous improvement
- **Decision Gate**: Legacy sunset readiness

**Change Management Integration** (embedded in each phase, not separate):
- Prosci ADKAR model application across phases
- Communication cadence (awareness → desire → knowledge → ability → reinforcement)
- Training program structure (e-learning, hands-on labs, shadowing, mentoring)
- Champion network and feedback mechanisms
- Resistance management strategies
- Success metrics (adoption rates, help desk ticket trends, user satisfaction)
- Connection to Paul's Mento coaching experience

**Risk Register**:
- Technical risks (IBMi integration, performance, data migration)
- Organizational risks (user resistance, sponsor fatigue, competing priorities)
- Compliance risks (HIPAA during migration, dual-system audit trail)
- Resource risks (IBMi expertise shortage, team attrition)
- For each: probability, impact, mitigation, contingency, owner

**Dependency Graph** (Mermaid):
- Sprint-level dependencies
- Cross-workstream dependencies
- Critical path identification

### Step 5: Validate KB and Update Engagement
After producing KB files:
1. Run `python tests/validate_knowledge_base.py` to validate against schemas
2. Update `knowledge_base/engagement.json`: set `lifecycle_state.estimate.status` and `lifecycle_state.project_plan.status` to `complete`

### Step 6: Run `/review` on All Artifacts
Review:
- `knowledge_base/estimate.json`
- `knowledge_base/project_plan.json`

Target >= 7.5/10 across all dimensions. Iterate if below threshold.

## Honesty Rules

1. **Cost estimates** → MUST cite authoritative sources for every price point. NO LLM-generated cost numbers without backing. Use ranges, not point estimates.
2. **Timeline estimates** → frame as ranges based on comparable projects. Cite benchmarks where available. Never present as certainties.
3. **Change management experience** → Paul has Mento coaching experience and has managed organizational change. Reference specific experience from career-data.json.
4. **Team composition** → based on industry benchmarks and comparable projects. Flag assumptions about internal CVS staff vs. contractors.
5. **Confidence scoring** → be genuinely calibrated. If something is LOW confidence, say so and explain why.
6. **Three-point estimates** → the range between P10 and P90 should be realistic, not artificially narrow.
7. **GCP pricing** → changes frequently. Label all prices with "as of [research date]" and recommend validation.

## Quality Gate

- Run `/review` on `estimate.json` and `project_plan.json`
- Minimum score: >= 7.5/10 across all 5 dimensions (completeness, technical soundness, well-architected, clarity, feasibility) for each artifact
- Every cost figure must have a cited source
- Change management must be integrated into every project phase (not a standalone workstream)
- Risk register must include mitigation strategies, not just risk statements
- Phased roadmap must align with strangler fig migration from Phase 2
- Confidence scores must be genuinely calibrated (not all HIGH)
- Team composition must include GenAI/ML roles (dual competency thread)

## Exit Criteria

Before proceeding to Phase 5:
- [ ] `knowledge_base/estimate.json` produced and reviewed
- [ ] `knowledge_base/project_plan.json` produced and reviewed
- [ ] All `/review` scores >= 7.5/10
- [ ] Every cost figure has a cited source URL
- [ ] Change management integrated into all 4 project phases
- [ ] Risk register complete with mitigations
- [ ] Phased roadmap with decision gates
- [ ] Team composition includes GenAI/ML roles
- [ ] All assumptions numbered (A-4-NNN series)
- [ ] `engagement.json` lifecycle_state updated for estimate and project_plan
- [ ] KB validation passes: `python tests/validate_knowledge_base.py`

## Context Handoff

After execution completes, save context for future phases:

1. **Write context summary** to `.claude/plans/cvs-engagement/context/phase-4-context.md` using the Context Summary Template (see master-plan.md)

2. **Update ALL remaining phase plan files** with:
   - Total cost ranges and timeline for Phase 5 (methodology section needs engagement scope context)
   - Change management framework details for Phase 6 (assembly needs change management section)
   - Team composition for Phase 5 (methodology should reference the team structure)
   - Risk register highlights for Phase 6 (key risks go in executive summary)
   - Project plan phases for Phase 6 (roadmap section of the deliverable)
   - Decision gates for Phase 7 (interview prep needs to explain gate criteria)
   - Any corrected or new assumptions

3. **Update master-plan.md** if any structural changes to the engagement

4. **Commit** all context and plan updates to git with message: `docs(plans): complete Phase 4 estimation and planning, update future plans`

## Human Checkpoint

Paul: review the following before proceeding to Phase 5:
- Estimate: `knowledge_base/estimate.json`
  - Are the cost ranges reasonable?
  - Is the team composition realistic?
  - Are the confidence scores honest?
- Project plan: `knowledge_base/project_plan.json`
  - Does the phased roadmap make sense for this scale of transformation?
  - Is change management sufficiently integrated (not an afterthought)?
  - Are the decision gates at the right points?
- Risk register: are the top risks the ones Paul would prioritize?
- Does the change management approach reflect Paul's Mento coaching philosophy?
- Updated future phase plans (review changes from this phase's learnings)
- Context summary accuracy
