# Brownfield / Existing-Project Refactor Mode

Use when the engagement starts from **existing deliverables** (requirements docs, architecture documents, diagrams, roadmaps, user stories) rather than a blank slate. Common triggers: solution handoffs between agents, pivots on a live project, iterative refinement after a scope change, assessment responses that must improve an existing codebase's documentation.

## When this mode applies

- User provides a file path (or sister-repo path) to an already-approved requirements doc, architecture doc, or roadmap
- User asks to "refactor in place", "update the existing X", "preserve Y and add Z"
- Target deliverables live **outside** the SA agent's CWD (e.g., a sister repo holding the implementation)
- Multiple agents may be touching the target repo concurrently

## Core rules

### 1. Read before write

Before invoking any skill, enumerate and read every existing artifact the user references. Do not regenerate content you have not read. Preserve stable IDs (component IDs like `C-NNN`, requirement IDs like `FR-NNN`, user story IDs) unless the user explicitly asks to renumber.

### 2. External target paths are explicit

If the final human-readable deliverable lives outside CWD, the user (or dispatch step) MUST provide an absolute path. Skills then:

- Keep **KB JSON artifacts** inside `knowledge_base/` in the SA agent repo (source of truth for downstream skills)
- Write the **human-readable deliverable** to the specified external path
- Never assume an external target; if unset, write to `outputs/<engagement_id>/` and warn the user

### 3. Refactor, don't rewrite

- Preserve section structure and stable headings where they still apply
- Replace stale sections in place; append new sections at the end of the relevant parent section
- Remove `STALE` banners only when the document has been fully refreshed and every citation verified
- Keep existing diagrams as a starting set; add new ones rather than regenerating the whole set
- When a technology decision changes (e.g., database swap), update the tech stack table in place and add a one-line decision log entry with date

### 4. Stable ID discipline

| Artifact | ID pattern | Rule |
|---|---|---|
| Requirements | `FR-NNN`, `NFR-NNN` | Never renumber; add new IDs at the next unused number |
| User stories | `US-N`, `NS-N` | Never renumber; new workstreams use new letter prefixes |
| Components | `C-NNN` | Preserve meaning; add new components only for genuinely new capabilities |
| Use cases | `UC#N` | Preserve the user's existing numbering |

### 5. Cross-repo coordination

If the target deliverable path is in a different git repo than CWD:

- Check for `COORDINATION-NOTES.md` or `COORDINATION-PROTOCOL.md` in the target repo's `.claude/plans/` directory
- If present, read the protocol and **follow it literally** (specific-path staging, pull --rebase, append before/after entries, etc.)
- Never use `git add -A` / `git add .` / `git add -u` in a target repo you do not own exclusively
- Pull --rebase before every commit; push immediately after
- Append a coordination entry **before** starting writes and **after** finishing each deliverable

### 6. Input ingestion checklist

When refactoring an existing project's SA artifacts, read **in this order** before planning:

1. Requirements doc (approved source of truth)
2. Assessment/brief/RFP (original client materials)
3. Existing architecture doc (component IDs, tech stack, diagrams)
4. Existing user stories
5. Existing diagrams (`*.mmd` files)
6. Existing research/grounding doc
7. Existing roadmap / project plan
8. Project-level conventions (`CLAUDE.md`, `.claude/rules/`)
9. Coordination files (if multi-agent)

Skip archived directories (e.g., `.claude/plans/archive/`) — they poison context with obsolete material.

### 7. Scope boundary enforcement

The SA agent **never modifies implementation code** during a brownfield refactor. Code changes happen in a separate session by an implementation agent consuming the refactored docs. If the user asks for code edits, acknowledge and defer.

## Integration with Deliverable-First Mode

Brownfield mode is usually paired with Deliverable-First Mode from `CLAUDE.md`:

- Scope negotiation establishes the target deliverable(s) up front
- Depth tier is usually **STANDARD** (QUICK loses rigor on brownfield; COMPREHENSIVE is overkill unless the existing docs are near-complete and need deep verification)
- Skills skip greenfield-only steps and lean into read-and-refactor

## Dispatch hint

When you detect brownfield signals (existing file paths provided, "refactor", "in place", "preserve", sister-repo references), route to the **Brownfield** flow:

```
brownfield: ingest (read existing) → research (verify + extend) →
            architecture (refactor in place) → diagrams (add new + refactor existing) →
            project-plan (rewrite roadmap preserving stable IDs) →
            estimate → security-review → review
```

Requirements ingestion in this flow uses the `/requirements` shortcut path with a **file path** reference, not inline $ARGUMENTS content. See `skills/requirements/SKILL.md` §4 Step 3 shortcut.
