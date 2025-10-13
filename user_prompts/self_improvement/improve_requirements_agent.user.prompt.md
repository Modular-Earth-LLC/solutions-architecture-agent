# Improve Requirements Agent

**Target**: `ai_agents/requirements_agent.system.prompt.md`  
**Specialty**: Requirements discovery, business analysis, stakeholder alignment

**Framework**: See `knowledge_base/system_config.json` → `self_improvement_framework` for methodology, principles, and validation requirements.

---

## Agent-Specific Focus Areas

**What makes this agent effective:**

1. **Discovery Process Quality**
   - Comprehensive workshop flows (quick, standard, comprehensive)
   - Questions uncover business needs effectively
   - Technical requirements captured accurately

2. **Requirements Structuring**
   - Clear, actionable requirements
   - Measurable success criteria
   - SMART objectives (Specific, Measurable, Achievable, Relevant, Time-bound)

3. **Knowledge Base Integration**
   - Properly writes to user_requirements.json
   - Schema-compliant output
   - Clean handoffs to Architecture Agent

4. **Stakeholder Alignment**
   - Multiple personas considered
   - Business goals clear
   - Acceptance criteria defined

---

## Integration Requirements

- Writes to `knowledge_base/user_requirements.json`
- Follows schema: `knowledge_base/schemas/user_requirements.schema.json`
- Smooth handoff to Architecture Agent
- References centralized technical docs

---

## Success Criteria

Beyond standard criteria (see system_config.json), ensure:

✅ Requirements complete and actionable  
✅ Knowledge base written correctly  
✅ Stakeholder needs captured  
✅ Smooth handoff to Architecture  
✅ Discovery workflows effective

---

