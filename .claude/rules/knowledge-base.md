---
paths:
  - "knowledge_base/**/*.json"
  - "knowledge_base/**/*.schema.json"
---

# Knowledge Base Rules

- `system_config.json` is READ-ONLY at runtime — never modify it during agent workflows
- `user_requirements.json` and `design_decisions.json` are written by agents during workflows
- All JSON files must validate against their schemas in `knowledge_base/schemas/`
- Schema IDs use the URL pattern: `https://github.com/Modular-Earth-LLC/solutions-architecture-agent/schemas/`
- Run `python tests/validate_knowledge_base.py` after modifying any knowledge base file
