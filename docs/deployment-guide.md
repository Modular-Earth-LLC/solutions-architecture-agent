# Deployment Guide

**Version**: See `.repo-metadata.json` | **Status**: Alpha

Deploy this framework to: Claude Code CLI • Claude Projects • GitHub Copilot

---

## Quick Start (Claude Code CLI - Recommended)

**2 minutes to running**:

```bash
git clone https://github.com/Modular-Earth-LLC/solutions-architecture-agent.git
cd solutions-architecture-agent
claude
```

**Done!** Claude Code automatically loads:
- `CLAUDE.md` — agent identity and core context
- `.claude/rules/` — scoped instructions loaded contextually
- `.claude/settings.json` — project permissions and hooks
- `.claude/skills/` — slash-command workflows (as they're added)

### Using Skills

Once skills are migrated from agent prompts, invoke them with:
```
/requirements    — Run a requirements discovery workshop
/architecture    — Design system architecture + cost estimates
/deployment      — Generate deployment guides
```

---

## Claude Projects

**10 minutes**:

1. Upload to project knowledge:
   - `knowledge_base/system_config.json`
   - `ai_agents/*.md` (all agents)

2. Custom Instructions:
   - Paste `supervisor_agent.system.prompt.md`

3. Test: "Help me build an AI system"

**Limitation**: ~32K character limit per custom instruction

---

## GitHub Copilot (CI/CD and Git Management)

GitHub Copilot is configured for CI/CD automation and git management, not as the primary development assistant.

1. `.github/copilot-instructions.md` is pre-configured
2. Use `@workspace` in VS Code for CI/CD tasks
3. Copilot manages GitHub Actions, PR automation, and code reviews

---

## Deploy Generated Systems

After building a system with this framework:

### To Claude Code CLI
- Copy generated code to a new project directory
- Add a `CLAUDE.md` with project-specific context

### To Claude Projects
- Upload generated code as project knowledge
- Use generated custom instructions

### To AWS Bedrock
- Follow generated deployment guide
- Use CDK/CloudFormation from Engineering agents

---

## Troubleshooting

**"Agent not responding"**: Check Claude Code CLI is running and `CLAUDE.md` exists
**"Can't find file"**: Ensure you're in the repo root directory
**"Out of context"**: Use `.claude/rules/` with path scoping to reduce always-loaded content

---
