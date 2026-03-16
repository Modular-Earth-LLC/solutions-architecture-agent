# Workflow Guide

How skills connect through the engagement lifecycle.

---

## Quick Reference

| Phase | Skill | Input | Output | Time |
|-------|-------|-------|--------|------|
| Requirements | `/requirements` | Client conversation | `requirements.json` | 15-60 min |
| Architecture | `/architecture` | `requirements.json` | `architecture.json` | 30-60 min |
| Data Modeling | `/data-model` | `architecture.json` | `data_model.json` | 20-40 min |
| Security Review | `/security-review` | `architecture.json` | `security_review.json` | 20-40 min |
| Integration Plan | `/integration-plan` | `requirements.json` + `architecture.json` | `integration_plan.json` | 20-40 min |
| Estimation | `/estimate` | All upstream KB files | `estimate.json` | 15-30 min |
| Project Plan | `/project-plan` | `requirements.json` + `architecture.json` + `estimate.json` | `project_plan.json` | 15-30 min |
| Proposal | `/proposal` | All upstream KB files | `outputs/*.md` | 10-20 min |
| Review | `/review` | All upstream KB files | `reviews.json` | 10-20 min |

---

## Engagement Flows

### Greenfield (Complete 0-to-1)

```
/requirements → /architecture → /data-model → /security-review → /estimate → /project-plan → /proposal → /review
```

Use when designing a new system from scratch. Every skill runs in sequence, building on upstream deliverables.

### Migration

```
/requirements → /integration-plan → /architecture → /data-model → /security-review → /estimate → /project-plan → /proposal → /review
```

Use for legacy modernization. Note: `/integration-plan` runs **before** `/architecture` because migration constraints (APIs, data flows, legacy bridging) inform the target architecture.

### Streamlined

```
/requirements → /architecture → /estimate → /proposal
```

Use for small projects or time-constrained engagements. Skips data modeling, security review, integration planning, and project planning.

### Assessment

```
/requirements → /architecture → [/security-review] → /proposal
```

Use for discovery-only engagements (pre-commitment). Security review is optional (brackets).

### Quick Qualify

```
/requirements (quick tier)
```

Use for pipeline qualification. The requirements skill has a "quick" tier that asks fewer questions and produces a lightweight assessment.

---

## How Skills Communicate

Skills use the **blackboard pattern** — they communicate exclusively through JSON files in `knowledge_base/`:

1. Each skill **reads** its upstream dependencies (declared in `$depends_on`)
2. Each skill **writes** to exactly one output file it owns
3. `engagement.json` tracks lifecycle state for all domain files
4. Prerequisites are validated before each skill runs

If a prerequisite is missing, the agent tells you which skill to run first.

---

## Human Checkpoints

After every skill completes, the agent presents:

1. **Summary** — What was produced and key findings
2. **Deliverables** — Files created or updated
3. **Next skill** — Suggested next step in the engagement flow

You review, approve, and decide whether to proceed. The agent never auto-advances to the next skill without your input.

---

## Key Principles

- **Skills design solutions — they don't implement them.** Code generation, deployment, and infrastructure provisioning are out of scope.
- **You always approve.** The agent generates, you review and decide.
- **Technology-agnostic.** The agent uses web search to recommend best-fit technology, not defaults.
- **Well-Architected compliance.** Every architecture is scored against AWS 6 pillars + GenAI Lens.
