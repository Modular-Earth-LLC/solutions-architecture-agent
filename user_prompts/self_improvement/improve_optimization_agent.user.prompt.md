# Improve Optimization Agent

**Target**: `ai_agents/optimization_agent.system.prompt.md`  
**Specialty**: System-wide AI optimization, lifecycle-aware improvements, Well-Architected enforcement

**Framework**: See `knowledge_base/system_config.json` → `self_improvement_framework` for shared methodology, principles, validation requirements, and quality benchmarks.

---

## Agent-Specific Focus Areas

**What makes the Optimization Agent uniquely effective:**

### 1. Implementation Effectiveness & Execution Quality

**Beyond analysis/recommendation - actually implements changes safely:**

- Executes refactorings using proven patterns (Martin Fowler)
- Safe change execution (incremental, tested, reversible)
- Production-ready, maintainable output
- Preserves all existing capabilities
- File categorization: Accurately identifies agent prompts, user prompts, code, configs, docs
- Dependency mapping: Thorough analysis, no circular references missed
- System boundaries: Clearly identified

**Target**: 100% of approved optimizations implemented safely with zero breaking changes

### 2. AWS Well-Architected Principles Enforcement

**Mandatory compliance with all 6 pillars + GenAI Lens:**

*Reference*: `knowledge_base/system_config.json` → `aws_well_architected_framework`

- Evaluates all 6 pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability
- Applies GenAI Lens: Model Selection, Prompt Engineering, RAG Optimization, Multi-Agent Coordination, Responsible AI, Knowledge Base Design
- Documents trade-offs between pillars explicitly
- Objective, measurable scoring methodology
- Evidence-based rationale for all scores

**Target**: Every optimization explicitly improves or maintains Well-Architected compliance

### 3. Lifecycle-Aware Optimization

**Stage-appropriate improvements:**

*Reference*: `optimization_agent.system.prompt.md` → Execution Instructions → Lifecycle-Aware Optimization

- Detects development stage: Requirements → Architecture → Development → Deployment → Operations → Maintenance
- Applies stage-specific optimization strategies
- Quality assurance appropriate to system maturity
- Reproducibility validation (workflows, configurations, environments)
- Monitoring patterns for production systems

**Target**: Stage-aware optimizations that improve quality assurance appropriate to system maturity

### 4. Measurable Impact & Quantified Value

**Every improvement proven with metrics:**

- Performance metrics: Response time, throughput, latency, token usage
- Cost metrics: API costs, infrastructure costs, model inference, TCO
- Quality metrics: Accuracy, error rates, user satisfaction
- Business metrics: Time to value, productivity gains, customer satisfaction, ROI
- Operational metrics: Deployment frequency, MTTR, change failure rate

**Target**: Every optimization includes quantified before/after metrics and validated business impact

### 5. Safe Refactoring & Change Management

**Zero unintentional breaking changes:**

*Reference*: `optimization_agent.system.prompt.md` → Phase 3: Implement → Refactoring Safety Principles

- Martin Fowler refactoring catalog applied systematically
- Change impact analysis: Dependency analysis, blast radius assessment, risk scoring
- Rollback procedures: Version control, feature flags, blue-green deployments
- Testing strategy: Pre-refactoring tests, refactoring validation, regression testing
- Incremental changes with validation at each step

**Target**: 100% successful rollback capability when needed, zero breaking changes

### 6. Discovery Comprehensiveness

**Finds ALL components in ANY system:**

- System analysis frameworks and methodologies
- Dependency analysis (call graphs, import analysis, pattern recognition)
- Edge case handling (unusual file structures, non-standard organizations)
- Development stage detection (Requirements → Maintenance)
- Well-Architected gap identification

**Target**: 100% component discovery across diverse system types with accurate stage identification

### 7. Validation Thoroughness & Quality Assurance

**No regressions reach production:**

*Reference*: `optimization_agent.system.prompt.md` → Phase 4: Validate & Report

- Testing strategy completeness (unit, integration, E2E, performance, security)
- Edge case identification methodology
- Well-Architected compliance testing
- Validation metrics (before/after comparisons)

**Target**: All critical workflows validated, no regressions, measurable Well-Architected improvements

---

## Integration Requirements

- References `ai_agents/shared/validation_framework.md` for quality standards
- Uses TRM patterns for recursive validation and multi-candidate generation
- Coordinates with all other agents when optimizing this framework
- References `knowledge_base/system_config.json` → `technical_references` for authoritative documentation URLs
- References `knowledge_base/system_config.json` → `aws_well_architected_framework` for pillar definitions (NEVER duplicates inline)

---

## Success Criteria

Beyond standard criteria (see system_config.json → self_improvement_framework), ensure:

✅ **Implementation**: Actually implements changes (not just recommends)  
✅ **Well-Architected**: All 6 pillars evaluated and improved  
✅ **Lifecycle-Aware**: Stage-appropriate optimizations  
✅ **Measurable**: Quantified improvements with before/after metrics  
✅ **Safe**: Zero breaking changes, 100% rollback capability  
✅ **Discovery**: 100% component discovery, accurate stage identification  
✅ **Validation**: All regressions caught, compliance improvements verified  
✅ **Backward Compatible**: All existing workflows preserved

---

## Framework Context (v2.0)

**23-Agent Architecture:**
- Main Supervisor (1)
- Top-Level Agents (5): Requirements, Architecture, Deployment, Optimization, Prompt Engineering
- Engineering Supervisor (1): Coordinates 16 specialists
- Engineering Specialists (16): Hyper-specialized by technology

**Engineering Specialists the Optimization Agent Must Understand:**
1. Streamlit UI Development
2. Claude Code (autonomous generation, subagents)
3. Claude Workspaces (multi-agent orchestration)
4. Anthropic Python Agents SDK (formal SDK)
5. MCP Services (Model Context Protocol)
6. LangChain Orchestration (LCEL, RAG)
7. Knowledge Engineering (vector DBs)
8. Data Engineering (SQLite, pandas)
9. AWS Bedrock AgentCore (Gateway/Identity/Runtime/Memory)
10. AWS Bedrock Strands (SDK, observability)
11. AWS Infrastructure (ECS, CDK, CloudWatch)
12. AWS Security & Networking (IAM, VPC, Cognito)
13. Claude Projects Deployment
14. Testing & QA (pytest)
15. GitHub & GitHub Copilot
16. Cursor IDE

**Tech Stack Focus**: Python, Streamlit, Anthropic Claude, AWS Bedrock, MCP, LangChain

**New Capabilities**:
- TRM Validation framework
- Shared quality standards across 16 specialists
- 3 streamlined optimization scenarios
- Consistent benchmarks

---

**Version**: 0.1 | **Updated**: 2025-01-12 | **Agent-Agnostic**: Works with Optimization or Prompt Engineering agents
