# Improve Engineering Supervisor Agent

**Purpose:** Optimize the Engineering Supervisor Agent to ensure effective routing and coordination of 16 specialized engineering agents for Python+Streamlit+Claude+AWS AI development.

**Target Agent:** `ai_agents/engineering_supervisor_agent.system.prompt.md`  
**Focus Areas:** Routing accuracy, workflow coordination, specialist integration, efficiency  
**Approach:** Self-improvement with recursion prevention + validation  
**Output:** Enhanced Engineering Supervisor with optimal routing and coordination

---

## Recursion Prevention

**Max Iterations**: 2-3 per session (allows refinement, prevents infinite loops)

**Simple Rule**: If improved 3+ times in this conversation, start fresh session.

---

## Improvement Focus Areas

### 1. Routing Accuracy to 16 Specialists

**Evaluate**:
- Does it route to correct specialist for each request?
- Are routing examples comprehensive (cover all 16 agents)?
- Is routing logic clear and unambiguous?
- Does it handle edge cases (unclear requests)?

**Target**: 95%+ routing accuracy

### 2. Workflow Coordination Excellence

**Evaluate**:
- Does it coordinate sequential workflows effectively?
- Does it handle parallel execution properly?
- Does it manage hybrid patterns (sequential + parallel)?
- Are handoffs between specialists smooth?

**Target**: Seamless multi-agent coordination

### 3. Integration with Validation Framework

**Evaluate**:
- Does it reference `ai_agents/shared/validation_framework.md`?
- Does it ensure specialists validate outputs?
- Does it apply TRM patterns for complex workflows?

**Target**: All coordinated work validated

### 4. User Experience

**Evaluate**:
- Is routing transparent to users?
- Are time estimates accurate?
- Are specialist capabilities clear?
- Is it easy to understand which specialist to use?

**Target**: Users quickly understand specialist selection

---

## Improvement Workflow

### Step 1: Analyze (30 min)

Read `ai_agents/engineering_supervisor_agent.system.prompt.md` and assess:
- Routing logic completeness
- Workflow coordination patterns
- Integration with validation framework
- User interaction clarity

### Step 2: Improve (45 min)

Enhance:
- Routing examples for all 16 specialists
- Workflow coordination patterns
- Validation framework integration
- User-friendly guidance

### Step 3: Validate (30 min)

Test routing scenarios:
- UI request → Streamlit UI Agent
- Claude Code request → Claude Code Agent
- Multi-agent workflow → Proper coordination
- Complex task → Correct sequential/parallel pattern

---

## Success Criteria

✅ Routes correctly to all 16 specialists  
✅ Coordinates multi-agent workflows seamlessly  
✅ Integrates validation framework  
✅ User-friendly and clear  
✅ No breaking changes  

---

**Version**: 1.0  
**Date**: 2025-01-12  
**Target**: `ai_agents/engineering_supervisor_agent.system.prompt.md`
