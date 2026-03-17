# Phase 0: Research and Requirements Foundation

Use ultrathink for this phase. Engage extended reasoning before every major output.

Perform deep web research using WebSearch before making any technical claims. Cite all sources with URLs. Cross-validate across multiple sources. This is the most research-intensive phase — it builds the factual foundation for all subsequent work.

## Objective

Build the research and requirements foundation for CVS Health's Legacy System Transformation. This phase produces:
1. A comprehensive research findings document covering 9 topic clusters
2. A `knowledge_base/requirements.json` via the `/requirements` skill (comprehensive tier)
3. A quality review of the requirements via `/review`

This phase is critical because Paul rates himself 1/5 on IBMi/AS/400 — every technical claim about IBMi must be web-researched and cited. The research findings document becomes the factual backbone for all subsequent phases.

## Input Dependencies

- `.claude/plans/references/solution-architect-case-study-and-interview.md` — the assignment (Use Case 1)
- `.claude/plans/references/CVS - GenAI Data Scientist Job Description .pdf` — GenAI DS JD (for dual competency thread)
- `.claude/plans/references/sa-best-practices-research-2026.md` — SA frameworks and Well-Architected research

## Prior Phase Context

This is the first phase — no prior context summaries exist yet. However, read the master plan to understand the full engagement arc:
- `.claude/plans/cvs-engagement/master-plan.md`

## Context Files

Read these files to understand Paul's experience and map it to requirements:

**Paul's Career Data** (base: `C:\dev\paulprae-com`):
- `data/generated/career-data.json` — career history (CRITICAL: maps Paul's actual experience to assignment requirements)
- `data/sources/knowledge/career/companies.json` — company history
- `data/sources/knowledge/career/projects.json` — project portfolio

**Agent Config** (this repo):
- `.claude/rules/guiding-principles.md` — 42 technology principles (inform requirements priorities)
- `knowledge_base/system_config.json` — agent configuration (READ-ONLY)

**Assignment**:
- `.claude/plans/references/solution-architect-case-study-and-interview.md` — the full case study
- `.claude/plans/references/CVS - GenAI Data Scientist Job Description .pdf` — GenAI DS JD

## Research Directives

Conduct web research across 9 topic clusters. For each cluster, execute 2-4 WebSearch queries and synthesize findings with citations. Document all sources.

### Cluster 1: IBMi/AS/400 Modernization Patterns
**Why**: Paul's biggest knowledge gap. Must understand the technical landscape before designing solutions.
- `IBMi AS/400 modernization strategies 2025 2026`
- `AS/400 green screen to web UI transformation approaches`
- `IBMi RPG COBOL modernization middleware APIs`
- `Rocket Software Profound Logic Fresche Legacy IBMi modernization tools`

### Cluster 2: CVS Health Technology Ecosystem
**Why**: Must understand CVS's specific tech stack, recent initiatives, and organizational context.
- `CVS Health technology stack GCP Google Cloud partnership`
- `CVS Health Health100 digital platform pharmacy`
- `CVS Health IBMi AS/400 pharmacy benefits PBM systems`
- `CVS Health Aetna technology integration modernization`

### Cluster 3: GCP Services for Legacy Modernization
**Why**: CVS JD emphasizes GCP (7+ years preferred). Must map GCP services to modernization patterns.
- `Google Cloud Platform legacy mainframe modernization services`
- `GCP Apigee API management legacy system integration`
- `GCP Cloud Run App Engine Kubernetes legacy workloads`
- `Google Cloud Dual Run mainframe modernization`

### Cluster 4: Healthcare IAM Standards and Patterns
**Why**: IAM is one of the 5 key considerations. Paul hasn't designed IAM from scratch.
- `healthcare IAM identity access management HIPAA compliance patterns`
- `SMART on FHIR OAuth2 healthcare authentication`
- `Google Cloud Identity healthcare IAM enterprise federation`
- `zero trust architecture healthcare pharmacy systems`

### Cluster 5: Human-Centered Design in Healthcare IT
**Why**: HCD is one of the 5 key considerations. Must ground in established healthcare HCD frameworks.
- `human centered design healthcare IT legacy modernization`
- `NIST human centered design guidelines`
- `usability testing green screen to web migration users`
- `healthcare UX design pharmacy workflow systems`

### Cluster 6: Change Management for Legacy Transitions
**Why**: Change management is one of the 5 key considerations. Users accustomed to green screens resist change.
- `change management legacy system modernization enterprise`
- `Prosci ADKAR change management technology transformation`
- `green screen to web UI user adoption strategies`
- `training strategies legacy to modern UI healthcare`

### Cluster 7: Pharmacy Benefits Management (PBM) Domain
**Why**: Must understand the business domain to design relevant solutions.
- `pharmacy benefits management PBM systems architecture`
- `PBM claims adjudication real-time processing systems`
- `pharmacy benefits IBMi mainframe workflow processing`
- `CVS Caremark PBM technology platform`

### Cluster 8: GenAI in Healthcare Operations
**Why**: Dual competency requirement — must show how GenAI integrates with the modernized system.
- `generative AI healthcare clinical notes NLP pipeline`
- `LLM clinical text extraction structured data healthcare`
- `GenAI pharmacy benefits automation referral processing`
- `GCP Vertex AI healthcare NLP pipeline production`

### Cluster 9: Modern Technology Stacks for Enterprise Modernization
**Why**: Technology stack is one of the 5 key considerations.
- `React Angular enterprise legacy modernization frontend 2025 2026`
- `micro frontend architecture legacy system strangler fig pattern`
- `BFF backend for frontend pattern API gateway legacy integration`
- `event driven architecture Kafka Pub/Sub legacy modernization`

## Execution Steps

### Step 1: Read All Context Files
Read every file listed in the Context Files section above. Take notes on:
- Paul's direct experience that maps to the assignment (for honesty mapping)
- Technical principles that should inform the solution design
- The exact scope and expectations from the case study

### Step 2: Execute Web Research
Run all 9 research clusters. For each:
1. Execute the WebSearch queries
2. Read key results with WebFetch where needed for deeper detail
3. Synthesize findings into a structured section with citations
4. Flag any contradictions or areas where sources disagree
5. Note areas where research was thin or inconclusive

### Step 3: Write Research Findings Document
Write to: `outputs/cvs-legacy-transformation/research-findings.md`

Structure:
```markdown
# CVS Legacy Transformation — Research Findings

**Date**: [date]
**Purpose**: Factual foundation for solution architecture engagement
**Confidence Key**: HIGH (multiple corroborating sources) | MEDIUM (limited sources) | LOW (inference/single source)

## 1. IBMi/AS/400 Modernization Landscape
[Findings with citations]

## 2. CVS Health Technology Context
[Findings with citations]

## 3. GCP Legacy Modernization Services
[Findings with citations]

## 4. Healthcare IAM Patterns
[Findings with citations]

## 5. Human-Centered Design in Healthcare
[Findings with citations]

## 6. Change Management for Legacy Transitions
[Findings with citations]

## 7. PBM Domain Knowledge
[Findings with citations]

## 8. GenAI in Healthcare Operations
[Findings with citations]

## 9. Technology Stack Options
[Findings with citations]

## Appendix A: Paul's Experience Mapping
[Map Paul's actual experience to each of the 5 key considerations]

## Appendix B: Assumption Register
[Numbered list of assumptions made during research]

## Appendix C: Source Bibliography
[All URLs cited, organized by cluster]
```

### Step 4: Create engagement.json
Before invoking skills, create `knowledge_base/engagement.json` to initialize engagement lifecycle tracking:
- `engagement_id`: `eng-2026-001`
- `engagement_type`: `modernization`
- `status`: `in_progress`
- `client.name`: `CVS Health`
- `client.industry`: `Healthcare / Pharmacy Benefits`
- `client.size`: `enterprise`
- `lifecycle_state`: set `requirements` to `in_progress`, all others to `not_started`

### Step 5: Run `/requirements` (Comprehensive Tier)
Invoke the `/requirements` skill with comprehensive tier. Provide the following context to the skill:
- The case study requirements (5 key considerations)
- Research findings from Step 3
- Paul's experience mapping from career-data.json
- The GenAI DS JD (for dual competency thread)
- System context: IBMi green screen apps, pharmacy benefits, CVS Health enterprise

The requirements should capture:
- **Functional requirements** for all 5 key considerations
- **Non-functional requirements** (performance, security, scalability, compliance)
- **AI/ML pipeline requirements** (from GenAI DS JD — the team Paul would lead)
- **Stakeholder needs** (end users, administrators, developers, business leaders)
- **Success criteria** with measurable KPIs
- **AI suitability assessment** for the modernization effort

### Step 6: Validate KB and Update Engagement
After `/requirements` produces `knowledge_base/requirements.json`:
1. Run `python tests/validate_knowledge_base.py` to validate against schemas
2. Update `knowledge_base/engagement.json`: set `lifecycle_state.requirements.status` to `complete`

### Step 7: Run `/review` on Requirements
Review `knowledge_base/requirements.json` using `/review`. Target >= 7.5/10 across all 5 dimensions (completeness, technical soundness, well-architected alignment, clarity, feasibility). If below threshold, iterate.

### Step 8: Create Experience-to-Assignment Honesty Map
Create a structured mapping document showing:

| Assignment Area | Paul's Direct Experience | Confidence | Evidence Source |
|----------------|------------------------|------------|-----------------|
| Legacy System Integration | [specific projects] | [1-5] | [career-data.json reference] |
| IAM Strategy | [specific projects] | [1-5] | [career-data.json reference] |
| HCD Design Principles | [Cognitive Science degree, specific projects] | [1-5] | [career-data.json reference] |
| Technology Stack | [specific tech experience] | [1-5] | [career-data.json reference] |
| Change Management | [Mento coaching, specific projects] | [1-5] | [career-data.json reference] |
| GenAI/ML Leadership | [specific AI projects] | [1-5] | [career-data.json reference] |
| GCP | [specific GCP experience] | [1-5] | [career-data.json reference] |
| Healthcare Domain | [any healthcare experience] | [1-5] | [career-data.json reference] |

Save this map to: `outputs/cvs-legacy-transformation/honesty-map.md`

This map is referenced by every subsequent phase to maintain honesty consistency.

## Honesty Rules

1. **Paul's direct experience** → state confidently, cite the specific role/project from career-data.json
2. **Researched for this assignment** → explicitly label: "Based on research conducted for this engagement..."
3. **Industry standard practice** → cite the source: "Per [framework/standard]..."
4. **Assumptions** → number them (A-0-NNN), flag for confirmation: "Assumption A-0-001: [statement]"
5. **IBMi/AS/400 claims** → MUST have a web source. Zero unsourced IBMi claims.
6. **GCP claims** → verify against official GCP documentation. Paul's AWS experience frames the narrative, but GCP specifics must be researched.
7. **Unknown areas** → frame as learning areas with a credible plan, not as existing expertise

## Quality Gate

- Run `/review` on `knowledge_base/requirements.json`
- Minimum score: >= 7.5/10 across all 5 dimensions (completeness, technical soundness, well-architected, clarity, feasibility)
- Research findings document must have citations for every technical claim
- Every research cluster must have at least 3 sources
- IBMi/AS/400 section must have >= 5 distinct sources
- Experience-to-assignment honesty map must be complete for all 8 areas

## Exit Criteria

Before proceeding to Phase 1:
- [ ] Research findings document written with citations across all 9 clusters
- [ ] `knowledge_base/requirements.json` produced via `/requirements` (comprehensive tier)
- [ ] `/review` score >= 7.5/10 on requirements
- [ ] Experience-to-assignment honesty map complete
- [ ] All assumptions numbered and tracked in Appendix B
- [ ] No unsourced IBMi/AS/400 technical claims
- [ ] `knowledge_base/engagement.json` created with lifecycle tracking
- [ ] KB validation passes: `python tests/validate_knowledge_base.py`

## Context Handoff

After execution completes, save context for future phases:

1. **Write context summary** to `.claude/plans/cvs-engagement/context/phase-0-context.md` using the Context Summary Template (see master-plan.md)

2. **Update ALL remaining phase plan files** with:
   - New artifacts and file paths produced in this phase (research findings, honesty map, requirements.json)
   - Refined research directives based on what was learned (e.g., if IBMi modernization tools have changed, update Phase 2's architecture plan)
   - Adjusted scope based on discoveries (e.g., if CVS's GCP usage is deeper than expected, expand Phase 2's GCP section)
   - Corrected or new assumptions
   - Specific insights that change downstream approaches

3. **Update master-plan.md** if any structural changes to the engagement

4. **Commit** all context and plan updates to git with message: `docs(plans): complete Phase 0 research and requirements, update future plans`

## Human Checkpoint

Paul: review the following before proceeding to Phase 1:
- Research findings document: `outputs/cvs-legacy-transformation/research-findings.md`
  - Are the IBMi/AS/400 findings accurate to your understanding?
  - Are the CVS Health technology context findings current?
  - Any research areas that need deeper investigation?
- Requirements: `knowledge_base/requirements.json`
  - Do the functional requirements capture the right scope?
  - Are the GenAI/ML pipeline requirements appropriate for the dual competency thread?
- Honesty map: `outputs/cvs-legacy-transformation/honesty-map.md`
  - Are the confidence ratings accurate for each area?
  - Any experience Paul wants to highlight or downplay?
- Assumption register: review assumptions in Appendix B
  - Any assumptions that should be confirmed or rejected now?
- Updated future phase plans (review changes from this phase's learnings)
- Context summary accuracy
