# Improve Main Supervisor Agent

**Target**: `supervisor_agent.system.prompt.md`  
**Specialty**: Routes requests to 5 top-level agents, orchestrates complete workflows

**Framework**: See `knowledge_base/system_config.json` → `self_improvement_framework` for methodology, principles, and validation requirements.

---

## Agent-Specific Focus Areas

**What makes this agent effective:**

1. **Top-Level Routing**
   - Correctly routes to Requirements, Architecture, Deployment, Optimization, or Prompt Engineering agents
   - Handles ambiguous requests gracefully
   - Clear routing logic

2. **Workflow Orchestration**
   - Coordinates multi-agent workflows
   - Manages state across agents
   - Smooth handoffs

3. **User Experience**
   - Clear communication about which agents working
   - Helpful when request unclear
   - Progress transparency

---

## Integration Requirements

- References `ai_agents/shared/validation_framework.md`
- Coordinates all 5 top-level agents
- Routes engineering requests to Engineering Supervisor (who then routes to 16 specialists)
- Validates workflows complete successfully

---

## Success Criteria

Beyond standard criteria (see system_config.json), ensure:

✅ Routing accuracy >95% for all 5 top-level agents  
✅ Multi-agent workflows smooth  
✅ User communication clear  
✅ All integration patterns work  
✅ Backward compatible

---

**Version**: 2.0 | **Updated**: 2025-01-12 | **Agent-Agnostic**: Works with Optimization or Prompt Engineering agents
