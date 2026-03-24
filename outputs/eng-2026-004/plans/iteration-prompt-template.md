# SA Engagement Iteration Template v2.0

> **Usage**: Fill in `{PLACEHOLDERS}`, paste into Claude Code with SA Agent plugin loaded. Phase 0 runs interactively before plan mode; remaining phases execute inside plan mode.

---

## Execution Protocol

```
1. Claude reads prompt → loads context files
2. Phase 0 [INTERACTIVE]: requirements validation with user
3. User confirms decisions → enters plan mode (/plan)
4. Claude generates execution plan from Phases 1–N
5. User approves plan
6. Claude executes, stopping at HUMAN CHECKPOINT gates
7. After each SA skill: validate KB → git commit → push
```

**Skill invocation**: Always use fully-qualified names: `solutions-architecture-agent:{skill-name}`
**Depth flag**: Append `--depth {QUICK|STANDARD|COMPREHENSIVE}` when invoking skills
**Verification**: Run `python tests/validate_knowledge_base.py` after every KB file change

---

## Phase 0: Requirements Validation [INTERACTIVE — BEFORE PLAN MODE]

### 0.1 Context Loading

Read these files to understand current engagement state:

<context_files>
- `knowledge_base/engagement.json` — lifecycle state and versions
- {PRIMARY_DELIVERABLE} — current main output
- {RESEARCH_FILE} — research findings
- {BACKLOG_FILE} — improvement backlog
- {UAT_FILE} — human review checklist
- {UPSTREAM_KB_FILES} — architecture, requirements, security, etc.
- {INPUT_FILES} — original assignment, career data, reference materials
</context_files>

### 0.2 Decisions Requiring Human Judgment

Present each unresolved item for decision. Do NOT proceed until all are confirmed.

| ID | Category | Decision | Current State | Question for User |
|----|----------|----------|---------------|-------------------|
| {ID} | {tech/scope/demo/presentation} | {What needs deciding} | {What the current deliverable assumes} | {Specific question} |

### 0.3 New Information

Ask: "Do you have new information from stakeholder conversations, research, feedback, or timeline changes?"

### 0.4 Scope Confirmation

Confirm before proceeding:
- **Depth tier**: {QUICK | STANDARD | COMPREHENSIVE}
- **Final deliverables**: {What are we producing?}
- **Audience**: {Who reads/sees the output?}
- **Timeline constraint**: {Human time budget}
- **Engagement versioning**: {Archive strategy for previous iteration}

> **GATE**: Do NOT enter plan mode until all decisions are confirmed and documented.

---

## Constraints

### Non-Negotiable Guardrails
<!-- Rules that must never be violated. Place highest-priority items first and last (primacy/recency). -->
1. {Guardrail — most critical}
2. {Guardrail}
N. {Guardrail — second most critical}

### Quality Standards
1. {Standard}

### Persona & Voice
- **Role**: {Role definition}
- **Strengths to leverage**: {Technologies, domains, experiences to emphasize}
- **Gaps to design around**: {Topics to simplify or avoid depth on}

---

## Phase {N}: {Phase Name}

> **Skill**: `solutions-architecture-agent:{skill-name}` | `--depth {TIER}`
> **Entry criteria**: {What must be true before starting}
> **Exit criteria**: {What must be true when done}
> **Parallel candidates**: {Can any tasks within this phase run concurrently?}

### Tasks
1. {Specific, actionable task}

### Feedback to Incorporate
<feedback>
- {Specific change from user's review, organized by what it affects}
</feedback>

### Deliverables
- `{file_path}` — {description}

### Verification
- [ ] {Functional check}
- [ ] `python tests/validate_knowledge_base.py` passes
- [ ] Git commit with descriptive message → push

**HUMAN CHECKPOINT** *(include only for phases with irreversible or high-impact outputs)*

---

<!-- Repeat the Phase block for each phase in the engagement lifecycle.
     Standard SA lifecycle:
       Phase 1: Research Update (WebSearch/WebFetch)
       Phase 2: Requirements Revision (solutions-architecture-agent:requirements)
       Phase 3: Architecture Redesign (solutions-architecture-agent:architecture)
       Phase 4: Security Review (solutions-architecture-agent:security-review)
       Phase 5: Data Model — if applicable (solutions-architecture-agent:data-model)
       Phase 6: Integration Plan — if applicable (solutions-architecture-agent:integration-plan)
       Phase 7: Estimation & Planning (solutions-architecture-agent:estimate, :project-plan)
       Phase 8: Proposal Assembly (solutions-architecture-agent:proposal)
       Phase 9: Comprehensive Review (solutions-architecture-agent:review)
       Phase 10: Final Output Assembly (custom tasks)
-->

---

## Output Structure

```
outputs/{engagement-id}-v{N}/
├── {primary_deliverable}
├── {supporting_documents}
├── diagrams/
├── plans/
└── {additional_outputs}
```

## Appendix: Backlog Items

| # | Item | Incorporate In Phase |
|---|------|---------------------|
| {N} | {Description} | Phase {N} |

## Appendix: Context Engineering Notes

- **Load context just-in-time**: Only read files when the current phase needs them
- **Primacy/recency**: Place critical constraints at the start and end of each phase prompt
- **Reference over inline**: Point to files by path instead of pasting large content blocks
- **Prune irrelevant context**: Explicitly mark directories/files to skip (e.g., archived engagements)
- **Progressive elaboration**: Start with summaries, drill into details only when needed
- **Verify before recommending**: If a memory or prior output references a file/function, confirm it still exists before acting on it
