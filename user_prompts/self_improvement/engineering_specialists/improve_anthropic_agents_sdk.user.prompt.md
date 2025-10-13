# Improve Anthropic Python Agents SDK Agent

**Target**: `ai_agents/anthropic_agents_sdk_agent.system.prompt.md`  
**Specialty**: Formal Anthropic Agents SDK, tool use patterns, prompt caching

**Framework**: See `knowledge_base/system_config.json` → `self_improvement_framework` for methodology, principles, and validation requirements.

---

## Agent-Specific Focus Areas

**What makes this agent effective:**

1. **SDK Mastery**
   - Correct use of Anthropic Agents SDK patterns
   - Proper tool definition and implementation
   - Safe tool execution (no eval, validated inputs)

2. **Performance Optimization**
   - Effective prompt caching strategies
   - Token efficiency through SDK features
   - Streaming responses when appropriate

3. **Pattern Implementation**
   - Subagent coordination
   - Tool use best practices  
   - Error handling and validation

---

## Integration Requirements

- References `ai_agents/shared/validation_framework.md`
- Uses SDK patterns from Anthropic documentation
- Coordinates with other Claude specialists
- Never uses eval() or unsafe code patterns

---

## Success Criteria

Beyond standard criteria (see system_config.json), ensure:

✅ SDK patterns correctly implemented  
✅ Tool use safe and validated  
✅ Caching strategies effective  
✅ No security vulnerabilities  
✅ Validation framework fully integrated

---

