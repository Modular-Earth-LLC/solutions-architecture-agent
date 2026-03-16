# Workflow Guide

How skills connect through the engagement lifecycle.

---

## Quick Reference

| Phase | Skill | Input | Output |
|-------|-------|-------|--------|
| Requirements | `/requirements` | Client conversation | `requirements.json` |
| Architecture | `/architecture` | `requirements.json` | `architecture.json` |
| Data Modeling | `/data-model` | `architecture.json` | `data_model.json` |
| Security Review | `/security-review` | `architecture.json` | `security_review.json` |
| Integration Plan | `/integration-plan` | `requirements.json` + `architecture.json` | `integration_plan.json` |
| Estimation | `/estimate` | All upstream KB files | `estimate.json` |
| Project Plan | `/project-plan` | `requirements.json` + `architecture.json` + `estimate.json` | `project_plan.json` |
| Proposal | `/proposal` | All upstream KB files | `outputs/*.md` |
| Review | `/review` | All upstream KB files | `reviews.json` |

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

## Re-running Skills (Mid-Engagement Changes)

When requirements or other upstream deliverables change mid-engagement:

1. **Re-run the changed skill first** — e.g., re-run `/requirements` with updated context
2. **Re-run downstream skills in order** — each skill reads the latest KB files, so downstream outputs automatically reflect upstream changes
3. **You do not need to re-run skills that are not downstream** — if only requirements changed, `/integration-plan` needs re-running but `/review` of a different file does not

The agent tracks versions in `engagement.json`. When you re-run a skill, it increments the MINOR version of that KB file.

---

## Starting a New Engagement

To start fresh after completing an engagement:

1. Archive current KB files: copy `knowledge_base/*.json` (except `system_config.json`) to `examples/<engagement-name>/`
2. Delete the archived files from `knowledge_base/`
3. Run `/requirements` to begin the new engagement

---

## Key Principles

- **Skills design solutions — they don't implement them.** Code generation, deployment, and infrastructure provisioning are out of scope.
- **You always approve.** The agent generates, you review and decide.
- **Technology-agnostic.** The agent uses web search to recommend best-fit technology, not defaults.
- **Well-Architected compliance.** Every architecture is scored against AWS 6 pillars + GenAI Lens.
