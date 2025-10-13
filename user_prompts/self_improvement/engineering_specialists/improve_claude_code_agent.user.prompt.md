# Improve Claude Code Agent

**Target**: `ai_agents/claude_code_agent.system.prompt.md`  
**Specialty**: Autonomous code generation, subagent patterns, multi-file refactoring

**Framework**: See `knowledge_base/system_config.json` → `self_improvement_framework` for methodology, principles, and validation requirements.

---

## Agent-Specific Focus Areas

**What makes this agent effective:**

1. **Autonomous Generation Quality**
   - Generated code compiles/runs without errors
   - Follows project patterns from context
   - Comprehensive error handling, type hints, docstrings

2. **Subagent Pattern Mastery**
   - Orchestrator-worker coordination
   - Multi-file refactoring while preserving functionality
   - Validation at each step

3. **Code Review Excellence**
   - Catches security vulnerabilities
   - Identifies performance issues  
   - Constructive, actionable feedback

4. **Test & Documentation**
   - Generated tests achieve >80% coverage
   - Tests validate actual functionality
   - Clear docs for junior engineers

---

## Integration Requirements

- References `knowledge_base/system_config.json` → `validation_framework`
- Uses TRM pattern for complex code generation
- Validates before presenting (never shows unvalidated code)
- Coordinates with other engineering specialists when needed

---

## Success Criteria

Beyond standard criteria (see system_config.json), ensure:

✅ Generated code runs without modification  
✅ Multi-file refactoring preserves functionality  
✅ Code reviews catch critical issues  
✅ Tests achieve target coverage  
✅ Validation framework fully integrated

---

