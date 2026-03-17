# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-03-17

### Added
- **Depth tiers**: QUICK/STANDARD/COMPREHENSIVE depth control in all 9 skills
- **Scope negotiation**: mandatory step in dispatch — asks deliverable, audience, length, time budget, user context
- **3 new canonical flows**: Direct Delivery, Rapid Assessment, Custom Document
- **Deliverable-first mode**: routes single-document requests to QUICK depth automatically
- **Skeleton-first generation**: `/proposal --type custom` generates outline, waits for approval, then expands
- **Review modes**: single-file, final-document (for outputs/), batch (--batch)
- **Output templates**: single-document-template.md, presentation-template.md
- **QUICK example**: examples/quick-assessment/ with minimal engagement + output
- 2 new test scripts: test_workflow_validation.py (8 checks), test_output_quality.py (5 checks)
- `engagement_depth` and per-lifecycle `depth` fields in engagement schema

### Changed
- **MANDATORY STOP** in all 9 skill completion sections — no auto-invocation of next skill
- Sub-agent invocations are now conditional on depth tier (QUICK skips all sub-agents)
- Per-tier output length constraints in all 9 skills
- `/proposal` now suggests final-document review of assembled output
- Prerequisite validation checks `reviewed` field before proceeding (STANDARD/COMPREHENSIVE)
- Version bumped to 1.1.0 across plugin.json and .repo-metadata.json

### Research Basis
- Skeleton-of-thought (ICLR 2024): 2x speed, equal quality
- Word budgets (arXiv 2508.13805): 95% length compliance
- Constrained output (arXiv 2407.19825): higher accuracy with shorter output
- STRIDE complexity scoring (IBM/NeurIPS 2025): 37% cost savings via task routing

## [1.0.0] - 2026-03-16

### Added
- 9 SA lifecycle skills: requirements, architecture, estimate, project-plan, proposal, data-model, security-review, integration-plan, review
- 2 sub-agents: parallel-wa-reviewer (6 WA pillars), stride-analyzer (6 STRIDE categories)
- 11 JSON schemas (Draft 2020-12) for knowledge base validation
- 8 automated validation scripts (schema, consistency, plugin structure, engagement flow, skill independence, Well-Architected, end-to-end example, URL health)
- Healthcare IBMi migration example (10 KB files + proposal)
- CI/CD via GitHub Actions with all 8 test steps
- Multi-cloud Well-Architected coverage: AWS 6 pillars + GenAI Lens, Azure WAF, GCP Architecture Framework
- Deterministic JSON output contracts for sub-agents
- Human gate thresholds in review skill (< 7.5 requires explicit review)
- URL validation scope configuration (`tests/url_validation_scope.json`)
- CHANGELOG.md (this file)

### Architecture
- Single-agent-with-skills design (Claude Code plugin)
- Blackboard pattern knowledge base with `$depends_on` DAG
- 5 canonical engagement flows: Greenfield, Migration, Streamlined, Assessment, Quick Qualify
- Skills are independently deployable and marketplace-ready
