# Meta-Planning Prompt: CVS Health Legacy System Transformation

> **What this prompt does**: Generates a master plan of phase-specific planning prompts, each written to `.claude/plans/` as standalone files that Paul and the agent will execute together, one phase at a time.
>
> **How to run**: Enter plan mode in Claude Code CLI, then paste or reference this prompt.

---

## Mission

You are a distinguished engineer and principal AI/LLM solutions architect. Your mission is to create a **master plan of planning prompts** — a series of phase plans that, when executed sequentially, will produce a complete solution architecture for the CVS Health Legacy System Transformation case study (Use Case 1).

**Critical framing**: You are NOT executing the assignment. You are designing the plan that will guide execution across multiple sessions. Each phase plan you write will be sent to Claude Code as a standalone planning prompt that Paul and the agent will iteratively review, improve, and execute together.

**This is a meta-task**: research → analyze → architect an approach → write planning prompts for later execution.

---

## Context Loading

### Assignment Source

Read and deeply analyze: `.claude/plans/references/solution-architect-case-study-and-interview.md`

Paul has selected **Use Case 1: Legacy System Transformation (SELECTED)** — modernizing IBMi (AS/400) green screen applications with new UI/UX while addressing Legacy System Integration, IAM Strategy, HCD Design Principles, Technology Stack, and Change Management.

**Use Case 2: Transitioning to a Domain-Based Architecture (NOT SELECTED)** is retained in the reference file as organizational context. It reveals CVS Health's broader technology direction — domain-based architecture, Domain-Driven Design, legacy service layer consolidation, cloud migration patterns, and multi-platform strategy. Use it to inform architectural decisions but do not solve it.

### Interview Format

- 15-20 minute presentation + Q&A from a panel of architects
- 6 interview expectations (per the assignment):
  1. **High-Level Solution Flow** — present an overview of key components and how they interrelate
  2. **Clarification and Questions** — ask questions at the beginning to clarify requirements and constraints
  3. **Diagram Development** — create and discuss visual representations of the architecture
  4. **Multiple Solution Options** — explore multiple options with pros/cons (feasibility, scalability, maintainability, business alignment)
  5. **Thought Process Articulation** — explain rationale behind design choices, integration strategies, and how they address key considerations
  6. **Focus on Key Considerations** — address all 5 key considerations from Use Case 1
- 5 key considerations to address:
  1. **Legacy System Integration** — seamless integration with existing green screen applications, minimizing disruption to current operations
  2. **IAM Strategy** — robust Identity and Access Management with compliance to industry standards
  3. **HCD Design Principles** — Human-Centered Design throughout, with user feedback and iterative design
  4. **Technology Stack** — balancing modern technologies with legacy system constraints
  5. **Change Management** — managing user transition, adoption, and minimizing resistance

### Target Audience

The hiring manager's profile (calibrate technical depth and language to this level):

> 20+ years of software engineering experience. Leads large-scale projects and global cross-functional teams to deliver digital transformation, complex solutions, and enterprise architectures supporting multi-billion-dollar revenue streams. Core competencies: software development and system design, team leadership, business outcomes alignment, software infrastructure and security, technology trends evaluation. Has developed and managed a $50M+ digital platform using cloud technologies and Microservices Architecture, established RESTful API platform compliant with TMForum industry standard, managed 5+ mission-critical systems generating $1.2B+ revenue, and consolidated and decommissioned 7+ applications.

The role Paul is interviewing for: **Principal Architect, Solution Engineering and Automation** — responsible for end-to-end solution architecture, technology incubation, emerging tech evaluation, AI/ML architecture, automation frameworks, and mentoring. The full job description is embedded in the assignment source file.

### CVS Health Strategic Context

CVS Health is investing heavily in AI as a core driver of digital health:

- Partnered with Google Cloud to launch **Health100**, an AI-enabled consumer engagement platform
- Uses Gemini models, Cloud Healthcare API, and BigQuery across payor, pharmacy, provider ecosystems
- Already embeds AI in pharmacy ops, benefits admin, and clinical workflows
- Recently published work on generative agents for care experience testing
- Positioning as an AI-powered health engagement platform provider, not just retailer/insurer
- Key tech partnerships: Google Cloud (primary), Databricks, DataRobot

For current context, perform deep web research on CVS Health's technology strategy, recent announcements, and digital transformation initiatives as of March 2026. Verify all citations.

### Paul's Background and Perspective

Read these files to understand Paul's voice, expertise, and personal brand — all deliverables must sound like him:

**Brand and voice** (read all):

- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\data\sources\knowledge\brand\identity.json`
- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\data\sources\knowledge\brand\communication-styles.json`
- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\data\sources\knowledge\brand\values.json`
- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\data\sources\knowledge\content\writing-formulas.json`

**Career context** (read for relevant experience to reference):

- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\data\generated\career-data.json`
- `\\wsl.localhost\Ubuntu\home\praeducer\dev\paulprae-com\lib\prompts\resume-writer.system.md`
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

Only reference Paul's previous work where highly relevant to CVS Health and this assignment. Do not force connections.

### Paul's Key Considerations Answers

Incorporate, challenge, and improve upon Paul's initial answers to the assignment's 5 key considerations. These represent his instincts — the plans should validate, deepen, and augment them with research:

1. **Legacy System Integration**: Bring in SMEs and real users for UX/UI collaboration. Partner with legacy system maintainers. The interface swap needs API, networking, and security components the legacy system lacks. Consider local-first apps targeting laptops and mobile. To minimize disruption: fork the backend to avoid downtime, implement multi-stage environments (local dev, QA, UAT, prod, DR), phased rollout (small UAT group → percentage-based production rollout → full swap), maintain legacy with DR plan for rollback. Communication and collaboration are key.

2. **IAM Strategy**: Follow standard frameworks and vendor guidance. Use AWS/Microsoft Well-Architected security reviews. Leverage NIST and MITRE guidance. Penetration testing and e2e testing are the most effective security hardening steps. Use platform-specific IAM audit tools.

3. **HCD Design Principles**: Paul studied HCI in college. Research the latest HCD best practices as of March 2026. Study the CVS brand to inform visual design. Ensure accessibility. Research what CVS Health and their technology partners say about HCD specifically.

4. **Technology Stack**: Prefer AI-native managed services from next-gen cloud platforms (see Paul's recent projects above). Balance technical debt, implementation speed, platform constraints, preferred vendor tooling, and peer preferences. Argue for future-proofing with proven, reliable tools.

5. **Change Management**: Extensive communication. Receptive to feedback and pivots. Announce migration ahead of design. Identify all stakeholder personas and design change management specifically for them. Play into emotions, psychology, behavioral neuroscience, and organizational politics.

### Agent Capabilities

This repo has 9 skills that map to the solutions architecture lifecycle. Each phase plan should reference the relevant skill for execution:

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

The `/review` skill should also be invoked after each major phase to validate quality before proceeding.

### Guiding Principles

Read and apply: `.claude/rules/guiding-principles.md` — 34 technology principles that govern all work in this repo. Key principles for this assignment: human-centered design (#1-8), KISS (#10), separation of concerns (#11), anticipate failure (#16), ship (#17), Zero Trust security (#18-20), ground AI in truth (#22), automate everything (#28), build local-first (#30), no dark patterns (#33).

---

## Phase Definitions

Write each phase as a standalone planning prompt file to `.claude/plans/`. Each file must be self-contained — executable without referencing this meta-prompt.

### Phase 0: Research and Requirements Foundation

**File**: `.claude/plans/phase-0-research-and-requirements.md`

**Objective**: Deep research on IBMi/AS/400, green screen modernization patterns, CVS Health's technology ecosystem, and healthcare UI/UX — then extract and organize all requirements from the assignment, Paul's answers, and research findings.

**This phase must**:

1. Perform thorough web research on:
   - IBMi (AS/400) systems: architecture, green screen applications, modernization approaches, common integration patterns, current vendor ecosystem (IBM, Rocket Software, Fresche, etc.)
   - Green screen modernization case studies in healthcare and pharmacy
   - CVS Health's current technology stack, recent AI/digital initiatives, Health100 platform, Google Cloud partnership
   - Healthcare UX best practices, WCAG accessibility standards, CVS brand guidelines
   - Identity and Access Management in healthcare: HIPAA requirements, modern IAM platforms
   - Industry frameworks: TOGAF, AWS Well-Architected, NIST, Zero Trust
   - Use Case 2 (not selected, but retained for context): extract insights about CVS's domain-based architecture direction, legacy service layer challenges, integration patterns, and multi-cloud strategy preferences
2. Compile a **requirements analysis document** capturing:
   - Functional requirements (what the system must do)
   - Non-functional requirements (performance, security, accessibility, compliance)
   - User stories for key personas (pharmacy tech, pharmacist, store manager, IT admin, end customer)
   - Assumptions — clearly stated with rationale
   - Open questions — curated into a single list Paul can ask his interviewers
   - Success criteria with measurable KPIs
3. Run `/requirements` skill with the compiled context to produce `knowledge_base/requirements.json`
4. Run `/review requirements.json` to validate completeness

**Quality gate**: Requirements must score PASS (>= 7.5) on review before proceeding.

**Output**: Research findings document + `knowledge_base/requirements.json` + requirements review

---

### Phase 1: Business Workflow and User Experience Design

**File**: `.claude/plans/phase-1-ux-and-workflow-design.md`

**Objective**: Design the human-centered business workflows and user experience that will inform all technical decisions. This is the people-and-process layer.

**This phase must**:

1. Map current-state business workflows for green screen applications (based on research from Phase 0)
2. Design future-state workflows showing how users transition from green screen to modern UI
3. Define key user personas with goals, pain points, and success criteria
4. Apply HCD principles — research and cite the latest as of March 2026:
   - Nielsen Norman Group heuristics
   - IDEO Human-Centered Design framework
   - W3C WCAG 2.2 accessibility guidelines
   - CVS Health's own published UX/design philosophy (research this)
5. Create UX design artifacts:
   - User journey maps for migration and steady-state usage
   - Information architecture showing navigation and task flows
   - Wireframe descriptions for key screens (keep generic but directly relevant)
   - Design system principles (typography, color informed by CVS brand, component patterns)
6. Document all UX design decisions with rationale
7. Design for the best-practice combination of conversational UI and traditional GUI — use chat/agent interfaces only where they genuinely improve the experience

**Important constraints**:

- Do NOT invent specific CVS internal systems or data — keep generalized but relevant
- Prioritize accessibility and usability over visual flair
- Reference Paul's guiding principles: augment humans (#1), sustainable flourishing (#2), individual flow (#4), easy-to-remember flows (#6)

**Output**: UX and workflow design document with journey maps, wireframes descriptions, and design principles

---

### Phase 2: Solution Architecture and Technical Design

**File**: `.claude/plans/phase-2-solution-architecture.md`

**Objective**: Design the complete solution architecture — current state, transition state, and future state — with technology stack selection, component design, and system diagrams.

**This phase must**:

1. Run `/integration-plan` first (this is a migration engagement):
   - Document IBMi integration patterns and legacy bridging approach
   - Define migration strategy (strangler fig recommended — validate with research)
   - Map API contracts between legacy and modern systems
   - Design CI/CD pipeline architecture
2. Run `/architecture` to produce the full solution architecture:
   - Current-state architecture diagram (IBMi/AS/400 + green screen)
   - Future-state architecture diagram (modern stack)
   - Transition architecture showing how both coexist during migration
   - Technology stack with rationale per layer (must consider GCP as primary given CVS-Google partnership, with multi-cloud awareness)
   - Component design with IDs, dependencies, and scalability approach
   - Data flow diagrams
   - Well-Architected scoring across all 6 pillars
   - Executive summary for business stakeholders
3. Present **multiple solution options** with pros/cons (the assignment explicitly requires this):
   - Option A: Screen-scraping/wrapping approach (quick, limited)
   - Option B: API-first modernization with strangler fig (balanced)
   - Option C: Full re-platform to cloud-native (comprehensive, higher investment)
   - For each: feasibility, scalability, maintainability, alignment with CVS strategic direction, cost range, timeline range
4. Run `/data-model` for data layer design
5. Run `/review architecture.json` to validate

**Key technical considerations**:

- CVS uses Google Cloud primarily — GCP services should be the default recommendation, with justification for any alternatives
- IBMi modernization has specific vendor tooling (research: Rocket Software, Fresche Legacy, IBM Rational) — acknowledge and evaluate
- Streaming platforms (Kafka, Pulsar) for integration layers between modern and legacy (per job requirements)
- AI/ML components: where does GenAI/LLM fit in the modernization? (Consider: automated code translation, intelligent form completion, conversational help, predictive workflows)
- Domain-Driven Design and microservices (per job requirements) — show how business domains map to services

**Output**: `knowledge_base/integration_plan.json` + `knowledge_base/architecture.json` + `knowledge_base/data_model.json` + architecture review + Mermaid diagrams

---

### Phase 3: Security, IAM, and Compliance

**File**: `.claude/plans/phase-3-security-and-iam.md`

**Objective**: Comprehensive security architecture with emphasis on IAM strategy — this is one of the 5 key considerations the panel will evaluate.

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
3. Document security-specific design decisions with rationale
4. Run `/review security_review.json` to validate

**Paul's strength**: AI governance, data security, data privacy — the security section should reflect deep expertise. This is where Paul differentiates himself.

**Output**: `knowledge_base/security_review.json` + IAM strategy document + security review

---

### Phase 4: Estimation, Team Composition, and Project Plan

**File**: `.claude/plans/phase-4-estimation-and-planning.md`

**Objective**: Realistic cost estimation, lean team composition, and phased delivery roadmap.

**This phase must**:

1. Run `/estimate` to produce:
   - LOE breakdown by phase (using three-point estimation)
   - Cost model (development + operational + AI-specific)
   - Team composition — keep lean and realistic, do not over-staff
   - Confidence scoring per estimate component
2. Run `/project-plan` to produce:
   - Phased delivery roadmap with sprint plans
   - Decision gates between phases
   - Risk register (technical, resource, timeline)
   - Critical path analysis
   - Communication and change management plan (per key consideration: Change Management)
   - Milestone definitions with measurable success criteria
3. Integrate change management throughout the project plan:
   - Training program for users transitioning from green screen
   - Communication cadence for all stakeholder personas
   - Feedback mechanisms and iteration cycles
   - Phased rollout strategy (small group → percentage-based → full)
   - Legacy system maintenance and DR plan during transition
4. Run `/review` on both estimate and project plan

**Output**: `knowledge_base/estimate.json` + `knowledge_base/project_plan.json` + reviews

---

### Phase 5: Deliverable Assembly and Quality Assurance

**File**: `.claude/plans/phase-5-deliverable-assembly.md`

**Objective**: Assemble all phase outputs into a cohesive, presentation-ready document.

**This phase must**:

1. Run `/review` on ALL knowledge base files as a final quality pass
2. Assemble the consolidated deliverable document with these sections:
   - **Executive Summary** — 1-page overview: problem, approach, recommendation, key differentiators
   - **Requirements Analysis** — functional/non-functional requirements, user stories, assumptions, open questions for interviewers
   - **User Experience Design** — personas, journey maps, wireframe descriptions, design principles, HCD methodology
   - **Solution Architecture** — current state, future state, transition approach, multiple options with pros/cons, technology stack with rationale, system diagrams (Mermaid), data flow, component design
   - **Security and IAM Strategy** — threat model summary, defense-in-depth, IAM architecture, compliance posture, Zero Trust application
   - **Team Composition** — lean team with roles, responsibilities, hiring priorities
   - **Technical Project Plan** — phased roadmap, milestones, risk register, change management plan, communication strategy
3. Apply quality constraints:
   - Elegant and minimalistic — do NOT overwhelm the reader
   - Grounded in truth — every claim has a verified citation from an authoritative source
   - Easy to read by average engineers — explain jargon, use clear headings, keep paragraphs short
   - Written in Paul's voice (informed by brand files)
   - Formatted in Markdown that exports cleanly to Microsoft Word
   - All diagrams in Mermaid format (renderable in Word via export tools)
   - NOT over-engineered — this is a 15-20 minute presentation, not a 200-page specification
4. Validate against the assignment's **Expectations and Tips** (the panel expects these):
   - A clear understanding of the challenges posed by legacy systems and how to address them
   - A comprehensive IAM strategy that includes user authentication, authorization, and role management
   - A commitment to HCD principles, including user research, prototyping, and usability testing
   - A well-defined technology stack that leverages modern frameworks while ensuring compatibility with legacy systems
   - A change management plan that includes training, support, and communication strategies to facilitate user transition
5. Invent and apply **3 SA review personas** for final validation:
   - **Enterprise Architect** (like the hiring manager): evaluates strategic alignment, scalability, business value
   - **Security Architect**: evaluates IAM, compliance, threat model rigor
   - **UX/HCD Specialist**: evaluates user-centeredness, accessibility, change management
   - Each persona reviews, provides feedback, and the document is iterated upon
6. Produce the final consolidated Markdown document ready for Word export

**Output**: `outputs/cvs-legacy-transformation/solution-architecture-document.md` + review results

---

### Phase 6: Interview Preparation

**File**: `.claude/plans/phase-6-interview-prep.md`

**Objective**: Prepare Paul to confidently present and defend every design decision in a 15-20 minute presentation with Q&A.

**This is Paul's eyes only — NOT part of the deliverable shared with interviewers.**

**This phase must**:

1. Create a **presentation script** (15-20 minutes):
   - Opening: 2-minute hook — problem statement, why this matters to CVS
   - Solution overview: 3-minute high-level flow with key diagram
   - Deep dives: 8-minute tour of architecture, IAM, UX, and migration approach — hitting all 5 key considerations (Legacy System Integration, IAM Strategy, HCD Design Principles, Technology Stack, Change Management)
   - Options analysis: 3-minute comparison of approaches with recommendation
   - Close: 2-minute team, timeline, and next steps
   - Timing markers throughout
2. Create a **technology study guide** covering every technology and design pattern in the solution:
   - IBMi/AS/400: what it is, how green screens work, RPG/COBOL basics, modern integration options
   - Every technology in the recommended stack: what it does, why it was chosen, alternatives considered
   - Every design pattern used: strangler fig, anti-corruption layer, Zero Trust, etc.
   - Key frameworks referenced: TOGAF, Well-Architected, NIST, STRIDE
   - Enough depth that Paul can answer "why did you choose X over Y?" for any component
3. Create an **anticipated Q&A document**:
   - 20+ likely questions the panel will ask, organized by key consideration
   - For each: the question, a concise answer, supporting evidence, and a pivot to Paul's strengths
   - Include tough/adversarial questions: "Why not just screen-scrape?", "How do you handle 99.99% uptime during migration?", "What's your rollback plan if the new IAM breaks?", "How do you convince pharmacy techs to adopt this?"
   - Questions Paul should ask the panel (demonstrates engagement and expertise)
4. Create a **talking points cheat sheet**:
   - Key metrics and numbers to cite
   - CVS-specific context to reference (Health100, Google partnership, recent initiatives)
   - Paul's relevant experience to weave in naturally (from career data files)
   - Phrases and framing that match the hiring manager's language (enterprise scale, revenue impact, cross-functional teams)

**Output**: `private/interview-prep/` directory with presentation script, study guide, Q&A document, and cheat sheet

---

## Output Structure

Write the master plan and all phase plans to these paths:

```text
.claude/plans/
├── master-plan-cvs-legacy-transformation.md   ← The master plan (overview + phase index)
├── phase-0-research-and-requirements.md       ← Standalone planning prompt
├── phase-1-ux-and-workflow-design.md          ← Standalone planning prompt
├── phase-2-solution-architecture.md           ← Standalone planning prompt
├── phase-3-security-and-iam.md                ← Standalone planning prompt
├── phase-4-estimation-and-planning.md         ← Standalone planning prompt
├── phase-5-deliverable-assembly.md            ← Standalone planning prompt
└── phase-6-interview-prep.md                  ← Standalone planning prompt
```

Each phase file must:

- Be a complete, self-contained prompt that can be sent to Claude Code CLI
- Open with the phase objective and what it produces
- Reference specific skill invocations (e.g., "Run `/requirements` with the following context...")
- List input dependencies (which files/artifacts from prior phases are needed)
- Define the quality gate and exit criteria
- End with a human checkpoint asking Paul to review before proceeding

The **master plan** file should:

- Open with an executive summary of the entire approach
- Include a dependency graph showing phase relationships
- Define the interaction model (plan → review → iterate → execute → next phase)
- Estimate the scope of each phase (not time — just relative complexity)
- List all assumptions made during planning

---

## Quality Constraints

Apply these constraints across ALL phase plans:

### Research Standards

- Perform deep web research for every technology, framework, and pattern referenced
- Cite authoritative sources: vendor documentation, NIST, OWASP, peer-reviewed research, official CVS Health publications
- Cross-validate claims across multiple sources — do not trust a single source
- Flag anything Paul is unfamiliar with (IBMi, green screens, RPG/COBOL) for extra research depth and fact-checking, as he cannot catch hallucinations in unfamiliar domains

### Design Standards

- Apply the 34 guiding principles from `.claude/rules/guiding-principles.md`
- Apply AWS Well-Architected Framework (6 pillars) to all architecture decisions
- Follow KISS — good design is less design
- Ensure all UX includes best-practice combination of conversational UI and GUI
- Design for accessibility (WCAG 2.2 AA minimum)

### Output Standards

- Elegant and minimalistic — every section must deliver tangible value, no filler
- Grounded in truth with verified citations
- Easy to read and understand by average engineers
- Written in Paul's voice and brand
- Markdown format that exports to valid, modern Microsoft Word
- NOT over-engineered — calibrate depth to a 15-20 minute presentation, not a 200-page RFP response

### Challenge Paul's Answers

- Do not accept Paul's initial answers uncritically — research and improve upon them
- Where Paul's instincts are strong, validate and deepen with evidence
- Where Paul's instincts have gaps, fill them with researched best practices
- Present alternative perspectives where relevant

---

## Interaction Model

Before writing any plans, ask Paul clarifying questions to fill gaps. Organize questions into:

1. **Must-answer before planning** — questions that change the plan structure
2. **Can answer during execution** — questions that refine individual phase outputs
3. **Questions for interviewers** — questions to include in the deliverable's open questions section

After gathering answers, write all phase plans and the master plan to `.claude/plans/`.

---

## Ultimate Success Criteria

The plans you write must, when executed, produce deliverables that:

1. **Prove Paul can do the job** — demonstrate principal-level architecture thinking, not junior implementation detail
2. **Earn trust of the hiring panel** — a 20-year veteran engineering leader and panel of architects must find the work credible and impressive
3. **Show AI-first thinking** — CVS expects AI-first development; the solution should demonstrate Paul lives this
4. **Differentiate Paul** — leverage his strengths in AI governance, data security, and human-centered design
5. **Stay grounded** — no hand-waving, no buzzword soup, no over-engineering; every decision justified by evidence and business value
