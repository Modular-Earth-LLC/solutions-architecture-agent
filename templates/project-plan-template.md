# Project Plan Template

Output template aligned with `/project-plan` skill and `project_plan.schema.json`.

## Document Metadata

- **Engagement ID**: [eng-YYYY-NNN]
- **Version**: [MAJOR.MINOR]
- **Date**: [YYYY-MM-DD]
- **Depth Tier**: [QUICK / STANDARD / COMPREHENSIVE]

## Depth Tier Guidance

| Tier | Required Sections | Optional Sections | Target Length |
|------|-----------------|------------------|---------------|
| QUICK | Phase Table, Timeline | All others | 1-2 pages |
| STANDARD | Phase Table, Sprint Plan, Risk Register, Milestones | Communication Plan | 4-8 pages |
| COMPREHENSIVE | All sections | None | 8-15 pages |

---

## Phase Overview

| Phase | Weeks | Key Deliverables | Team | Decision Gate |
|-------|-------|-----------------|------|---------------|
| Foundation | 1-2 | Dev environment, CI/CD, auth skeleton | [N] FTE | Gate 1 |
| Core Development | 3-6 | Business logic, primary UI, API layer | [N] FTE | Gate 2 |
| AI Integration | 7-10 | AI/ML components, orchestration | [N] FTE | — |
| Testing & Polish | 11-12 | Integration tests, security hardening | [N] FTE | Gate 3 |
| Launch | 13-14 | Production deploy, monitoring, docs | [N] FTE | — |
| **Total** | **[N] weeks** | | | |

---

## Sprint Plan

| Sprint | Dates | Goal | Points | Key Features | Dependencies |
|--------|-------|------|--------|-------------|-------------|
| S1 | [Date] | [Goal] | [N] | [Features] | [Deps] |
| S2 | [Date] | [Goal] | [N] | [Features] | [Deps] |

---

## Decision Gates

| Gate | Timing | GO Criteria | Decision Owner |
|------|--------|------------|----------------|
| Gate 1 | Post-Architecture | Strategic alignment, ROI >3x, resources available | [Owner] |
| Gate 2 | Post-MVP (~Week 6) | Core features working, user feedback >7/10 | [Owner] |
| Gate 3 | Pre-Production | Acceptance tests passed, security audit complete | [Owner] |

---

## Risk Register

| ID | Description | Category | Likelihood | Impact | Risk Score | Mitigation | Owner |
|----|------------|---------|-----------|--------|-----------|-----------|-------|
| R-001 | [Description] | Technical | H/M/L | H/M/L | [1-10] | [Mitigation] | [Owner] |

---

## Dependencies

| ID | Description | Owner | Needed By | Fallback |
|----|------------|-------|-----------|---------|
| D-001 | [External dependency] | [Owner] | [Date] | [Fallback plan] |

---

## Milestones

| Milestone | Target Date | Phase | Gate Type | Success Criteria |
|-----------|------------|-------|-----------|-----------------|
| [Name] | [Date] | [Phase] | Approval / Demo / Signoff | [Criteria] |
