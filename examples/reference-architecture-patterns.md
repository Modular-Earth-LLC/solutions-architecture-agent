# Reference Architecture Patterns

> **WARNING**: These patterns are extracted from a DIFFERENT project (paulprae.com — a Next.js career platform). They are included as REFERENCE ONLY for architectural inspiration. Do NOT confuse these with the target architecture for the PAI packaging pipeline.

## Pattern 1: Build Pipeline (Ingest → Generate → Export)

paulprae.com uses a sequential pipeline:
1. `ingest` — parse structured inputs into normalized JSON
2. `generate` — AI generates artifacts from structured data
3. `export` — produce output formats (PDF, DOCX, images)
4. `build` — assemble final deliverable
5. `deploy` — push to hosting

**Relevance to PAI**: The packaging pipeline follows the same pattern: parse SKU brief → construct prompts → generate images → overlay text → upload to S3.

## Pattern 2: Model Routing (Tiered by Task)

| Use Case | Model | Rationale |
|----------|-------|-----------|
| Fast runtime tasks | Claude Sonnet 4.6 | Speed + cost ($3/$15 per MTok) |
| Quality artifacts | Claude Opus 4.6 | Depth for permanent outputs |
| Classification | Claude Haiku 4.5 | Sub-second, cheapest |

**Relevance to PAI**: Apply same tiering — Titan V2 for dev ($0.01), Nova Canvas for iteration ($0.04), SD3.5 Large for final renders ($0.08).

## Pattern 3: Context Injection Over RAG (at Small Scale)

When the full dataset fits in the context window, inject it directly rather than building a vector retrieval system. Migrate to RAG only when data grows beyond context limits.

**Relevance to PAI**: SKU briefs and brand guidelines are small — inject into prompts directly. No vector DB needed for PoC.

## Pattern 4: Prompt Caching

Anthropic's ephemeral caching (5-min TTL) reduces costs ~90% on follow-up API calls when the system prompt is stable across a session.

**Relevance to PAI**: If the pipeline makes multiple Bedrock calls with similar prompt prefixes, explore caching to reduce costs during batch generation.

## Pattern 5: Cost Controls

- Output token caps per use case
- Model tiering (expensive models only for final output)
- Rate limiting on public-facing endpoints
- Spend limits in provider consoles
- Local caching to avoid re-generation during debugging

**Relevance to PAI**: Cache generated images locally. Use `--dry-run` flag for zero-cost pipeline validation. Default to cheapest model during development.

## Pattern 6: Single Agent with Tools (Not Multi-Agent)

For narrow-scope tasks, a single agent with well-defined tools outperforms multi-agent orchestration. Use tool-calling (`tool()` definitions with schemas) rather than agent delegation.

**Relevance to PAI**: The pipeline is a single agent (Claude Code) with tools (skills/commands). No LangChain, no CrewAI, no multi-agent framework needed.
