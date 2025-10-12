# Improve Architecture Agent

**Target**: `ai_agents/architecture_agent.system.prompt.md`  
**Specialty**: System design, cost estimation, tech stack selection, Well-Architected enforcement

**Framework**: See `knowledge_base/system_config.json` → `self_improvement_framework` for methodology, principles, and validation requirements.

---

## Agent-Specific Focus Areas

**What makes this agent effective:**

1. **Architecture Design Excellence**
   - Selects appropriate patterns (supervisor-worker, RAG, etc.)
   - Well-Architected compliance (all 6 pillars)
   - GenAI Lens applied
   - Clear component diagrams

2. **Cost Estimation Accuracy**
   - Development costs realistic
   - Infrastructure costs comprehensive
   - API/model usage costs calculated
   - 15% contingency included

3. **Tech Stack Decisions**
   - Requirements-driven selection
   - Trade-offs documented
   - Platform compatibility verified
   - Team skills considered

4. **Knowledge Base Integration**
   - Reads user_requirements.json correctly
   - Writes design_decisions.json properly
   - Schema-compliant output
   - Clean handoff to Engineering Supervisor

---

## Integration Requirements

- Reads `knowledge_base/user_requirements.json`
- Writes `knowledge_base/design_decisions.json`
- Follows schema: `knowledge_base/schemas/design_decisions.schema.json`
- References `system_config.json` → `aws_well_architected_framework`
- References `system_config.json` → `technical_references`
- Smooth handoff to Engineering Supervisor (who routes to 16 specialists)

---

## Success Criteria

Beyond standard criteria (see system_config.json), ensure:

✅ Architecture designs sound  
✅ Cost estimates accurate  
✅ Well-Architected compliant  
✅ Tech stack justified  
✅ Knowledge base operations correct  
✅ Handoff to Engineering smooth

---

## System Context (v2.0)

**Must understand 23-agent architecture:**
- Main Supervisor, 5 top-level agents, Engineering Supervisor, 16 specialists

**Tech stack focus**: Python, Streamlit, Anthropic Claude, AWS Bedrock, MCP, LangChain

---

**Version**: 0.1 | **Updated**: 2025-01-12 | **Status**: Alpha - Untested, undergoing initial validation
