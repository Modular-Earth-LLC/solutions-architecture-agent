# Human-AI Collaboration Guide

**Key Principle**: The agent **augments** your expertise — it doesn't replace your judgment.

---

## Core Pattern

**Agent GENERATES → YOU REVIEW → YOU APPROVE → YOU DELIVER**

| The Agent Does | You Do |
|----------------|--------|
| Discover requirements through structured questions | Answer questions, validate completeness |
| Design architectures with WA scoring | Select approach, approve trade-offs |
| Model data structures and relationships | Validate domain accuracy |
| Identify security threats (STRIDE) | Prioritize mitigations, accept risk |
| Plan integrations and migrations | Confirm constraints, approve sequencing |
| Estimate effort, cost, team composition | Validate assumptions, approve budgets |
| Generate project plans with sprints | Adjust timelines, approve milestones |
| Assemble proposals from deliverables | Review, customize, deliver to client |
| Review deliverables (LLM-as-judge) | Interpret scores, decide on revisions |

---

## What the Agent Never Does

- Commit code or push to repositories
- Deploy to any environment
- Send deliverables to clients
- Make business or budget decisions
- Spend money or provision resources
- Auto-advance to the next skill without your approval

---

## Human Checkpoints

Every skill pauses at completion and presents:

1. **Summary** of what was produced
2. **Deliverables** created or updated (file paths)
3. **Suggested next skill** in the engagement flow

You decide whether to:
- Proceed to the suggested next skill
- Re-run the current skill with adjustments
- Skip ahead in the flow
- Stop and review deliverables

---

## Automation Levels

| Level | Mode | Agent Behavior | Your Role |
|-------|------|---------------|-----------|
| **1 — Advisory** | Default for all skills | Generates recommendations | Review, decide, execute |
| **2 — Structured** | Requirements, Estimation | Asks questions, structures answers | Answer, validate, approve |
| **3 — Analytical** | Architecture, Security | Designs + scores + recommends | Select, approve trade-offs |

Even at Level 3, the agent never acts without your explicit approval.

---

## Scope Boundary

| This Agent Does (Design) | Future Engineering Agent (Implementation) |
|--------------------------|------------------------------------------|
| Requirements discovery | Code generation |
| System architecture | Deployment scripts |
| Data modeling | CI/CD pipelines |
| Security review | Infrastructure provisioning |
| Integration planning | Testing implementation |
| Cost estimation | Monitoring setup |
| Project planning | Production operations |
| Proposal assembly | — |

If you request implementation, the agent acknowledges the request, explains its design-only scope, and notes the request for a future Engineering Agent.

---

## Guiding Principle

> "Human review is mandatory before client-facing deliverables. AI assists the SA; the SA owns the output. Never send unreviewed AI work to clients."
>
> — Principle #42, guiding-principles.md
