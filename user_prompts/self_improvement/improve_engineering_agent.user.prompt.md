# ⚠️ DEPRECATED - Improve Engineering Agent

**Status**: DEPRECATED as of v2.0.0 (2025-01-12)

---

## Migration Guide

**Old Architecture** (v1.x):
- Single monolithic Engineering Agent

**New Architecture** (v2.0+):
- Engineering Supervisor Agent (coordinates 16 specialists)
- 16 hyper-specialized engineering agents

---

## Use Instead

**To improve the engineering system:**
- `improve_engineering_supervisor.user.prompt.md` - Improve routing and coordination
- `engineering_specialists/improve_[specialist]_agent.user.prompt.md` - Improve individual specialists

**To optimize entire AI system:**
- `improve_ai_engineering_assistant.user.prompt.md` - System-wide optimization

---

**Deprecated**: 2025-01-12  
**Reason**: Replaced by two-layer specialist architecture  
**Migration**: Use Engineering Supervisor + specialist improvement prompts
