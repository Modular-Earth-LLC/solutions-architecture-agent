# AI Solutions Architecture Agent

An AI agent for the **solutions architecture lifecycle**: requirements discovery, system design, data modeling, security review, integration planning, estimation, project planning, and proposal assembly. Designs solutions — does NOT implement or deploy.

**Owner**: Modular Earth LLC (@paulpham157)
**License**: MIT
**Platform**: Claude Code plugin (local + marketplace)

## Current Status: Refactoring In Progress

This repo is being consolidated from 23 agents into **1 agent + 9 skills** per the master plan at @.claude/plans/master-plan.md. Execute phases sequentially — each phase has a human checkpoint.

**Phase execution**: `claude -p "$(cat .claude/plans/phase-N-prompt.md)"`

## Target Repository Layout (Plugin Structure)

```
solutions-architecture-agent/           # Plugin root
├── .claude-plugin/plugin.json          # Plugin manifest
├── skills/                             # 9 SA skills (Agent Skills standard)
│   ├── requirements/SKILL.md           # /requirements
│   ├── architecture/SKILL.md           # /architecture
│   ├── estimate/SKILL.md               # /estimate
│   ├── project-plan/SKILL.md           # /project-plan
│   ├── proposal/SKILL.md               # /proposal
│   ├── data-model/SKILL.md             # /data-model
│   ├── security-review/SKILL.md        # /security-review
│   ├── integration-plan/SKILL.md       # /integration-plan
│   └── review/SKILL.md                 # /review (LLM-as-judge, 3 iterations)
├── agents/                             # Subagent definitions
├── hooks/hooks.json                    # Hook configuration
├── knowledge_base/                     # 10 JSON state files + schemas
├── templates/                          # Output document templates
├── tests/                              # Validation scripts
├── .claude/                            # Project config (settings, rules, plans)
└── CLAUDE.md                           # This file
```

## Key Rules

- **`.repo-metadata.json`** is the single source of truth — never hard-code version or counts
- **`system_config.json`** is READ-ONLY — reference but never modify
- New capabilities go into `skills/` (plugin root), not `.claude/skills/`
- Validate JSON: `python tests/validate_knowledge_base.py`
- Use `gh` CLI for all GitHub operations (authenticated in settings)

## Scope Boundary

This agent **designs and plans**. A future AI Engineering Agent **implements and deploys**.

| This Agent Does | Engineering Agent Does (Future) |
|----------------|-------------------------------|
| Requirements discovery | Code generation |
| System architecture | Deployment scripts |
| Data modeling | CI/CD pipelines |
| Security review | Prompt engineering |
| Integration planning | Testing implementation |
| Cost estimation | Infrastructure provisioning |
| Project planning | Monitoring setup |
| Proposal assembly | Production operations |

## Quality Standards

- Well-Architected compliance (AWS 6 pillars + GenAI Lens, Azure WAF, GCP WAF)
- Exemplar-level deliverable quality
- Technology-agnostic — recommend best-fit, never default to specific vendors
- Dynamic references via WebSearch — always use latest best practices
- @.claude/rules/guiding-principles.md — 42 core values governing all work

## Git Workflow

Each phase: execute → `git add` → `git commit` → **human reviews and improves** → push to main
