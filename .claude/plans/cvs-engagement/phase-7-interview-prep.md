# Phase 7: Interview Preparation

Use ultrathink for this phase. Engage extended reasoning before every major output.

Perform web research using WebSearch for any technology or pattern in the solution that Paul needs to discuss confidently. This phase prepares Paul to present AND defend the deliverable.

**All outputs from this phase go to `private/interview-prep/`** — this directory must be gitignored.

## Objective

Prepare Paul for the CVS Health Principal Architect interview. The interview consists of **three separate 45-minute interviews**, each with a different interviewer drilling into different components of the solution. The solution architecture document is sent to the hiring manager before the interview stage — interviewers will have read it (or sections of it) before speaking with Paul.

This phase produces:
1. **3 Interview Prep Guides** — one per interview, each with topic overview, 40+ Q&A pairs, opening strategy, cheat sheet, and questions for the interviewer
2. **Cross-Interview Study Guide** — technology deep dives organized by likely interview grouping
3. **Q&A Bank** — 125+ questions reorganized by likely interview grouping (not just by topic)
4. **3 Interview-Specific Cheat Sheets + 1 Master** — quick references for 30 minutes before each interview

**Important**: Interview-specific guides cannot be fully finalized until Paul knows who the 3 interviewers are and what they focus on. This phase produces comprehensive materials + templates that can be quickly customized once interviewer assignments are known.

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

**Phase 1 Insights for Interview Prep**:
- HCD interview is Paul's strongest of the three — prepare detailed answers for: "How does your Cognitive Science background inform your design approach?" and "How do you handle resistance from expert users faster on the old system?"
- Six design principles with cited theories (Hick's Law, Fitts's Law, Dreyfus model, Johnson-Laird, Reason's taxonomy, Miller's Law) provide deep interview content
- Command palette as bridge pattern is a concrete, defensible design decision with industry examples
- CVS's 120+ accessibility professionals mean the interviewer likely has deep accessibility knowledge — don't oversimplify WCAG discussion
- The GenAI PA wireframe demonstrates dual competency — use it in the architecture interview too

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

### Step 4: Write Interview Prep Guides
Write 3 interview prep guides to: `private/interview-prep/interview-{1,2,3}-prep.md`

Since the specific interviewers and their focus areas are not yet known, create guides for three likely interview groupings based on the 5 key considerations:

**Interview A: Architecture & Legacy Integration** (likely a senior architect or tech lead)
- Key Considerations: Legacy System Integration (#1) + Technology Stack (#4)
- Depth areas: Strangler fig pattern, IBMi integration, GCP services, 3-option analysis
- GenAI pipeline architecture (dual competency)
- Duration: 45 minutes — plan for 5-10 min overview + 35 min deep Q&A

**Interview B: HCD & Change Management** (likely a UX leader or org change specialist)
- Key Considerations: HCD Design Principles (#3) + Change Management (#5)
- Depth areas: Cognitive Science grounding, personas, journey maps, ADKAR, training
- Paul's differentiator interview — lean into Cognitive Science BA
- Duration: 45 minutes — plan for 5-10 min overview + 35 min deep Q&A

**Interview C: Security, IAM & Compliance** (likely a security/IAM specialist)
- Key Consideration: IAM Strategy (#2) + Security Architecture
- Depth areas: Zero trust, SMART on FHIR, RBAC/ABAC, HIPAA, AI security controls
- Paul's highest-risk interview — prepare honestly for gaps
- Duration: 45 minutes — plan for 5-10 min overview + 35 min deep Q&A

Each guide includes:
```markdown
# Interview [A/B/C] Prep Guide — [Topic]

## Interview Strategy
- Opening approach (how to set the frame in first 2 minutes)
- Key themes to weave throughout
- Strengths to lead with
- Gaps to prepare for honestly
- Questions to ask the interviewer (shows engagement + fills knowledge gaps)

## Topic Overview (5-10 min talk track)
[What to say if asked "walk me through your approach to [topic]"]
[Key diagrams to reference from the document]

## Q&A Pairs (40+ questions)
### Warm-up (10 questions)
### Technical Depth (15 questions)
### Edge Cases & Challenges (10 questions)
### Curveballs & Honesty Tests (5+ questions)

## Cheat Sheet
[Key numbers, patterns, service names, framework citations]

## Honesty Map for This Interview
[What Paul can claim vs. what is researched vs. what is a gap]
```

### Step 5: Write Cross-Interview Study Guide
Write to: `private/interview-prep/cross-interview-study-guide.md`

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

### Step 7: Write Cheat Sheets
Write master cheat sheet to: `private/interview-prep/master-cheat-sheet.md`
Write interview-specific cheat sheets to: `private/interview-prep/interview-{1,2,3}-cheat-sheet.md`

Master cheat sheet covers the full solution. Interview-specific cheat sheets focus on the topics for that interview — what to review in the 30 minutes before each session:

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
  - [ ] Each interview prep guide covers sufficient depth for a 45-minute focused interview
  - [ ] Study guide covers every technology and pattern in the solution
  - [ ] Q&A bank has 125+ questions across all categories
  - [ ] Cheat sheet fits on one rendered page
  - [ ] Behavioral answers use STAR format with real projects

## Exit Criteria

This is the final phase. Exit criteria = engagement complete:
- [ ] `private/interview-prep/interview-{1,2,3}-prep.md` — 3 interview prep guides complete (40+ Q&A each)
- [ ] `private/interview-prep/cross-interview-study-guide.md` complete
- [ ] `private/interview-prep/qa-bank.md` with 125+ questions organized by likely interview grouping
- [ ] `private/interview-prep/master-cheat-sheet.md` complete
- [ ] `private/interview-prep/interview-{1,2,3}-cheat-sheet.md` — 3 interview-specific cheat sheets
- [ ] All files in `private/interview-prep/` (gitignored)
- [ ] Every answer verified against career-data.json
- [ ] Gap areas honestly labeled with positive framing
- [ ] Each interview prep guide provides sufficient depth for 45 minutes of focused questioning

## Context Handoff

This is the final phase. Context handoff is for record-keeping:

1. **Write context summary** to `.claude/plans/cvs-engagement/context/phase-7-context.md` using the Context Summary Template (see master-plan.md)

2. **Update master-plan.md** with engagement completion status

3. **Update `knowledge_base/engagement.json`**: set status to `completed`

4. **Commit** context summary to git with message: `docs(plans): complete Phase 7 interview prep, engagement complete`

Note: Do NOT commit `private/interview-prep/` — it is gitignored.

## Human Checkpoint

Paul: final review of the engagement:
- Interview prep guides: `private/interview-prep/interview-{1,2,3}-prep.md`
  - Review each guide — does the opening strategy feel natural?
  - Are the Q&A pairs sufficient for 45 minutes of deep questioning?
  - Are the honesty notes helpful for navigating tricky questions?
  - Once interviewers are assigned, customize guides for specific people
- Cross-interview study guide: `private/interview-prep/cross-interview-study-guide.md`
  - Are the gap areas ([GAP]) accurately identified?
  - Focus study time on [GAP] items, especially for the security/IAM interview
- Q&A bank: `private/interview-prep/qa-bank.md`
  - Practice the hardball and curveball questions across all 3 interviews
- Cheat sheets: `private/interview-prep/master-cheat-sheet.md` + interview-specific
  - Review interview-specific cheat sheets 30 min before each session
  - Are your questions for each interviewer good?
- Overall: do you feel prepared for three 45-minute deep dives?

**The engagement is complete when Paul feels confident sustaining 45 minutes of focused questioning on each key topic area.**
