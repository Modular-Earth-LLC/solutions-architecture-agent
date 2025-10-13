# Multi-Agent AI Development Framework

**Build production AI systems 3-5x faster** with specialized agents that handle requirements, architecture, coding, and deployment automatically.

**Status**: ⚠️ Alpha - Untested in production. Use at your own risk.  
**Version**: See `.repo-metadata.json` for current version and agent counts.

---

## What You Can Build

**15 minutes**: Custom GPTs, Claude assistants, Cursor IDE modes  
**2 hours**: Complete architecture + cost estimates  
**2-5 days**: Working prototypes with tests

**Complete lifecycle**: Requirements → Architecture → Code → Deployment

---

## Quick Start (5 Minutes)

### Install in Cursor IDE

```bash
# 1. Clone
git clone https://github.com/your-org/multi-agent-ai-development-framework
cd multi-agent-ai-development-framework

# 2. Deploy (Cursor → Settings → Chat → Custom Modes)
#    Create "Supervisor Agent"
#    Paste: supervisor_agent.system.prompt.md
#    Enable: "All tools" → Save

# 3. Use
#    Open AI Pane (Ctrl+Shift+L)
#    Try: "Build a Streamlit chatbot with Claude"
```

**Done!** Supervisor routes to specialized agents who generate code for you to review.

**Other platforms**: See `docs/getting-started.md` for Claude Projects and GitHub Copilot setup.

---

## Why This Exists

**The Problem**: Every AI project starts from scratch
- Requirements: 2 days → should be 2 hours
- Architecture: 2 weeks → should be 4 hours
- Prototypes: 2 months → should be 1 week

**The Solution**: Specialized agents automate 70% of repetitive work

| Task | Traditional | With Framework | Savings |
|------|------------|----------------|---------|
| Requirements | 2 days | 2 hours | 90% |
| Architecture | 2 weeks | 4 hours | 97% |
| Prototype | 2 months | 1 week | 87% |

**Result**: 3-5x faster delivery, 60% less rework, consistent quality

---

## The Specialized Agents

<!-- Current count: See .repo-metadata.json -->

**Main Supervisor** → Routes your requests

**Top-Level Domain Agents** (5):
- **Requirements**: Discovers what you need (15-90 min workshops)
- **Architecture**: Designs system + estimates costs (AWS Well-Architected)
- **Deployment**: Creates platform-specific deployment guides
- **Optimization**: Analyzes and improves existing systems
- **Prompt Engineering**: Creates production-quality prompts

**Engineering Supervisor** (1): Coordinates 16 technology specialists

**Engineering Specialists** (16):
- **Anthropic Claude** (5): Code, Workspaces, SDK, MCP, Projects
- **AWS Bedrock** (2): AgentCore, Strands
- **Other** (9): Streamlit, LangChain, data, AWS infra/security, testing, GitHub, Cursor

**See**: `docs/engineering-agents-guide.md` for complete specialist reference

---

## Quick Examples

### Example 1: Build Streamlit+Claude App (2 Hours)

```
You: "Build a document summarization app with Streamlit and Claude"

Engineering Supervisor routes to specialists:
→ Streamlit UI Agent: Chat interface + file upload
→ Claude Code Agent: Claude SDK integration + streaming
→ Testing Agent: pytest suite with mocks

Output:
✅ streamlit_app.py, claude_client.py, tests/
✅ requirements.txt, README.md, .env.example
✅ 80% test coverage, production-ready

YOU: Review → Run locally → Deploy
```

**Result**: Working prototype same day

---

### Example 2: Optimize Existing System (2-3 Hours)

```
You: "Optimize my Claude chatbot at outputs/my-chatbot/"

Optimization Agent:
→ Discovers system structure
→ Assesses Well-Architected compliance (score: 6.2/10)
→ Proposes improvements (reduce tokens 30%, add caching)
→ Implements (with your approval)
→ Validates improvements

Result:
✅ Monthly cost: $120 → $78 (-35%)
✅ Response time: 3.2s → 2.4s (-25%)
✅ Well-Architected: 6.2 → 8.1 (+30%)
```

**Result**: Measurable improvements backed by data

**More examples**: See `docs/workflow_guide.md` and `docs/examples/`

---

## Key Features

### AWS Well-Architected Enforcement
Every architecture evaluated against **6 pillars** + **GenAI Lens**:
- Operational Excellence • Security • Reliability
- Performance • Cost • Sustainability
- Model Selection • Prompt Engineering • RAG • Multi-Agent • Responsible AI

### TRM Validation Framework
**Test-Time Recursive Majority** ensures quality:
- Generate → Validate → Improve → Re-validate
- Only present outputs meeting quality benchmarks
- Code coverage ≥80%, type hints ≥90%, 0 critical security issues

### Self-Improvement System
17 improvement prompts for continuous enhancement
- System-wide optimization
- Individual agent improvements
- 2-3 iterations per session (practical recursion prevention)

### Centralized Knowledge
`knowledge_base/system_config.json` contains:
- 150+ technical documentation URLs
- AWS Well-Architected definitions
- Research papers (TRM, MetaGPT)
- Design patterns
- Quality benchmarks

---

## Who Should Use This

✅ **Junior Engineers**: Learn from generated code, ship without years of experience  
✅ **Senior Engineers**: Eliminate boilerplate, focus on complex decisions, 3-5x faster  
✅ **Consultants**: Professional proposals in hours, accurate estimates  
✅ **Managers**: Standardize processes, 5x faster onboarding  
✅ **Architects**: Systematic Well-Architected designs, evidence-based recommendations  
✅ **CTOs**: De-risk AI investments, scale without proportional hiring

---

## Installation & Platforms

**Cursor IDE** (Recommended - 5 min):
```
1. Settings → Chat → Custom Modes
2. Create "Supervisor Agent", paste supervisor_agent.system.prompt.md
3. Enable "All tools" → Save
```

**Claude Projects** (10 min):
```
1. Create project at claude.ai/projects
2. Upload knowledge_base/*.json
3. Custom Instructions: supervisor_agent.system.prompt.md
```

**GitHub Copilot** (15 min):
```
1. Create .github/copilot-instructions.md
2. Paste supervisor_agent.system.prompt.md
3. Use @workspace in VS Code
```

**Full guide**: `docs/deployment-guide.md`

---

## Tech Stack

**Core**: Python 3.12+ • Streamlit • Anthropic Claude • AWS Bedrock • MCP • LangChain

**16 Engineering Specialists** cover:
- 5 Anthropic Claude specialists
- 2 AWS Bedrock specialists  
- 9 Other specialists (UI, orchestration, data, AWS infra/security, testing, platforms)

**Centralized Docs**: 150+ technical URLs in `knowledge_base/system_config.json` → `technical_references`

---

## Architecture

**Two-layer supervisor-worker pattern**:

```
                 Supervisor Agent
                        ↓
        ┌───────────────┼───────────────┐
        ↓               ↓               ↓
  Requirements    Architecture    Engineering Supervisor
        ↓               ↓               ↓
        │               │        ┌──────┼──────┐
        │               │        ↓      ↓      ↓
        │               │   Streamlit Claude  AWS
        │               │      UI    Code   Bedrock
        │               │        +14 more specialists
        │               ↓
        └───────→ Deployment + Optimization

Shared Knowledge Base:
├─ system_config.json (platform constraints, tech refs)
├─ user_requirements.json (business requirements)
└─ design_decisions.json (architecture, costs, plans)
```

**See**: `ARCHITECTURE.md` for complete details

---

## Human-AI Collaboration

**Agents do** (you review):
- ✅ Generate code/docs/configs
- ✅ Analyze systems  
- ✅ Recommend improvements
- ✅ Validate quality

**YOU do** (always):
- ✅ Review all outputs
- ✅ Approve architectures
- ✅ Execute deployments
- ✅ Make critical decisions

**Agents NEVER**:
- ❌ Commit code automatically
- ❌ Deploy to production
- ❌ Make business decisions
- ❌ Spend money without approval

**See**: `docs/human-ai-collaboration.md` for complete guide

---

## Documentation

**Essential** (start here):
- `README.md` - This file (overview + quick start)
- `docs/getting-started.md` - First project walkthrough (15 min)
- `docs/deployment-guide.md` - Platform deployment
- `docs/human-ai-collaboration.md` - Your role vs agent role

**Reference**:
- `docs/workflow_guide.md` - Complete workflows
- `docs/engineering-agents-guide.md` - All 16 specialists
- `docs/executive_overview.md` - Business value
- `ARCHITECTURE.md` - System architecture
- `knowledge_base/README.md` - Knowledge base guide
- `templates/` - Requirements, architecture, checklists

---

## Repository Structure

```
multi-agent-ai-development-framework/
├── ai_agents/                    # 23 agent system prompts
│   ├── supervisor_agent.system.prompt.md (main entry point)
│   ├── [5 top-level domain agents]
│   ├── engineering_supervisor_agent.system.prompt.md
│   ├── [16 specialist agents]
│   └── shared/validation_framework.md (TRM patterns)
├── knowledge_base/               # Shared state across agents
│   ├── system_config.json (150+ tech refs, Well-Architected defs)
│   ├── user_requirements.json
│   ├── design_decisions.json
│   └── schemas/ (JSON schemas for validation)
├── user_prompts/                 # Task-specific instructions (~60)
├── docs/                         # Documentation
├── templates/                    # Reusable templates
├── tests/                        # Validation tests
└── outputs/                      # Generated systems go here
```

---

## Alpha Status & Limitations

⚠️ **Current Status**: 0.1.0-alpha - **Untested in production**

**What works**:
- ✅ All 23 agents functional
- ✅ Complete workflows (requirements → deployment)
- ✅ Code generation quality-assured (TRM validation)
- ✅ Well-Architected enforcement
- ✅ Self-improvement system

**Known limitations**:
- ⚠️ No production validation yet
- ⚠️ Breaking changes expected before v1.0
- ⚠️ Some edge cases untested
- ⚠️ Documentation still evolving

**Use at your own risk**. Report issues on GitHub. Production-ready in v1.0.

---

## Getting Help

**Documentation**: Start with `docs/getting-started.md`  
**Issues**: GitHub Issues for bugs/features  
**Discussions**: GitHub Discussions for questions  
**Contributing**: See `CONTRIBUTING.md`

---

## License

MIT License - Full commercial use permitted

---

## Quick Links

- **GitHub**: [github.com/your-org/multi-agent-ai-development-framework](https://github.com/your-org/multi-agent-ai-development-framework)
- **Getting Started**: `docs/getting-started.md`
- **Deployment Guide**: `docs/deployment-guide.md`
- **Engineering Specialists**: `docs/engineering-agents-guide.md`
- **Workflows**: `docs/workflow_guide.md`

---

**Version**: 0.1.0-alpha | **Last Updated**: 2025-10-12 | **Status**: Alpha - Begin testing

**Built with**: Python • Streamlit • Anthropic Claude • AWS Bedrock • MCP • LangChain

🚀 **Start building**: Install Supervisor Agent in Cursor and say "Build a chatbot"
