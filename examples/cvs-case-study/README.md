# Case Study: CVS Health Legacy System Transformation

> **Status**: Case study planning artifacts are archived in `.claude/plans/archive/` (not publicly visible). This README documents the methodology and lessons learned. The actual deliverables are in `outputs/cvs-legacy-transformation/`.

This case study demonstrates the SA Agent executing a full migration engagement — from a take-home interview assignment to a complete solution architecture document.

## Assignment

A Principal Architect candidate was given a case study: propose a modernization approach for CVS Health's IBMi green screen pharmacy benefits management system serving 500+ users.

**Input**: `PAI-Take_Home_Exercise.pdf` and `assignment-brief.md`

## Final Deliverables

Located in `outputs/cvs-legacy-transformation/`:

| File | Description |
|------|-------------|
| `solution-architecture-document.md` | 55-page solution architecture (condensed to 284 lines for submission) |
| `solution-architecture-presentation.md` | Executive presentation version |
| `ux-design-document.md` | UX research with 5 personas, 3 workflows, WCAG 2.2 AA |
| `iam-strategy.md` | Identity and access management strategy |
| `research-findings.md` | 9 research clusters, 54 sources |
| `ai-methodology.md` | GenAI pipeline design methodology |
| `honesty-map.md` | Transparent experience-to-assignment mapping |
| `*.docx` | Word exports via pandoc + mmdc |

## How It Was Built

The engagement used the **migration** canonical flow across 8 phases using a combination of SA Agent skills and manual research:

| Phase | Skills Used |
|-------|------------|
| 0: Research & Requirements | `/requirements` (comprehensive) |
| 1: UX & Workflow Design | WebSearch + manual |
| 2: Solution Architecture | `/integration-plan`, `/architecture`, `/data-model` |
| 3: Security & IAM | `/security-review` |
| 4: Estimation & Planning | `/estimate`, `/project-plan` |
| 5: AI Methodology | WebSearch + manual |
| 6: Deliverable Assembly | `/proposal` (custom) |
| 7: Interview Prep | Manual |

Phase planning artifacts (phase plans, context files, master plan) are archived and not included in this repository.

## Lessons Learned

This engagement exposed the design flaws that led to v1.1.0:

1. **13 hours** across 8 phases for a ~10-page document
2. **5,919 lines** of KB JSON produced, then manually condensed to **284 lines**
3. No scope negotiation — agent treated an interview assignment like a full consulting engagement
4. 18 sub-agent invocations where inline scoring would suffice

These findings drove the v1.1.0 overhaul: depth tiers, deliverable-first mode, QUICK depth, skeleton-first generation. See `CHANGELOG.md` for details.

## Using This as a Reference

To run a similar engagement with the v1.1.0 improvements:

```
"Write a 10-page solution architecture for modernizing a legacy healthcare system.
 Target audience: interview panel. --depth QUICK"
```

This would use the **Direct Delivery** flow and complete in a single pass.
