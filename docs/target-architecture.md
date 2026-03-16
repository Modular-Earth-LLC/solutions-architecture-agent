# Target Architecture Reference

## Overview

The solutions-architecture-agent will be a **single agent** that orchestrates the complete solutions architecture lifecycle through **skills** rather than separate agent prompts.

## Deployment Model

### 1. Claude Code CLI (Local, Primary)

```
~/.claude/                              # User-level config
C:\dev\solutions-architecture-agent/
├── CLAUDE.md                           # Core agent identity + always-loaded context
├── .claude/
│   ├── settings.json                   # Project permissions and hooks
│   ├── rules/                          # Scoped instructions loaded on demand
│   ├── skills/                         # Lifecycle skills (slash commands)
│   │   ├── requirements/SKILL.md       # /requirements
│   │   ├── architecture/SKILL.md       # /architecture
│   │   ├── deployment/SKILL.md         # /deployment
│   │   └── ...
│   ├── agents/                         # Subagents for parallel work
│   └── plans/references/               # Planning reference materials
├── knowledge_base/                     # On-demand reference data
└── templates/                          # Output templates
```

**How it works locally:**
- `CLAUDE.md` defines the agent's identity and core capabilities
- Skills are invoked via `/skill-name` in Claude Code CLI
- Rules load contextually based on which files are being edited
- Knowledge base files are read on-demand, not always loaded
- Subagents handle parallel review/analysis tasks

### 2. Anthropic Cloud Platform (SaaS, Future)

```
Deployed Agent Service:
├── System Prompt          ← Built from CLAUDE.md + core rules
├── Skills/Tools           ← Mapped from .claude/skills/
├── Reference Files        ← Mapped from knowledge_base/
└── API Endpoint           ← Accessible by other Solutions Architects
```

**How it works in cloud:**
- System prompt compiled from CLAUDE.md + selected rules
- Skills become tool definitions in the agent API
- Knowledge base uploaded as retrievable context
- Accessed over API by other users (SaaS model)

## Context Budget Strategy

To stay within context limits, the agent uses a layered loading approach:

| Layer | Loaded When | Size Target |
|-------|-------------|-------------|
| CLAUDE.md | Always | < 200 lines |
| Rules (unscoped) | Session start | < 100 lines total |
| Rules (scoped) | When matching files opened | As needed |
| Skills | On invocation only | No limit |
| Knowledge base | On explicit reference | No limit |
| Subagent context | Isolated per agent | Separate window |

## Key Design Decisions

1. **Single agent, not multi-agent** — skills replace agent routing
2. **Lazy loading** — only load context when needed
3. **Skills are self-contained** — each skill has all instructions needed to complete its task
4. **Knowledge base is reference, not context** — read on demand, not injected into every conversation
5. **Cloud-compatible structure** — skills map to API tools, CLAUDE.md maps to system prompt
