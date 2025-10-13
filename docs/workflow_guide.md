# Workflow Guide

Complete development lifecycle: Requirements → Architecture → Engineering → Deployment

<!-- Version in .repo-metadata.json -->

---

## Quick Reference

**Build AI system**:
1. Requirements Agent → Discover needs (15-30 min)
2. Architecture Agent → Design system (30-60 min)
3. Engineering Supervisor → Build prototype (1-3 hours)
4. Deployment Agent → Deploy guide (15-30 min)

**Optimize existing system**:
1. Optimization Agent → Analyze & improve (1-3 hours)

**Create prompts**:
1. Prompt Engineering Agent → Build/optimize (30-60 min)

---

## Full Workflow

### 1. Requirements Discovery

**Start**: "Help me discover requirements for [project]"

**Questions asked** (15-30 min):
- Business problem?
- Users and use cases?
- Success criteria?
- Constraints (budget, timeline, technical)?

**Output**: `knowledge_base/user_requirements.json`

**Next**: Architecture design

### 2. Architecture Design

**Start**: "Design architecture for my requirements"

**Agents generate** (30-60 min):
- Tech stack selection
- Architecture diagrams
- Cost estimation
- Team composition
- Project plan

**Output**: `knowledge_base/design_decisions.json`

**Next**: Engineering/prototype

### 3. Engineering

**Start**: "Build prototype for my system"

**Engineering Supervisor routes to specialists**:
- Streamlit UI Agent → Interface code
- Claude Code Agent → Claude integration
- Data Engineering Agent → Database
- Testing Agent → Test suite

**Output**: Working code in `outputs/prototypes/[project]/`

**Next**: Deployment

### 4. Deployment

**Start**: "Create deployment guide for [platform]"

**Agent generates**:
- Platform-specific instructions
- Infrastructure code (CDK, docker-compose, etc.)
- CI/CD workflows
- Monitoring setup

**Output**: Deployment guide + configs

**YOU execute deployment** (agents don't deploy automatically)

---

## Optimization Workflow

**For existing systems**:

1. "Optimize my AI system at [path]"
2. Agent discovers system structure
3. Agent assesses against best practices
4. Agent proposes improvements
5. YOU approve which to implement
6. Agent implements (if approved)
7. Agent validates changes

**Time**: 1-3 hours depending on system size

---

## Key Principles

**YOU always**:
- Answer questions (requirements)
- Approve designs (architecture)
- Review code (engineering)
- Execute deployment
- Make all critical decisions

**Agents generate, YOU approve.**

---

