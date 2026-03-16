# Phase 5 Context — Skill Implementation

> Created: 2026-03-15 | Purpose: Reference context for Phase 5 execution
> Sources: Phase 4 results, Claude Code skills/plugin spec research (March 2026), SA best practices research

---

## Phase 4 Results Summary

**Commit**: `f61aff4` — 130 files changed, 227 insertions, 42,607 deletions

### Post-Phase 4 Repository State (60 files, excluding .git/.venv/references)

```
.claude-plugin/plugin.json          # Plugin manifest (created Phase 4)
.claude/plans/*.md                  # 9 planning docs (preserved)
.claude/rules/guiding-principles.md # 42 principles (KEEP)
.claude/rules/knowledge-base.md     # KB rules (UPDATE in Phase 5)
.claude/rules/security.md           # Security rules (KEEP)
.claude/settings.json               # Settings (UPDATE in Phase 5)
.github/                            # GitHub config (5 files, Phase 8)
.gitignore                          # Updated with PII patterns
.repo-metadata.json                 # Updated: 9 skills, 2 sub-agents
.vscode/                            # 3 files (Phase 8)
ARCHITECTURE.md                     # Phase 8
CLAUDE.md                           # REWRITE in Phase 5
CONTRIBUTING.md                     # Phase 8
LICENSE                             # KEEP
README.md                           # Phase 8
SECURITY.md                         # KEEP
agents/.gitkeep                     # WRITE agent defs in Phase 5
docs/                               # 5 files (Phase 8)
hooks/protect-sensitive-files.sh    # Moved from .claude/hooks/
knowledge_base/system_config.json   # READ-ONLY (Phase 6)
knowledge_base/README.md            # Phase 6
knowledge_base/schemas/             # 3 files (Phase 6)
outputs/.gitkeep                    # Clean (Phase 4)
private/                            # 2 files (KEEP)
skills/*/  .gitkeep                 # 9 dirs ready for SKILL.md (Phase 5)
templates/                          # 3 files (Phase 6)
tests/                              # 4 files (Phase 6)
```

---

## Claude Code Skills Specification (verified March 15, 2026)

### SKILL.md Frontmatter — ALL Supported Fields

| Field | Required | Type | Notes |
|---|---|---|---|
| `name` | No | string | Lowercase, hyphens, max 64 chars. Defaults to directory name |
| `description` | Recommended | string | Used by Claude to decide when to auto-load |
| `argument-hint` | No | string | Shown during autocomplete |
| `disable-model-invocation` | No | boolean | When `true`, only user `/name` invokes (not auto-loaded) |
| `user-invocable` | No | boolean | When `false`, hidden from `/` menu |
| `allowed-tools` | No | string (comma-separated) | Tools without permission prompts |
| `model` | No | string | Model alias or full ID |
| `context` | No | string | `fork` to run in forked subagent |
| `agent` | No | string | Subagent type when `context: fork` |
| `hooks` | No | object | Lifecycle hooks scoped to skill |

**No other fields exist.** This is the complete set.

### String Substitutions in Skill Body

- `$ARGUMENTS` — all arguments passed
- `$ARGUMENTS[N]` — specific argument (0-based, bracket syntax since v2.1.19)
- `$N` — shorthand for `$ARGUMENTS[N]`
- `${CLAUDE_SESSION_ID}` — current session ID
- `${CLAUDE_SKILL_DIR}` — directory containing SKILL.md (since v2.1.72)

### Dynamic Context: `` !`command` `` syntax runs shell commands, output replaces placeholder.

### Size Limits

- SKILL.md: **under 500 lines** recommended
- Skill description budget: **2% of context window** (fallback 16,000 chars)
- CLAUDE.md: **under 200 lines** for best adherence

### Tool Names (canonical, for `allowed-tools`)

Read, Write, Edit, Glob, Grep, Bash, Agent, WebSearch, WebFetch, AskUserQuestion, LSP, NotebookEdit, Skill, EnterPlanMode, ExitPlanMode, EnterWorktree, ExitWorktree, CronCreate, CronDelete, CronList, TaskCreate, TaskGet, TaskList, TaskOutput, TaskStop, TaskUpdate, TodoWrite, ToolSearch, ListMcpResourcesTool, ReadMcpResourceTool

### Sub-Agent Definition Fields (agents/*.md)

| Field | Required | Type | Notes |
|---|---|---|---|
| `name` | Yes | string | Lowercase + hyphens |
| `description` | Yes | string | When to delegate |
| `tools` | No | string/array | Defaults to inherit all |
| `disallowedTools` | No | string/array | Deny list |
| `model` | No | string | `sonnet`, `opus`, `haiku`, full ID, or `inherit` |
| `permissionMode` | No | string | `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`, `plan` |
| `maxTurns` | No | integer | Max agentic turns |
| `skills` | No | array | Skills to preload |
| `mcpServers` | No | array | MCP servers |
| `hooks` | No | object | Lifecycle hooks |
| `memory` | No | string | `user`, `project`, or `local` |
| `background` | No | boolean | Always run as background |
| `isolation` | No | string | `worktree` for git isolation |

### Hooks Configuration (hooks/hooks.json)

22 hook events supported. Key events: PreToolUse, PostToolUse, UserPromptSubmit, Stop, SessionStart, SubagentStart/Stop.

Handler types: `command`, `http`, `prompt`, `agent`.

### Plugin Discovery

- Marketplace: copied to `~/.claude/plugins/cache/`
- Local: `--plugin-dir` flag
- Reload: `/reload-plugins` without restart
- Namespacing: `/plugin-name:skill-name`
- `${CLAUDE_PLUGIN_ROOT}` provides absolute path

### Breaking Changes (Jan-March 2026)

- v2.1.63: `Task` tool renamed to `Agent` (alias still works)
- v2.1.19: Argument syntax changed from `$ARGUMENTS.0` to `$ARGUMENTS[0]`
- v2.1.72: Effort levels simplified to low/medium/high (removed `max`)
- v2.1.74: Fixed full model IDs silently ignored in agent frontmatter

**Critical for our skills**: Use `Agent` not `Task` in allowed-tools. Use bracket syntax for arguments.

---

## SA Best Practices Research Summary (March 2026)

### Well-Architected Frameworks (Current State)

- **AWS**: 6 pillars + GenAI Lens (updated Nov 2025, covers agentic AI) + new Responsible AI Lens
- **Azure**: 5 pillars + dedicated AI workload section with 5 AI-specific design principles (updated March 2026)
- **GCP**: 6 pillars (combines Security + Privacy + Compliance). Reviewed Jan 2026

### AI Architecture Patterns (2025-2026)

- RAG: Evolved to Naive → Advanced → Modular → GraphRAG → Agentic RAG
- Multi-Agent: Anthropic 5 workflow patterns (Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer)
- GraphRAG: Microsoft Research pattern (knowledge graph extraction + community summarization + hierarchical retrieval)
- AI Security: OWASP Top 10 for LLMs, Microsoft AI/ML Threat Taxonomy (17 failure modes), EU AI Act (full applicability Aug 2026)

### Estimation Best Practices

- Three-pass model: T-shirt sizing → Plan estimates (+/-50%) → Task estimates (+/-15%)
- PERT: E = (O + 4M + P) / 6
- AI/ML: 30-50% contingency for data quality, 3-5 model iterations, evaluation sprints
- Confidence: HIGH (80-95%), MEDIUM (50-80%), LOW (20-50%), SWAG (<20%)

### Security Frameworks

- STRIDE extended for AI (prompt injection → EoP, data poisoning → Tampering)
- NIST AI RMF: GOVERN, MAP, MEASURE, MANAGE
- EU AI Act: 4 risk tiers (Unacceptable, High, Transparency, Minimal)

---

## Phase 5 Deliverables (from technical-design.md)

Phase 5 reads technical-design.md and produces:

1. **CLAUDE.md** — Rewrite (~98 lines, from Section 2 draft)
2. **9 SKILL.md files** — One per `skills/*/` directory (from Section 3 specs)
3. **2 agent definition files** — `agents/parallel-wa-reviewer.md`, `agents/stride-analyzer.md` (from Section 6)
4. **2 rule files** — Update `knowledge-base.md`, create `skills.md` (from Section 5)
5. **hooks/hooks.json** — Hook configuration (from Section 4 in technical-design.md)

### Deferred Items to Address in Phase 5

| ID | Finding | Action |
|---|---|---|
| VARGAS-002 | /proposal selective section loading | Detail which KB sections to read in SKILL.md body |
| Gap #1 | Neurosymbolic AI architecture | /data-model includes WebSearch for latest patterns |
| Gap #6 | Strangler fig pattern | /integration-plan includes WebSearch for migration patterns |
| Gap #7 | Legacy system bridging | /integration-plan includes WebSearch for legacy patterns |
| Gap #11 | Competitive analysis section | /proposal adds optional competitive analysis via WebSearch |

---

## Quality Benchmarks for Phase 5

### What "Exemplar-Level" Means

Skills must produce output comparable to:
- **Hyperbloom/AGADA**: 23-page architecture doc, 16-page project plan
- **Revelex**: 10-page proposal with 3-phase $90K structure
- **AVAHI SOW templates**: Discovery ($5K-$25K) and implementation SOWs
- **Florence Healthcare**: MongoDB topology, DR recommendations, access governance

### Sales Principles Integration

14 consulting sales principles embedded in skill behavior (not bolted on):
- Treat clients as partners (collaborative tone)
- Sell solutions not hours (value-based recommendations)
- Active listening before recommending
- Eliminate surprises (surface risks early)
- Highlight losses rather than gains (cost of inaction)
- Every output delivers tangible value (no filler)
