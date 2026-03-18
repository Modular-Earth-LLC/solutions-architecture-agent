---
name: Bug Report
about: Report an issue with an agent prompt, workflow, or configuration
title: '[Bug] '
labels: bug
assignees: praeducer
---

## Description
A clear description of the bug.

## Severity
<!-- Choose one -->
- [ ] **Critical** — skill crashes or produces empty output
- [ ] **High** — incorrect KB output, schema validation fails
- [ ] **Medium** — incorrect advice, missing depth tier behavior
- [ ] **Low** — wording, formatting, minor UX

## Skill/Agent Affected
<!-- Choose one -->
- [ ] `/requirements`
- [ ] `/architecture`
- [ ] `/estimate`
- [ ] `/project-plan`
- [ ] `/data-model`
- [ ] `/security-review`
- [ ] `/integration-plan`
- [ ] `/review`
- [ ] `/proposal`
- [ ] `parallel-wa-reviewer` (sub-agent)
- [ ] `stride-analyzer` (sub-agent)
- [ ] Dispatch / CLAUDE.md
- [ ] Other: ___

## Steps to Reproduce
1. Platform used (Claude Code CLI / Claude Desktop / VS Code)
2. Depth tier used (QUICK / STANDARD / COMPREHENSIVE)
3. What you asked the agent (paste your exact message)
4. What happened (paste relevant output)
5. What you expected instead

**Example of a useful reproduction:** "I typed `/architecture --depth QUICK` after running `/requirements`. The agent skipped scope negotiation and produced no executive summary."

## Expected Behavior
What should have happened?

## Additional Context
Paste relevant agent output or error messages (redact any sensitive info).
