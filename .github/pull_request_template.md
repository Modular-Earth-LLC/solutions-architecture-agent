## Summary
<!-- What does this PR do? -->

## Changes
<!-- List key changes -->
-

## Testing
<!-- How was this tested? -->
- [ ] `python tests/validate_knowledge_base.py` — 0 FAIL
- [ ] `python tests/validate_consistency.py` — 0 FAIL
- [ ] Skill tested via `claude --plugin-dir .` (if skill changed)
- [ ] Documentation updated if applicable

## Checklist
- [ ] No secrets or credentials committed
- [ ] `.repo-metadata.json` updated if skills/agents/schemas added or removed (increment `architecture.skills`, `knowledge_base.files`, or `knowledge_base.schemas` as applicable)
- [ ] SKILL.md follows 6-section structure (if new/modified skill)
- [ ] Schema alignment verified (field names match between SKILL.md and schema)
- [ ] Envelope fields present in Section 5 output rules (if new skill)
- [ ] Manual skill test passed (see [CONTRIBUTING.md § Manual Skill Testing](CONTRIBUTING.md#manual-skill-testing))
