# Improve Claude Code Agent

**Target**: `ai_agents/claude_code_agent.system.prompt.md`  
**Focus**: Autonomous code generation, subagent patterns, code quality validation  
**Recursion Prevention**: Single execution per session

---

## Focus Areas

1. **Autonomous Generation Quality**
   - Generated code compiles/runs without errors
   - Follows project patterns from context
   - Includes comprehensive error handling
   - Type hints and docstrings complete

2. **Subagent Pattern Effectiveness**
   - Orchestrator-worker coordination
   - Multi-file refactoring accuracy
   - Preserve functionality during refactoring
   - Validation at each step

3. **Code Review Accuracy**
   - Catches security vulnerabilities
   - Identifies performance issues
   - Suggests actionable improvements
   - Maintains constructive tone

4. **Test & Doc Generation**
   - Generated tests achieve >80% coverage
   - Tests validate actual functionality
   - Documentation clear for junior engineers
   - Examples are realistic and helpful

---

## Validation Framework Integration

Ensure agent references `ai_agents/shared/validation_framework.md` and:
- Uses TRM pattern for complex code generation
- Validates generated code before presenting
- Recursively improves until quality threshold met
- Reports validation scores

---

## Success Criteria

✅ Generated code runs without modification  
✅ Multi-file refactoring preserves functionality  
✅ Code reviews catch critical issues  
✅ Tests achieve target coverage  
✅ Validation framework integrated  

**Version**: 1.0 | **Date**: 2025-01-12
