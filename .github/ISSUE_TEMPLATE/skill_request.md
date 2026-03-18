---
name: Skill Request
about: Propose a new SA lifecycle skill for the plugin
title: '[Skill] '
labels: enhancement, skill
assignees: praeducer
---

## Skill Name
What would the slash command be? (e.g., `/risk-analysis`)

**Naming convention**: Skill names must be kebab-case and verb-based (e.g., `risk-analysis`, not `riskAnalysis` or `risk_analysis`).

**Example of a well-formed skill request**: `/risk-analysis` — a skill that runs a dedicated risk identification and scoring session after architecture is complete, producing a `risk_analysis.json` KB file with categorized risks, likelihood/impact scores, and mitigation strategies. Depends on `architecture.json` and `requirements.json`. Fits between `/architecture` and `/estimate` in the Greenfield flow.

## Purpose
What SA lifecycle phase does this cover? What problem does it solve?

## Engagement Flow Position
Where does this skill fit in the canonical flows (Greenfield, Migration, Streamlined, etc.)?

## Upstream Dependencies
Which existing KB files would this skill read? (`$depends_on`)

## Output
What KB file would this skill produce? What key fields?

## Additional Context
Reference materials, examples, or related skills. See [CONTRIBUTING.md § How to Add a New Skill](../../CONTRIBUTING.md#how-to-add-a-new-skill) for implementation requirements.
