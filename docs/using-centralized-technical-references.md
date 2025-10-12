# Using Centralized Technical References

**Purpose**: Guide for agents to reference centralized documentation in `system_config.json`  
**Benefit**: Single source of truth for all technical URLs, easy to update system-wide  
**Version**: 1.0  
**Date**: 2025-01-12

---

## Overview

All technical documentation URLs, research papers, and design patterns are centralized in:

**`knowledge_base/system_config.json` → `technical_references`**

Agents should **reference this section** instead of hardcoding URLs inline.

---

## Why Centralized References?

### Problems with Inline URLs

❌ **Redundancy**: Same URL repeated across 10+ agents  
❌ **Maintenance**: Updating URLs requires changing multiple files  
❌ **Inconsistency**: URLs might differ slightly across agents  
❌ **Broken Links**: Hard to find and fix broken links system-wide

### Benefits of Centralized References

✅ **Single Source of Truth**: One place to update all references  
✅ **Easy Maintenance**: Update once, applies to all agents  
✅ **Consistency**: All agents reference same URLs  
✅ **Version Controlled**: Changes tracked in git  
✅ **Reduced Redundancy**: Agents stay focused, less bloat

---

## How to Reference

### Pattern for Agents

**Instead of hardcoding URLs**:
```markdown
## Process Alignment

**Authoritative References:**
- [Anthropic Claude API](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
- [AWS Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Strands SDK](https://strandsagents.com/latest/)
```

**Use centralized reference**:
```markdown
## Process Alignment

**Authoritative References**: See `knowledge_base/system_config.json` → `technical_references` for all documentation links:
- Anthropic Claude: `anthropic_claude.*` (11 references)
- AWS Bedrock AgentCore: `aws_bedrock_agentcore.*` (6 references)
- AWS Bedrock Strands: `aws_bedrock_strands.*` (4 references)
- Research Papers: `research_papers.*` (TRM, MetaGPT, etc.)
- Design Patterns: `design_patterns.*` (Supervisor-worker, TRM, etc.)

Consult system_config.json for latest URLs and research updates.
```

### Referencing Specific Sections

**Anthropic Claude Documentation**:
```markdown
*See: `system_config.json` → `technical_references` → `anthropic_claude`*

Key references:
- Official docs: `anthropic_claude.official_docs`
- Python SDK: `anthropic_claude.python_sdk`
- Multi-agent patterns: `anthropic_claude.multi_agent_research`
```

**AWS Bedrock AgentCore**:
```markdown
*See: `system_config.json` → `technical_references` → `aws_bedrock_agentcore`*

All 4 components documented:
- Gateway: `aws_bedrock_agentcore.gateway`
- Identity: `aws_bedrock_agentcore.identity`
- Runtime: `aws_bedrock_agentcore.runtime`
- Memory: Documented in AgentCore overview
```

**Research Papers & Patterns**:
```markdown
*See: `system_config.json` → `technical_references` → `research_papers` and `design_patterns`*

Key patterns:
- TRM validation: `research_papers.test_time_recursive_majority`
- Supervisor-worker: `design_patterns.supervisor_worker`
```

---

## Available References

### Complete List

**Anthropic Claude** (11):
- official_docs, api_reference, python_sdk, streaming, tool_use
- prompt_engineering, building_effective_agents, multi_agent_research
- claude_code_best_practices, agents_sdk, claude_projects

**Model Context Protocol** (3):
- specification, python_sdk, building_mcp_servers

**AWS Bedrock** (7):
- agents, knowledge_bases, guardrails, model_evaluation
- agents_best_practices_part1, agents_best_practices_part2, multi_agent_collaboration

**AWS Bedrock AgentCore** (6):
- overview, gateway, identity, runtime, code_interpreter, github_samples

**AWS Bedrock Strands** (4):
- announcement, documentation, github, technical_deep_dive

**AWS General** (11):
- well_architected_framework, genai_lens, security_pillar, reliability_pillar
- cdk_python, ecs, lambda, iam_best_practices, vpc, cognito, secrets_manager

**LangChain** (5):
- documentation, lcel, agents, anthropic_integration, vector_stores

**Streamlit** (3):
- documentation, chat_elements, session_state

**GitHub** (5):
- actions, copilot, copilot_workspace, advanced_security, api

**Cursor IDE** (4):
- documentation, rules_guide, custom_modes, composer

**Data Tools** (5):
- chromadb, faiss, pandas, numpy, sqlite

**Testing** (2):
- pytest, python_testing_best_practices

**Research Papers** (3):
- metagpt, test_time_recursive_majority, small_language_models

**Design Patterns** (4):
- supervisor_worker, sequential_chain, parallel_execution, test_time_recursive_majority

**Validation Framework**:
- shared_framework location, quality_benchmarks, trm_pattern

---

## Agent Update Process

### For New Agents

When creating new agents, use:
```markdown
## Process Alignment

*📚 TECHNICAL REFERENCES: `knowledge_base/system_config.json` → `technical_references`*

This agent implements [phase] of AWS Generative AI Lifecycle.

**Key Documentation** (see system_config.json for URLs):
- [Technology 1]: `technical_references.[category].[key]`
- [Technology 2]: `technical_references.[category].[key]`

Consult system_config.json for latest documentation and research.
```

### For Existing Agents

**Phase 1** (Optional - Future Enhancement):
- Update agent "Authoritative References" sections
- Replace inline URLs with references to system_config.json
- Reduces each agent by 20-50 lines
- Improves maintainability

**Estimated Time**: 15-30 min per agent × 23 agents = 6-12 hours

---

## Benefits Realized

### Current State

**With Centralized References**:
- ✅ 150+ technical URLs in one place
- ✅ Easy to update system-wide
- ✅ Version controlled
- ✅ Consistent across all agents
- ✅ Research papers included
- ✅ Design patterns documented

### Maintenance

**To Update a URL**:
1. Edit `knowledge_base/system_config.json`
2. Update single URL in technical_references
3. All agents automatically reference updated URL
4. Commit change
5. Done!

**Before**: Update 10+ agent files individually  
**After**: Update 1 config file

---

## Usage Examples

### Claude Code Agent

**References**:
```markdown
*See: `system_config.json` → `technical_references` → `anthropic_claude`*

Key capabilities based on:
- Claude Code best practices: `anthropic_claude.claude_code_best_practices`
- Building effective agents: `anthropic_claude.building_effective_agents`
- Multi-agent research: `anthropic_claude.multi_agent_research`
```

### AWS Bedrock AgentCore Agent

**References**:
```markdown
*See: `system_config.json` → `technical_references` → `aws_bedrock_agentcore`*

AgentCore components:
- Gateway (API→MCP): `aws_bedrock_agentcore.gateway`
- Identity (auth): `aws_bedrock_agentcore.identity`
- Runtime (serverless): `aws_bedrock_agentcore.runtime`
- Code Interpreter: `aws_bedrock_agentcore.code_interpreter`
- Samples: `aws_bedrock_agentcore.github_samples`
```

### Validation Framework Reference

**All Engineering Agents**:
```markdown
*See: `system_config.json` → `technical_references` → `validation_framework`*

Quality standards:
- Shared framework: `validation_framework.shared_framework`
- Benchmarks: `validation_framework.quality_benchmarks`
- TRM pattern: `validation_framework.trm_pattern`
- Research: `research_papers.test_time_recursive_majority`
```

---

## Future Enhancement

**Optional Task**: Update all 23 agents to use centralized references

**Estimated Effort**: 6-12 hours (15-30 min per agent)

**Benefits**:
- Reduces each agent by 20-50 lines
- Eliminates URL redundancy
- Improves maintainability
- Makes updates trivial

**Current State**: Framework in place, agents can reference it manually

---

**Version**: 1.0  
**Status**: Centralized references available  
**Next**: Optional - update agents to reference (not required for functionality)  
**Impact**: Easier maintenance, consistent documentation, single source of truth
