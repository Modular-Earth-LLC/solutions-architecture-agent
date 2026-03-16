# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
