# Proposal Template

Output template aligned with `/proposal` skill. Supports 4 proposal types.

## Document Metadata

- **Engagement ID**: [eng-YYYY-NNN]
- **Proposal Type**: [discovery / implementation / internal / pitch]
- **Version**: [MAJOR.MINOR]
- **Date**: [YYYY-MM-DD]
- **Depth Tier**: [QUICK / STANDARD / COMPREHENSIVE]

## Depth Tier Guidance

| Tier | Behavior | Target Length |
|------|----------|--------------|
| QUICK | Executive summary only — no SOW sections, no KB reads | 1-4 pages |
| STANDARD | Full proposal per type below | No limit |
| COMPREHENSIVE | Full proposal + competitive analysis + extended Q&A | No limit |

---

## Type A: Discovery Proposal

A 3-phase assessment proposal ($5K-$25K range, 2-6 weeks).

### Engagement Description

[One paragraph: what we are doing and why it matters to the client]

### Assessment Phases

**Phase 1 — Research & Planning** (Days 1-3)
- Stakeholder interviews
- System documentation review
- Goal alignment workshop

**Phase 2 — Technical Investigation** (Days 4-15)
- Architecture assessment
- Data flow analysis
- Security posture review

**Phase 3 — Analysis & Recommendation** (Days 16-END)
- Findings report
- Roadmap
- Go/No-Go recommendation

### Decision Scenarios

| Scenario | Description | Recommended Next Step |
|----------|------------|----------------------|
| Clear GO | Strong fit, low risk | Proceed to Implementation SOW |
| GO with Modifications | Viable with adjustments | Address gaps, re-scope |
| PAUSE | Needs more data | Define specific data needed |
| NO-GO | Not recommended | Document rationale |

---

## Type B: Implementation SOW (12 Sections)

### 1. Engagement Description
[From requirements.json client_context + engagement_type]

### 2. Business Objectives
[From requirements.json problem_statement + success_criteria — measurable KPIs]

### 3. Technical Requirements
[From requirements.json + architecture.json — MVP scope, tech choices, WA scores]

### 4. Team Leads and Roles
[From estimate.json team_composition — service provider roles + required client roles]

### 5. Project Scope
[From project_plan.json phases + estimate.json LOE — weekly deliverables with estimated cost]

### 6. Services Out of Scope
[From requirements.json scope_boundaries — explicit exclusions]

### 7. Change Order
Scope changes require mutual written execution. Either party may terminate with 10 business days written notice.

### 8. Anticipated Schedule
[From project_plan.json — start/end dates, hours/week, sprint methodology, acceptance process]

### 9. Project Rate
[From estimate.json — blended hourly rate, total estimate, payment schedule]

### 10. Payment Methods
Monthly invoices. Net 30 payment terms. ACH or wire transfer.

### 11. Assumptions
[From requirements.json assumptions + estimate.json caveats]

### 12. Signature Block
| Party | Name | Title | Signature | Date |
|-------|------|-------|-----------|------|
| Service Provider | | | | |
| Client | | | | |

---

## Type C: Internal Proposal (12-18 Slides)

**Audience differentiation**:
- CEO: Strategic alignment, market opportunity
- CFO: ROI (3 scenarios), payback period
- CTO: Technical feasibility, architecture overview
- VPs: Operational impact, timeline

[Executive summary: 2 pages, financial model, presenter guide, anticipated Q&A]

---

## Type D: Pitch Deck (10-15 Slides)

**Act 1 — The Challenge** (Slides 1-3): Current state pain, cost of inaction, market context

**Act 2 — The Solution** (Slides 4-11): Architecture overview, technology, team, timeline, investment options

**Act 3 — The Path Forward** (Slides 12-15): Phased investment options, 3 commitment options, next steps
