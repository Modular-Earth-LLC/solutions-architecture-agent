# Solutions Architecture Agent

## What This Repository Is

A specialized AI agent system for the **solutions architecture lifecycle**: ideation, requirements gathering, architecture design, team composition, cost estimation, and deployment planning. Built by a Principal Solutions Architect / AI Engineer at Modular Earth LLC.

**Dual deployment targets:**
1. **Local**: System prompt + skills for the Claude Code CLI (primary, daily driver)
2. **Cloud**: Packaged as a service on Anthropic's cloud platform for other Solutions Architects (future SaaS product)

## Repository Structure

```
solutions-architecture-agent/
├── CLAUDE.md                              # This file — Claude Code project context
├── supervisor_agent.system.prompt.md      # Main supervisor (entry point prompt)
├── ai_agents/                             # 22 specialized agent system prompts
│   ├── *_agent.system.prompt.md           # Each agent is a standalone prompt
├── knowledge_base/                        # Shared state (JSON + schemas)
│   ├── system_config.json                 # READ-ONLY config (150+ tech refs, Well-Architected)
│   ├── user_requirements.json             # Written by Requirements Agent
│   ├── design_decisions.json              # Written by Architecture Agent
│   └── schemas/                           # JSON Schema validation
├── user_prompts/                          # 69 task-specific user prompts
│   ├── architecture/                      # Architecture workflows
│   ├── requirements/                      # Discovery workshops
│   ├── engineering/                       # Specialist tasks
│   ├── deployment/                        # Deployment guides
│   ├── proposals/                         # Proposal generation
│   ├── prompt_engineering/                # Self-improvement
│   └── self_improvement/                  # Agent optimization
├── docs/                                  # User documentation
├── templates/                             # Reusable templates
├── tests/                                 # Validation scripts
├── outputs/                               # Generated outputs (git-ignored content)
├── private/                               # Sensitive data (git-ignored content)
├── .repo-metadata.json                    # Single source of truth for version/counts
└── .github/                               # GitHub community files + CI
```

## Key Conventions

- **Agent prompts** are markdown files ending in `.system.prompt.md` — they are the core product
- **User prompts** are markdown files ending in `.user.prompt.md` — task-specific instructions
- **Knowledge base** files are JSON validated against schemas in `knowledge_base/schemas/`
- **`.repo-metadata.json`** is the single source of truth for version, agent counts, and prompt counts — never hard-code these values elsewhere
- **`system_config.json`** is READ-ONLY at runtime — agents reference it but never modify it
- **`user_requirements.json`** and **`design_decisions.json`** are written by agents during workflows

## Architecture Pattern

Two-layer supervisor-worker:
- **Supervisor Agent** routes requests to domain agents
- **5 Top-Level Domain Agents**: Requirements, Architecture, Deployment, Optimization, Prompt Engineering
- **Engineering Supervisor** coordinates 16 technology specialists
- **16 Engineering Specialists**: Anthropic Claude (5), AWS Bedrock (2), UI/Framework (2), Orchestration (2), Infrastructure (3), DevOps (2)

## Current Project Goals

This repo is being **refactored from a multi-agent system into a highly specialized single-agent system with skills**. The 23 agent prompts are being consolidated into:
1. A single solutions architecture agent system prompt
2. A set of skills that the agent can invoke (mapped from the current agent prompts)
3. Reference files the agent loads as needed (mapped from knowledge base)

The target platforms are:
- **Claude Code CLI** (local, primary) — system prompt in CLAUDE.md, skills as Claude Code skills
- **Anthropic Cloud Platform** (SaaS, future) — deployed as an API-accessible agent service

## Working With This Repo

When editing agent prompts:
- Preserve the existing prompt structure and section headers
- Keep cross-references between agents consistent
- Update `.repo-metadata.json` if adding or removing agents/prompts
- Validate knowledge base JSON against schemas after changes
- Test prompts in Claude Code CLI or Cursor IDE before committing

When refactoring:
- The goal is to collapse 23 agents into 1 agent + N skills
- Each current agent prompt maps to a potential skill
- The supervisor prompt becomes the core system prompt
- Knowledge base files become reference files loaded on demand
- User prompts become skill invocation templates

## Tech Stack

- **Language**: Python 3.12+
- **UI**: Streamlit (for prototypes)
- **LLM**: Anthropic Claude, AWS Bedrock
- **Orchestration**: LangChain, MCP, Strands SDK, AgentCore
- **Platforms**: Claude Code CLI, Cursor IDE, Claude Projects, GitHub Copilot, AWS Bedrock
- **Validation**: JSON Schema (Draft 2020-12), pytest

## Quality Standards

- AWS Well-Architected Framework compliance (6 pillars + GenAI Lens)
- TRM (Test-Time Recursive Majority) validation for generated outputs
- Code coverage >= 80%, type hints >= 90% for any Python code
- No secrets in version control — use `private/` directory for sensitive outputs
