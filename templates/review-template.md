# Review Template

Output template aligned with `/review` skill and `reviews.schema.json`.

## Document Metadata

- **Engagement ID**: [eng-YYYY-NNN]
- **Review ID**: [R-NNN]
- **Target File**: [path/to/file.json]
- **Target Version**: [MAJOR.MINOR]
- **Date**: [YYYY-MM-DD]
- **Depth Tier**: [QUICK / STANDARD / COMPREHENSIVE]

## Depth Tier Guidance

| Tier | Required Sections | Optional Sections | Target Length |
|------|-----------------|------------------|---------------|
| QUICK | Score Card, Top Findings | WA Pillar Scores, Improvement Plan | < 50 lines |
| STANDARD | All sections (3 iterations) | Cross-deliverable analysis | No limit |
| COMPREHENSIVE | All sections | None | No limit |

---

## Score Card

| Dimension | Iteration 1 | Iteration 2 | Iteration 3 (Final) |
|-----------|------------|------------|---------------------|
| Completeness (1-10) | [N] | [N] | **[N]** |
| Technical Soundness (1-10) | [N] | [N] | **[N]** |
| Well-Architected Alignment (1-10) | [N] | [N] | **[N]** |
| Clarity (1-10) | [N] | [N] | **[N]** |
| Feasibility (1-10) | [N] | [N] | **[N]** |
| **Overall (1-10)** | **[N]** | **[N]** | **[N]** |

**Pass/Fail**: [PASS (≥7.5) / CONDITIONAL PASS (5.0-7.4) / FAIL (<5.0)]

---

## WA Pillar Scores (architecture reviews only)

| Pillar | Score | Strengths | Gaps |
|--------|-------|-----------|------|
| Operational Excellence | [0-10] | [Strengths] | [Gaps] |
| Security | [0-10] | [Strengths] | [Gaps] |
| Reliability | [0-10] | [Strengths] | [Gaps] |
| Performance Efficiency | [0-10] | [Strengths] | [Gaps] |
| Cost Optimization | [0-10] | [Strengths] | [Gaps] |
| Sustainability | [0-10] | [Strengths] | [Gaps] |

---

## Findings

| ID | Priority | Severity | Description | Recommendation |
|----|---------|---------|------------|----------------|
| F-001 | P0 | Critical/High/Medium/Low | [Description] | [Advisory recommendation — SA must approve before applying] |

---

## Improvement Plan

| Priority | Item | Current State | Target State | Effort | Impact |
|---------|------|-------------|-------------|--------|--------|
| P0 | [Quick win] | [Current] | [Target] | Low | High |
| P1 | [Strategic] | [Current] | [Target] | High | High |

> **Note**: All improvement suggestions are advisory only. The SA must review and approve each recommendation before applying changes to any deliverable.

---

## Approval Decision

- **Decision**: [APPROVED / APPROVED WITH CONDITIONS / REJECTED]
- **Conditions (if any)**: [List conditions]
- **Reviewer**: [SA name]
- **Date**: [YYYY-MM-DD]
