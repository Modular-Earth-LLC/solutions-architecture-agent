# Getting Started

**Version**: 0.1.0-alpha | **Status**: Alpha - First-time use guide

Get productive in 15 minutes.

---

## Prerequisites

- Cursor IDE (recommended) OR Claude Projects OR GitHub Copilot
- Git (to clone repository)
- Basic understanding of AI/LLMs

---

## 5-Minute Setup

**1. Clone**:
```bash
git clone https://github.com/your-org/multi-agent-ai-development-framework
cd multi-agent-ai-development-framework
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

**23 specialized agents**:
- **1 Main Supervisor**: Routes your requests
- **5 Top-Level**: Requirements, Architecture, Deployment, Optimization, Prompt Engineering
- **1 Engineering Supervisor**: Coordinates 16 specialists
- **16 Engineering Specialists**: One technology each (Streamlit, Claude Code, AWS Bedrock, etc.)

**How it works**:
1. You make request
2. Supervisor identifies which agent(s) needed
3. Agents generate code/docs/configs
4. YOU review and approve
5. YOU deploy when ready

**Key**: Agents AUGMENT you, don't replace you. See `docs/HUMAN_AI_COLLABORATION.md`.

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

## Next Steps

**Learn more**:
- `docs/workflow_guide.md` - Detailed workflows
- `docs/engineering-agents-guide.md` - All 16 specialists
- `docs/HUMAN_AI_COLLABORATION.md` - Your role vs agent role

**Get help**:
- GitHub Issues: Bug reports, feature requests
- Discussions: Questions, community support

---

**Version**: 0.1.0-alpha | **Updated**: 2025-10-12 | **Alpha**: Expect bugs, report issues
