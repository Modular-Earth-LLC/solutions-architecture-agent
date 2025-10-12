# Improve Engineering Supervisor Agent

**Target**: `ai_agents/engineering_supervisor_agent.system.prompt.md`  
**Specialty**: Coordinates 16 engineering specialists, routes tasks to appropriate specialists

**Framework**: See `knowledge_base/system_config.json` → `self_improvement_framework` for methodology, principles, and validation requirements.

---

## Agent-Specific Focus Areas

**What makes this agent effective:**

1. **Routing Accuracy**
   - Correctly identifies which specialist(s) needed
   - Clear routing logic for all 16 specialists
   - Handles multi-specialist coordination

2. **Workflow Coordination**
   - Sequential, parallel, hybrid patterns
   - Smooth handoffs between specialists
   - State management across specialists

3. **Integration with Validation Framework**
   - References `ai_agents/shared/validation_framework.md`
   - Ensures specialists use consistent quality benchmarks
   - Coordinates TRM validation when needed

4. **User Experience**
   - Clear communication about which specialists working
   - Progress updates during multi-specialist work
   - Helpful when routing unclear

---

## Success Criteria

Beyond standard criteria (see system_config.json), ensure:

✅ Routing accuracy >95% for all 16 specialists  
✅ Multi-specialist workflows smooth  
✅ Specialists use shared validation framework  
✅ User communication clear  
✅ All integration patterns work

---

**Version**: 0.1 | **Updated**: 2025-10-12 | **Status**: Alpha - Untested, undergoing initial validation
