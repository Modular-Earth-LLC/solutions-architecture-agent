# Getting Started

Get productive in 15 minutes.

<!-- Version in .repo-metadata.json -->

---

## Prerequisites

- Cursor IDE (recommended) OR Claude Projects OR GitHub Copilot
- Git (to clone repository)
- Basic understanding of AI/LLMs

---

## 5-Minute Setup

**1. Clone**:
```bash
git clone https://github.com/Modular-Earth-LLC/solutions-architecture-agent.git
cd solutions-architecture-agent
```

**2. Deploy to Cursor** (recommended):
- Open Cursor → Settings → Chat → Custom Modes
- Create "Supervisor Agent" mode
- Paste `supervisor_agent.system.prompt.md`
- Enable "All tools" → Save

**3. Test**:
- Open AI Pane (Ctrl+Shift+L)
- Select "Supervisor Agent"
- Type: "Build a customer support chatbot"
- Watch it work!

---

## Your First AI System

**Build a Streamlit chatbot with Claude (30 min)**:

1. "I need a Streamlit chat interface with Claude"
2. Supervisor routes to → Streamlit UI + Claude Code agents
3. They generate code
4. YOU review code
5. Copy to new project
6. Run: `streamlit run app.py`

**YOU always approve before using generated code.**

---

## Understanding the System

**Specialized agent system** (see `.repo-metadata.json` for counts):
- **1 Main Supervisor**: Routes your requests
- **5 Top-Level Domain Agents**: Requirements, Architecture, Deployment, Optimization, Prompt Engineering
- **1 Engineering Supervisor**: Second-tier orchestrator coordinating 16 technology specialists
- **16 Engineering Specialists**: Each focused on one technology (Streamlit, Claude Code, AWS Bedrock, etc.)

**How it works**:
1. You make request
2. Supervisor identifies which agent(s) needed
3. Agents generate code/docs/configs
4. YOU review and approve
5. YOU deploy when ready

**Key**: Agents AUGMENT you, don't replace you. See `docs/human-ai-collaboration.md`.

---

## Common Workflows

**Get requirements**:
"Help me discover requirements for [project]"
→ Requirements Agent asks questions

**Design architecture**:
"Design architecture for [system]"  
→ Architecture Agent creates design + estimates

**Build prototype**:
"Build a Streamlit app that does [X]"
→ Engineering agents generate code

**Optimize system**:
"Optimize my AI system at [path]"
→ Optimization Agent analyzes + improves

---

## Security & Sensitive Data

**Protecting sensitive information:**

If you're working with proprietary designs, sensitive data, or confidential information:

1. Use the `private/` directory for any sensitive files
2. Read `private/README.md` for comprehensive security guidelines
3. Instruct AI agents to save sensitive outputs to `private/sensitive-ai-agent-outputs/`
4. Verify with `git status` that sensitive files are never staged for commit

**The `private/` directory is automatically excluded from Git** but provides local workspace for development with sensitive content.

---

## Next Steps

**Learn more**:
- `docs/workflow_guide.md` - Detailed workflows
- `docs/engineering-agents-guide.md` - All 16 specialists
- `docs/human-ai-collaboration.md` - Your role vs agent role
- `private/README.md` - Security guidelines for sensitive data

**Get help**:
- GitHub Issues: Bug reports, feature requests
- Discussions: Questions, community support

---

