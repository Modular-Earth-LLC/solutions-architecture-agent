# Deployment Guide

**Version**: 0.1.0-alpha | **Status**: Alpha

Deploy this framework to: Cursor IDE • Claude Projects • GitHub Copilot

---

## Quick Start (Cursor IDE - Recommended)

**5 minutes to running**:

1. Open Cursor → Settings → Chat → Custom Modes
2. Create mode: "Supervisor Agent"
3. Paste `supervisor_agent.system.prompt.md`
4. Enable "All tools"
5. Save & test: "Build a chatbot"

**Done!** Supervisor routes to specialized agents automatically.

### Optional: Install All Agents

Repeat for each agent in `ai_agents/`:
- Requirements, Architecture, Engineering Supervisor
- Deployment, Optimization, Prompt Engineering
- 16 engineering specialists (optional)

**Tip**: Start with Supervisor only. Add specialists as needed.

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

## GitHub Copilot (VS Code)

**15 minutes**:

1. Create `.github/copilot-instructions.md`
2. Paste `supervisor_agent.system.prompt.md`
3. Configure workspace in VS Code
4. Test: "@workspace build chatbot"

**Note**: Copilot integration experimental

---

## Deploy Generated Systems

After building a system with this framework:

### To Cursor
- Copy generated code to new project
- Install as custom mode (if agent-based)

### To Claude Projects
- Upload generated code as project knowledge
- Use generated custom instructions

### To AWS Bedrock
- Follow generated deployment guide
- Use CDK/CloudFormation from Engineering agents

---

## Troubleshooting

**"Agent not responding"**: Check tools enabled  
**"Can't find file"**: Ensure workspace root correct  
**"Out of memory"**: Install individual agents, not all 23

---

**Version**: 0.1.0-alpha | **Updated**: 2025-10-12
