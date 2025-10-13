# Improve Streamlit UI Development Agent

**Target**: `ai_agents/streamlit_ui_agent.system.prompt.md`  
**Specialty**: Streamlit interfaces, session state, UX patterns, Claude integration

**Framework**: See `knowledge_base/system_config.json` → `self_improvement_framework` for methodology, principles, and validation requirements.

---

## Agent-Specific Focus Areas

**What makes this agent effective:**

1. **Interface Quality**
   - Chat interfaces intuitive and responsive
   - Components render correctly on mobile and desktop
   - Visual polish and consistency

2. **Session State Mastery**
   - State initialized correctly, persists across reruns
   - No state corruption, efficient updates
   - Proper use of Streamlit patterns

3. **Integration & Performance**
   - Clear handoffs to Claude, LangChain, Data agents
   - Fast load times (<2s), efficient caching
   - Loading states for async operations

---

## Integration Requirements

- References `ai_agents/shared/validation_framework.md`
- Validates UI code before presenting
- Tests rendering across devices
- Coordinates with Claude and Data agents

---

## Success Criteria

Beyond standard criteria (see system_config.json), ensure:

✅ UIs render correctly first time  
✅ Session state managed properly  
✅ Integration points clear  
✅ Performance targets met  
✅ Validation framework fully integrated

---

