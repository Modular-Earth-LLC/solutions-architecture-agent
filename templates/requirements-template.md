# Requirements Discovery Template

Output template aligned with `/requirements` skill output fields and `requirements.schema.json`.

---

## Client Context

- **Legal Name**: [Client legal entity name]
- **Brand Name**: [Trade name, if different]
- **Industry**: [Industry vertical]
- **Company Size**: [startup / smb / mid_market / enterprise]
- **AI Maturity**: [beginner / intermediate / advanced]
- **AI History**: [Prior AI/ML experience, if any]

---

## Problem Statement

**Title**: [One-line problem title]

**Summary**: [2-3 sentence problem description]

**Current State**:
- Process: [How things work today]
- Tools in use: [List current tools/systems]
- Pain points: [Classified list of pain points]
- Annual cost: [Current cost of the problem]
- Volume: [Scale/throughput metrics]

**Desired State**:
- Description: [What success looks like]
- Target improvements: [Measurable targets]

---

## AI Suitability Assessment

- **Score**: [1-10]
- **Recommendation**: [strong_fit / good_fit / conditional_fit / poor_fit / not_recommended]
- **Rationale**: [Why this score]
- **Favorable Factors**: [List]
- **Risk Factors**: [List]

---

## Pain Points

[Classified list from discovery — each with category and severity]

---

## Functional Requirements

| ID | Title | Priority | Complexity | Acceptance Criteria |
|----|-------|----------|------------|-------------------|
| FR-001 | [Title] | must_have / should_have / nice_to_have | low / medium / high / very_high | [Criteria] |

---

## Non-Functional Requirements

**Performance**: Response time p95: [N]ms, Throughput: [N] rps, Concurrent users: [N]
**Availability**: Target: [N]%, Maintenance window: [schedule]
**Scalability**: Current volume: [N], Growth: [%/year], Peak multiplier: [N]x
**Security**: Authentication: [method], Authorization: [model], Data classification: [level]
**Data Residency**: Required regions: [list], Retention: [N] days

---

## Data Landscape

**Sources**:
| Name | Type | Format | Volume | PII Present | Quality Notes |
|------|------|--------|--------|-------------|---------------|
| [Source] | database / api / file / wiki / streaming | [Format] | [Volume] | yes / no | [Notes] |

**Integration Points**:
| System | Direction | Protocol | Auth Method |
|--------|-----------|----------|-------------|
| [System] | read / write / bidirectional | [Protocol] | [Auth] |

---

## Constraints

- **Budget**: [Range]
- **Timeline**: [N] weeks, Flexibility: [hard / moderate / soft]
- **Technology Restrictions**: [List]
- **Team Constraints**: [Description]

---

## Success Criteria

| ID | Metric | Baseline | Target | Measurement | Timeframe |
|----|--------|----------|--------|-------------|-----------|
| SC-001 | [Metric] | [Current] | [Target] | [How measured] | [When] |

---

## Stakeholders

| Name | Role | Type | Approval Authority | Communication Preference |
|------|------|------|--------------------|--------------------------|
| [Name] | [Role] | decision_maker / contributor / end_user / reviewer | [Authority] | [Preference] |

---

## Scope Boundaries

**In Scope**: [List]
**Out of Scope**: [List with justification]

---

## Assumptions

- [Documented assumption 1]
- [Documented assumption 2]

---

## Metadata

- **Discovery Tier**: [quick / standard / comprehensive]
- **Discovery Date**: [YYYY-MM-DD]
- **Participants**: [List]
- **Completeness**: [incomplete / partial / complete]
