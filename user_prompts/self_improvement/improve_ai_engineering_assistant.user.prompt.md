# Improve AI Engineering Assistant - System-Wide Optimization

**Target**: Entire AI Engineering Assistant framework (all agents, prompts, knowledge base, documentation)  
**Scope**: System-wide improvements across 23 agents

**Framework**: See `knowledge_base/system_config.json` → `self_improvement_framework` for methodology, principles, and validation requirements.

---

## What Makes This Prompt Different

**Standard agent improvement**: Focuses on ONE agent  
**System-wide optimization**: Analyzes and improves ALL components together for coherence and efficiency

**This prompt tells WHICH agents to optimize. Your agent prompt tells HOW to optimize them.**

---

## Optimization Scope

### Components to Analyze

**Agent System** (`ai_agents/` - 23 agents):
- Main Supervisor, 5 top-level agents, Engineering Supervisor, 16 specialists

**User Prompts** (`user_prompts/` - ~60 prompts):
- requirements/, architecture/, engineering/, deployment/, self_improvement/, prompt_engineering/, proposals/

**Knowledge Base** (`knowledge_base/`):
- system_config.json, user_requirements.json, design_decisions.json, schemas/

**Documentation** (`docs/`, `templates/`):
- guides, templates, README, ARCHITECTURE

---

## System-Specific Focus Areas

**What to assess across the entire system:**

1. **Coherence** - Do all agents work together smoothly?
2. **Consistency** - Are patterns and terminology consistent?
3. **Completeness** - Are all workflows end-to-end functional?
4. **Efficiency** - Is there redundancy to eliminate?
5. **Quality** - Do all agents meet benchmarks?
6. **Integration** - Do handoffs work properly?
7. **Documentation** - Is everything clear and accurate?

---

## Critical Workflows to Validate

After optimization, verify these work end-to-end:

✅ Requirements → Architecture → Engineering → Deployment (full lifecycle)  
✅ Engineering Supervisor routes to correct specialist (all 16)  
✅ Multi-agent coordination (sequential, parallel, hybrid)  
✅ Knowledge base operations (read/write/update)  
✅ Output organization (all deliverables to outputs/)  
✅ Cross-references (all agent ↔ KB ↔ doc refs valid)  
✅ All use cases (fork-and-use, deploy to Claude/AWS/Cursor/GitHub)

---

##Success Criteria

Beyond standard criteria (see system_config.json), ensure:

✅ All 23 agents optimized for coherence  
✅ System-wide quality improved 10%+ across assessment dimensions  
✅ User time to first result ≤15 minutes  
✅ No regressions in any workflows  
✅ All cross-references valid  
✅ Terminology consistent throughout

---

## Framework Context (v2.0)

**23-Agent Architecture:**
- Main Supervisor (1)
- Top-Level Agents (5): Requirements, Architecture, Deployment, Optimization, Prompt Engineering
- Engineering Supervisor (1): Coordinates 16 specialists
- Engineering Specialists (16): Hyper-specialized by technology

**Tech Stack**: Python, Streamlit, Anthropic Claude, AWS Bedrock, MCP, LangChain

**New Capabilities**:
- TRM Validation framework
- Shared quality standards
- 3 streamlined scenarios
- Centralized technical references (150+ URLs)

---

**Version**: 2.0 | **Updated**: 2025-01-12 | **Agent-Agnostic**: Works with Optimization or Prompt Engineering agents
