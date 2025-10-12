# Improve AI Engineering Assistant - System-Wide Optimization

**Purpose:** Comprehensively optimize the entire AI Engineering Assistant multi-agent framework for maximum effectiveness, usability, and maintainability.

**Target System:** {{TARGET_SYSTEM}} = AI Engineering Assistant (this repository)  
**Scope:** All agents, user prompts, knowledge base, documentation, workflows, and templates  

**Role Clarity:** This user prompt specifies WHAT to optimize (target system, components, scope). Your system prompt defines HOW to optimize (methodology, assessment framework, validation protocols). Follow your standard Discover → Assess → Improve → Validate process.

---

## Recursion Prevention

**Max Iterations**: 2-3 per session (system-wide optimization can iterate for refinement)

**Simple Rule**: If you've run full system optimization 3 times in this conversation, stop and start a fresh session.

**Why**: Allows iterative refinement (initial pass + 1-2 improvements) while preventing infinite loops.

---

## Optimization Scope

Systematically analyze and improve ALL components of the AI Engineering Assistant:

### 1. Agent System Prompts (`ai_agents/`)

**System Architecture** (v2.0 - 23 Agents):
- Main Supervisor (1): Multi-agent orchestration
- Top-Level Agents (5): Requirements, Architecture, Deployment, Optimization, Prompt Engineering
- Engineering Supervisor (1): Coordinates 16 engineering specialists
- **Engineering Specialists (16)**: Hyper-specialized by technology
  * Anthropic Claude (5): Code, Workspaces, SDK, MCP Services, Projects
  * AWS Bedrock (2): AgentCore, Strands
  * Other (9): Streamlit UI, LangChain, Data×2, AWS×2, Testing, GitHub, Cursor

**Assessment focus:**
- Anthropic/OpenAI/AWS prompt engineering best practices
- TRM validation framework integration (`ai_agents/shared/validation_framework.md`)
- Clear role definitions, structured instructions, concrete examples
- Chain-of-thought reasoning, tool usage patterns
- Separation of concerns, no capability overlap (each agent ONE technology)
- AWS Well-Architected alignment
- Reference system_config.json → technical_references (150+ URLs)
- Consistent quality benchmarks across all 16 engineering specialists

---

### 2. User Prompts (`user_prompts/`)

**Categories (v2.0 - ~60 prompts)**:
- `requirements/*.user.prompt.md` - Discovery workflows (4 prompts)
- `architecture/*.user.prompt.md` - Architecture tasks (6 prompts)
- `engineering/*.user.prompt.md` - Engineering tasks (22 prompts across 12 specialist categories)
- `deployment/*.user.prompt.md` - Deployment tasks (2 prompts)
- `self_improvement/*.user.prompt.md` - Agent improvement (24 prompts: 17 engineering specialists + 7 others)
- `self_improvement/engineering_specialists/*.user.prompt.md` - Specialist improvements (17 prompts)
- `prompt_engineering/*.user.prompt.md` - Prompt engineering tasks (6 prompts)
- `proposals/*.user.prompt.md` - Proposal assembly (4 prompts)

**Assessment focus:**
- Clarity and conciseness
- Specialist-specific task coverage (each of 16 specialists needs 3-5 essential prompts)
- Consistency across similar prompt types
- Integration with agent system prompts and validation framework
- Token efficiency
- Reference to centralized technical_references in system_config.json

---

### 3. Knowledge Base (`knowledge_base/`)

**Files:**
- `user_requirements.json` - Customer needs, use cases
- `design_decisions.json` - Architecture, estimates, costs
- `system_config.json` - Platform settings, constraints
- `README.md` - Usage documentation

**Assessment focus:**
- Schema completeness and extensibility
- Documentation clarity
- Access patterns across agents
- Version control friendliness

---

### 4. Documentation & Templates (`docs/`, `templates/`, `outputs/`)

**Files to optimize:**
- User guides (getting-started.md, workflow_guide.md, platform_deployment.md, executive_overview.md)
- Technical documentation (agent-architecture-and-collaboration.md, agent-design-patterns.md)
- Templates (requirements-template.md, architecture-template.md, handoff-checklist.md, development-checklist.md)
- Output organization (outputs/README.md)

**Assessment focus:**
- Beginner accessibility (<15 min to productivity)
- Completeness (all workflows documented)
- Accuracy (examples work as documented)
- Platform-specific guidance (Cursor, AWS Bedrock, Claude Projects)
- Terminology clarity and consistency
- Output organization (all deliverables to `outputs/`)

---

### 5. Cross-Cutting Concerns

**End-to-end workflows:**
- Requirements → Architecture → Engineering → Deployment (complete lifecycle)
- Multi-shot Architecture Agent workflow (6 orchestrated user prompts)
- Knowledge base read/write patterns
- Supervisor routing logic
- Prompt Engineering Agent integration with other agents
- Output directory organization (all deliverables to `outputs/`)

**User experience:**
- Clear entry points (which agent/prompt for which task)
- Time to first result (<15 minutes for simple workflows)
- Example consistency (financial operations AI system throughout)
- Error handling and troubleshooting guidance
- Support for all use cases (fork-and-use, deploy to platforms, custom modes)

---

## Assessment Framework

Use your standard optimization dimensions and assessment criteria from your system prompt, with special attention to:

- **Prompt Engineering Excellence**: Anthropic/OpenAI best practices across all agents
- **Multi-Agent Coordination**: Clean separation of concerns, smooth handoffs, supervisor orchestration
- **Knowledge Management**: JSON schema quality, access patterns, documentation
- **User Experience**: Time to first result (<15 min), navigation clarity, platform deployment completeness
- **Documentation Quality**: Onboarding, examples, troubleshooting guidance
- **AWS Well-Architected Alignment**: Architecture Agent enforcement of 6 pillars + GenAI Lens
- **Terminology Clarity**: Consistent use of "optimize" vs "improve" vs "enhance"

*Note: Your system prompt contains the detailed assessment framework. This section highlights areas of particular importance for the AI Engineering Assistant.*

---

## Special Considerations

### Meta-Optimization Awareness
You're optimizing the system you're part of. Handle carefully:

- **Self-improvement:** When optimizing `optimization_agent.system.prompt.md` or `prompt_engineering_agent.system.prompt.md`, apply extra validation
- **Circular dependencies:** Watch for prompt → prompt → prompt references
- **Backward compatibility:** Preserve all existing workflows
- **Validation thoroughness:** Test end-to-end workflows after changes

### Agent-Specific Improvement Prompts
Consider whether to use specialized improvement prompts for each agent (in `user_prompts/self_improvement/`):
- `improve_requirements_agent.user.prompt.md`
- `improve_architecture_agent.user.prompt.md`
- `improve_engineering_agent.user.prompt.md`
- `improve_deployment_agent.user.prompt.md`
- `improve_optimization_agent.user.prompt.md`
- `improve_supervisor_agent.user.prompt.md`

**Decision:** Use if they provide value beyond your standard optimization workflow. Skip if redundant.

---

## Success Criteria

This optimization succeeds when these **system-specific outcomes** are achieved:

✅ **Complete System Coverage**
- All 7 agents optimized (supervisor + 6 specialized agents)
- All 30+ user prompts reviewed and improved
- Knowledge base schemas validated (3 JSON files)
- Documentation updated (guides, templates, README)

✅ **Measurable System Improvements**
- Overall system quality: 10%+ improvement across assessment dimensions
- User time to first result: ≤15 minutes maintained or improved
- Prompt engineering consistency: Common patterns across all agents
- End-to-end workflows: Requirements → Architecture → Engineering → Deployment validated
- Terminology clarity: Consistent "optimize" vs "improve" vs "enhance" usage

✅ **No Regressions**
- All existing capabilities preserved
- Multi-agent coordination functional
- Knowledge base integration working
- All cross-references valid
- Examples remain functional

✅ **Recursion Safety**
- OPTIMIZATION_ITERATION_COUNT = 1 (single execution)
- No infinite loops triggered
- All changes version controlled (git)

---

## Optimization Report Requirements

Generate your standard optimization report (as defined in your system prompt), ensuring it includes these **system-specific elements**:

### System-Specific Validation Tests

Test these critical workflows:
- **Complete Lifecycle**: Requirements Agent → Architecture Agent → Engineering Agent → Deployment Agent
- **Multi-shot Architecture Workflow**: Orchestration of 6 user prompts (tech stack → diagram → team → LOE → cost → plan)
- **Knowledge Base Operations**: Write user_requirements.json → Read → Write design_decisions.json
- **Output Directory Operations**: All agents write deliverables to `outputs/[category]/[project]/`
- **Supervisor Routing**: Correct agent selection based on user request types
- **Cross-references**: All agent ↔ knowledge base ↔ documentation references valid
- **Terminology Consistency**: Verify correct usage of "optimize" vs "improve" vs "enhance" across all files
- **Use Case Support**: Fork-and-use, Claude Projects deployment, AWS Bedrock deployment, custom Cursor modes

### System-Specific Metrics to Track

| Dimension | Before | After | Change |
|-----------|--------|-------|--------|
| Prompt Engineering Quality | X/10 | Y/10 | +N |
| Multi-Agent Coordination | X/10 | Y/10 | +N |
| Knowledge Management | X/10 | Y/10 | +N |
| User Experience | X/10 | Y/10 | +N |
| Documentation Quality | X/10 | Y/10 | +N |
| AWS Well-Architected Enforcement | X/10 | Y/10 | +N |
| Terminology Clarity | X/10 | Y/10 | +N |

### Files Modified by Category
- Agent prompts (ai_agents/*.system.prompt.md): [COUNT]
- User prompts (user_prompts/*/*.user.prompt.md): [COUNT]
- Knowledge base (knowledge_base/*.json): [COUNT]
- Documentation (docs/*, templates/*, outputs/README.md): [COUNT]
- Root files (README.md, ARCHITECTURE.md): [COUNT]

### Recursion Status
- ✅ OPTIMIZATION_ITERATION_COUNT: 1/1 (complete)
- ✅ No infinite loops detected
- ✅ Next cycle: Requires new session

---

## Usage Instructions

**Execution Triggers:**
- Quarterly system reviews
- After significant AI research updates (new Anthropic/OpenAI guidance)
- Following 5+ user projects (incorporate learnings)
- When user feedback indicates systemic issues
- After major feature additions or structural changes

**Execution Steps:**
1. Start **fresh session** (ensures OPTIMIZATION_ITERATION_COUNT = 0)
2. Load Optimization Agent with `optimization_agent.system.prompt.md`
3. Reference this prompt: `@improve_ai_engineering_assistant.user.prompt.md`
4. Monitor execution and review optimization report
5. Next cycle: 3-6 months or as triggered by conditions above

---

## Notes

**Meta-Optimization Context:** You're optimizing the system you're part of—handle with extra validation rigor.

**Recursion Safety (Critical):** The iteration tracking mechanism (OPTIMIZATION_ITERATION_COUNT = 1) is non-negotiable. This prevents infinite loops during meta-optimization.

**Validation Emphasis:** Test all critical workflows end-to-end before completion, including supervisor routing and multi-agent coordination.

**Terminology Note:** This repository uses precise terminology (see README.md glossary):
- **Optimize**: System-level improvements (Optimization Agent's role)
- **Improve**: Agent-level enhancements (this prompt's purpose) and prompt-level refinements
- **Enhance**: User experience and documentation improvements

---

**Version:** 2.0  
**Last Updated:** 2025-01-12  
**Maintained By:** AI Engineering Assistant Core Team  
**Optimization Cycle:** Quarterly or as-needed  
**Safety Mechanism:** Iteration tracking prevents infinite loops (MAX_ITERATIONS = 1)  
**System Version**: v2.0.0 (23 agents, 16 engineering specialists, TRM validation framework)
