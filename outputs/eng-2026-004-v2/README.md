# eng-2026-004 v2: AI-Driven Prior Authorization
## Solution Architecture — Autonomize AI Interview
### Paul Prae | www.paulprae.com | March 24, 2026

---

## Quick Start

1. **Open `proposal.md`** — Slide content with full speaker notes (this is the primary deliverable)
2. **Open `presentation.md`** — GitHub-renderable version with inline Mermaid diagrams
3. **Review `plans/uat-checklist-v2.md`** — Human review checklist before presenting
4. **Review `plans/risk-assessment.md`** — Interview outcome risks and mitigations
5. **Review `plans/decisions-made-without-paul.md`** — 3 decisions made during overnight execution

## Deliverables

### Primary Documents
| File | Description |
|------|-------------|
| `proposal.md` | 11-slide deck content with speaker notes, priority-tiered (A/B/C) |
| `presentation.md` | GitHub-renderable Markdown deck with inline Mermaid diagrams |
| `solution-architecture-source-of-truth.md` | Master reference document — all other docs are views of this |
| `research-context.md` | Research findings with 50+ verified source URLs |
| `requirements-traceability.md` | Assignment → slide mapping (27 requirements, 100% coverage) |
| `email-draft.md` | Interview response email for panel |

### Slide Generation Prompts
| File | Slide |
|------|-------|
| `slide-generation-prompts/slide-01-introduction.md` | Title & Introduction |
| `slide-generation-prompts/slide-02-executive-summary.md` | Executive Summary |
| `slide-generation-prompts/slide-03-high-level-architecture.md` | System Context |
| `slide-generation-prompts/slide-04-system-architecture.md` | Component Architecture |
| `slide-generation-prompts/slide-05-pa-processing-flow.md` | PA Processing Flow |
| `slide-generation-prompts/slide-06-security.md` | Security & Zero Trust |
| `slide-generation-prompts/slide-07-clinical-data.md` | Clinical Data Integration |
| `slide-generation-prompts/slide-08-llmops.md` | LLMOps Pipeline |
| `slide-generation-prompts/slide-09-roadmap.md` | Implementation Roadmap |
| `slide-generation-prompts/slide-10-scaling.md` | Future State & Scaling |
| `slide-generation-prompts/slide-11-discussion.md` | Discussion Starters |

### Interview Prep
| File | Description |
|------|-------------|
| `interview-prep/qa-prep.md` | 18 anticipated questions organized by panelist |
| `interview-prep/technical-deep-dive.md` | Per-diagram talking points and depth guides |
| `interview-prep/azure-aws-mapping.md` | Complete Azure↔AWS service mapping |
| `interview-prep/assumptions-and-questions.md` | Discovery questions organized by interview flow |
| `interview-prep/presentation-coaching.md` | Time management, pivot guides, opening/closing scripts |

### Diagrams (6 progressive views)
| File | View | Format |
|------|------|--------|
| `diagrams/01-system-context` | Business stakeholder view (3-4 components) | .mmd / .svg / .png |
| `diagrams/02-component-architecture` | Internal components with Azure labels | .mmd / .svg / .png |
| `diagrams/03-pa-request-flow` | PA lifecycle (submit → determine → respond) | .mmd / .svg / .png |
| `diagrams/04-clinical-data-access` | FHIR R4 + legacy with security boundaries | .mmd / .svg / .png |
| `diagrams/05-security-zero-trust` | Layered security with AI-specific controls | .mmd / .svg / .png |
| `diagrams/06-llmops-pipeline` | Eval pipeline, guardrails, feedback loop | .mmd / .svg / .png |

### Plans
| File | Description |
|------|-------------|
| `plans/demo-implementation-prompt.md` | Claude Code plan for demo build (March 24 morning) |
| `plans/execution-log.md` | Autonomous overnight execution log |
| `plans/decisions-made-without-paul.md` | 3 technical decisions made without Paul |
| `plans/risk-assessment.md` | Interview outcome risks and mitigations |
| `plans/uat-checklist-v2.md` | Human review checklist before presenting |

## Architecture Summary

- **10 components**, **10 data flows**, **6 diagrams**
- **Azure-primary**: AI Foundry + Service Bus + Container Apps + Health Data Services
- **AI Engine**: Autonomize PA Copilot + Claude (via Azure AI Foundry)
- **Pattern**: Single agent with skills (ReAct), confidence-based routing
- **Security**: PHI tokenization, prompt injection defense, tamper-proof audit trail
- **Review Score**: 9.1/10 — PASS, 0 blockers

## Review Score

| Dimension | Score |
|-----------|-------|
| Completeness | 9.0 |
| Technical Soundness | 9.0 |
| Well-Architected | 8.0 |
| Clarity | 9.5 |
| Feasibility | 9.0 |
| **Overall** | **9.1** |
