# Improve Streamlit UI Development Agent

**Target**: `ai_agents/streamlit_ui_agent.system.prompt.md`  
**Focus**: Streamlit interface quality, session state, UX patterns, Claude integration  
**Recursion Prevention**: Single execution per session

---

## Focus Areas

1. **Interface Quality**
   - Chat interfaces intuitive and responsive
   - Components render correctly
   - Layouts work on mobile and desktop
   - Visual polish and consistency

2. **Session State Management**
   - State initialized correctly
   - No state corruption
   - Persists across reruns
   - Efficient state updates

3. **Integration Points**
   - Clear connection to Claude Integration Agent
   - Smooth data flow to LangChain Agent
   - Proper integration with Data Engineering Agent
   - Loading states for all async operations

4. **Performance**
   - Fast load times (<2s)
   - Efficient caching (@st.cache_data, @st.cache_resource)
   - Minimal reruns
   - Smooth interactions

---

## Validation Framework Integration

Ensure agent:
- Validates UI code before presenting
- Tests rendering across devices
- Checks session state correctness
- Reports UI quality metrics

---

## Success Criteria

✅ UIs render correctly first time  
✅ Session state managed properly  
✅ Integration points clear  
✅ Performance acceptable  
✅ Validation framework integrated  

**Version**: 1.0 | **Date**: 2025-01-12
