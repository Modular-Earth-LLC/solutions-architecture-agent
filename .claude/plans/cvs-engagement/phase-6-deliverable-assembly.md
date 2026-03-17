# Phase 6: Deliverable Assembly and Quality Assurance

Use ultrathink for this phase. Engage extended reasoning before every major output.

This phase assembles all prior work into a single cohesive Markdown document. No new research — this is assembly, integration, and polish. The focus is coherence, voice consistency, and document quality.

## Objective

Assemble all phase outputs into a single, cohesive Solution Architecture Document for CVS Health's Legacy System Transformation. This phase produces:
1. `outputs/cvs-legacy-transformation/solution-architecture-document.md` — the final deliverable
2. Quality reviews from 3 review personas
3. Final GFM formatting validation

The document must:
- Be a single Markdown file that renders correctly in GitHub
- Export cleanly to Word (no complex HTML, no embedded images — Mermaid diagrams only)
- Address all 5 key considerations from the case study
- Demonstrate dual competency (architect + GenAI team leader)
- Sound like Paul (collaborative, empirical, warm, solution-focused)
- Be < 300 KB total file size
- **Serve as pre-interview reading** for the hiring manager and interviewers — sent before the interview stage
- **Each key consideration section must be self-contained** so an interviewer assigned to one topic can read only that section and have full context
- **Cross-references between sections** so an IAM interviewer understands how IAM connects to architecture, HCD, etc.
- **Executive summary must work as a standalone overview** for the hiring manager to assign interviewers to topics
- **Each key consideration section must provide sufficient depth** for a 45-minute focused interview
- Consider adding a **Reading Guide** at the top mapping sections to interview topics

## Input Dependencies

All artifacts from all prior phases:

**Knowledge Base Files**:
- `knowledge_base/engagement.json` — engagement lifecycle state
- `knowledge_base/requirements.json` — Phase 0
- `knowledge_base/integration_plan.json` — Phase 2
- `knowledge_base/architecture.json` — Phase 2
- `knowledge_base/data_model.json` — Phase 2
- `knowledge_base/security_review.json` — Phase 3
- `knowledge_base/estimate.json` — Phase 4
- `knowledge_base/project_plan.json` — Phase 4
- `knowledge_base/reviews.json` — all phases

**Output Documents**:
- `outputs/cvs-legacy-transformation/research-findings.md` — Phase 0
- `outputs/cvs-legacy-transformation/honesty-map.md` — Phase 0
- `outputs/cvs-legacy-transformation/ux-design-document.md` — Phase 1
- `outputs/cvs-legacy-transformation/iam-strategy.md` — Phase 3
- `outputs/cvs-legacy-transformation/ai-methodology.md` — Phase 5
- `outputs/cvs-legacy-transformation/llm-citations.md` — Phase 5
- `outputs/cvs-legacy-transformation/portfolio-narrative.md` — Phase 5

**All Phase Context Summaries**:
- `.claude/plans/cvs-engagement/context/phase-*-context.md`

## Prior Phase Context

Read ALL completed phase context summaries before executing:
- `.claude/plans/cvs-engagement/context/phase-*-context.md`

This phase has context from ALL 6 preceding phases. Use this to:
- Ensure the document tells a coherent story across all sections
- Resolve any contradictions between phases
- Incorporate Paul's feedback from every phase
- Maintain consistent assumptions (reference the assumption register)
- Thread the dual competency narrative throughout

## Context Files

**Paul's Voice and Brand** (base: `C:\dev\paulprae-com`):
- `data/sources/knowledge/brand/identity.json` — brand identity
- `data/sources/knowledge/brand/communication-styles.json` — communication styles (CRITICAL for voice)
- `data/sources/knowledge/brand/values.json` — values alignment
- `data/sources/knowledge/content/writing-formulas.json` — writing formulas (STAR, PAS, BAB, AIDA)

**Quality Benchmarking Exemplars** (for calibrating deliverable quality):
- `.claude/plans/references/reference-materials-index.md` — index of real-world SA deliverables
- Reference the Hyperbloom, AVAHI, Florence, and AGADA exemplars in `.claude/plans/references/` to benchmark section depth, diagram density, and professional tone against real SA deliverables

**Agent Config**:
- `.claude/rules/guiding-principles.md` — for principle references in the document

## Research Directives

No new web research in this phase. Assembly only. If a gap is discovered during assembly that requires research, document it and consult with Paul before researching.

## `/proposal` Skill Consideration

The SA Agent's `/proposal` skill assembles proposals from KB data (supports 4 types: discovery, implementation, internal, pitch deck). Evaluate whether invoking `/proposal` with type `internal` or `pitch deck` adds value as a structural starting point, or whether manual assembly better serves this custom document format. The `/proposal` skill reads all KB files and structures them into a deliverable — which is exactly what this phase does. Consider using it as a scaffolding step, then customizing the output.

## Execution Steps

### Step 1: Read ALL Input Files
Read every artifact, output document, and context summary listed above. Create a mental model of:
- The complete narrative arc
- Any contradictions or gaps between phases
- Paul's voice and direction changes (from context summaries)
- The assumption register across all phases
- The dual competency thread across phases

### Step 2: Benchmark Against Exemplars
Read `.claude/plans/references/reference-materials-index.md` and skim 1-2 exemplar deliverables (Hyperbloom architecture PDF, AVAHI SOW template) to calibrate:
- Expected section depth and detail level
- Diagram density and placement
- Professional tone and formatting standards
- Executive summary structure

### Step 3: Evaluate `/proposal` Skill
Decide whether to invoke `/proposal` as a scaffolding step:
- If yes: invoke with type `internal`, then restructure/customize the output
- If no: proceed with manual assembly using the document structure below

### Step 4: Define Document Structure
The document structure maps to the 5 key considerations plus supporting sections:

```markdown
# Legacy System Transformation: IBMi Green Screen Modernization
## Solution Architecture Document — CVS Health

**Author**: Paul Pham
**Date**: [date]
**Version**: 1.0

---

## Table of Contents
[Auto-generated from headers]

---

## Executive Summary
[1-2 pages — the "elevator pitch" version of the entire document]
- Business context and challenge
- Recommended approach (strangler fig, GCP-native)
- Key differentiators of this approach
- High-level timeline and investment range
- Risk summary and mitigation approach

---

## 1. Understanding the Challenge
### 1.1 Current State Assessment
[IBMi green screen landscape, business criticality, user impact]
### 1.2 Modernization Drivers
[Why now, business value, competitive pressure]
### 1.3 Success Criteria
[Measurable outcomes — from requirements.json]

---

## 2. Legacy System Integration Strategy
[KEY CONSIDERATION 1]
### 2.1 IBMi Integration Architecture
[Integration patterns, middleware, API layer]
### 2.2 Strangler Fig Migration Approach
[Phased migration strategy with rollback]
### 2.3 Data Synchronization
[CDC, event-driven, consistency guarantees]
### 2.4 Coexistence Strategy
[Parallel run, feature toggles, gradual cutover]

---

## 3. Human-Centered Design Approach
[KEY CONSIDERATION 3 — Paul's Cognitive Science differentiator]
### 3.1 Design Philosophy
[Cognitive Science-grounded principles]
### 3.2 User Personas
[Key personas with workflows]
### 3.3 UX Design Principles
[6 principles from Phase 1]
### 3.4 Transition Design
[How users move from green screen to modern UI]
### 3.5 Usability Testing Strategy
[Methods, cadence, feedback integration]

---

## 4. Solution Architecture
[KEY CONSIDERATION 4 — Technology Stack]
### 4.1 Architecture Overview
[System context diagram — Mermaid]
### 4.2 Solution Options Analysis
[3 options with pros/cons — from architecture.json]
### 4.3 Recommended Architecture
[Detailed container diagram — Mermaid]
### 4.4 Technology Stack
[GCP services, frontend framework, middleware]
### 4.5 Data Architecture
[Data model, storage strategy, from data_model.json]
### 4.6 AI/ML Pipeline Architecture
[GenAI pipeline — dual competency demonstration]
### 4.7 Well-Architected Assessment
[6-pillar scoring with justification]

---

## 5. Identity and Access Management Strategy
[KEY CONSIDERATION 2 — potential 45-minute interview topic]
### 5.1 IAM Architecture Overview
[Identity flow diagram — Mermaid]
### 5.2 Authentication Strategy
[SSO, MFA, federation, migration path]
### 5.3 Authorization Model
[RBAC + ABAC, policy engine, pharmacy-specific patterns]
### 5.4 Zero Trust Implementation
[BeyondCorp adaptation, phased approach]
### 5.5 Compliance and Audit
[HIPAA, SOC 2, DEA requirements]

---

## 6. Security Architecture
### 6.1 Threat Model
[STRIDE summary — top threats and mitigations]
### 6.2 Defense-in-Depth
[Layer-by-layer security architecture]
### 6.3 AI Security Controls
[Prompt injection, output validation, responsible AI]
### 6.4 Compliance Framework
[Regulatory mapping table]

---

## 7. Change Management Strategy
[KEY CONSIDERATION 5]
### 7.1 Change Management Framework
[ADKAR model application]
### 7.2 Stakeholder Engagement
[Communication plan, champion network]
### 7.3 Training Program
[Multi-modal training approach]
### 7.4 Adoption Measurement
[KPIs, success metrics, feedback loops]

---

## 8. Implementation Roadmap
### 8.1 Phased Approach
[4-phase roadmap with decision gates]
### 8.2 Team Composition
[Roles, responsibilities, GenAI team]
### 8.3 Investment Summary
[Cost ranges with confidence levels]
### 8.4 Risk Register
[Top risks with mitigations]
### 8.5 Timeline
[Gantt-style Mermaid diagram]

---

## 9. AI-Assisted Methodology
[How this document was produced — from Phase 5]
### 9.1 Human-AI Collaboration Model
### 9.2 Quality Assurance Process
### 9.3 Responsible AI Practice

---

## Appendices
### Appendix A: Assumption Register
[Consolidated from all phases: A-0-NNN through A-5-NNN]
### Appendix B: Technology Reference
[GCP services, tools, and versions referenced]
### Appendix C: Glossary
[PBM, IBMi, and healthcare terminology]
### Appendix D: LLM Attribution
[From llm-citations.md]
### Appendix E: About the Author
[Brief bio connecting to portfolio-narrative.md]

---

**Document produced with AI assistance. See Section 9 and Appendix D for methodology and attribution.**
```

### Step 5: Assemble the Document
Write the complete document to: `outputs/cvs-legacy-transformation/solution-architecture-document.md`

Assembly guidelines:
1. **Extract, don't copy-paste**: Transform KB JSON and design documents into polished prose sections
2. **Consistent voice**: Every section should sound like Paul — collaborative, empirical, warm
3. **Narrative thread**: The document should tell a story from problem → analysis → solution → plan
4. **Visual density**: Mermaid diagrams at every major section; tables for comparisons
5. **Assumption consistency**: Use the consolidated assumption register; don't introduce new ones
6. **Cross-references**: Sections should reference each other naturally ("as discussed in Section 4.3...")
7. **Dual competency thread**: The GenAI pipeline should appear in architecture, security, estimation, and methodology — not as an afterthought
8. **Honesty markers**: Use the framework from honesty-map.md consistently

### Step 6: GFM Formatting Validation
Ensure the document follows GitHub-Flavored Markdown:
- Standard ATX headers (# through ####)
- Pipe tables with header rows
- Fenced code blocks with language identifiers
- Mermaid blocks in ```mermaid fences
- No HTML except essential (e.g., `<br>` in table cells if needed)
- Proper link syntax
- Clean whitespace (no trailing spaces, consistent blank lines)

### Step 7: Update engagement.json
Update `knowledge_base/engagement.json`:
- Set overall status to `in_review`
- Verify all domain lifecycle entries are `complete`

Run `python tests/validate_knowledge_base.py` to validate all KB files one final time.

### Step 8: Run `/review` with 3 Personas
Run `/review` three times with different reviewer contexts:

**Persona 1: Technical Architecture Reviewer**
- Focus: technical soundness, architecture patterns, GCP accuracy, diagram quality
- Looking for: unsupported claims, missing components, integration gaps

**Persona 2: Hiring Panel Member (IAM Specialist)**
- Focus: IAM strategy depth, compliance accuracy, security completeness
- Looking for: shallow treatment, missing standards, generic advice

**Persona 3: Business Stakeholder / Executive Reviewer**
- Focus: clarity, business value, feasibility, change management
- Looking for: jargon without explanation, missing ROI justification, unrealistic timelines

Each `/review` invocation scores across 5 dimensions: completeness, technical soundness, well-architected alignment, clarity, and feasibility. Target >= 7.5/10 from each persona. Iterate if any persona scores below threshold.

### Step 9: Final Voice and Coherence Pass
After reviews and iterations:
1. Read the entire document start to finish
2. Check for voice consistency (does every section sound like Paul?)
3. Check for narrative flow (does the story hold together?)
4. Check for assumption consistency (no contradictions)
5. Check for dual competency thread (GenAI appears naturally throughout)
6. Check for honesty consistency (experience claims match honesty map)
7. Verify document size < 300 KB

### Step 10: Verify File Size and Rendering
- Check file size: `wc -c outputs/cvs-legacy-transformation/solution-architecture-document.md`
- Verify Mermaid diagram syntax (all blocks should be valid)
- Count sections against table of contents

## Honesty Rules

1. **Assembly phase** → don't introduce new claims or analysis. Everything should trace back to a prior phase.
2. **Voice consistency** → if a section sounds too formal or too casual for Paul, adjust.
3. **Assumption consolidation** → the appendix must reconcile assumptions across all phases. If Phase 3 rejected an assumption from Phase 0, note that.
4. **Credit attribution** → the AI methodology section is honest about human vs. AI contributions.
5. **No filler** → every paragraph must add value. Remove generic boilerplate. (Per guiding principle 38: "Every output must deliver tangible value.")
6. **Experience claims** → verify every "in my experience" statement against career-data.json one final time.

## Quality Gate

- Run `/review` with 3 personas
- Minimum score: >= 7.5/10 from each persona across all 5 dimensions (completeness, technical soundness, well-architected, clarity, feasibility)
- Document renders correctly as GFM
- File size < 300 KB
- All 5 key considerations have dedicated sections with sufficient depth for 45-minute interviews
- Each key consideration section is self-contained with cross-references to related sections
- Executive summary works standalone for the hiring manager to assign interviewers
- Mermaid diagrams render correctly (syntax validation)
- Voice is consistently Paul's across all sections
- Dual competency thread is visible in sections 4, 5, 6, 8, and 9
- Assumption register is consolidated and consistent
- No orphaned references or broken cross-references
- KB validation passes: `python tests/validate_knowledge_base.py`

## Exit Criteria

Before proceeding to Phase 7:
- [ ] `outputs/cvs-legacy-transformation/solution-architecture-document.md` complete
- [ ] All 3 review personas scored >= 7.5/10
- [ ] Document < 300 KB
- [ ] GFM validation passed
- [ ] All Mermaid diagrams syntax-valid
- [ ] Voice consistency verified
- [ ] Dual competency thread present throughout
- [ ] Assumption register consolidated
- [ ] No unsourced technical claims
- [ ] engagement.json updated with final lifecycle state
- [ ] KB validation passes

## Context Handoff

After execution completes, save context for future phases:

1. **Write context summary** to `.claude/plans/cvs-engagement/context/phase-6-context.md` using the Context Summary Template (see master-plan.md)

2. **Update ALL remaining phase plan files** with:
   - Final document file path and structure for Phase 7 (interview prep needs the complete document)
   - Section numbers and headers for Phase 7 (Q&A bank maps to document sections)
   - Review scores and feedback for Phase 7 (weaknesses to prepare for)
   - Any areas that were flagged during review that Paul should be prepared to defend
   - Voice and framing decisions that affect how Paul presents

**Phase 2 Insights for Assembly**:
- 5 Mermaid diagrams ready: system context, deployment view, data flow, GenAI pipeline, strangler fig migration
- Three-option analysis (GCP/AWS/Modern Cloud) maps directly to interview expectation #4: "explore and present multiple options"
- Each option has cited vendor reference architectures (AWS Healthcare Industry Lens, GCP Dual Run docs, Vercel HIPAA guide, Supabase Healthcare Solutions)
- Architecture sections are self-contained for interview topic assignment (per Phase 6 document structure)
- GenAI pipeline diagram (C-006, C-007) shows confidence-based routing, HITL, evaluation framework — visual proof of dual competency
- WA scores (overall 7.7) with per-pillar notes — embed in Section 4.7 of deliverable
- Key trade-off to highlight: GCP recommended for CVS partnership alignment, but AWS is technically strongest (HealthLake + Comprehend Medical), and Modern Cloud is fastest to deliver
- 13 data entities with PBM domain ontology — include simplified ER diagram in Section 4.5
- API contracts (10) with specific SLAs provide interview-ready depth for architecture questions
- Review scores (8.1-8.3/10) indicate solid quality — no major rework needed before assembly
- Cost comparison table across three options needed in Section 8.3 (flagged in review RF-016)

**Phase 1 Insights for Assembly**:
- HCD section is a strength area — 6 design principles with cited cognitive science theories provide depth for the 45-minute interview
- Wireframe descriptions for Claims Adjudication Dashboard and PA Workflow show concrete thinking, not just abstract principles
- CVS brand alignment should reference their existing accessibility annotation kit methodology
- Design principles section should be positioned prominently — Paul's Cognitive Science degree is a genuine differentiator
- UX design document is comprehensive (65KB) — assembly should distill key elements, not reproduce in full

3. **Update master-plan.md** if any structural changes to the engagement

4. **Commit** all context and plan updates to git with message: `docs(plans): complete Phase 6 deliverable assembly, update future plans`

## Human Checkpoint

Paul: this is the most important review in the engagement. Review thoroughly:
- Complete document: `outputs/cvs-legacy-transformation/solution-architecture-document.md`
  - Read the entire document start to finish
  - Does it sound like you wrote it?
  - Would you be proud presenting this to CVS Health's hiring panel?
  - Are there any claims you can't defend in an interview?
  - Is the dual competency thread (architect + GenAI leader) convincing?
- Review scores from 3 personas — any areas below 7.5/10?
- Assumption register — any assumptions you want to confirm or revise?
- AI methodology section — are you comfortable with the transparency level?
- Updated Phase 7 plan (review changes from this phase's learnings)
- Context summary accuracy

**This is the "would I put my name on this?" checkpoint.** If the answer is anything less than "yes, confidently," we iterate before moving to Phase 7.
