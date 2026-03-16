# Phase 7: Interview Preparation

Use ultrathink for this phase. Engage extended reasoning before every major output.

Perform web research using WebSearch for any technology or pattern in the solution that Paul needs to discuss confidently. This phase prepares Paul to present AND defend the deliverable.

**All outputs from this phase go to `private/interview-prep/`** — this directory must be gitignored.

## Objective

Prepare Paul for the CVS Health Principal Architect interview. The interview is a 15-20 minute presentation of the solution architecture document, followed by panel Q&A where individual members drill on specific key considerations. This phase produces:
1. Presentation script (15-20 minute talk track)
2. Study guide (technology deep dives for every system in the architecture)
3. Q&A bank (125+ questions across all key considerations)
4. Cheat sheet (one-page quick reference)

Everything produced must be something Paul can confidently say based on his actual experience + the research conducted in this engagement. Nothing should require Paul to claim expertise he doesn't have.

## Input Dependencies

- `outputs/cvs-legacy-transformation/solution-architecture-document.md` — the complete deliverable (Phase 6)
- `outputs/cvs-legacy-transformation/honesty-map.md` — Paul's experience mapping (Phase 0)
- `outputs/cvs-legacy-transformation/ai-methodology.md` — AI methodology section (Phase 5)
- All knowledge base files (for technical detail)
- All phase context summaries (for understanding the engagement arc)
- Paul's career data (for experience-grounded answers)

**All Phase Context Summaries**:
- `.claude/plans/cvs-engagement/context/phase-*-context.md`

## Prior Phase Context

Read ALL completed phase context summaries before executing. This phase has the richest context — use it to:
- Identify areas where Paul was most/least confident during the engagement
- Note review feedback that suggests potential weaknesses
- Understand which decisions Paul made vs. which were AI-suggested
- Map every technology and pattern to Paul's ability to discuss it

## Context Files

**Paul's Career Data** (base: `C:\dev\paulprae-com`):
- `data/generated/career-data.json` — CRITICAL: every answer must map to real experience
- `data/sources/knowledge/career/companies.json` — company context for experience stories
- `data/sources/knowledge/career/projects.json` — project details for STAR stories

**Paul's Communication Style** (base: `C:\dev\paulprae-com`):
- `data/sources/knowledge/brand/communication-styles.json` — how Paul communicates
- `data/sources/knowledge/content/writing-formulas.json` — STAR format for behavioral answers

**Both Job Descriptions**:
- `.claude/plans/references/solution-architect-case-study-and-interview.md` — SA JD + case study
- `.claude/plans/references/CVS - GenAI Data Scientist Job Description .pdf` — GenAI DS JD

## Research Directives

### Cluster 1: Technology Deep Dives (Gap Areas)
Research specific technologies Paul needs to discuss but hasn't used extensively:
- `GCP Apigee X API management architecture deep dive`
- `IBMi AS/400 RPG ILE free format modernization explained`
- `Google Cloud Identity Platform vs Firebase Auth enterprise`
- `Prosci ADKAR certification change management detailed`

### Cluster 2: CVS Health Current Context
- `CVS Health technology leadership team 2025 2026`
- `CVS Health pharmacy benefits modernization initiatives recent`
- `CVS Health Google Cloud partnership announcements`
- `CVS Health digital transformation strategy recent`

### Cluster 3: Interview Best Practices
- `principal architect interview presentation tips panel format`
- `solution architecture presentation structure 20 minutes`
- `technical interview panel questions legacy modernization`

## Execution Steps

### Step 1: Ensure Private Directory is Gitignored
Before writing any files, ensure `private/` is in `.gitignore`:
```bash
# Check if private/ is gitignored
grep -q "^private/" .gitignore || echo "private/" >> .gitignore
```

Create the output directory:
```bash
mkdir -p private/interview-prep
```

### Step 2: Read All Context and Input Files
Read the complete deliverable document, all context summaries, and Paul's career data. Create a comprehensive mapping:
- Every technology mentioned in the document → Paul's experience level (1-5)
- Every design decision → Paul's rationale and confidence
- Every assumption → Paul's ability to defend or acknowledge it
- Every key consideration → depth of treatment and potential weakness

### Step 3: Execute Web Research
Run research clusters to fill Paul's knowledge gaps. Focus on:
- Technologies Paul rated 1-2/5 in the honesty map
- CVS-specific context for contextual answers
- Presentation best practices for the interview format

### Step 4: Write Presentation Script
Write to: `private/interview-prep/presentation-script.md`

Structure for a 15-20 minute presentation:

```markdown
# Presentation Script — CVS Legacy Transformation

## Timing Guide
- Opening (2 min): Context setting + approach overview
- Architecture (5 min): High-level flow + recommended option
- Key Considerations Deep Dive (8 min): 5 considerations, 90 sec each
- AI/Innovation Angle (2 min): Dual competency demonstration
- Close (2 min): Summary + questions transition

## Slide-by-Slide Talk Track

### Opening [2 minutes]
[What to say, key phrases, energy level]
[Hook: start with the user problem, not the technology]

### Architecture Overview [5 minutes]
[Walk through the system context diagram]
[Present 3 options briefly, recommend Option B]
[Key talking points for each diagram]
[Transition to deep dive]

### Key Consideration 1: Legacy Integration [90 seconds]
[Strangler fig approach — crisp explanation]
[Key phrase: "..."]

### Key Consideration 2: IAM Strategy [90 seconds]
[Zero trust + phased migration — confident delivery]
[Key phrase: "..."]

### Key Consideration 3: HCD Principles [90 seconds]
[Cognitive Science angle — Paul's differentiator]
[Key phrase: "..."]

### Key Consideration 4: Technology Stack [90 seconds]
[GCP-native, justified choices]
[Key phrase: "..."]

### Key Consideration 5: Change Management [90 seconds]
[ADKAR integration, coaching philosophy]
[Key phrase: "..."]

### AI/Innovation [2 minutes]
[GenAI pipeline, AI-assisted methodology]
[Key phrase: "..."]

### Close [2 minutes]
[Summary, confidence, questions invitation]
[Closing phrase: "..."]

## Delivery Notes
- Pace: conversational, not rushed
- Diagrams: reference but don't read from them
- Questions: welcome them, they show engagement
- If you don't know: "That's a great question — here's how I'd approach finding the answer..."
```

### Step 5: Write Study Guide
Write to: `private/interview-prep/study-guide.md`

For every technology and pattern in the solution, provide:

```markdown
# Study Guide — Technology Deep Dives

## How to Use This Guide
Review each section. Focus on areas marked [GAP] (gap areas).
For each technology: know what it does, why it was chosen, and one alternative.

## GCP Services

### Cloud Run
- What it is: [one sentence]
- Why chosen: [rationale from architecture]
- Paul's experience: [from career-data.json]
- Key talking point: [one sentence for interview]
- Alternative: [and why not chosen]
- [GAP]? [yes/no + what to study]

### Apigee X
[Same structure]

### Vertex AI
[Same structure]

[...repeat for every technology in the solution...]

## Architecture Patterns

### Strangler Fig
- What it is: [one sentence]
- How it's applied here: [specific to CVS solution]
- Paul's experience: [from career-data.json]
- Key talking point: [for interview]
- [GAP]? [yes/no]

### Anti-Corruption Layer
[Same structure]

[...repeat for every pattern...]

## Domain Knowledge

### Pharmacy Benefits Management
- Key concepts: [claims adjudication, formulary, prior auth...]
- Paul's experience: [from career-data.json]
- [GAP]? [yes/no + key terms to know]

### IBMi / AS/400
- Key concepts: [RPG, DB2 for i, 5250 screens, data queues...]
- Paul's experience: [minimal — researched]
- [GAP]? YES — key points to know:
  [Focused study points]

## Compliance and Security

### HIPAA Technical Safeguards
[Key requirements, how the solution addresses them]

### Zero Trust / BeyondCorp
[Key principles, how applied in the solution]

[...repeat for all relevant areas...]
```

### Step 6: Write Q&A Bank
Write to: `private/interview-prep/qa-bank.md`

125+ questions organized by key consideration and difficulty:

```markdown
# Q&A Bank — 125+ Interview Questions

## How to Use
- Review all questions
- Practice answers out loud (not just reading)
- For each: have 1 concrete example ready
- [GAP] marks questions where Paul needs extra preparation

## Key Consideration 1: Legacy System Integration (25 questions)

### Softball (warm-up)
1. What's your overall approach to modernizing the IBMi applications?
   **Answer**: [2-3 sentence response grounded in the solution]
   **Experience anchor**: [career-data.json reference]

2. Why did you choose the strangler fig pattern?
   **Answer**: [...]

### Medium (architectural depth)
5. How would you handle data consistency between the IBMi system and the new platform during the migration?
   **Answer**: [...]
   **If pressed**: [deeper technical detail]

### Hardball (edge cases, challenges)
15. [GAP] What if the IBMi business logic is too complex to extract into APIs? How would you handle undocumented business rules?
    **Answer**: [honest answer + approach to discovery]
    **Honesty note**: [what Paul can and can't claim here]

### Curveball (unexpected angles)
20. Have you personally worked with IBMi systems? How did you prepare for this modernization design?
    **Answer**: [HONEST — researched for this engagement, not personal IBMi experience. Frame positively.]

## Key Consideration 2: IAM Strategy (25 questions)
[Same structure: softball → medium → hardball → curveball]

## Key Consideration 3: HCD Design Principles (20 questions)
[Paul's strength area — more confident answers]

## Key Consideration 4: Technology Stack (25 questions)
[GCP depth, alternatives, trade-offs]

## Key Consideration 5: Change Management (15 questions)
[ADKAR, coaching, adoption strategies]

## Dual Competency: GenAI Leadership (15 questions)
[How would you lead the GenAI DS team? Pipeline architecture? Evaluation frameworks?]

## Meta Questions: Methodology and Approach (10+ questions)
[Why did you use AI assistance? How do you ensure quality? Architecture philosophy?]

## Behavioral Questions (10+ questions)
[STAR format — all mapped to career-data.json]
[Leadership, conflict, ambiguity, failure, collaboration]
```

### Step 7: Write Cheat Sheet
Write to: `private/interview-prep/cheat-sheet.md`

One-page quick reference for 30 minutes before the interview:

```markdown
# Interview Cheat Sheet — CVS Legacy Transformation

## The Solution in 30 Seconds
[Elevator pitch version]

## 5 Key Considerations — One Line Each
1. Legacy Integration: Strangler fig + anti-corruption layer, phased migration
2. IAM: GCP Identity Platform, zero trust, RBAC+ABAC, phased SSO migration
3. HCD: Cognitive Science-grounded, dual-mode interface, progressive disclosure
4. Tech Stack: GCP-native (Cloud Run, Apigee, Vertex AI), React frontend
5. Change Management: ADKAR model integrated into every phase, champion network

## My Differentiators
1. Cognitive Science degree → genuine HCD expertise
2. AI-first practice → demonstrated, not claimed
3. Full-stack architecture → UX to infrastructure
4. Collaborative leadership → coaching philosophy

## Confidence Map
- Strong: HCD, architecture patterns, AI/ML, change management, security
- Moderate: GCP specifics (AWS-primary but transferable), IAM design
- Researched: IBMi/AS/400, PBM domain, GCP pricing

## If I Don't Know the Answer
"That's a great question. Based on what I've researched, [partial answer].
In practice, I'd [approach to finding the full answer]. Can I follow up
on that?"

## Key Numbers to Remember
- Timeline: [X-Y months]
- Team: [N people, key roles]
- Budget range: [range]
- Phases: 4, with decision gates

## My Questions for Them
1. [About the existing IBMi application portfolio]
2. [About the current user base and workflows]
3. [About the GenAI team's current state and roadmap]
4. [About success metrics for this transformation]
5. [About the broader technology modernization vision]
```

## Honesty Rules

1. **Every answer must be something Paul can actually say.** If Paul can't confidently deliver an answer, rewrite it or add an honesty note.
2. **Experience anchors must map to career-data.json.** No invented experience stories.
3. **Gap areas must be honestly labeled.** Don't pretend Paul has IBMi expertise.
4. **The "I researched this" framing is a strength, not a weakness.** It shows thoroughness and intellectual honesty.
5. **Behavioral answers (STAR format) must use real projects.** Verify against projects.json and companies.json.
6. **The AI methodology answer must be genuine.** Paul should be proud of how he used AI, not defensive.
7. **"I don't know" answers must have a credible follow-up approach.** Show how Paul would find the answer.

## Quality Gate

- No formal `/review` for this phase (preparation materials, not deliverable)
- Self-review against these criteria:
  - [ ] Every Q&A answer is something Paul can confidently deliver
  - [ ] All experience anchors verified against career-data.json
  - [ ] Gap areas ([GAP]) have honest answers with positive framing
  - [ ] Presentation fits in 15-20 minutes when read at conversational pace
  - [ ] Study guide covers every technology and pattern in the solution
  - [ ] Q&A bank has 125+ questions across all categories
  - [ ] Cheat sheet fits on one rendered page
  - [ ] Behavioral answers use STAR format with real projects

## Exit Criteria

This is the final phase. Exit criteria = engagement complete:
- [ ] `private/interview-prep/presentation-script.md` complete
- [ ] `private/interview-prep/study-guide.md` complete
- [ ] `private/interview-prep/qa-bank.md` with 125+ questions
- [ ] `private/interview-prep/cheat-sheet.md` complete (one page)
- [ ] All files in `private/interview-prep/` (gitignored)
- [ ] Every answer verified against career-data.json
- [ ] Gap areas honestly labeled with positive framing

## Context Handoff

This is the final phase. Context handoff is for record-keeping:

1. **Write context summary** to `.claude/plans/cvs-engagement/context/phase-7-context.md` using the Context Summary Template (see master-plan.md)

2. **Update master-plan.md** with engagement completion status

3. **Update `knowledge_base/engagement.json`**: set status to `completed`

4. **Commit** context summary to git with message: `docs(plans): complete Phase 7 interview prep, engagement complete`

Note: Do NOT commit `private/interview-prep/` — it is gitignored.

## Human Checkpoint

Paul: final review of the engagement:
- Presentation script: `private/interview-prep/presentation-script.md`
  - Practice the presentation out loud — does it flow naturally?
  - Does it fit in 15-20 minutes at conversational pace?
  - Are you comfortable with every claim and framing?
- Study guide: `private/interview-prep/study-guide.md`
  - Are the gap areas ([GAP]) accurately identified?
  - Focus study time on [GAP] items
- Q&A bank: `private/interview-prep/qa-bank.md`
  - Practice the hardball and curveball questions
  - Are the honesty notes helpful for navigating tricky questions?
- Cheat sheet: `private/interview-prep/cheat-sheet.md`
  - Does it capture the essence in one page?
  - Are your questions for the panel good?
- Overall: do you feel prepared to present and defend this solution?

**The engagement is complete when Paul feels confident presenting the deliverable.**
