# PAI Take-Home Exercise — Solution Re-Architecture & Plan of Plans

## Objective

Re-run the SA agent's greenfield workflow with improved inputs to produce higher-quality deliverables for the Adobe PAI Take-Home Exercise. Iterate on the previous run's KB artifacts — preserve what worked, close identified gaps, and incorporate the resolved architecture decisions below.

**Primary output**: A **plan of plans** — standalone, phase-based Claude Code plan files that a coding assistant can execute to implement the full solution from zero to deployed demo in one work day.

**Secondary output**: An improved proposal.md for the Adobe interview panel.

**Two audiences**:
1. Adobe interview panel (senior engineers + hiring manager) — they review the GitHub repo, proposal, and live demo
2. Claude Code implementation agent — it receives only the plan-of-plans, the exercise file, and context snapshots from prior phases

**Depth**: STANDARD
**Engagement type**: greenfield (re-run, informed by previous deliverables)

---

## SA Agent Workflow

Run the full greenfield workflow in a single session:

```
/requirements → /architecture → /data-model → /security-review → /estimate → /project-plan → /proposal → /review
```

After `/project-plan`, produce the plan-of-plans (see §Plan-of-Plans Specification).
After `/proposal`, the proposal should reference the plan-of-plans and serve as the human-readable companion document.

**Previous run context**: KB artifacts in `knowledge_base/` and the previous proposal at `outputs/eng-2026-003/proposal.md` inform this re-run. Reference them for decisions that worked, gaps identified in reviews, and content worth preserving. Do not start from zero — iterate and improve.

---

## Exercise Requirements

Source: `inputs/PAI-Take_Home_Exercise.md`

### Must-Have (from exercise)

- Accept SKU brief (JSON): 2+ products/flavors, target region/market, audience/demographics, key attributes
- Accept input assets from S3; generate missing assets via GenAI
- Packaging designs in 3 aspect ratios: front label (1:1), back label (9:16), wraparound (16:9)
- Display product messaging, key attributes, and regulatory information on final designs
- Run in AWS (CLI is acceptable)
- Save outputs to S3 organized by SKU, Region, and format
- README: how to run, example I/O, design decisions, assumptions/limitations
- Deploy AWS resources via CloudFormation
- Public GitHub repository
- Working CI/CD via GitHub Actions (competitive differentiator — treat as must-have)

### Nice-to-Have (implement last, after all must-haves are demo-ready)

- Brand compliance checks (logo presence, required color usage, font consistency)
- Regulatory content checks (allergen disclosures, ingredient lists, certifications by region)
- Approval status tracking and generation logging

### Interview Format

- 20–30 min: present code + live demo/edit with engineers
- 10–15 min: foundational technical questions (not necessarily related to deliverables)
- 5–10 min: candidate questions

---

## Previous Run: What Worked, What Changes

### Preserve

- Simple GenAI pipeline pattern — direct function calls, no orchestration frameworks
- S3 organized by `{SKU}/{Region}/{format}/`
- CloudFormation for IaC
- Tiered model strategy: cheap models for dev, quality models for final renders
- Direct boto3 API calls (no LangChain/LlamaIndex)
- Pillow for text overlay compositing
- 5 core data entities: SKU Brief, Brand Asset, Generated Image, Packaging Output, Pipeline Run
- STRIDE threat model (12 threats) and IAM least-privilege design
- Task-level time blocks (sub-day PoC, not sprint-based)

### Change

- **Claude Code IS the interface** — no separate CLI or UI to build. Custom skills/commands control pipeline runs, result viewing, deployment, and admin
- **CI/CD is must-have** — GitHub Actions with automated testing, linting, and deployment
- **Text reasoning via Bedrock** — use `anthropic.AnthropicBedrock()` for any Claude text tasks in the pipeline (prompt construction, compliance checks), consolidating billing and auth with image generation
- **Agentic = Claude Code skills + AWS MCP tools** — not orchestration frameworks
- **No database** — flat JSON + S3 only. PostgreSQL/RDS moves to future roadmap
- **Automated QA** — Claude Code hooks for linting, testing, and deployment safety
- **Budget unconstrained** — optimize for quality and speed, not cost minimization
- **Estimate AI-assisted hours** — Claude Code + Sonnet do the coding. Do not estimate raw human labor hours

### Gaps to Close (from R-001, R-002 reviews)

- GenAI model quality criteria not elicited → add to requirements
- Nova Canvas vs SD3.5 Large: no benchmark evidence → resolve via web research
- Reliability was lowest WA score (6/10) → add retry/backoff
- S3 Block Public Access missing from CloudFormation template → add
- Credential management strategy undocumented → document AWS CLI named profiles

---

## Resolved Architecture Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Language | Python 3.12 + Bash | boto3 is canonical Bedrock SDK; Pillow is battle-tested for image ops; `anthropic.AnthropicBedrock()` for text reasoning; most Bedrock docs/examples are Python-first. Bash for automation scripts. Single programming language minimizes complexity. |
| IaC | CloudFormation (YAML) | All-in on AWS; self-contained; no npm or HCL dependency; exercise lists it explicitly |
| CI/CD | GitHub Actions | Native GitHub integration; AWS deployment actions available; GitHub Copilot for workflow authoring |
| Interface | Claude Code CLI | Zero UI development time; custom skills = pipeline commands; MCP tools = AWS admin; natural language interaction for everything |
| Text reasoning | Claude on Bedrock via `anthropic.AnthropicBedrock()` | Consolidated AWS billing; single IAM auth; same credential story as image gen. Research simplest approach between this and direct Anthropic API — choose whichever minimizes integration complexity. |
| Image generation | Bedrock: SD3.5 Large (primary), Nova Canvas (secondary), Titan V2 (dev) | Tiered cost strategy. Verify model availability and benchmark quality via web research. Avoid generic Amazon models (Nova, Titan) for final renders — use specialized models. |
| Image processing | Pillow (PIL) | Sub-second text overlay; Lambda-compatible; no native binary complications |
| Database | None (flat JSON + S3) | PoC scope; simplicity; databases are future roadmap |
| Orchestration | None (direct function calls) | No LangChain, LlamaIndex, or agent frameworks. Pipeline stages are simple Python functions. |
| Compute | Local CLI + Lambda-extensible | Simplest execution model for PoC; demo-friendly; Lambda wrapper is a natural extension |
| Region | Verify via web research | Check SD3.5 Large, Nova Canvas, Titan V2, and Claude availability by region. Choose region with full model coverage. |
| Repo name | `pai-take-home-exercise` | GitHub naming conventions from exercise filename |
| Dev environment | Windows 11, Git Bash, C:\dev | See `inputs/windows-dev-environment.md` |

---

## Claude Code as Application Interface

Claude Code is the conversational interface and command center. All admin, pipeline runs, result viewing, and deployment happen through Claude Code. This eliminates the need to build a separate UI or CLI framework.

### Custom Skills to Build (`.claude/skills/` in target repo)

| Skill | Purpose | Safety |
|-------|---------|--------|
| `/run-pipeline <sku-brief>` | Execute packaging pipeline for a given SKU brief | `disable-model-invocation: true` |
| `/pipeline-status` | Show recent runs, output counts, S3 contents | Read-only |
| `/view-results <sku> [region]` | Display/open generated packaging images | Read-only |
| `/deploy [env]` | Deploy CloudFormation stack | `disable-model-invocation: true` |
| `/teardown [env]` | Destroy CloudFormation stack | `disable-model-invocation: true`, confirm |
| `/health-check` | Verify AWS resources, Bedrock access, S3 buckets | Read-only |
| `/run-tests` | Execute full test suite | Safe |
| `/generate-demo` | Run pipeline with sample SKU briefs for demo data | `disable-model-invocation: true` |

### Hooks (`.claude/settings.json` in target repo)

- `PostToolUse` on `Edit|Write` → auto-lint changed files
- `Stop` → run tests before Claude considers a task complete (block if tests fail)
- `PreToolUse` on `Bash` → validate no destructive AWS commands without confirmation

### MCP Servers (`.mcp.json` in target repo)

Install the latest official AWS MCP servers via stdio transport. On Windows, use `cmd /c npx -y @awslabs/<server>` wrapper.

Recommended servers (verify latest at github.com/awslabs/mcp):
- **AWS Knowledge MCP Server** — documentation and architectural guidance
- **AWS IaC MCP Server** — CloudFormation best practices and security validation
- **AWS CloudFormation MCP Server** — direct resource management via Cloud Control API

Deprecated (do NOT use): AWS Cloud Control API, AWS CDK, AWS Terraform MCP servers.

---

## Design Principles

1. **Simplicity over enterprise** — extra-minimal MVP. Flat JSON over databases. Direct function calls over frameworks. Three similar lines over a premature abstraction.
2. **Always demo-ready** — every completed phase must be fully functional. Nice-to-haves are last. If time runs out, the demo still works.
3. **AI-first development** — Claude Code + GitHub Copilot do all coding. Estimate AI-assisted development speed, not raw human labor hours.
4. **Scope ruthlessly** — challenge any requirement that does not directly impress Adobe interviewers or meet the exercise spec. No work they will not see or ask about.
5. **Fake what you must** — this is a demo. Synthetic data, placeholder assets, simulated compliance databases are acceptable. Document honestly and explicitly what is real vs. simulated.
6. **Minimize dependencies** — one language (Python). No frameworks beyond boto3 + Pillow + anthropic. Minimal pip packages. Simple `requirements.txt`.
7. **Flat-file-first** — start with flat JSON files along the pipeline. Add complexity only when proven necessary.
8. **Cache everything** — generated images, prompt templates, API responses. Avoid re-generation during debugging. Implement `--dry-run` for zero-cost pipeline validation.
9. **Regulatory compliance matters** — AI governance and data compliance are part of Paul's professional brand. Enforce meaningfully, not as a checkbox.
10. **Brand consistency via prompts + data** — encode brand guidelines in prompt templates and SKU brief schema. No vector DB or RAG unless trivially simple to add.
11. **Generate text and graphics separately** — use best-fit models for each task, then composite via Pillow. Text overlay is separate from image generation.
12. **Open source data only if easier** — if a free dataset (regions, cultures, compliance) saves time vs. synthesizing, use it. Otherwise synthesize.
13. **Lean documentation** — concise, elegant, simple. No bloat. Clear separation of concerns between docs. Each doc is a single source of truth for its topic.
14. **LLM-as-judge for QA** — use Claude Code and GitHub Copilot for automated review of code, architecture, and outputs during development. Use Bedrock Claude for runtime quality checks in the pipeline itself where appropriate.
15. **Use native SDKs and APIs directly** — boto3, not wrapper libraries. AWS CLI, not third-party tools. Pre-built managed service configurations over custom implementations.
16. **Leverage boilerplate from authoritative sources** — AWS sample projects, official starter templates, pre-configured IAM policies from AWS documentation.

---

## Plan-of-Plans Output Specification

After `/project-plan`, produce a plan of plans. This is the PRIMARY deliverable for driving implementation.

### Structure

Produce these files in `outputs/eng-2026-003/plans/`:

```
outputs/eng-2026-003/plans/
  00-master-plan.md              # Index, dependency graph, usage instructions
  phase-01-foundation.md         # Env setup, repo creation, AWS config
  phase-02-core-pipeline.md      # SKU parser, Bedrock gen, Pillow overlay
  phase-03-output-quality.md     # Multi-ratio gen, S3 org, caching, manifest
  phase-04-cicd-testing.md       # GitHub Actions, tests, linting, deploy
  phase-05-docs-demo.md          # README, example I/O, demo data, design doc
  phase-06-enhancements.md       # Nice-to-haves (brand checks, regulatory, tracking)
```

Phase count and boundaries should be determined by the architecture — the above is a starting structure to adapt.

### Master Plan (`00-master-plan.md`)

- Links to all phase plans in execution order
- Global acceptance criteria (what "done" looks like for the whole project)
- Phase dependency graph (which phases depend on which)
- Instructions: load SA plugin in Claude Code, enter plan mode, execute phase by phase
- Reference to exercise spec: `inputs/PAI-Take_Home_Exercise.md`

### Each Phase Plan (`phase-NN-<name>.md`)

Each phase plan must be **self-contained** — loadable into a fresh Claude Code session with zero prior context beyond the exercise spec and context snapshots from completed phases.

**Required sections in each phase plan**:

1. **Phase Objective** — what this phase delivers, in 2-3 sentences
2. **Prerequisites Checklist** — files, resources, and AWS services that must exist before starting. Include verification commands.
3. **Context from Prior Phases** — reference `phase-NN-complete.md` snapshots. First phase references only the exercise spec.
4. **Architecture Decisions Relevant to This Phase** — subset of the full architecture table that applies here
5. **Tasks** — numbered, specific, actionable. Each task has:
   - What to build/configure
   - Acceptance criteria
   - Verification command (test, lint, or manual check)
6. **Automated Verification** — commands to run before human review (tests, linting, health checks, dry-run pipeline execution)
7. **Human Gate** — after automated verification passes, present summary to human for approve/continue. The human should not need to make manual edits — only review and approve.
8. **Exit Protocol**:
   - Save `phase-NN-complete.md` context snapshot documenting: what was built, what changed from the plan, decisions made during execution, any deviations
   - Update ALL subsequent phase plans with changes from this phase's execution (paths, decisions, discovered constraints)
   - Commit and push completed work

### Phase Plan Design Constraints

- **Fault-tolerant**: If Claude crashes mid-phase, the context snapshot from the last completed phase + the current phase plan is sufficient to resume
- **Pivot-friendly**: Each phase plan includes enough context to adapt if prior phases deviated from the original plan. The exit protocol's "update future phases" step ensures downstream plans reflect reality.
- **Multi-session safe**: No assumptions about conversation history. Each phase starts from filesystem state + plan file only.
- **AI-first execution**: Plans assume Claude Code (Sonnet) executes all coding, testing, and deployment tasks. Human actions are limited to: approve/continue, enable Bedrock model access in AWS console, and provide AWS credentials.

### Implementation Context

The implementation agent operates in the NEW repo (`C:\dev\pai-take-home-exercise`) with:
- The current phase plan file
- The exercise spec (`inputs/PAI-Take_Home_Exercise.md`, copied into the new repo during Phase 1)
- Context snapshots from all completed prior phases
- The repo's own CLAUDE.md, skills, hooks, and MCP config (set up in Phase 1)

Claude Code enters plan mode first to review and refine the phase plan, then switches to execution mode. This plan→execute cycle repeats for each phase.

---

## Technical Project Management

- **Phase 1 automation**: Script the full local dev environment setup — repo creation (`gh repo create praeducer/pai-take-home-exercise --public`), directory structure, Python venv, AWS CLI auth verification, Bedrock model access check, MCP server installation, CLAUDE.md + skills + hooks scaffolding
- **Human action list**: Enumerate all manual steps required before or during implementation:
  - Enable Bedrock model access (SD3.5 Large, Nova Canvas, Titan V2, Claude) in AWS console
  - Run `aws configure sso` or `aws configure` for CLI authentication
  - Verify GitHub CLI auth (`gh auth status`)
  - Any other console-only operations
- **Always demo-ready**: Every phase ends with a working, demo-able state. Phase 2 completion = a pipeline that generates at least one image. Phase 3 = all three aspect ratios working. And so on.
- **Business-focused outputs**: Pipeline results should render as Markdown + images viewable on GitHub.com — the primary interface where hiring managers review the work
- **Honest backlog**: Maintain `BACKLOG.md` in the target repo with future improvements. Log items during development. Include QuickSight integration (point to S3 buckets), PostgreSQL data layer, multi-language localization, fine-tuned models.
- **Skill-appropriate tasks**: Flag any exercise requirements that may be challenging for Paul. Strengths: AWS architecture, Python, data engineering, AI/ML, Claude Code, boto3. Potential gaps: advanced graphic design, font rendering, image generation prompt engineering. See `inputs/paul-prae-profile.md`.
- **GitHub as showcase**: The repo itself is a deliverable. Clean commit history, clear PR descriptions, meaningful branch names, comprehensive README. Hiring managers will browse the repo before the interview.

---

## QA Personas

Embed review prompts in phase plans that evaluate outputs from two perspectives:

1. **Adobe hiring managers and principal engineers** (primary) — evaluate: code quality, architecture decisions, technical depth, clarity of design rationale, AWS best practices, clean repo structure
2. **Imaginary CPG manufacturer stakeholders** (secondary) — evaluate: business value of pipeline outputs, packaging image quality, brand consistency, regulatory compliance, time-to-market improvement

---

## Guardrails

1. **Meet all exercise requirements** — the final application MUST satisfy every must-have from the exercise spec. Cross-reference the requirements checklist before declaring any phase complete.
2. **No hallucinated data** — no fabricated numbers, costs, benchmarks, or pricing. Cite authoritative sources for all numerical claims. Be skeptical of any numbers generated by LLMs, including yourself.
3. **Internal consistency** — all decisions, code, documentation, and claims must be consistent across all deliverables. Cross-reference everything.
4. **Current as of March 18, 2026** — all technologies, features, pricing, model availability, and API references must be verified current. Perform web research to confirm.
5. **Accessible services only** — no AWS services unavailable in Paul's region, restricted to enterprise accounts, or in private preview without access.
6. **One work day** — the plan-of-plans must be executable in one focused work day with AI-assisted development. If it cannot, scope down until it can. Always have a working demo at any point after Phase 2.
7. **Solo developer** — there are no other engineers. Paul + Claude Code + GitHub Copilot. Do not plan for team coordination, code reviews from others, or handoffs.

---

## Future Roadmap Items (Deferred to BACKLOG.md)

Include these in the target repo's `BACKLOG.md` with brief implementation notes:

- PostgreSQL on RDS for structured data (approval tracking, run history)
- Amazon QuickSight dashboard (point to S3 output buckets for visual analytics)
- Multi-language localization beyond English
- Fine-tuned image models for brand-specific style
- Production auto-scaling (Lambda, API Gateway)
- A/B testing pipeline for packaging variants
- Real regulatory compliance database integration
- Web dashboard UI for non-technical stakeholders
- Brand asset library management system

---

## Input Files

| File | Purpose |
|------|---------|
| `inputs/PAI-Take_Home_Exercise.md` | Original exercise specification — the source of truth for all requirements |
| `inputs/paul-prae-profile.md` | Developer profile: skills, certifications, relevant AWS experience, potential gaps |
| `inputs/windows-dev-environment.md` | Development environment: Windows 11, Git Bash, D:\dev, Dev Drive |
| `examples/reference-architecture-patterns.md` | Architecture patterns from a prior project — REFERENCE ONLY, not the target architecture |
| `knowledge_base/*.json` | Previous run KB artifacts — iterate on these, do not start from zero |
| `outputs/eng-2026-003/proposal.md` | Previous proposal — iterate and improve |

---

## Real Data

| Field | Value |
|-------|-------|
| AWS Account | `arn:aws:account::730007904340:account` |
| AWS Root Email | `paul@modular.earth` |
| GitHub Username | `praeducer` |
| Developer Name | Paul Prae |
| Target Repo | `pai-take-home-exercise` (public, under `praeducer`) |
| Dev Path | `C:\dev\pai-take-home-exercise` |
| Budget | Unconstrained. Optimize for quality and development speed, not cost. |
| Timeline | One full work day for implementation |
