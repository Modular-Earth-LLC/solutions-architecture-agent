# Mermaid Diagram Quality Rules

When generating Mermaid diagrams, follow these rules to ensure reliable rendering across Mermaid v10-v11+, mmdc CLI, and export to PNG/SVG/Word/PDF:

1. **Quote all node labels** with special characters (`@`, `(`, `)`, `#`, `&`, `<`, `>`, `/`, `|`, `+`, `=`, etc.) — this includes ANY label with `<br/>`. Use `["label"]` not `[label]`.
2. **Quote all subgraph titles**: `subgraph "Title"` not `subgraph Title`.
3. **Keep labels short**: 3-5 words max. Move details to surrounding prose or tables.
4. **Limit `<br/>`**: Max 2 per node. More means the label is too long.
5. **Avoid bare `@`**: Quote labels containing `@`, or remove it if just a naming hint.
6. **Quote edge labels** with spaces or special chars: `-->|"label"|` not `-->|label|`.
7. **Node IDs**: `UPPER_SNAKE_CASE` or `camelCase` only — no hyphens, dots, or special chars.
8. **Declare direction**: Always `flowchart LR`, `flowchart TB`, etc. Never rely on defaults.
9. **Avoid `&` parallel links** in complex diagrams: use separate edges instead.
10. **Prefer `flowchart`** (LR/TB/RL/BT) and `graph`. Avoid `gantt`, `sequenceDiagram`, etc. unless they genuinely fit.

Full rules with examples: `C:\dev\scripts\md-to-docx\mermaid-diagram-quality-rules.md`
