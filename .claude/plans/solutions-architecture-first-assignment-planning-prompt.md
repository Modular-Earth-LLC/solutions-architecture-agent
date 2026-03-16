# Meta-Planning Prompt: CVS Health Legacy System Transformation

Use ultrathink for this entire prompt. Engage extended reasoning before every major output.

> **What this prompt does**: Generates a master plan of phase-specific planning prompts, each written to `.claude/plans/cvs-engagement/` as standalone files that Paul and the agent will execute together, one phase at a time.
>
> **How to run**: Load the SA Agent plugin (`claude --plugin-dir .`), then paste or reference this prompt.
>
> **Date**: 2026-03-16 | **Plugin version**: 1.0.0 | **CLI version**: 2.1.75+

---

## Mission

You are a distinguished engineer and principal AI/LLM solutions architect. Your mission is to create a **master plan of planning prompts** — a series of phase plans that, when executed sequentially, will produce a complete solution architecture for the CVS Health Legacy System Transformation case study (Use Case 1).

**Critical framing**: You are NOT executing the assignment. You are designing the plan that will guide execution across multiple sessions. Each phase plan you write will be sent to Claude Code as a standalone planning prompt that Paul and the agent will iteratively review, improve, and execute together.

**This is a meta-task**: research → analyze → architect an approach → write planning prompts for later execution.

**Every phase plan you write must include the directive**: `Use ultrathink for this phase. Engage extended reasoning before every major output.`

---

## Context Loading

### CRITICAL: Directory Exclusions

**NEVER read, reference, or index** any file in `.claude/plans/archive/`. That directory contains completed artifacts from an **unrelated project** (the SA Agent's own development). Referencing those files will poison your context with irrelevant information.

### Assignment Source

Read and deeply analyze: `.claude/plans/references/solution-architect-case-study-and-interview.md`

This file contains two sections:
1. **The full job description** for Principal Architect, Solution Engineering and Automation (sourced from https://jobs.cvshealth.com/us/en/job/R0771820/Principal-Architect-Solutions-and-Automation — updated March 2026)
2. **The case study assignment** with two use cases

Paul has selected **Use Case 1: Legacy System Transformation (SELECTED)** — modernizing IBMi (AS/400) green screen applications with new UI/UX while addressing Legacy System Integration, IAM Strategy, HCD Design Principles, Technology Stack, and Change Management.

**Use Case 2: Transitioning to a Domain-Based Architecture (NOT SELECTED)** is retained in the reference file as organizational context. It reveals CVS Health's broader technology direction — domain-based architecture, Domain-Driven Design, legacy service layer consolidation, cloud migration patterns, and multi-platform strategy. Use it to inform architectural decisions but do not solve it.

There is also a second CVS job description in the references directory for a **GenAI Data Scientist** role. Paul must demonstrate through this assignment that he can lead engineers in both capacities — as a principal architect AND as a thought leader capable of guiding the data scientists he would lead. The deliverable should demonstrate this dual competency.

### Interview Format and Submission

This is a **high-stakes, multi-round evaluation**:

1. **Written submission first** — Paul submits a single document (Markdown, later exported to Word) to the hiring panel before any interview is scheduled
2. **Panel drills** — each of the 5 key considerations has an associated panel member who will drill Paul in depth on that topic and report back to the hiring team
3. **Depth over speed** — interviews won't be scheduled until the written deliverable is complete. Optimize for thoroughness and quality, not brevity

**6 interview expectations** (per the assignment):
1. **High-Level Solution Flow** — present an overview of key components and how they interrelate
2. **Clarification and Questions** — ask questions at the beginning to clarify requirements and constraints
3. **Diagram Development** — create and discuss visual representations of the architecture
4. **Multiple Solution Options** — explore multiple options with pros/cons (feasibility, scalability, maintainability, business alignment)
5. **Thought Process Articulation** — explain rationale behind design choices, integration strategies, and how they address key considerations
6. **Focus on Key Considerations** — address all 5 key considerations from Use Case 1

**5 key considerations** (each maps to a panel member who will drill Paul):
1. **Legacy System Integration** — seamless integration with existing green screen applications, minimizing disruption to current operations
2. **IAM Strategy** — robust Identity and Access Management with compliance to industry standards
3. **HCD Design Principles** — Human-Centered Design throughout, with user feedback and iterative design
4. **Technology Stack** — balancing modern technologies with legacy system constraints
5. **Change Management** — managing user transition, adoption, and minimizing resistance

### Target Audience

The hiring manager's profile (calibrate technical depth and language to this level):

> 20+ years of software engineering experience. Leads large-scale projects and global cross-functional teams to deliver digital transformation, complex solutions, and enterprise architectures supporting multi-billion-dollar revenue streams. Core competencies: software development and system design, team leadership, business outcomes alignment, software infrastructure and security, technology trends evaluation. Has developed and managed a $50M+ digital platform using cloud technologies and Microservices Architecture, established RESTful API platform compliant with TMForum industry standard, managed 5+ mission-critical systems generating $1.2B+ revenue, and consolidated and decommissioned 7+ applications.

The role: **Principal Architect, Solution Engineering and Automation** — responsible for end-to-end solution architecture, technology incubation, emerging tech evaluation, AI/ML architecture, automation frameworks, and mentoring. The full job description is embedded in the assignment source file.

### CVS Health Strategic Context

CVS Health is investing heavily in AI as a core driver of digital health:

- Partnered with Google Cloud to launch **Health100**, an AI-enabled consumer engagement platform
- Uses Gemini models, Cloud Healthcare API, and BigQuery across payor, pharmacy, provider ecosystems
- Already embeds AI in pharmacy ops, benefits admin, and clinical workflows
- Recently published work on generative agents for care experience testing
- Positioning as an AI-powered health engagement platform provider, not just retailer/insurer
- Key tech partnerships: Google Cloud (primary), Databricks, DataRobot

**MANDATORY**: Perform deep web research on CVS Health's technology strategy, recent announcements, digital transformation initiatives, IBMi/AS/400 footprint, and pharmacy technology systems as of March 2026. Use `WebSearch` extensively. Cross-validate all claims across multiple sources. Cite every factual claim with its source URL.

### Paul's Background — Honest Calibration

Read these files to understand Paul's exact experience, voice, and brand:

**Career data** (read to map Paul's experience to the assignment — CRITICAL for honesty):
- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\data\generated\career-data.json`

**Brand and voice** (read ALL — deliverables must sound like Paul):
- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\data\sources\knowledge\brand\identity.json`
- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\data\sources\knowledge\brand\communication-styles.json`
- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\data\sources\knowledge\brand\values.json`
- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\data\sources\knowledge\content\writing-formulas.json`

**Career context** (read for relevant experience to reference):
- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\data\sources\knowledge\career\companies.json`
- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\data\sources\knowledge\career\projects.json`

**Recent project architectures** (read for patterns and tech stack precedent):
- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\README.md`
- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\docs\technical-design-document.md`
- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\docs\ai-architecture.md`
- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\docs\devops.md`
- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\docs\security.md`
- `C:\dev\paloist-core\docs\solution-architecture.md`
- `C:\dev\paloist-core\docs\security-and-privacy.md`

#### Honesty Rules

Paul's experience is extensive but has specific gaps relevant to this assignment. The deliverable must be honest about what Paul knew beforehand, what he learned during the assignment, and what he needs to confirm with the panel.

**What Paul brings (strong — leverage these):**
- 15 years of AI/data engineering across healthcare, life science, insurance, financial services
- AWS SA experience (3 years at Amazon): Well-Architected Reviews, reference architectures, enterprise customer engagement
- AI governance, algorithmic bias mitigation, HIPAA/FedRAMP compliance (Booz Allen)
- Healthcare data platform architecture (Arine: Snowflake, CDC pipelines, AI agent observability)
- Human-centered design education (BS Cognitive Science with AI focus, BA Computer Science with AI emphasis from UGA)
- Executive coaching and change management experience (Mento)
- Open-source, local-first architecture principles (Modular Earth)
- Pre-sales/consulting lifecycle (Hyperbloom, AVAHI, Slalom, Decooda)

**What Paul does NOT have (be transparent — frame as "areas I researched for this assignment"):**
- IBMi/AS/400 experience — Paul rates himself 1/5. He has heard the terms but does not understand the architecture, RPG/COBOL, or green screen systems. He did not know CVS was old enough to have such legacy systems.
- GCP-native architecture — Paul's cloud narrative is primarily AWS with some Azure. GCP is the JD's primary cloud. Frame cloud skills as transferable while being honest about the learning curve.
- IAM as a first-class design concern — Paul has worked within IAM boundaries (FedRAMP, HIPAA) but has not designed an IAM strategy from scratch for a transformation.
- RPA platforms (UiPath, Automation Anywhere) — listed in JD, not in Paul's direct experience.

**Writing rules tied to honesty:**
- Every technical claim must be either (a) publicly sourced and cited, or (b) explicitly framed as an assumption Paul needs to confirm
- Only make assumptions that help Paul speak to important aspects of the solution (especially the 5 key considerations)
- Nothing in the final document should be something Paul can't comfortably speak to given his actual experience
- Where Paul's experience maps directly → state confidently and cite the relevant role/project
- Where Paul researched for this assignment → say so explicitly: "In preparing this design, I researched [topic] and found..."
- Where assumptions are made → flag with: "**Assumption [N]**: [statement] — to be confirmed with the CVS architecture team"

### Paul's Key Considerations Answers

These are Paul's raw instincts. The plans should validate, deepen, augment with research, and fill gaps — but preserve the authentic voice:

1. **Legacy System Integration**: Bring in SMEs and real users for UX/UI collaboration. Partner with legacy system maintainers. The interface swap needs API, networking, and security components the legacy system lacks. Consider local-first apps targeting laptops and mobile. To minimize disruption: fork the backend to avoid downtime, implement multi-stage environments (local dev, QA, UAT, prod, DR), phased rollout (small UAT group → percentage-based production rollout → full swap), maintain legacy with DR plan for rollback. Communication and collaboration are key.

2. **IAM Strategy**: Follow standard frameworks and vendor guidance. Use AWS/Microsoft Well-Architected security reviews. Leverage NIST and MITRE guidance. Penetration testing and e2e testing are the most effective security hardening steps. Use platform-specific IAM audit tools.

3. **HCD Design Principles**: Paul studied HCI in college (BS Cognitive Science with AI focus). Research the latest HCD best practices as of March 2026. Study the CVS brand to inform visual design. Ensure accessibility. Research what CVS Health and their technology partners say about HCD specifically.

4. **Technology Stack**: Prefer AI-native managed services from next-gen cloud platforms (see Paul's recent projects above). Balance technical debt, implementation speed, platform constraints, preferred vendor tooling, and peer preferences. Argue for future-proofing with proven, reliable tools.

5. **Change Management**: Extensive communication. Receptive to feedback and pivots. Announce migration ahead of design. Identify all stakeholder personas and design change management specifically for them. Play into emotions, psychology, behavioral neuroscience, and organizational politics. Paul's coaching experience at Mento is directly relevant here.

### Agent Capabilities

This repo is a Claude Code plugin with 9 skills that map to the solutions architecture lifecycle. Each phase plan must reference the specific skill invocation for execution:

| Skill | Invocation | Purpose |
| ----- | ---------- | ------- |
| Requirements | `/requirements` | Progressive requirements discovery (7 categories, AI suitability) |
| Integration Plan | `/integration-plan` | Legacy bridging, migration strategy, API contracts, CI/CD |
| Architecture | `/architecture` | Tech stack, component design, Mermaid diagrams, WA scoring |
| Data Model | `/data-model` | ER schemas, vector DB, knowledge graphs, data governance |
| Security Review | `/security-review` | STRIDE threat model, compliance mapping, defense-in-depth, IAM |
| Estimate | `/estimate` | LOE, cost modeling, team composition, confidence scoring |
| Project Plan | `/project-plan` | Phased roadmap, sprints, milestones, risk register |
| Proposal | `/proposal` | Assemble deliverables into client-ready documents |
| Review | `/review` | LLM-as-judge quality review, 5-dimension scoring |

**Skill workflow for migration engagements**: requirements → integration-plan → architecture → (data-model + security-review in parallel) → estimate → project-plan → review → proposal

The `/review` skill must be invoked after each major phase to validate quality before proceeding. Quality gate: >= 7.5/10 across all 5 dimensions (completeness, technical soundness, well-architected, clarity, feasibility).

### Guiding Principles

Read and apply: `.claude/rules/guiding-principles.md` — 42 technology principles that govern all work in this repo. Key principles for this assignment: human-centered design (#1-8), KISS (#10), separation of concerns (#11), anticipate failure (#16), ship (#17), Zero Trust security (#18-20), ground AI in truth (#22), automate everything (#28), build local-first (#30), client partnership (#33-39), no dark patterns (#40-41), human review mandatory (#42).

### Formatting Requirements

The final deliverable is a Markdown file that must:

1. **Render correctly on GitHub.com** — GitHub uses GitHub Flavored Markdown (GFM), a superset of CommonMark. Research current GFM capabilities via `WebSearch` before writing.
2. **Support future Word export** — use standard GFM syntax that pandoc handles cleanly. Avoid raw HTML except `<details>` for collapsible sections.
3. **Render Mermaid diagrams natively** — GitHub renders ` ```mermaid ` code blocks as diagrams. Use this for all architecture diagrams.
4. **Use GFM features**: tables, task lists, footnotes, fenced code blocks.
5. **For callouts**: use `> **Note:** ...` instead of `> [!NOTE]` — the alert syntax renders on GitHub but pandoc exports it as plain blockquote, losing the styling. Bold-prefixed blockquotes work in both.
6. **Avoid**: `<details>`/`<summary>` (stripped by pandoc), inline HTML tables (use GFM pipe tables), raw `<img>` tags (use `![alt](url)`), LaTeX math (spell out equations or use code blocks).
7. **Document size**: keep the final deliverable under 300 KB for reliable GitHub rendering. GitHub truncates README rendering at 512 KB; blob view handles ~1 MB but degrades.

---

## Phase Definitions

Write each phase as a standalone planning prompt file to `.claude/plans/cvs-engagement/`. Each file must be self-contained — executable without referencing this meta-prompt.

**Every phase plan must open with**: `Use ultrathink for this phase. Engage extended reasoning before every major output.`

**Every phase plan must include a web research directive**: `Perform deep web research using WebSearch before making any technical claims. Cite all sources with URLs. Cross-validate across multiple sources.`

### Phase 0: Research and Requirements Foundation

**File**: `.claude/plans/cvs-engagement/phase-0-research-and-requirements.md`

**Objective**: Deep research on IBMi/AS/400, green screen modernization patterns, CVS Health's technology ecosystem, and healthcare UI/UX — then extract and organize all requirements from the assignment, Paul's answers, and research findings.

**This phase must**:

1. Perform thorough web research on (use `WebSearch` for each topic cluster — do not rely on training data):
   - IBMi (AS/400) systems: architecture, green screen applications (5250 terminals), RPG/COBOL, modernization approaches, common integration patterns, current vendor ecosystem (IBM, Rocket Software, Fresche, etc.)
   - Why IBMi systems persist in 2026: reliability, transaction throughput, cost of replacement — Paul genuinely didn't know why these systems are still in production. This research informs his honest framing.
   - Green screen modernization case studies in healthcare and pharmacy specifically
   - CVS Health's current technology stack, recent AI/digital initiatives, Health100 platform, Google Cloud partnership, pharmacy technology systems
   - CVS Health's IBMi/AS/400 footprint — what is publicly known about their legacy systems
   - Healthcare UX best practices, WCAG accessibility standards, CVS brand guidelines
   - Identity and Access Management in healthcare: HIPAA requirements, modern IAM platforms, identity federation
   - Industry frameworks: TOGAF, AWS Well-Architected, GCP Architecture Framework, NIST, Zero Trust
   - Use Case 2 context: extract insights about CVS's domain-based architecture direction, legacy service layer challenges, integration patterns, and multi-cloud strategy preferences
2. Compile a **requirements analysis document** capturing:
   - Functional requirements (what the system must do)
   - Non-functional requirements (performance, security, accessibility, compliance)
   - User stories for key personas (pharmacy tech, pharmacist, store manager, IT admin, end customer)
   - Assumptions — clearly numbered, each with rationale, each flagged for confirmation
   - Open questions — organized by key consideration topic so Paul can ask the right panel member. The assignment is intentionally vague — Paul believes they want to see how he asks questions.
   - Success criteria with measurable KPIs
3. Run `/requirements` skill (comprehensive tier) with the compiled context to produce `knowledge_base/requirements.json`
4. Run `/review requirements.json` to validate completeness

**Quality gate**: Requirements must score >= 7.5 on review before proceeding.

**Output**: Research findings document + `knowledge_base/requirements.json` + requirements review

---

### Phase 1: Business Workflow and User Experience Design

**File**: `.claude/plans/cvs-engagement/phase-1-ux-and-workflow-design.md`

**Objective**: Design the human-centered business workflows and user experience that will inform all technical decisions. This is the people-and-process layer.

**Paul's HCD credibility**: Paul holds a BS in Cognitive Science with a focused foundation in Artificial Intelligence from UGA. He studied Human-Computer Interaction formally. This phase should leverage that academic foundation while updating it with current research.

**This phase must**:

1. Map current-state business workflows for green screen applications (based on research from Phase 0)
2. Design future-state workflows showing how users transition from green screen to modern UI
3. Define key user personas with goals, pain points, and success criteria
4. Apply HCD principles — web search and cite the latest as of March 2026:
   - Nielsen Norman Group heuristics
   - IDEO Human-Centered Design framework
   - W3C WCAG 2.2 accessibility guidelines
   - CVS Health's own published UX/design philosophy (research this)
   - Google Material Design and healthcare-specific design systems
5. Create UX design artifacts:
   - User journey maps for migration and steady-state usage
   - Information architecture showing navigation and task flows
   - Wireframe descriptions for key screens (keep generic but directly relevant)
   - Design system principles (typography, color informed by CVS brand, component patterns)
6. Document all UX design decisions with rationale
7. Design for the best-practice combination of conversational UI and traditional GUI — use chat/agent interfaces only where they genuinely improve the experience

**Important constraints**:

- Do NOT invent specific CVS internal systems or data — everything must be publicly sourced or framed as an assumption
- Prioritize accessibility and usability over visual flair
- Reference Paul's guiding principles: augment humans (#1), sustainable flourishing (#2), individual flow (#4), easy-to-remember flows (#6)

**Output**: UX and workflow design document with journey maps, wireframe descriptions, and design principles

---

### Phase 2: Solution Architecture and Technical Design

**File**: `.claude/plans/cvs-engagement/phase-2-solution-architecture.md`

**Objective**: Design the complete solution architecture — current state, transition state, and future state — with technology stack selection, component design, and system diagrams.

**This phase must**:

1. Run `/integration-plan` first (this is a migration engagement):
   - Document IBMi integration patterns and legacy bridging approach
   - Define migration strategy (strangler fig recommended — validate with web research and cite sources)
   - Map API contracts between legacy and modern systems
   - Design CI/CD pipeline architecture
2. Run `/architecture` to produce the full solution architecture:
   - Current-state architecture diagram (IBMi/AS/400 + green screen) — based on publicly available information and clearly labeled assumptions
   - Future-state architecture diagram (modern stack)
   - Transition architecture showing how both coexist during migration
   - Technology stack with rationale per layer (GCP as primary given CVS-Google partnership, with multi-cloud awareness)
   - Component design with IDs, dependencies, and scalability approach
   - Data flow diagrams
   - Well-Architected scoring across all 6 AWS pillars + GCP Architecture Framework cross-reference
   - Executive summary for business stakeholders
3. Present **multiple solution options** with pros/cons (the assignment explicitly requires this):
   - Option A: Screen-scraping/wrapping approach (quick, limited)
   - Option B: API-first modernization with strangler fig (balanced)
   - Option C: Full re-platform to cloud-native (comprehensive, higher investment)
   - For each: feasibility, scalability, maintainability, alignment with CVS strategic direction
4. Run `/data-model` for data layer design
5. Run `/review architecture.json` to validate

All Mermaid diagrams must use ` ```mermaid ` fencing for native GitHub rendering.

**Key technical considerations**:

- CVS uses Google Cloud primarily — GCP services should be the default recommendation, with justification for any alternatives. Cite GCP documentation.
- IBMi modernization has specific vendor tooling (web search: Rocket Software, Fresche Legacy, IBM Rational) — acknowledge and evaluate
- Streaming platforms (Kafka, Pulsar) for integration layers between modern and legacy (per job requirements)
- AI/ML components: where does GenAI/LLM fit in the modernization? (Consider: automated code translation, intelligent form completion, conversational help, predictive workflows)
- Domain-Driven Design and microservices (per job requirements) — show how business domains map to services

**Output**: `knowledge_base/integration_plan.json` + `knowledge_base/architecture.json` + `knowledge_base/data_model.json` + architecture review + Mermaid diagrams

---

### Phase 3: Security, IAM, and Compliance

**File**: `.claude/plans/cvs-engagement/phase-3-security-and-iam.md`

**Objective**: Comprehensive security architecture with emphasis on IAM strategy — this is one of the 5 key considerations the panel will evaluate. A dedicated panel member will drill Paul on IAM specifically.

**Paul's security credibility**: AI governance and data security at Booz Allen (FedRAMP/HIPAA-compliant AI delivery, algorithmic bias mitigation), COINSTAC differential privacy, Hyperbloom blockchain-based data platform with CCPA/GDPR/HIPAA compliance. Paul has worked *within* IAM frameworks but has not designed one from scratch — this phase fills that gap through research.

**This phase must**:

1. Run `/security-review` with healthcare compliance context (HIPAA, SOC2, PCI-DSS, HITRUST):
   - STRIDE threat model across all components
   - Defense-in-depth architecture (5 layers)
   - AI-specific security controls
   - Compliance mapping with posture assessment
2. Design a detailed **IAM strategy** (this gets special attention per the assignment):
   - Authentication architecture: SSO, MFA, session management for pharmacy workers
   - Authorization model: RBAC/ABAC for different user roles across legacy and modern systems
   - Identity federation: bridging legacy IBMi user profiles to modern identity provider
   - Privileged access management for admin and system accounts
   - Service-to-service identity for microservices
   - Zero Trust architecture principles applied to this specific use case
   - Cite and leverage: NIST SP 800-63, NIST Cybersecurity Framework, MITRE ATT&CK, OWASP
   - All IAM claims must be sourced from current vendor documentation and framework standards — no unsourced assertions
3. Document security-specific design decisions with rationale, citing Paul's relevant Booz Allen and COINSTAC experience where applicable
4. Run `/review security_review.json` to validate

**Output**: `knowledge_base/security_review.json` + IAM strategy document + security review

---

### Phase 4: Estimation, Team Composition, and Project Plan

**File**: `.claude/plans/cvs-engagement/phase-4-estimation-and-planning.md`

**Objective**: Realistic effort estimation, lean team composition, and phased delivery roadmap.

**This phase must**:

1. Run `/estimate` to produce:
   - LOE breakdown by phase using **T-shirt sizes** (S/M/L/XL) — do NOT generate time estimates in days/weeks/months
   - Cloud cost model — **MANDATORY**: cite all inputs, write out the equations AND proofs that they are correct, verify pricing is current as of March 2026, and reference the specific GCP/cloud pricing calculator pages used. If pricing data cannot be verified as current, flag it explicitly.
   - Team composition — keep lean and realistic, do not over-staff
   - Confidence scoring per estimate component (HIGH/MEDIUM/LOW with rationale)
2. Run `/project-plan` to produce:
   - Phased delivery roadmap with sprint plans
   - Decision gates between phases
   - Risk register (technical, resource, timeline)
   - Critical path analysis
   - Communication and change management plan (per key consideration: Change Management)
   - Milestone definitions with measurable success criteria
3. Integrate change management throughout the project plan — Paul's Mento coaching experience is directly relevant:
   - Training program for users transitioning from green screen
   - Communication cadence for all stakeholder personas
   - Feedback mechanisms and iteration cycles
   - Phased rollout strategy (small group → percentage-based → full)
   - Legacy system maintenance and DR plan during transition
   - Behavioral change frameworks (cite research — Paul's instinct is to leverage psychology and behavioral neuroscience)
4. Run `/review` on both estimate and project plan

**Output**: `knowledge_base/estimate.json` + `knowledge_base/project_plan.json` + reviews

---

### Phase 5: Deliverable Assembly and Quality Assurance

**File**: `.claude/plans/cvs-engagement/phase-5-deliverable-assembly.md`

**Objective**: Assemble all phase outputs into a cohesive, panel-ready document formatted for GitHub rendering and future Word export.

**This phase must**:

1. Run `/review` on ALL knowledge base files as a final quality pass
2. Assemble the consolidated deliverable document with these sections:
   - **Executive Summary** — 1-page overview: problem, approach, recommendation, key differentiators
   - **Clarifying Questions** — organized by key consideration, demonstrating SA depth (the assignment says to ask questions at the beginning)
   - **Requirements Analysis** — functional/non-functional requirements, user stories, assumptions (numbered), open questions for panel
   - **User Experience Design** — personas, journey maps, wireframe descriptions, design principles, HCD methodology with Paul's Cognitive Science background
   - **Solution Architecture** — current state, future state, transition approach, multiple options with pros/cons, technology stack with rationale, Mermaid diagrams, data flow, component design
   - **Security and IAM Strategy** — threat model summary, defense-in-depth, IAM architecture, compliance posture, Zero Trust application
   - **AI-Assisted Methodology** — dedicated section showing the human-AI workflow (see Phase 7 for full spec)
   - **Team Composition** — lean team with roles, responsibilities, effort in T-shirt sizes
   - **Technical Project Plan** — phased roadmap, milestones, risk register, change management plan, communication strategy
   - **Assumptions Register** — consolidated numbered list of all assumptions made throughout, each flagged for confirmation
   - **References** — all sources cited throughout the document, formatted as a bibliography
3. Apply quality constraints:
   - Elegant and minimalistic — do NOT overwhelm the reader
   - Grounded in truth — every claim has a verified citation from an authoritative source or is flagged as assumption
   - Easy to read by average engineers — explain jargon, use clear headings, keep paragraphs short
   - Written in Paul's voice (collaborative, solution-focused, confidence without arrogance, value-first, empirical)
   - Formatted in GitHub Flavored Markdown that renders natively on github.com
   - All diagrams in Mermaid ` ```mermaid ` blocks (native GitHub rendering)
   - NOT over-engineered — calibrate to a document that supports a 15-20 minute presentation per key consideration, with enough depth to survive panel drilling
4. Validate against the assignment's **Expectations and Tips** (the panel expects these):
   - A clear understanding of the challenges posed by legacy systems and how to address them
   - A comprehensive IAM strategy that includes user authentication, authorization, and role management
   - A commitment to HCD principles, including user research, prototyping, and usability testing
   - A well-defined technology stack that leverages modern frameworks while ensuring compatibility with legacy systems
   - A change management plan that includes training, support, and communication strategies to facilitate user transition
5. Apply **3 SA review personas** for final validation:
   - **Enterprise Architect** (like the hiring manager): evaluates strategic alignment, scalability, business value
   - **Security Architect**: evaluates IAM, compliance, threat model rigor
   - **UX/HCD Specialist**: evaluates user-centeredness, accessibility, change management
   - Each persona reviews, provides feedback, and the document is iterated upon
6. Produce the final consolidated Markdown document

**Output**: `outputs/cvs-legacy-transformation/solution-architecture-document.md` + review results

---

### Phase 6: Interview Preparation

**File**: `.claude/plans/cvs-engagement/phase-6-interview-prep.md`

**Objective**: Prepare Paul to confidently present and defend every design decision across multiple panel drill sessions.

**This is Paul's eyes only — NOT part of the deliverable shared with interviewers.**

**This phase must**:

1. Create a **presentation script** (15-20 minutes):
   - Opening: 2-minute hook — problem statement, why this matters to CVS
   - Solution overview: 3-minute high-level flow with key diagram
   - Deep dives: 8-minute tour of architecture, IAM, UX, and migration approach — hitting all 5 key considerations
   - Options analysis: 3-minute comparison of approaches with recommendation
   - Close: 2-minute team, timeline, and next steps
   - Timing markers throughout
2. Create a **technology study guide** covering every technology and design pattern in the solution — Paul needs this because he is learning IBMi/AS/400 from scratch:
   - IBMi/AS/400: what it is, how green screens work (5250 protocol), RPG/COBOL basics, why these systems persist, modern integration options — enough depth to answer "tell me about your understanding of IBMi" confidently
   - GCP services in the solution: what each does, why it was chosen, AWS equivalent Paul already knows
   - Every design pattern used: strangler fig, anti-corruption layer, Zero Trust, etc.
   - Key frameworks referenced: TOGAF, Well-Architected, NIST, STRIDE
   - For each technology: what it does, why it was chosen, alternatives considered, and how it maps to Paul's existing experience
3. Create an **anticipated Q&A document** — organized by key consideration (since each panel member drills one topic):
   - 25+ likely questions per key consideration
   - For each: the question, a concise answer, supporting evidence, and a pivot to Paul's actual experience
   - Include tough/adversarial questions: "Why not just screen-scrape?", "How do you handle 99.99% uptime during migration?", "What's your rollback plan if the new IAM breaks?", "How do you convince pharmacy techs to adopt this?", "You don't have IBMi experience — why should we trust this design?", "Your background is AWS — why are you recommending GCP?"
   - Questions Paul should ask the panel — demonstrates engagement and expertise, organized by topic
4. Create a **talking points cheat sheet**:
   - Key metrics and numbers to cite
   - CVS-specific context to reference (Health100, Google partnership, recent initiatives)
   - Paul's relevant experience mapped to each key consideration, with specific role and project references
   - Phrases and framing that match the hiring manager's language (enterprise scale, revenue impact, cross-functional teams)
   - Honest framing for gap areas: how to discuss IBMi learning, GCP transition, IAM design experience

**Output**: `private/interview-prep/` directory with presentation script, study guide, Q&A document, and cheat sheet

---

### Phase 7: AI-Assisted Methodology and Portfolio Documentation

**File**: `.claude/plans/cvs-engagement/phase-7-ai-methodology-and-citation.md`

**Objective**: Document how Paul used AI tooling (Claude Code + this SA Agent) throughout the assignment, position it as a professional differentiator, and produce portfolio-worthy documentation of the process.

**Why this matters**: CVS expects AI-first development. Paul built an AI agent that designed this system with a human in the loop. This is not just a footnote — it demonstrates exactly the kind of technology incubation and emerging tech evaluation the Principal Architect role demands.

**This phase must**:

1. Write a **dedicated section for the deliverable document** (inserted as "AI-Assisted Methodology" section) covering:
   - The SA Agent: what it is, how it works, that Paul built it as an open-source Claude Code plugin
   - The human-AI workflow: how Paul directed the agent through each phase, set strategic direction through prompting, reviewed and iterated on every output, and made all final decisions
   - Phase-by-phase breakdown of human vs. AI contributions — Paul set direction and reviewed; AI executed research, structured output, and validated quality
   - How this approach embodies the role's requirements: technology incubation, emerging tech evaluation, AI/ML architecture, automation frameworks
   - Honest limitations: what the AI got wrong, what Paul corrected, where human judgment was essential

2. Produce **LLM citations** following standard academic/professional citation formats:
   - In-text: `(Claude Opus 4, Anthropic, 2026, via Claude Code CLI v2.1.75)`
   - Bibliography entry:
     ```
     Anthropic. (2026). Claude Opus 4 [Large language model]. https://www.anthropic.com/claude
     Accessed via Claude Code CLI v2.1.75. https://docs.anthropic.com/en/docs/claude-code
     ```
   - SA Agent citation:
     ```
     Prae, P. (2026). Solutions Architecture Agent (v1.0.0) [Claude Code plugin].
     Modular Earth LLC. https://github.com/Modular-Earth-LLC/solutions-architecture-agent
     ```

3. Write a **portfolio-ready summary** (for Paul's resume and GitHub profile):
   - 3-5 bullet points describing what was built and the outcome
   - Framed in STAR format (Situation → Task → Action → Result) per Paul's writing formulas
   - Quantified where possible: number of skills, validation checks, phases executed
   - Suitable for LinkedIn, resume, and the repo's README

4. Write a **"How I Built the AI Agent That Designed This System"** narrative section:
   - The SA Agent's development story: 9 phases of development, 9 skills, 2 sub-agents, 11 JSON schemas, 57 automated validation checks
   - Architecture decisions: single-agent with skills (not multi-agent), blackboard pattern for knowledge base, Well-Architected scoring on every design
   - Human-in-the-loop throughout: Paul set every architectural direction, reviewed every output, iterated on quality
   - Open-source commitment: MIT licensed, designed as a Claude Code plugin for other Solutions Architects to use
   - Link to the repo: https://github.com/Modular-Earth-LLC/solutions-architecture-agent

5. Integrate citations and the methodology section into the Phase 5 deliverable document

**Output**: AI methodology section for deliverable + LLM citations + portfolio summary + narrative

---

## Output Structure

Write the master plan and all phase plans to these paths:

```text
.claude/plans/cvs-engagement/
├── master-plan.md                          ← The master plan (overview + phase index)
├── phase-0-research-and-requirements.md    ← Standalone planning prompt
├── phase-1-ux-and-workflow-design.md       ← Standalone planning prompt
├── phase-2-solution-architecture.md        ← Standalone planning prompt
├── phase-3-security-and-iam.md             ← Standalone planning prompt
├── phase-4-estimation-and-planning.md      ← Standalone planning prompt
├── phase-5-deliverable-assembly.md         ← Standalone planning prompt
├── phase-6-interview-prep.md               ← Standalone planning prompt
└── phase-7-ai-methodology-and-citation.md  ← Standalone planning prompt
```

Each phase file must:

- Open with `Use ultrathink for this phase. Engage extended reasoning before every major output.`
- Include `Perform deep web research using WebSearch before making any technical claims. Cite all sources with URLs. Cross-validate across multiple sources.`
- Be a complete, self-contained prompt executable in Claude Code CLI with the SA Agent plugin loaded
- Reference specific skill invocations (e.g., "Run `/requirements` with the following context...")
- List input dependencies (which files/artifacts from prior phases are needed)
- Include all relevant file paths from the Context Loading section that the phase needs
- Define the quality gate and exit criteria
- End with a human checkpoint asking Paul to review before proceeding

The **master plan** file should:

- Open with an executive summary of the entire approach
- Include a Mermaid dependency graph showing phase relationships
- Define the interaction model (plan → review → iterate → execute → next phase)
- Describe the scope of each phase using relative complexity (not time estimates)
- List all assumptions made during planning
- Include a consolidated list of all files that need to be read across all phases

---

## Quality Constraints

Apply these constraints across ALL phase plans:

### Research Standards

- **Web research is mandatory** — use `WebSearch` for every technology, framework, pattern, and CVS Health claim. Do not rely on training data for factual claims.
- Cite authoritative sources: vendor documentation, NIST, OWASP, peer-reviewed research, official CVS Health publications
- Cross-validate claims across multiple sources — do not trust a single source
- Flag anything Paul is unfamiliar with (IBMi, green screens, RPG/COBOL, GCP specifics, RPA platforms) for extra research depth and fact-checking, as he cannot catch hallucinations in unfamiliar domains
- Every citation must include a working URL

### Design Standards

- Apply the 42 guiding principles from `.claude/rules/guiding-principles.md`
- Apply AWS Well-Architected Framework (6 pillars) and GCP Architecture Framework to all architecture decisions
- Follow KISS — good design is less design
- Ensure all UX includes best-practice combination of conversational UI and GUI
- Design for accessibility (WCAG 2.2 AA minimum)

### Output Standards

- Elegant and minimalistic — every section must deliver tangible value, no filler
- Grounded in truth with verified citations
- Easy to read and understand by average engineers
- Written in Paul's voice: collaborative, solution-focused, confidence without arrogance, value-first, empirical, professional warmth. Use the Before-After-Bridge and Problem-Agitate-Solve writing formulas where appropriate.
- GitHub Flavored Markdown that renders natively on github.com with Mermaid diagrams
- NOT over-engineered — calibrate depth to survive panel drilling on each key consideration, not a 200-page RFP response

### Honesty and Authenticity

- Do not accept Paul's initial answers uncritically — research and improve upon them
- Where Paul's instincts are strong, validate and deepen with evidence
- Where Paul's instincts have gaps, fill them with researched best practices and frame honestly
- Every claim in the final document must be something Paul can confidently speak to, grounded in either his direct experience or his documented research for this assignment
- Present alternative perspectives where relevant

---

## Interaction Model

Before writing any plans, ask Paul clarifying questions to fill gaps. Organize questions into:

1. **Must-answer before planning** — questions that change the plan structure
2. **Can answer during execution** — questions that refine individual phase outputs
3. **Questions for interviewers** — questions to include in the deliverable's open questions section (generate these — Paul will add his own later)

After gathering answers, write all phase plans and the master plan to `.claude/plans/cvs-engagement/`.

---

## Ultimate Success Criteria

The plans you write must, when executed, produce deliverables that:

1. **Prove Paul can do the job** — demonstrate principal-level architecture thinking, not junior implementation detail. Show he can lead both the solution architecture AND guide the data scientists who build within it.
2. **Earn trust of the hiring panel** — a 20-year veteran engineering leader and panel of architects must find the work credible and impressive
3. **Show AI-first thinking** — CVS expects AI-first development; Paul built an AI agent to design this system, demonstrating exactly the technology incubation the role demands
4. **Differentiate Paul** — leverage his strengths in AI governance, data security, human-centered design (Cognitive Science degree), healthcare domain expertise, and coaching/change management experience
5. **Stay grounded** — no hand-waving, no buzzword soup, no over-engineering; every decision justified by evidence and business value
6. **Be honest** — transparent about what Paul knew, what he researched, what he assumes. This authenticity builds trust with a senior panel.
