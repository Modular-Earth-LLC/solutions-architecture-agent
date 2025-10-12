# Improve Claude Workspaces Agent

**Target**: `ai_agents/claude_workspaces_agent.system.prompt.md`  
**Focus**: Multi-agent orchestration, coordination patterns, state management  
**Recursion Prevention**: Single execution per session

---

## Focus Areas

1. **Orchestration Pattern Quality**
   - Supervisor-worker routing accuracy
   - Sequential chain coordination
   - Parallel execution efficiency
   - Hybrid pattern implementation

2. **Inter-Agent Communication**
   - Clear contracts between agents
   - Efficient context passing
   - State management accuracy
   - No information loss in handoffs

3. **AWS Bedrock Fallback**
   - Smooth transition Anthropic → Bedrock
   - Feature parity maintained
   - Configuration-driven deployment
   - Performance comparable

4. **Error Recovery**
   - Failures don't cascade
   - Fallback mechanisms work
   - Resilient multi-agent execution
   - Clear error reporting

---

## Validation Framework Integration

Ensure agent:
- Validates multi-agent workflows
- Uses TRM for orchestration decisions
- Ensures all agents' outputs validated
- Reports coordination quality

---

## Success Criteria

✅ Routing accuracy >95%  
✅ No information loss in handoffs  
✅ AWS fallback works seamlessly  
✅ Error recovery prevents cascading failures  
✅ Validation framework integrated  

**Version**: 1.0 | **Date**: 2025-01-12
