# eng-2026-004: AI-Driven Prior Authorization — Autonomize AI

## Overview

This directory contains the complete solution architecture deliverables for an AI-driven Prior Authorization (PA) system designed for a large US health plan, using Autonomize AI's Genesis Platform. The work was produced as part of Paul Prae's interview assignment at Autonomize AI.

**Client**: Fictional US Health Plan (~45M members, 20 LOBs)
**Platform**: Autonomize AI Genesis + AWS
**Engagement Type**: Assessment (architecture + security + estimation + planning)
**Depth**: COMPREHENSIVE
**Duration**: Single session, ~4 hours

---

## Deliverables

### Primary Output
| File | Description |
|------|-------------|
| [`proposal.md`](proposal.md) | **12-slide interview presentation** with speaker notes for a 1-hour panel. Covers all 3 parts of the assignment: technical architecture, business planning, and advanced challenges (MLOps + multi-tenant scaling). |

### Implementation
| File | Description |
|------|-------------|
| [`plans/implementation-prompt.md`](plans/implementation-prompt.md) | Self-contained Claude Code planning prompt for building a **tightly scoped demo** (12-16 hours). Portal-only ingestion, mock services, Amazon Bedrock for AI determination, local Docker Compose. |

### Quality Assurance
| File | Description |
|------|-------------|
| [`plans/backlog.md`](plans/backlog.md) | Prioritized backlog of fixes and improvements (P0-P3). 4 items to address before the interview, 9 enhancements, 4 future items. |
| [`plans/uat-checklist.md`](plans/uat-checklist.md) | UAT verification checklist for Paul to validate all deliverables. Highlights areas of LOW and MEDIUM confidence requiring human expert review. |

### Research
| File | Description |
|------|-------------|
| [`research-context.md`](research-context.md) | Full research synthesis: Autonomize AI platform, Paul's career data mapping, industry PA statistics, questionnaire answers. |

### Knowledge Base (in `knowledge_base/`)
| File | Description | Score |
|------|-------------|-------|
| `requirements.json` | 12 functional requirements, 6 success criteria, AI suitability 9/10 | Complete |
| `architecture.json` | 14 components, 10 data flows, 6 Mermaid diagrams, WA scoring | Complete |
| `security_review.json` | 18 STRIDE threats, 5-layer defense-in-depth, HIPAA compliance mapping | Complete |
| `estimate.json` | $1.2M Year 1, $33K/month infra, 13 FTEs, 1322% 3-year ROI | Complete |
| `project_plan.json` | 5 phases, 6 sprints, 3 decision gates, 7 risks | Complete |
| `reviews.json` | 3-iteration review, 8.8/10 PASS, 0 blockers | Complete |

---

## Solution Architecture Summary

### The Problem
A large US health plan processes 2.5M prior authorization requests per month. 60% arrive via fax, requiring manual data entry and clinical review. Average turnaround is 5 business days with only 15% auto-approval. Annual PA operational cost: $33.75M across 450 FTEs.

### The Solution
Deploy Autonomize AI's multi-agent PA Copilot integrated with the payer's AWS infrastructure via an event-driven integration layer. A pipeline of specialized AI agents (Document, NLP, Eligibility, Guidelines, Decision) automates intake, clinical data aggregation, guidelines matching, and determination — routing complex cases to human reviewers with pre-assembled evidence packages.

### Key Metrics
| Metric | Current | Target |
|--------|---------|--------|
| PA Turnaround | 5 days | < 24 hours |
| Auto-Determination Rate | 15% | 60% |
| PA FTEs | 450 | 270 (-40%) |
| Annual Savings | — | $11.7M |
| CMS-0057-F Compliance | No | Yes (by Jan 2027) |

### Technology Stack
- **AI Platform**: Autonomize AI Genesis + Amazon Bedrock + Comprehend Medical + Textract
- **Event Bus**: Apache Kafka (Amazon MSK)
- **Data**: PostgreSQL (RDS) + DynamoDB + S3 + Snowflake + AWS HealthLake
- **Compute**: ECS Fargate + Lambda + Step Functions
- **Security**: SMART on FHIR, mTLS, AES-256 KMS, PHI field-level encryption, immutable DynamoDB audit trail

---

## Process: AI Agent vs. Human Contributions

### AI Agent (Claude Opus 4.6 via Solutions Architecture Agent plugin)
The AI agent autonomously executed the full solutions architecture lifecycle:

1. **Research** (4 parallel agents): Autonomize AI customers, paulprae.com background, MLOps best practices, CMS-0057-F regulations
2. **Requirements Discovery** (`/requirements`): Extracted 12 functional requirements from the assignment PDF, Paul's questionnaire answers, and research findings
3. **Architecture Design** (`/architecture`): Designed 14-component event-driven architecture with 6 Mermaid diagrams
4. **Security Review** (`/security-review`): STRIDE threat modeling (6 parallel STRIDE analyzers), 18 threats, HIPAA compliance mapping
5. **Estimation** (`/estimate`): Bottom-up cost modeling, team composition, ROI analysis
6. **Project Planning** (`/project-plan`): 12-week roadmap with sprints, gates, and risk register
7. **Proposal Assembly** (`/proposal`): 12-slide presentation with speaker notes
8. **Review** (`/review`): 3-iteration quality review, 8.8/10 PASS
9. **Implementation Prompt**: Demo-scoped planning prompt for Claude Code
10. **Final QA**: Fact-checking (10/12 verified), numerical consistency, assignment coverage

**Total background agents spawned**: 20+ (research, WA reviewers, STRIDE analyzers, fact-checkers)
**Total commits**: 12 (iteratively pushed to GitHub for remote monitoring)
**KB validation**: 10/10 files pass schema validation

### Human (Paul Prae)
Paul provided the strategic direction that shaped every deliverable:

- **Questionnaire answers**: Client scale assumptions, technology landscape (mapped to Paul's skills), compliance scope (only frameworks Paul has worked with), automation targets, multi-tenant decision, differentiation strategy
- **Quality standards**: Iterative QA, fact-checking, no hallucinations, healthcare security lens, archive old assets
- **Scope decisions**: Multi-tenant (not multi-instance), business outcome focus, speed-to-value + clinical accuracy positioning, auto-approval only (no auto-denial in Phase 1)
- **Demo scoping**: Implementation prompt must be tightly scoped for a small, achievable demo
- **Review authority**: All deliverables require Paul's review before the interview

---

## Git History

```
cf8bff5 chore(eng-2026-004): initialize research context
832111e chore(eng-2026-004): complete research synthesis
fabea4a feat(eng-2026-004): complete requirements discovery — COMPREHENSIVE
d83cc87 feat(eng-2026-004): complete architecture design — COMPREHENSIVE
8e08b71 feat(eng-2026-004): complete security review — STRIDE + HIPAA
939cd9d feat(eng-2026-004): complete estimation — 12-week, $1.2M Phase 1
d31b9f2 feat(eng-2026-004): complete project plan — 12 weeks, 6 sprints
2192c1d feat(eng-2026-004): assemble 12-slide presentation with speaker notes
01ff98d feat(eng-2026-004): complete review — 8.8/10 PASS
244d207 fix(eng-2026-004): fix review schema compliance
ab1528c feat(eng-2026-004): implementation prompt — demo scoped
9247dde chore(eng-2026-004): final QA complete — all checks pass
```

---

*Generated by the Solutions Architecture Agent (v1.1.1) — a Claude Code plugin by Modular Earth LLC*
