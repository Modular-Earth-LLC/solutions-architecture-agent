# eng-2026-004 v2: AI-Driven Prior Authorization
## Autonomize AI Interview | Paul Prae | www.paulprae.com

---

## How to Use These Files

| When | Open This | Purpose |
|------|-----------|---------|
| **Night before** | [interview-prep/study-guide.md](interview-prep/study-guide.md) | Azure mapping, diagram talking points, assumptions, key numbers |
| **1 hour before** | [interview-prep/pre-show-checklist.md](interview-prep/pre-show-checklist.md) | Checklists, risk awareness, rehearsal items |
| **During presentation** | [presentation.md](presentation.md) + [speaker-script.md](speaker-script.md) | Slides on screen + speaking notes in hand |
| **During Q&A** | [interview-prep/quick-reference.md](interview-prep/quick-reference.md) | 18 anticipated questions with 60-second answers |
| **Morning demo build** | [plans/demo-implementation-prompt.md](plans/demo-implementation-prompt.md) | Claude Code plan for building the PA review demo |
| **Before sending email** | [email-draft.md](email-draft.md) | Email to panel with attachments |

---

## File Index

### Presentation
| File | Description |
|------|-------------|
| [presentation.md](presentation.md) | 11-slide deck — standalone, GitHub-renderable, no speaker notes |
| [speaker-script.md](speaker-script.md) | Speaking notes, timing, coaching, pivot guides — references presentation slides |

### Interview Prep (3 files, organized by when you use them)
| File | When | Description |
|------|------|-------------|
| [study-guide.md](interview-prep/study-guide.md) | Night before | Azure↔AWS mapping, diagram talking points, 15 assumptions, key numbers |
| [pre-show-checklist.md](interview-prep/pre-show-checklist.md) | 1 hour before | Checklists (email, content, demo, diagrams), risk tables, sign-off |
| [quick-reference.md](interview-prep/quick-reference.md) | During Q&A | 18 panel questions with scripted answers, quick pivots table |

### Reference Documents
| File | Description |
|------|-------------|
| [solution-architecture-source-of-truth.md](solution-architecture-source-of-truth.md) | Master architecture reference — all other docs are views of this |
| [research-context.md](research-context.md) | Research findings with 50+ verified source URLs |
| [requirements-traceability.md](requirements-traceability.md) | Assignment → slide mapping (27 requirements, 100% coverage) |
| [email-draft.md](email-draft.md) | Interview email for panel |

### Slide Generation (for Claude for PowerPoint)
| File | Description |
|------|-------------|
| [slide-generation-prompts/README.md](slide-generation-prompts/README.md) | All 11 prompts referencing presentation.md as source of truth |

### Diagrams (6 progressive views, 3 formats each)
| Diagram | .mmd | .svg | .png |
|---------|------|------|------|
| 01 System Context | [mmd](diagrams/01-system-context.mmd) | [svg](diagrams/01-system-context.svg) | [png](diagrams/01-system-context.png) |
| 02 Component Architecture | [mmd](diagrams/02-component-architecture.mmd) | [svg](diagrams/02-component-architecture.svg) | [png](diagrams/02-component-architecture.png) |
| 03 PA Request Flow | [mmd](diagrams/03-pa-request-flow.mmd) | [svg](diagrams/03-pa-request-flow.svg) | [png](diagrams/03-pa-request-flow.png) |
| 04 Clinical Data Access | [mmd](diagrams/04-clinical-data-access.mmd) | [svg](diagrams/04-clinical-data-access.svg) | [png](diagrams/04-clinical-data-access.png) |
| 05 Security & Zero Trust | [mmd](diagrams/05-security-zero-trust.mmd) | [svg](diagrams/05-security-zero-trust.svg) | [png](diagrams/05-security-zero-trust.png) |
| 06 LLMOps Pipeline | [mmd](diagrams/06-llmops-pipeline.mmd) | [svg](diagrams/06-llmops-pipeline.svg) | [png](diagrams/06-llmops-pipeline.png) |

### Plans
| File | Description |
|------|-------------|
| [demo-implementation-prompt.md](plans/demo-implementation-prompt.md) | Claude Code plan for demo build (March 24 morning) |
| [execution-log.md](plans/execution-log.md) | Autonomous overnight execution log |
| [decisions-made-without-paul.md](plans/decisions-made-without-paul.md) | 3 technical decisions made overnight |
