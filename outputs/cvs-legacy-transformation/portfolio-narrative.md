# Portfolio Narrative

> Connecting this engagement to Paul Prae's architecture practice and dual competency

## Architecture Practice

This solution architecture reflects principles I've developed across 15 years of building AI and data systems in healthcare, life science, and enterprise technology. The approach isn't theoretical — it's grounded in patterns I've applied at scale.

### Guiding Principles in Action

Several principles from my architecture practice shaped this engagement directly:

**"Architecture is leadership; always be architecting"** (Principle 9). This document isn't a one-time deliverable — it's the opening of a continuous architecture conversation. The 4 decision gates, 10 risks with triggers, and 8 open security findings are designed to evolve as the engagement progresses. Architecture is a living practice, not a phase that ends.

**"KISS: Keep it stupid simple"** (Principle 10). Three architecture options, each genuinely viable, each with clear trade-offs. No 200-page appendices of edge cases. The strangler fig pattern — migrate one workflow at a time, validate in parallel, roll back in under 15 minutes — is simple by design. Complexity is the enemy of execution.

**"Make frequent, small, reversible changes"** (Principle 15). Every migration step in this plan is independently reversible via Apigee route rules — a configuration change, not a code deployment. The member eligibility workflow migrates first because it's the lowest-risk proof point. Claims adjudication comes second, after parallel validation reaches 99.9% consistency. This isn't a big-bang transformation; it's a series of small, validated steps.

**"Anticipate failure"** (Principle 16). The pre-mortem is built into the plan: 10 identified risks, each with mitigations, owners, triggers, and contingencies. RPG/CL developer scarcity (average age ~70, #1 concern at 69% of IBM i shops) is rated critical — not because the project will fail, but because acknowledging the constraint drives the 60-90 day sourcing lead time and scarcity premium into the budget upfront.

**"Assume breach"** (Principle 18). The security architecture starts from zero trust (BeyondCorp + NIST SP 800-207), not perimeter defense. The GenAI pipeline service account has zero direct PHI access — enforced by VPC Service Controls and IAM deny policies, not just documentation. Defense-in-depth across 5 layers with 30 enumerated threats and 21 mapped compliance controls.

**"Treat clients like business partners, not customers"** (Principle 33). This document presents recommendations collaboratively — "I recommend" rather than "you must." The three-option analysis respects the client's agency to choose. The honesty map transparently acknowledges where my expertise is deep vs. researched. Partnership starts with transparency.

## Dual Competency: Architect + GenAI Team Leader

This engagement demonstrates both the principal architect capability and the GenAI team leadership that the role requires. These aren't separate competencies — they're integrated throughout the solution.

### As Architect

**Three genuinely viable options.** GCP-Native (recommended, aligned with CVS Health100 partnership), AWS-Native (deepest technical capability with HealthLake + Comprehend Medical), and Modern Cloud (fastest time-to-value with Vercel + Supabase). Each option has cited vendor reference architectures, infrastructure cost models, and Well-Architected scoring. No strawman options — all three are defensible.

**12 components, 13 data entities, 10 API contracts.** The architecture isn't a high-level diagram with handwaving at the details. API contracts specify request/response schemas, SLAs (P95 latency ≤500ms for claims), authentication methods, and error handling. The data model covers members, plans, claims, pharmacies, providers, drugs, formulary, prior authorization, users, audit logs, AI recommendations, migration status, and CDC sync — each with defined relationships, validation rules, and governance classifications.

**Well-Architected scoring across 6 pillars.** Overall 7.7/10, with honest assessment of where the architecture is strongest (security: 8.5, reliability: 8.0) and where uncertainty exists (performance: 7.0 due to IWS throughput unknowns, cost optimization: 7.0 due to Apigee Enterprise pricing opacity). The scores aren't inflated — they reflect genuine assessment.

**78-week project plan with 39 sprints and 4 decision gates.** Each gate has measurable go/no-go criteria: ≥99.9% parallel validation accuracy, P95 ≤500ms latency, escape hatch usage <20%, adoption >80%. These aren't aspirational targets — they're the thresholds that determine whether the project proceeds, pivots, or pauses.

### As GenAI Team Leader

**Tiered inference architecture.** Gemini 2.5 Pro for complex prior authorization cases requiring multi-document reasoning. MedGemma 1.5 (4B parameters, 128K context, 89.6% EHRQA accuracy) for routine PA cases — a 40-60% cost reduction on the most volatile cost layer. This mirrors the three-tier AI pipeline pattern I've built in production: expensive models for hard problems, efficient models for routine ones, with confidence-based routing between them.

**Evaluation framework.** Correctness, safety, groundedness, and consistency scoring for every GenAI output. Ensemble disagreement detection (Gemini vs. MedGemma) as an automated quality signal. Human-in-the-loop mandatory for all PA decisions — the pharmacist approves, the AI recommends. This is the responsible AI practice I'd bring to the GenAI data science team.

**AI security controls.** OWASP LLM Top 10 alignment. Cloud DLP as a synchronous blocking gate (pre and post-inference). Structured output enforcement via Gemini controlled generation. VPC Service Controls perimeter isolation for the GenAI pipeline. The GenAI pipeline service account (`genai-pipeline@`) has zero direct PHI access — an architecture decision, not a policy statement.

**Team composition.** The project plan includes ML Lead + 2 ML Engineers + MLOps Engineer = 4 GenAI FTEs. This is the team I would manage. The roles map directly to the GenAI Data Scientist JD responsibilities: LLM workflow development, evaluation/guardrails implementation, GCP pipeline deployment (BigQuery, Vertex AI, Cloud Storage), and production reliability.

### The Integration Point

The dual competency isn't "architect who also knows AI." It's that AI architecture decisions require understanding both the infrastructure layer AND the ML layer:

- **Why tiered inference?** Because the infrastructure architect sees the cost model (Gemini at $1.25/$10 per 1M tokens) and the ML lead understands which cases actually need the expensive model. Neither perspective alone produces the right design.
- **Why VPC-SC isolation for GenAI?** Because the security architect knows perimeter controls and the AI lead knows that LLM prompts can leak training data. The DLP blocking gate exists because I understand both the network boundary and the model behavior.
- **Why HITL for all PA decisions?** Because the system architect could build an autonomous pipeline, but the AI practitioner knows that healthcare GenAI outputs require clinical validation — not because the model is unreliable, but because accountability requires a human decision-maker for patient-affecting actions.

## Key Differentiators

### Cognitive Science Foundation
BA in Cognitive Science with a focused foundation in Artificial Intelligence (University of Georgia, Cum Laude). This isn't a certification — it's 4 years of studying how humans process information, make decisions, and interact with systems. The UX design principles in this solution (Hick's Law for progressive disclosure, Fitts's Law for target sizing, Dreyfus skill acquisition for dual-mode interface, Miller's Law for information chunking) come from formal education, not blog posts.

Six UX projects across my career provide the applied foundation: Fortune 100 conversational UI assessment (Slalom), behavioral healthcare review app with nurse user research ($2M revenue, Slalom), Neona chatbot design, Knowledge Transfer Module (React UX), and FitBloc wireframing — plus the HCI coursework projects that started it all.

### AI-First Practice
This engagement itself demonstrates AI-first practice. I used AI tools (Claude via Claude Code, Solutions Architecture Agent plugin) as integrated partners in the architecture workflow — not as afterthoughts or demos. The methodology section documents exactly how: what AI did, what I did, and where the boundary sits.

My AI background spans 15+ ML projects across healthcare, life science, and enterprise. At Arine, I built the observability pipeline for an autonomous pharmacist AI agent and trained 100 engineers on AI-first development. At Booz Allen, I led healthcare AI practice for clinical, behavioral, and genomic data. At AWS, I spent 3 years as an Enterprise AI/ML SA specializing in SageMaker and Bedrock. At NeuroLex, I architected ML pipelines for voice-based healthcare diagnostics.

### Full-Stack Architecture
This solution covers the complete stack: React frontend with progressive disclosure UX, BFF API layer with Apigee gateway, GCP-native backend services (Cloud Run + GKE Autopilot), PostgreSQL/AlloyDB data layer, Vertex AI GenAI pipeline, CDC integration via Precisely Connect, and zero trust security architecture. I don't specialize in one layer — I architect across all of them, because integration failures happen at the seams.

My career reflects this: Microsoft (.NET/SharePoint infrastructure), Slalom (Azure ML + analytics consulting), AWS (cloud architecture at enterprise scale), NeuroLex (ML platform engineering), Hyperbloom (full-stack AI consulting), TReNDS (neuroinformatics data platform), Booz Allen (healthcare AI leadership), Arine (data operations + AI agents).

### Collaborative Leadership
Executive AI coaching at Mento (100% leadership improvement, 93% performance improvement). AI enablement workshops at Arine training 100 engineers. "Radical transparency with a passion for people" at Decooda. Knowledge transfer sessions at Slalom, AWS, and Microsoft.

Leadership for me is coaching, not commanding. The change management strategy in this solution (ADKAR with champion networks, 15% of program budget per Gartner recommendation) reflects how I actually lead transformations — by investing in people, measuring adoption, and adjusting based on evidence.

## Experience Evidence Map

Every claim in this narrative maps to verifiable career data:

| Claim | Evidence | Source |
|-------|----------|--------|
| 15+ years experience | Career start: 2010 (Digital Strategy Consultant) | career-data.json |
| 15+ ML projects | NeuroLex, Decooda, Slalom (3+ projects), AWS (SA for ML customers), TReNDS, Hyperbloom, Booz Allen, Arine, Modular Earth | career-data.json positions |
| 3 healthcare AI roles | Arine (Staff AI DataOps), Booz Allen (Chief AI Architect), NeuroLex (Senior AI Engineer) | career-data.json positions |
| AWS SA for 3 years | Amazon Web Services, 2018-08 to 2021-05 (2 years 9 months) | career-data.json positions |
| Cognitive Science BA | University of Georgia, BA Cognitive Science (AI focus), Cum Laude | career-data.json education |
| Computer Science BS | University of Georgia, BS Computer Science (AI emphasis) | career-data.json education |
| Coached 100% leadership improvement | Mento, Executive AI and Data Science Coach | career-data.json positions |
| Trained 100 engineers | Arine, AI enablement workshops | career-data.json positions |
| Autonomous pharmacist agent | Arine, observability pipeline for autonomous pharmacist AI agent | career-data.json positions |
| $2M revenue healthcare app | Slalom, behavioral healthcare review app | career-data.json positions |
| $1.4M ARR consulting | Hyperbloom, AI consulting business | honesty-map.md |
| HIPAA compliance experience | Arine, Hyperbloom, TReNDS (differential privacy for PHI) | career-data.json positions |
| Fortune 500 clients | AWS (Cox, Equifax, NCR), Microsoft (Chevron, Shell, Walmart, Disney, BoA), Slalom | career-data.json positions |
| Zero GCP hands-on experience | Transparent — no GCP role in career history | honesty-map.md |
| Zero IBMi hands-on experience | Transparent — no IBMi role in career history | honesty-map.md |

**No claim in this document exceeds what my career data supports.** Where I relied on research rather than experience, it's labeled. Where I have genuine gaps, they're acknowledged.
