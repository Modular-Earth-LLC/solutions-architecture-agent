# Solutions Architecture Agent — Master Plan

> Generated: 2026-03-15 | Status: Final Draft — Awaiting human review

---

## Vision & Objectives

### Technical Objective

Consolidate a 23-agent multi-agent system into a single **AI Solutions Architecture Agent** with 9 on-demand skills, packaged as a Claude Code plugin. The agent follows Anthropic's Agent Skills open standard (adopted by 30+ platforms as of March 2026) and uses progressive disclosure for context efficiency. Google/MIT research (arXiv:2512.08296, December 2025) validates this: for sequential reasoning tasks, multi-agent systems degrade performance by 39–70% vs. single-agent, while being 3x less token-efficient.

**Scope boundary**: This agent covers **solutions architecture only** — from requirements discovery through technical project planning. It produces designs, specifications, and plans. Implementation, deployment, CI/CD, and code generation are handled by a future **AI Engineering Agent** that consumes this agent's outputs.

### Business Objective

Build the definitive AI-augmented SA tool covering the full lifecycle gap no existing tool addresses. Package as a Claude Code plugin installable locally and via marketplace. Open-source under MIT license. Quality bar: exemplar-level deliverables that embody cutting-edge SA best practices for enterprise solutions and AI-driven products.

---

## Resolved Design Decisions

| # | Decision | Resolution |
|---|----------|-----------|
| 1 | Knowledge base | Evolve from scratch — 10 specialized JSON files with engagement-centered topology |
| 2 | Cloud deployment | Out of scope — future AI Engineering Agent |
| 3 | Sub-agents | Follow Anthropic's guidance — `context: fork` for parallel reviews (e.g., Well-Architected pillar reviews) |
| 4 | License | MIT |
| 5 | Distribution | Plugin-first — ASAP marketplace submission. Plugin works both locally and from marketplace |
| 6 | Quality bar | Maximum — exemplar-level deliverables |
| 7 | Architecture vs Estimation | Separate skills. `/architecture` = system design + diagrams. `/estimate` = financial analysis |
| 8 | Technology references | Maximally dynamic — skills use `WebSearch` + `WebFetch` to pull latest best practices, platform features, and AI research at invocation time. No static vendor knowledge embedded |
| 9 | KB schema | 10-file engagement-centered design: `engagement.json`, `requirements.json`, `architecture.json`, `data_model.json`, `security_assessment.json`, `integration_map.json`, `estimates.json`, `project_plan.json`, `reviews.json`, plus `system_config.json` (read-only reference) |
| 10 | Plugin manifest | `.claude-plugin/plugin.json` per Anthropic's official schema. Skills at `skills/` (plugin root), agents at `agents/`, hooks at `hooks/` |
| 11 | Review iterations | 3 passes (LLM-as-judge standard) |
| 12 | Git workflow | Each phase commits work before human checkpoint. Human reviews, improves, then approves push to main |
| 13 | Portability | No references to operator's filesystem. Runs on arbitrary Windows and Linux environments |

---

## Target Plugin Structure

Per Anthropic's official plugin documentation ([code.claude.com/docs/en/plugins](https://code.claude.com/docs/en/plugins)):

```
solutions-architecture-agent/           # Plugin root
├── .claude-plugin/
│   └── plugin.json                     # Plugin manifest (name, version, description, author, license)
├── skills/                             # Skills at plugin root (Anthropic standard)
│   ├── requirements/SKILL.md           # /requirements
│   ├── architecture/SKILL.md           # /architecture
│   ├── estimate/SKILL.md               # /estimate
│   ├── project-plan/SKILL.md           # /project-plan
│   ├── proposal/SKILL.md               # /proposal
│   ├── data-model/SKILL.md             # /data-model
│   ├── security-review/SKILL.md        # /security-review
│   ├── integration-plan/SKILL.md       # /integration-plan
│   └── review/SKILL.md                 # /review (LLM-as-judge)
├── agents/                             # Subagent definitions (Anthropic standard)
│   └── (parallel-reviewer.md, etc.)
├── hooks/
│   └── hooks.json                      # Hook configuration
├── .claude/                            # Project config (NOT plugin components)
│   ├── settings.json                   # Permissions and hooks
│   ├── settings.local.json             # Local overrides (git-ignored)
│   ├── rules/                          # Path-scoped and unscoped rules
│   │   ├── guiding-principles.md       # 34 core values (unscoped)
│   │   ├── skills.md                   # Skill editing rules (path-scoped: skills/**)
│   │   ├── knowledge-base.md           # KB rules (path-scoped: knowledge_base/**)
│   │   └── security.md                 # Security rules (path-scoped: private/**)
│   └── plans/                          # Planning artifacts
│       ├── master-plan.md              # This file
│       └── references/                 # Planning reference materials (git-ignored)
├── knowledge_base/                     # Persistent engagement state (JSON + schemas)
│   ├── system_config.json              # Read-only system reference
│   ├── engagement.json                 # Engagement metadata and lifecycle
│   ├── requirements.json               # Discovery output
│   ├── architecture.json               # Architecture decisions and diagrams
│   ├── data_model.json                 # Data model specifications
│   ├── security_assessment.json        # Threat model and compliance
│   ├── integration_map.json            # Integration points and data flows
│   ├── estimates.json                  # Cost models and team composition
│   ├── project_plan.json               # Phases, milestones, dependencies
│   ├── reviews.json                    # LLM-as-judge scores and iteration history
│   ├── schemas/                        # JSON Schema validation
│   └── README.md
├── templates/                          # Output document templates
├── tests/                              # Validation scripts
├── docs/                               # User documentation
├── .github/                            # GitHub configuration
├── CLAUDE.md                           # Core agent identity (<200 lines)
├── ARCHITECTURE.md                     # System architecture documentation
├── README.md                           # Plugin README
├── CONTRIBUTING.md                     # Contributor guide
├── LICENSE                             # MIT
└── .repo-metadata.json                 # Version and counts metadata
```

### Plugin Manifest

```json
{
  "name": "solutions-architecture-agent",
  "version": "1.0.0",
  "description": "AI Solutions Architecture Agent — 9 skills covering the full SA lifecycle from requirements discovery through technical project planning. Produces designs and plans, not implementation.",
  "author": {
    "name": "Modular Earth LLC",
    "url": "https://github.com/Modular-Earth-LLC"
  },
  "homepage": "https://github.com/Modular-Earth-LLC/solutions-architecture-agent",
  "repository": "https://github.com/Modular-Earth-LLC/solutions-architecture-agent",
  "license": "MIT",
  "keywords": ["solutions-architecture", "system-design", "AI", "enterprise", "well-architected"]
}
```

---

## Skill Inventory (9 Skills)

### Core SA Lifecycle (5)

| # | Skill | Invocation | Purpose |
|---|-------|-----------|---------|
| 1 | Requirements Discovery | `/requirements` | Discovery workshops (quick/standard/comprehensive), pain points, AI suitability. Greenfield + migration |
| 2 | Solution Architecture | `/architecture` | High-level and detailed system design, tech stack decisions, ASCII + Mermaid diagrams |
| 3 | Estimation | `/estimate` | Cost analysis, LOE, team composition, infrastructure cost modeling |
| 4 | Technical Project Plan | `/project-plan` | Roadmaps, phasing, milestones, dependencies. 0-to-1 + migration timelines |
| 5 | Proposal Assembly | `/proposal` | Discovery/implementation/internal/pitch proposals from KB data |

### Specialized Domain (3)

| # | Skill | Invocation | Purpose |
|---|-------|-----------|---------|
| 6 | Data Modeling | `/data-model` | Knowledge bases, neurosymbolic AI, ontologies, knowledge graphs, vector/relational schemas |
| 7 | Security & Privacy Review | `/security-review` | Threat modeling, compliance (HIPAA/SOC2/CCPA/GLBA), defense-in-depth, encryption |
| 8 | Integration Planning | `/integration-plan` | API design, migration strategies, legacy bridging, data flows, strangler fig patterns |

### Quality Assurance (1)

| # | Skill | Invocation | Purpose |
|---|-------|-----------|---------|
| 9 | Deliverable Review | `/review` | LLM-as-judge: score and iteratively improve any SA deliverable (3 passes). Evaluates against Well-Architected frameworks, guiding principles, and exemplar quality |

### Engagement Flows

**0-to-1 New Build**: `/requirements` → `/architecture` → `/data-model` → `/security-review` → `/estimate` → `/project-plan` → `/proposal` → `/review`

**Migration/Modernization**: `/requirements` → `/integration-plan` → `/architecture` → `/data-model` → `/security-review` → `/estimate` → `/project-plan` → `/proposal` → `/review`

### Technology Reference Strategy

All skills use `WebSearch` and `WebFetch` as allowed tools to dynamically pull the latest:
- Platform features and pricing (AWS, Azure, GCP, etc.)
- AI model capabilities and benchmarks
- Framework documentation and best practices
- Research papers and industry standards

No static vendor knowledge is embedded in skills. This ensures recommendations always reflect the current landscape.

---

## Knowledge Base Schema Design

**Topology**: Engagement-centered with unidirectional data flow.

```
system_config (read-only) ──→ engagement ──→ requirements
                                                  ↓
                                             architecture
                                            ↙    ↓    ↘
                               data_model  security  integration_map
                                            ↘    ↓    ↙
                                             estimates
                                                  ↓
                                            project_plan
                                                  ↓
                                              reviews
```

| File | Owner Skill | Purpose |
|------|------------|---------|
| `system_config.json` | READ-ONLY | Agent configuration, framework references |
| `engagement.json` | All skills | Engagement envelope: client, type (greenfield/migration), status, skills invoked |
| `requirements.json` | `/requirements` | Problem statement, pain points, success criteria, stakeholders, AI suitability |
| `architecture.json` | `/architecture` | System design, component decisions, tech stack, diagram references |
| `data_model.json` | `/data-model` | Entity relationships, schemas, ontologies, vector/graph specs |
| `security_assessment.json` | `/security-review` | Threat model, compliance checklist, security architecture |
| `integration_map.json` | `/integration-plan` | API contracts, data flows, migration strategies |
| `estimates.json` | `/estimate` | Cost models, LOE breakdowns, team composition |
| `project_plan.json` | `/project-plan` | Phases, milestones, dependencies, timelines |
| `reviews.json` | `/review` | Per-deliverable scores (completeness, technical soundness, well-architected, clarity, feasibility), findings, iteration history |

Each file declares `$depends_on` upstream dependencies. Skills never write to files they don't own. `/proposal` reads from all KB files and writes to `outputs/`, not the KB.

---

## Phase Overview

| Phase | Name | Goal | Human Checkpoint |
|-------|------|------|-----------------|
| 1 | Inventory & Extraction | Extract patterns from agents, classify every file | Review extraction, approve deletions |
| 2 | Requirements & Workflow Design | Define structured requirements and user stories for 9 skills | Review requirements completeness |
| 3 | System Architecture & Technical Design | Design plugin structure, skill frontmatter, KB schemas, CLAUDE.md | Review architecture decisions |
| 4 | Cleanup & Restructure | Delete old files, create plugin directory layout | Verify no valuable content lost |
| 5 | Core System Prompt & Skills | Write CLAUDE.md, implement all 9 skills | Test each skill end-to-end |
| 6 | Knowledge Base & Templates | Implement 10 KB schemas, expand templates, create references | Review KB schema quality |
| 7 | Validation & Testing | Test against case studies (0-to-1 + migration), iterate with `/review` | Review deliverable quality |
| 8 | Documentation & Plugin Packaging | Write docs, create plugin manifest, test local install | Test plugin installation |
| 9 | Marketplace Release | Final QA, MIT license, marketplace submission | Approve public release |

### Git Workflow Per Phase

Every phase follows this commit protocol:

1. Phase executes and produces deliverables
2. `git add` specific files produced in phase
3. `git commit -m "Phase N: [description]"` — commit before human checkpoint
4. **Human checkpoint**: operator reviews, makes improvements, approves
5. Operator pushes approved commits to `main` on github.com

This ensures work is preserved incrementally and the operator can review, improve, and control what gets pushed.

---

## Phase 1: Inventory & Extraction

### Goal

Extract reusable patterns from all 23 agents. Classify every file as KEEP/DELETE/REFACTOR/MERGE. All extracted knowledge must be self-contained — no references to external filesystems or private repos.

### Prompt

Save as `.claude/plans/phase-1-prompt.md`:

```markdown
<role>
You are a Distinguished Engineer performing inventory and pattern extraction for a repository refactoring.
</role>

<instructions>
Phase 1: Inventory & Extraction.

1. Read every file in this repository (excluding .git/ and .venv/).
2. For each file: record path, purpose, line count, disposition (KEEP/DELETE/REFACTOR/MERGE).
3. Extract reusable patterns from all 22 agent prompts in ai_agents/ and supervisor_agent.system.prompt.md:
   - Architectural patterns (supervisor-worker, RAG pipeline, event-driven, etc.)
   - Quality guidelines (TRM validation, Well-Architected checks, security checklists)
   - Prompt engineering techniques (CoT, Step-Back, MODP, Tree-of-Thoughts)
   - Workflow patterns (progressive discovery, phased delivery, iterative refinement)
   - All knowledge must be extracted INLINE — no references to external filesystems, private repos, or paths outside this repository.
4. Produce deletion plan with justifications.

Write output to .claude/plans/phase-1-results.md.
</instructions>

<constraints>
- Do NOT delete or modify any files. Output is documentation only.
- Exclude .git/ and .venv/ from inventory.
- Extract ALL valuable knowledge inline. After this phase, the source agent files will be deleted.
- No references to paths outside this repository (no C:\dev\paloist-core\, no \\wsl.localhost\, no D:\dev\).
</constraints>

<git>
After producing deliverables:
git add .claude/plans/phase-1-results.md
git commit -m "Phase 1: Inventory and pattern extraction complete"
</git>

<human_checkpoint>
Present: file counts by disposition, projected repo size after cleanup, top 10 extracted patterns, uncertain dispositions. Wait for human review and approval before Phase 2.
</human_checkpoint>
```

### Deliverables
- `.claude/plans/phase-1-results.md`

### Success Criteria
- Every non-git/non-venv file has a disposition
- All valuable patterns extracted inline (no external references)
- Deletion plan is complete with justifications

---

## Phase 2: Requirements & Workflow Design

### Goal

Define structured requirements, user stories, and acceptance criteria for the 9-skill SA agent. Define interaction patterns and engagement flows for both 0-to-1 and migration/modernization.

### Prompt

Save as `.claude/plans/phase-2-prompt.md`:

```markdown
<role>
You are a Principal Solutions Architect defining requirements for an AI Solutions Architecture Agent.
</role>

<instructions>
Phase 2: Requirements & Workflow Design.

Read: .claude/plans/master-plan.md, .claude/plans/phase-1-results.md, .claude/rules/guiding-principles.md (42 principles), and ALL files in .claude/plans/references/ — especially:
   - references/pre-sales-lifecycle.md (complete pre-sales process with SA agent augmentation points)
   - references/reference-materials-index.md (real-world exemplar deliverables inventory)
   - references/README.md (comprehensive index of all reference materials)
   - The case study PDFs and PAI exercise

Produce two documents:

1. .claude/plans/requirements.md:
   - Functional requirements by SA lifecycle phase (9 skills)
   - Non-functional requirements (context efficiency, portability, quality)
   - User stories with acceptance criteria for 3 personas: SA at enterprise, independent consultant, startup technical founder
   - Test scenarios from the case study PDFs, PAI exercise, AND real engagement scenarios (AGADA 0-to-1, migration assessments — see references/reference-materials-index.md)
   - Engagement type coverage: 0-to-1 new builds AND migration/modernization
   - Pre-sales lifecycle integration: how skills map to the pre-sales process (see references/pre-sales-lifecycle.md)
   - Sales principles that govern agent behavior (see pre-sales-lifecycle.md section on Sales Principles)

2. .claude/plans/workflow-design.md:
   - User journey map for each engagement type (informed by real pre-sales lifecycle)
   - Skill invocation sequences and interaction patterns
   - KB state flow between skills
   - Multi-session workflow support
   - Error handling and fallback behaviors
   - SOW template structure (from pre-sales-lifecycle.md) as /proposal output format
   - Three-pass estimation model integration (T-shirt -> Plan -> Task estimates)
   - Sprint methodology alignment (2-week sprints, capacity model from consulting delivery model)
</instructions>

<constraints>
- SA scope only — no implementation/deployment requirements.
- Technology-agnostic — agent recommends, not dictates.
- No external filesystem references.
- Quality bar: exemplar-level deliverables.
</constraints>

<git>
git add .claude/plans/requirements.md .claude/plans/workflow-design.md
git commit -m "Phase 2: Requirements and workflow design complete"
</git>

<human_checkpoint>
Present: skill inventory confirmation, user story count by persona, test scenario coverage, open questions. Wait for human review.
</human_checkpoint>
```

### Deliverables
- `.claude/plans/requirements.md`
- `.claude/plans/workflow-design.md`

---

## Phase 3: System Architecture & Technical Design

### Goal

Design the complete technical architecture: plugin structure, skill frontmatter, KB schemas, CLAUDE.md structure, rules, sub-agent strategy, context budget.

### Prompt

Save as `.claude/plans/phase-3-prompt.md`:

```markdown
<role>
You are a Distinguished AI Architect designing a Claude Code plugin for solutions architecture.
</role>

<instructions>
Phase 3: System Architecture & Technical Design.

Read: master-plan.md, requirements.md, workflow-design.md, phase-1-results.md, guiding-principles.md.

Produce .claude/plans/technical-design.md containing:

1. Plugin directory layout (per Anthropic's official plugin structure: skills/ at root, .claude-plugin/plugin.json)
2. CLAUDE.md design (<200 lines, @imports for guiding principles)
3. Skill inventory with complete SKILL.md frontmatter for all 9 skills
4. KB schema specifications (10 JSON files with field definitions)
5. Rules design (unscoped vs path-scoped)
6. Sub-agent strategy (which tasks use context: fork)
7. Context budget allocation (hot/warm/cold tiers in tokens)
8. Mermaid architecture diagrams (skill dispatch, context loading, KB data flow)
9. Plugin manifest specification

Use web research to verify latest Claude Code plugin docs and skill format.
</instructions>

<constraints>
- CLAUDE.md under 200 lines. Unscoped rules under 100 lines total.
- Skills at plugin root (skills/), not .claude/skills/.
- Plugin manifest at .claude-plugin/plugin.json per Anthropic's schema.
- All skills technology-agnostic with WebSearch/WebFetch for dynamic references.
- Include "ultrathink" in skills requiring deep reasoning (architecture, data-model, security-review, review).
- No external filesystem references.
</constraints>

<git>
git add .claude/plans/technical-design.md
git commit -m "Phase 3: Technical design and plugin architecture complete"
</git>

<human_checkpoint>
Present: plugin structure visualization, skill frontmatter table, KB schema summary, context budget, architecture diagrams. Wait for human review.
</human_checkpoint>
```

### Deliverables
- `.claude/plans/technical-design.md`

---

## Phase 4: Cleanup & Restructure

### Goal

Delete old files. Create the target plugin directory layout. Update configuration.

### Prompt

Save as `.claude/plans/phase-4-prompt.md`:

```markdown
<role>
You are a senior engineer performing a controlled repository restructuring into a Claude Code plugin.
</role>

<instructions>
Phase 4: Cleanup & Restructure.

Read: phase-1-results.md (deletion plan), technical-design.md (target layout).

Execute IN ORDER:
1. Create target directories: skills/, agents/, hooks/, .claude-plugin/
2. Delete files marked DELETE (ai_agents/, supervisor_agent, user_prompts/self_improvement/, user_prompts/engineering/, .cursorrules, etc.)
3. Remove empty directories
4. Create .claude-plugin/plugin.json with manifest
5. Move any .claude/skills/ content to skills/ (plugin root)
6. Update .repo-metadata.json for new structure
7. Update .gitignore for plugin structure
8. Remove ALL references to external filesystems (C:\dev\paloist-core\, \\wsl.localhost\, D:\dev\) from any remaining files
9. Run git status to show all changes
</instructions>

<constraints>
- Do NOT delete KEEP or REFACTOR files.
- Do NOT delete .claude/plans/ — planning artifacts.
- Keep knowledge_base/, templates/, tests/ intact.
- Verify phase-1 deletion plan was human-approved.
</constraints>

<git>
git add -A
git commit -m "Phase 4: Repository restructured as Claude Code plugin"
</git>

<human_checkpoint>
Present: deleted file count, created directories, modified configs, git status. Verify no external filesystem references remain. Wait for human review.
</human_checkpoint>
```

### Deliverables
- Clean plugin-structured repository
- `.claude-plugin/plugin.json`
- Updated configuration files

---

## Phase 5: Core System Prompt & Skills

### Goal

Write CLAUDE.md and implement all 9 skills. Each skill produces exemplar-level deliverables.

### Prompt

Save as `.claude/plans/phase-5-prompt.md`:

```markdown
<role>
You are a Distinguished AI Architect implementing the core prompt and skills for an AI Solutions Architecture Agent plugin.
</role>

<instructions>
Phase 5: Core System Prompt & Skills.

Read: technical-design.md, requirements.md, workflow-design.md, phase-1-results.md (extracted patterns), guiding-principles.md (42 principles including client partnership section), references/pre-sales-lifecycle.md (pre-sales process, SOW structure, consulting delivery model, sales principles), references/reference-materials-index.md (real exemplar deliverables as quality bar).

Implement:

1. CLAUDE.md (<200 lines): SA agent identity, scope boundary (design only, not implementation), skill reference, @import guiding principles, plugin-compatible.

2. Nine SKILL.md files in skills/ (plugin root):

   Core (5):
   - skills/requirements/SKILL.md — Progressive discovery (quick/standard/comprehensive). Greenfield + migration.
   - skills/architecture/SKILL.md — Sub-modes: high-level design, detailed component, technology selection, diagrams (ASCII + Mermaid). ultrathink.
   - skills/estimate/SKILL.md — Cost, LOE, team composition, infrastructure modeling.
   - skills/project-plan/SKILL.md — Roadmaps, phasing, milestones. 0-to-1 + migration timelines.
   - skills/proposal/SKILL.md — Assembly from KB: discovery/implementation/internal/pitch.

   Specialized (3):
   - skills/data-model/SKILL.md — Knowledge bases, neurosymbolic AI, ontologies, graphs, vector schemas. ultrathink.
   - skills/security-review/SKILL.md — Threat modeling, compliance, defense-in-depth, encryption. ultrathink.
   - skills/integration-plan/SKILL.md — API design, migration strategies, legacy bridging, strangler fig.

   Quality (1):
   - skills/review/SKILL.md — LLM-as-judge: 3 iteration passes. Scores: completeness, technical soundness, well-architected, clarity, feasibility. ultrathink.

3. Updated .claude/rules/:
   - skills.md (path-scoped: skills/**)
   - knowledge-base.md (updated for new KB schema)

All skills must use WebSearch/WebFetch for dynamic technology references. No static vendor knowledge. No external filesystem references.
</instructions>

<constraints>
- CLAUDE.md under 200 lines.
- Each skill self-contained per Agent Skills standard.
- Technology-agnostic — recommend, never default to specific vendors.
- Quality: exemplar-level output (maximum, not "good enough").
- ultrathink in architecture, data-model, security-review, review skills.
- Runs on arbitrary Windows and Linux — no operator-specific paths.
</constraints>

<git>
git add CLAUDE.md skills/ .claude/rules/
git commit -m "Phase 5: Core system prompt and 9 skills implemented"
</git>

<human_checkpoint>
Present: CLAUDE.md with line count, each skill with frontmatter summary, context budget. Test each skill with a sample invocation. Wait for human review.
</human_checkpoint>
```

### Deliverables
- `CLAUDE.md` + 9 `skills/*/SKILL.md` + updated `.claude/rules/`

---

## Phase 6: Knowledge Base & Templates

### Goal

Implement the 10-file KB schema. Expand templates. Create reference documents. All knowledge extracted inline — no external dependencies.

### Prompt

Save as `.claude/plans/phase-6-prompt.md`:

```markdown
<role>
You are a data architect implementing the knowledge base for a 9-skill AI Solutions Architecture Agent.
</role>

<instructions>
Phase 6: Knowledge Base & Templates.

Implement:

1. KB JSON files (10): engagement.json, requirements.json, architecture.json, data_model.json, security_assessment.json, integration_map.json, estimates.json, project_plan.json, reviews.json, system_config.json (updated).
2. JSON Schema files for each in knowledge_base/schemas/.
3. Templates for all 9 skill outputs in templates/.
4. Reference documents (loaded on-demand by skills):
   - Well-Architected Framework summary (AWS 6 pillars + GenAI Lens + Responsible AI Lens, Azure WAF, GCP WAF)
   - Common architecture patterns (supervisor-worker, RAG, event-driven, CQRS, strangler fig, etc.)
   - Neurosymbolic AI architecture patterns
   - SA quality rubric (used by /review skill)
5. Update tests/validate_knowledge_base.py for new schemas.
6. Cross-reference audit: verify all @path references in CLAUDE.md, skills, and rules.

All reference content must be extracted inline in this repo — no references to external filesystems, private repos, or the Paloist project directory.
</instructions>

<constraints>
- All JSON must validate against schemas.
- Templates must match exemplar quality.
- No external filesystem references.
- KB supports both greenfield and migration engagements.
</constraints>

<git>
git add knowledge_base/ templates/ tests/
git commit -m "Phase 6: Knowledge base schemas, templates, and references implemented"
</git>

<human_checkpoint>
Present: KB schema inventory, template inventory, reference documents, validation results, cross-reference audit. Wait for human review.
</human_checkpoint>
```

### Deliverables
- 10 KB JSON files + schemas + templates + references + updated tests

---

## Phase 7: Validation & Testing

### Goal

Test against case studies (0-to-1 and migration) and PAI exercise. Use `/review` skill to iterate on quality. Target: exemplar-level output.

### Prompt

Save as `.claude/plans/phase-7-prompt.md`:

```markdown
<role>
You are a QA architect validating an AI Solutions Architecture Agent against real-world scenarios.
</role>

<instructions>
Phase 7: Validation & Testing.

Read: references/reference-materials-index.md and references/README.md for real-world exemplar deliverables to compare against.

Test 5 scenarios (see references/README.md for full details):

1. Healthcare Platform (0-to-1, from AGADA Hyperbloom engagement): /requirements → /architecture → /data-model → /security-review → /estimate → /project-plan → /proposal → /review. Compare against: hyperbloom-agada-architecture.pdf, hyperbloom-agada-project-plan.pdf.
2. Cloud Migration Assessment (migration, from AVAHI Bluebird/SmartTrix): /requirements → /integration-plan → /architecture → /security-review → /estimate → /project-plan → /proposal → /review. Compare against AVAHI migration SOWs.
3. GenAI Agent Platform (0-to-1, from Revelex Hyperbloom engagement): /requirements → /architecture → /data-model → /estimate → /project-plan → /proposal → /review. Compare against: hyperbloom-revelex-proposal.pdf.
4. Discovery-Only Assessment (from AVAHI AInnocence): /requirements → /architecture → /security-review → /proposal. Compare against AInnocence assessment SOW.
5. Multi-Industry Quick Discovery (from AVAHI RAPID templates): /requirements (all 3 tiers). Compare against: avahi-rapid-assessment-templates.xlsx.

For each scenario:
- Run each skill in sequence
- Use /review (3 iterations) to improve each deliverable
- Score against: completeness, technical soundness, well-architected alignment, clarity, feasibility
- Document pass/fail per skill per scenario
- Fix any issues found

Write results to .claude/plans/phase-7-results.md.
</instructions>

<constraints>
- Quality target: exemplar-level.
- All 9 skills must be tested at least once.
- /review must run 3 improvement iterations per deliverable.
- Document all fixes applied.
</constraints>

<git>
git add .claude/plans/phase-7-results.md skills/ knowledge_base/
git commit -m "Phase 7: Validation complete — all scenarios pass"
</git>

<human_checkpoint>
Present: pass/fail matrix, quality scores, top issues and fixes, remaining limitations, readiness assessment. Wait for human review.
</human_checkpoint>
```

### Deliverables
- `.claude/plans/phase-7-results.md` + any skill fixes

---

## Phase 8: Documentation & Plugin Packaging

### Goal

Write user docs. Finalize plugin packaging. Test local installation on Windows.

### Prompt

Save as `.claude/plans/phase-8-prompt.md`:

```markdown
<role>
You are a technical writer and release engineer packaging an AI Solutions Architecture Agent as a Claude Code plugin.
</role>

<instructions>
Phase 8: Documentation & Plugin Packaging.

1. Plugin packaging:
   - Finalize .claude-plugin/plugin.json
   - Test: claude --plugin-dir . (local installation)
   - Verify all 9 skills are discoverable as solutions-architecture-agent:skill-name
   - No hardcoded absolute paths anywhere

2. Documentation:
   - README.md: what it does (SA lifecycle, not implementation), quick start, 9-skill reference, engagement types, target users, scope boundary, MIT license
   - ARCHITECTURE.md: plugin structure, skill dispatch, KB data flow, context hierarchy (Mermaid diagrams)
   - CONTRIBUTING.md: how to create/modify skills, testing, PR process
   - docs/getting-started.md: 0-to-1 walkthrough, migration walkthrough
   - Update .github/ files

3. Verify portability: no operator-specific paths, runs on arbitrary Windows + Linux.
</instructions>

<constraints>
- README under 200 lines.
- No external filesystem references.
- Plugin must install and work from local path.
- MIT license.
</constraints>

<git>
git add README.md ARCHITECTURE.md CONTRIBUTING.md LICENSE docs/ .claude-plugin/ .github/
git commit -m "Phase 8: Documentation and plugin packaging complete"
</git>

<human_checkpoint>
Present: local plugin install test results, README preview, architecture diagrams, getting started walkthrough. Wait for human review.
</human_checkpoint>
```

### Deliverables
- All documentation + finalized plugin manifest + LICENSE

---

## Phase 9: Marketplace Release

### Goal

Final QA. Push to GitHub. Submit to Claude Code marketplace.

### Prompt

Save as `.claude/plans/phase-9-prompt.md`:

```markdown
<role>
You are a release engineer performing final QA and marketplace submission.
</role>

<instructions>
Phase 9: Marketplace Release.

1. Final QA:
   - Run all validation scripts
   - Verify no secrets, credentials, PII, or external filesystem references
   - Verify .gitignore covers sensitive paths
   - Verify .repo-metadata.json is accurate
   - Run /review on the plugin's own architecture (dogfooding)

2. License: MIT, Copyright Modular Earth LLC

3. Release:
   - Create GitHub release tag (v1.0.0)
   - Test install from GitHub: claude /plugin install github:Modular-Earth-LLC/solutions-architecture-agent
   - Submit to official Claude Code marketplace
   - Document: what outputs from this agent the future AI Engineering Agent will consume → .claude/plans/references/engineering-agent-interface.md
</instructions>

<constraints>
- Do NOT publish without explicit human approval.
- All validation must pass.
</constraints>

<git>
git add -A
git commit -m "Phase 9: Final QA complete — ready for release"
git tag v1.0.0
</git>

<human_checkpoint>
Present: final QA report, plugin install test from GitHub URL, marketplace listing preview, release notes. Ask: "Ready to push and publish?"
</human_checkpoint>
```

### Deliverables
- MIT LICENSE, GitHub release tag, marketplace submission, engineering agent interface doc

---

## Appendix A: Research Findings Summary

### Claude Code Plugin System

- **Plugin manifest**: `.claude-plugin/plugin.json`. Only required field: `name`. Optional: version, description, author, homepage, repository, license, keywords, custom paths for skills/agents/hooks/mcp.
- **Directory convention**: `skills/` at plugin root (not `.claude/skills/`), `agents/`, `hooks/hooks.json`, `.mcp.json`.
- **Installation**: Local (`--plugin-dir`), GitHub (`/plugin install github:org/repo`), marketplace (`/plugin install name@marketplace`).
- **Namespacing**: Plugin skills appear as `plugin-name:skill-name`.
- Source: [code.claude.com/docs/en/plugins](https://code.claude.com/docs/en/plugins), [code.claude.com/docs/en/plugins-reference](https://code.claude.com/docs/en/plugins-reference)

### Agent Skills Standard

- Released December 18, 2025. 32 platforms adopted as of March 2026.
- Source: [agentskills.io](https://agentskills.io), [anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

### Single-Agent vs Multi-Agent

- Google/MIT (arXiv:2512.08296): 180 experiments. Multi-agent degrades sequential reasoning 39–70%. Single-agent: 67.7 successful tasks per 1K tokens vs 21.5 for centralized multi-agent. Threshold: if single agent solves >45% correctly, multi-agent rarely helps.
- Source: [arxiv.org/abs/2512.08296](https://arxiv.org/abs/2512.08296)

### Well-Architected Frameworks

- **AWS**: 6 pillars + 3 AI lenses (Responsible AI Lens [new], ML Lens [updated], GenAI Lens [updated] — all at re:Invent 2025). GenAI Lens includes agentic AI patterns.
- **Azure**: 5 pillars + dedicated AI workload section with maturity models.
- **GCP**: 5 pillars + AI/ML cross-pillar perspective.
- Sources: [docs.aws.amazon.com](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html), [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/well-architected/ai/), [docs.cloud.google.com](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml)

### Competitive Landscape

No widely adopted tool covers the full SA lifecycle (ideation → requirements → architecture → team → cost → project plan). Market is fragmented across diagramming (Eraser.io, Mermaid), IaC generation (Pulumi Neo, Brainboard), compliance (AWS WAF Tool, CloudCheckr), and coding tools (Copilot, Claude Code).

---

## Appendix B: Extracted Patterns (from Appendix C of v1)

Preserved inline from Phase 1 extraction. Key patterns:

1. **Progressive Discovery** — tiered workshops (quick 30min / standard 60min / comprehensive 90min)
2. **6-Step Design Process** — Requirements → Tech Stack → Diagram → Team → LOE → Cost
3. **Generate-Validate-Improve** — produce candidates, validate, iterate (max 3 rounds)
4. **Well-Architected Compliance** — 6 pillars + GenAI Lens for every design
5. **Confidence & Escalate** — AI estimates with confidence scoring, threshold-based human escalation
6. **Assembly from KB** — read structured state, assemble into executive deliverable
7. **Prompt Engineering Techniques** — CoT (25–40%), Step-Back (15–20%), MODP (26%), Tree-of-Thoughts (20–35%)
8. **Dual-Persona Validation** — Builder generates, Tester validates
9. **Phased Delivery** — MVP → Enhancement → Scale with decision gates
10. **Security-First** — least-privilege, encryption at rest/transit, parameterized queries

---

## Appendix C: User Prompt Migration Map

| Source | Count | Target | Deleted |
|--------|-------|--------|---------|
| Requirements (4) | 4 | → `/requirements` | 0 |
| Architecture (6) | 6 | → `/architecture` + `/estimate` + `/project-plan` | 0 |
| Proposals (4) | 4 | → `/proposal` | 0 |
| Deployment (3) | 0 | Out of scope | 3 |
| Prompt Engineering (5) | 0 | Out of scope | 5 |
| Engineering (20) | 0 | Patterns extracted to `/data-model`, `/security-review` | 20 |
| Self-Improvement (18) | 0 | Meta-improvement not needed | 18 |
| **Total: 60** | **14 migrated** | **→ 9 skills** | **46 deleted** |
