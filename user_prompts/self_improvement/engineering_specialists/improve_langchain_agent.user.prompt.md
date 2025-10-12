# Improve LangChain Orchestration Agent

**Target**: `ai_agents/langchain_agent.system.prompt.md`  
**Focus**: LCEL chains, memory management, tool use, RAG integration  
**Recursion Prevention**: Single execution per session

---

## Focus Areas

1. **LCEL Chain Quality**
   - Pipe operator composition clear
   - Chain logic maintainable
   - Error handling comprehensive
   - Streaming works correctly

2. **Memory Management**
   - Appropriate memory type selection
   - Buffer/summary/window usage correct
   - Memory persists across conversations
   - No memory leaks

3. **Tool Use & Agent Integration**
   - Tools defined properly
   - Agent executor works correctly
   - Tool results processed properly
   - Max iterations respected

4. **RAG Chain Excellence**
   - Retriever integration smooth
   - Context formatting correct
   - Citations included
   - Answer quality high

---

## Validation Framework Integration

Ensure agent:
- Validates LangChain workflows
- Tests chain execution
- Checks memory correctness
- Reports workflow quality

---

## Success Criteria

✅ Chains execute correctly  
✅ Memory managed properly  
✅ Tools integrate reliably  
✅ RAG chains work well  
✅ Validation framework integrated  

**Version**: 1.0 | **Date**: 2025-01-12
