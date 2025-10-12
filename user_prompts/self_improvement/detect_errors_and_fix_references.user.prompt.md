---
title: Detect Errors and Fix References
description: Systematically validates and fixes all references, consistency issues, and collaboration artifacts in the multi-agent AI development framework through comprehensive error detection and automated remediation
usage: Execute via Optimization Agent to validate repository integrity after iterative human-AI collaboration
execution_context: This is a task instruction for the Optimization Agent running IN Cursor, validating the entire repository system
---

## Usage Instructions

**How to use this user prompt**:
1. Open Cursor AI Pane with Optimization Agent mode active
2. Attach or reference this file in your chat
3. Say: "Execute the error detection and reference validation workflow"
4. The agent will systematically validate the entire repository

**What this does**: Instructs the Optimization Agent to perform comprehensive validation of all repository components, fixing errors and inconsistencies from iterative collaboration

**What you get**: A validated, consistent repository with all references fixed and documented changes

**When to run**: 
- After major refactoring or restructuring
- Before committing significant changes
- Periodically (weekly/monthly) for maintenance
- When you suspect reference issues or inconsistencies

---

## Role and Mission

You are a **Repository Integrity Validator** specializing in detecting and fixing errors that accumulate during fast-paced human-AI collaboration on software projects.

**Mission**: Systematically discover, validate, and fix all reference errors, consistency issues, hallucinations, and collaboration artifacts across the entire multi-agent AI development framework while preserving all functionality and improving system reliability.

## Variables

- **{{VALIDATION_SCOPE}}**: Scope of validation - "full", "documentation", "code", "knowledge-base", or "critical-path" (default: "full")
- **{{FIX_MODE}}**: Execution mode - "analyze-only", "fix-minor", or "fix-all-with-approval" (default: "fix-minor")
- **{{SEVERITY_THRESHOLD}}**: Minimum severity to report - "critical", "high", "medium", "low" (default: "medium")
- **{{VALIDATION_TOOLS}}**: Leverage existing validation tools - true/false (default: true)

## Success Criteria

✓ All file paths and cross-references validated and functional  
✓ All line number references point to correct locations  
✓ All knowledge base field references exist and are accurate  
✓ No contradictory instructions across agents  
✓ Consistent terminology throughout repository  
✓ All external links verified as accessible  
✓ Documentation reflects current code structure  
✓ No orphaned files or dead code  
✓ All {{variable}} definitions consistent  
✓ Git history reflects accurate commit messages  
✓ Existing validation tools pass 100%  
✓ Measurable improvement in repository health score

## Context

### Common Issues from Human-AI Collaboration

**Reference Degradation**:
- Stale file paths after refactoring
- Line numbers outdated after edits
- Cross-references broken after file moves
- Knowledge base fields renamed without updating references

**Consistency Drift**:
- Terminology inconsistencies between agents
- Conflicting instructions in different prompts
- Variable definitions that diverge over time
- Documentation that doesn't match implementation

**Collaboration Artifacts**:
- Temporary files not cleaned up
- Commented-out sections never removed
- Duplicate implementations from parallel work
- Merged conflicts resolved inconsistently

**Hallucinations and Assumptions**:
- AI agents citing non-existent files
- References to features not yet implemented
- Assumptions about system behavior not validated
- Documentation describing ideal state vs. actual state

### Existing Validation Infrastructure

This repository includes validation tools that MUST be leveraged:

- **`tests/validate_consistency.py`**: Python validation script
- **`tests/validate_knowledge_base.py`**: JSON schema validation
- **`tests/workflow_validation_checklist.md`**: Manual validation checklist
- **`ai_agents/shared/validation_framework.md`**: Quality standards framework
- **Knowledge base schemas**: Define expected structure for JSON files

## Tasks and Process

You WILL follow this comprehensive methodology for repository validation:

### Phase 1: Discovery & Baseline Assessment (15-30 min)

**Objective**: Establish current repository state and run existing validation tools.

**1.1 Execute Existing Validation Tools**:

```bash
# Run all existing validation scripts
python tests/validate_consistency.py
python tests/validate_knowledge_base.py

# Document results
- Validation errors found: [COUNT]
- Warnings found: [COUNT]
- Critical issues: [LIST]
```

**1.2 Comprehensive Repository Scan**:

<thinking>
Mapping repository structure...

1. Inventory all files by type:
   - Agent prompts (.system.prompt.md): [COUNT]
   - User prompts (.user.prompt.md): [COUNT]
   - Documentation (.md): [COUNT]
   - Knowledge base (.json): [COUNT]
   - Code files (.py, .js, .ts): [COUNT]
   - Configuration files: [COUNT]
   - Templates: [COUNT]
   - Tests: [COUNT]

2. Extract all references:
   - File paths: [LIST with source location]
   - Line numbers: [LIST with context]
   - Knowledge base fields: [LIST]
   - External URLs: [LIST]
   - {{Variable}} definitions: [LIST]
   - Agent cross-references: [LIST]

3. Identify potential issues:
   - Files referenced but not found: [COUNT]
   - Suspicious line number references: [COUNT]
   - Dead links: [COUNT]
   - Inconsistent terminology: [EXAMPLES]
</thinking>

**1.3 Git History Analysis**:

```bash
# Recent changes that may have broken references
git log --oneline --since="30 days ago" --name-status

# Identify:
- Renamed files: [LIST]
- Deleted files: [LIST]
- Moved files: [LIST]
- Large refactorings: [COMMITS]
```

**1.4 Calculate Repository Health Score**:

| Metric | Score (0-100) | Status |
|--------|---------------|--------|
| Reference Integrity | [X] | 🔴/🟡/🟢 |
| Documentation Currency | [X] | 🔴/🟡/🟢 |
| Consistency Score | [X] | 🔴/🟡/🟢 |
| Validation Tool Pass Rate | [X] | 🔴/🟡/🟢 |
| Code Quality | [X] | 🔴/🟡/🟢 |
| **Overall Health** | **[X]** | **🔴/🟡/🟢** |

**Scoring**:
- 90-100: 🟢 Excellent
- 70-89: 🟡 Good (needs minor fixes)
- 50-69: 🟠 Fair (needs attention)
- 0-49: 🔴 Poor (requires immediate action)

---

### Phase 2: Reference Validation & Error Detection (30-45 min)

**Objective**: Systematically validate all references and detect errors.

**2.1 File Path Validation**:

For every file reference in the repository:

```python
# Pseudo-code validation logic
for reference in all_file_references:
    source_file = reference.source
    target_file = reference.target
    
    if not file_exists(target_file):
        issues.append({
            "severity": "HIGH",
            "type": "broken_file_reference",
            "source": source_file,
            "line": reference.line_number,
            "target": target_file,
            "suggestion": find_similar_files(target_file)
        })
```

**Issues to Detect**:
- ❌ File referenced but doesn't exist
- ❌ File path uses wrong separator (\ vs /)
- ❌ Relative path broken after file move
- ❌ Case sensitivity issues (File.md vs file.md)

**2.2 Line Number Reference Validation**:

```text
Pattern: "See lines 123-145 in file.md"
Pattern: "```123:145:path/to/file.md"

Validation:
1. File exists ✓/✗
2. Line range exists ✓/✗
3. Content at lines matches description ✓/✗
4. Lines haven't shifted significantly ✓/✗
```

**2.3 Knowledge Base Field Validation**:

```python
# Load schemas
system_config_schema = load_schema("knowledge_base/schemas/system_config.schema.json")
user_requirements_schema = load_schema("knowledge_base/schemas/user_requirements.schema.json")
design_decisions_schema = load_schema("knowledge_base/schemas/design_decisions.schema.json")

# Find all references like: "knowledge_base/system_config.json → field_name"
for reference in kb_field_references:
    kb_file = load_json(reference.kb_file)
    field_path = reference.field_path
    
    if not field_exists(kb_file, field_path):
        issues.append({
            "severity": "HIGH",
            "type": "invalid_kb_field",
            "source": reference.source,
            "field": field_path,
            "available_fields": list_similar_fields(kb_file, field_path)
        })
```

**2.4 Cross-Reference Integrity**:

Validate references between agents:

```text
Example: "Architecture Agent references Engineering Agent via: ai_agents/engineering_agent.system.prompt.md"

Check:
- ✓ Target agent file exists
- ✓ Referenced sections exist
- ✓ No circular dependencies
- ✓ Handoff protocols match
```

**2.5 External Link Validation**:

```python
# Extract all URLs
urls = extract_urls(all_markdown_files)

for url in urls:
    status = check_url(url, timeout=5)
    if status != 200:
        issues.append({
            "severity": "MEDIUM",
            "type": "broken_external_link",
            "url": url,
            "status_code": status,
            "locations": find_url_locations(url)
        })
```

**2.6 Variable Consistency Validation**:

```python
# Find all {{VARIABLE}} definitions
variable_definitions = extract_variables(all_prompts)

# Check for conflicts
for var_name, definitions in variable_definitions.items():
    if len(definitions) > 1:
        # Multiple definitions - check consistency
        if not all_definitions_consistent(definitions):
            issues.append({
                "severity": "HIGH",
                "type": "conflicting_variable_definitions",
                "variable": var_name,
                "definitions": definitions,
                "recommendation": "Consolidate into single source of truth"
            })
```

**2.7 Terminology Consistency Check**:

```python
# Define canonical terms
canonical_terms = {
    "AI agent": ["AI agent", "agent", "AI system"],  # Accept these
    "knowledge base": ["knowledge base", "KB"],
    "user prompt": ["user prompt", "task prompt"],
    # ...
}

# Scan for inconsistent usage
inconsistencies = find_terminology_inconsistencies(
    all_text_files,
    canonical_terms
)
```

**2.8 Documentation-Code Alignment**:

```python
# Example: Check if documented features exist in code
documented_features = extract_features_from_docs("README.md", "docs/")
implemented_features = extract_features_from_code("ai_agents/", "*.py")

missing_in_code = documented_features - implemented_features
missing_in_docs = implemented_features - documented_features

if missing_in_code:
    issues.append({
        "severity": "HIGH",
        "type": "documented_but_not_implemented",
        "features": list(missing_in_code)
    })
```

---

### Phase 3: Issue Classification & Prioritization (15 min)

**Objective**: Categorize and prioritize detected issues for remediation.

**3.1 Severity Classification**:

| Severity | Criteria | Examples | Auto-Fix |
|----------|----------|----------|----------|
| 🔴 **CRITICAL** | Breaks functionality | Missing agent files, circular dependencies, validation tool failures | ❌ Needs approval |
| 🟠 **HIGH** | Causes confusion/errors | Broken file references, invalid KB fields, conflicting instructions | ✓ Auto-fix if {{FIX_MODE}} allows |
| 🟡 **MEDIUM** | Reduces quality | Stale line numbers, broken external links, minor inconsistencies | ✓ Auto-fix |
| 🟢 **LOW** | Cosmetic/minor | Terminology variations, formatting inconsistencies, stylistic issues | ✓ Auto-fix |

**3.2 Issue Grouping**:

```text
GROUP 1: REFERENCE INTEGRITY (Priority 1)
├── Broken file paths: [COUNT]
├── Invalid line numbers: [COUNT]
├── Missing KB fields: [COUNT]
└── Dead external links: [COUNT]

GROUP 2: CONSISTENCY ISSUES (Priority 2)
├── Variable conflicts: [COUNT]
├── Terminology inconsistencies: [COUNT]
├── Conflicting instructions: [COUNT]
└── Documentation-code misalignment: [COUNT]

GROUP 3: COLLABORATION ARTIFACTS (Priority 3)
├── Orphaned files: [COUNT]
├── Temporary files: [COUNT]
├── Commented-out sections: [COUNT]
└── Duplicate implementations: [COUNT]

GROUP 4: CODE QUALITY (Priority 4)
├── Linting errors: [COUNT]
├── Missing docstrings: [COUNT]
├── Dead code: [COUNT]
└── Style violations: [COUNT]
```

**3.3 Impact Analysis**:

For each issue:
```text
Issue: [Description]
├── Severity: [CRITICAL/HIGH/MEDIUM/LOW]
├── Impact: [What breaks or degrades]
├── Affected Files: [COUNT]
├── Blast Radius: [How many systems affected]
├── Fix Complexity: [SIMPLE/MODERATE/COMPLEX]
└── Recommended Action: [Specific fix]
```

---

### Phase 4: Automated Remediation (30-60 min)

**Objective**: Fix issues according to {{FIX_MODE}} and severity.

**4.1 Auto-Fix Decision Matrix**:

```python
def should_auto_fix(issue, fix_mode):
    if fix_mode == "analyze-only":
        return False
    
    if fix_mode == "fix-minor":
        return issue.severity in ["LOW", "MEDIUM"]
    
    if fix_mode == "fix-all-with-approval":
        if issue.severity in ["CRITICAL", "HIGH"]:
            # Present plan, wait for approval
            present_fix_plan(issue)
            return await_user_approval()
        else:
            return True
    
    return False
```

**4.2 Reference Fixing Strategies**:

**A. File Path Fixes**:
```python
# Strategy 1: Direct match (file renamed)
old_path = "ai_agents/old_name.md"
new_path = find_exact_match(old_path, all_files)

# Strategy 2: Fuzzy match (file moved)
if not new_path:
    new_path = find_best_match(old_path, all_files, threshold=0.8)

# Strategy 3: Interactive (ambiguous)
if not new_path:
    candidates = find_similar_files(old_path, all_files, top_n=3)
    new_path = prompt_user_selection(candidates)

# Apply fix
for source_file in files_referencing(old_path):
    update_reference(source_file, old_path, new_path)
```

**B. Line Number Updates**:
```python
# Detect content shift
reference = "See lines 100-120 in file.md for details"
target_file = "file.md"
expected_content_snippet = extract_context(reference)

# Find where content actually is now
actual_lines = find_content_location(target_file, expected_content_snippet)

if actual_lines and actual_lines != (100, 120):
    # Update reference
    update_line_reference(
        source=reference.source_file,
        old_range=(100, 120),
        new_range=actual_lines
    )
```

**C. Knowledge Base Field Fixes**:
```python
# Invalid field reference
reference = "system_config.json → deployment.aws_region"
actual_field = "deployment_config.aws.region"

# Fix with JSONPath
update_kb_reference(
    source=reference.source_file,
    old_path="deployment.aws_region",
    new_path="deployment_config.aws.region"
)
```

**D. Terminology Standardization**:
```python
# Standardize terminology
inconsistent_terms = {
    "AI system": "AI agent",  # Use "AI agent" everywhere
    "task prompt": "user prompt",
    "prompt engineering": "prompt engineering",  # Keep
}

for file in all_markdown_files:
    apply_terminology_fixes(file, inconsistent_terms)
```

**4.3 Fix Implementation Protocol**:

For each fix:

1. **Create Backup**: Store original state for rollback
2. **Apply Fix**: Use search_replace with high precision
3. **Validate Fix**: Re-check reference works
4. **Document Change**: Add to fix log
5. **Test Impact**: Run validation tools
6. **Commit**: Git commit with descriptive message

```bash
# Example commit message
"fix(references): Update file paths after agent reorganization

- Updated 23 references from old_agent.md → new_agent.md
- Fixed 12 line number references after content edits
- Standardized terminology: 'AI system' → 'AI agent'

Validation: All tests passing
Issue: Detected by automated validation workflow"
```

---

### Phase 5: Consistency Enforcement (20-30 min)

**Objective**: Ensure repository-wide consistency in structure, style, and terminology.

**5.1 Structural Consistency**:

**Agent Prompt Structure**:
```markdown
Required sections (in order):
1. Title and metadata
2. Role and Mission
3. Core Principles
4. Capabilities
5. Workflow/Process
6. Success Criteria
7. Guardrails
8. Version information

Check: All agent prompts follow this structure
```

**User Prompt Structure**:
```markdown
Required sections (in order):
1. Title and metadata (YAML frontmatter)
2. Usage Instructions
3. Role and Mission
4. Variables
5. Success Criteria
6. Context
7. Tasks and Process
8. Constraints and Guidelines
9. Response Format
10. Version information

Check: All user prompts follow this structure
```

**5.2 Naming Convention Validation**:

```python
naming_rules = {
    "agent_prompts": r"^[a-z_]+_agent\.system\.prompt\.md$",
    "user_prompts": r"^[a-z_]+\.user\.prompt\.md$",
    "knowledge_base": r"^[a-z_]+\.(json|schema\.json)$",
    "documentation": r"^[a-z\-]+\.md$",
}

violations = check_naming_conventions(all_files, naming_rules)
```

**5.3 Cross-Agent Consistency**:

```python
# All agents should reference shared validation framework
shared_framework = "ai_agents/shared/validation_framework.md"

for agent_file in agent_prompts:
    if not references_framework(agent_file, shared_framework):
        issues.append({
            "severity": "MEDIUM",
            "type": "missing_framework_reference",
            "agent": agent_file,
            "recommendation": f"Add reference to {shared_framework}"
        })
```

**5.4 Version Consistency**:

```python
# Check version information consistency
version_info = extract_versions(all_prompts)

inconsistent_versions = find_version_inconsistencies(version_info)
outdated_versions = find_outdated_versions(version_info)
```

---

### Phase 6: Validation & Quality Assurance (15-20 min)

**Objective**: Confirm all fixes work and repository is healthy.

**6.1 Re-Run Validation Tools**:

```bash
# After fixes, re-run all validation
python tests/validate_consistency.py
python tests/validate_knowledge_base.py

# Compare results
Before: [X errors, Y warnings]
After:  [X errors, Y warnings]
Improvement: [X% reduction in issues]
```

**6.2 Comprehensive Validation Checklist**:

**Reference Integrity**:
- [ ] All file paths resolve correctly
- [ ] All line number references point to correct content
- [ ] All knowledge base field references are valid
- [ ] All cross-references between agents work
- [ ] All external links are accessible (or marked as broken with intent)
- [ ] All {{variable}} definitions are consistent

**Consistency Validation**:
- [ ] Terminology is standardized throughout
- [ ] Agent prompt structures are uniform
- [ ] User prompt structures are uniform
- [ ] Naming conventions followed
- [ ] Version information consistent
- [ ] No conflicting instructions

**Completeness Validation**:
- [ ] No orphaned files (all files referenced or documented as intentionally standalone)
- [ ] No dead code (or marked as TODO/future feature)
- [ ] All documented features exist in code
- [ ] All code features documented
- [ ] README accurate and current
- [ ] CONTRIBUTING.md reflects actual workflow

**Code Quality Validation** (if applicable):
- [ ] All Python files pass linting (flake8, black, mypy)
- [ ] All JavaScript/TypeScript files pass linting (eslint, prettier)
- [ ] No security vulnerabilities (run security scanners)
- [ ] Dependencies up to date
- [ ] Tests pass (if test suite exists)

**6.3 Repository Health Score Recalculation**:

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Reference Integrity | [X] | [Y] | +[Z]% |
| Documentation Currency | [X] | [Y] | +[Z]% |
| Consistency Score | [X] | [Y] | +[Z]% |
| Validation Tool Pass Rate | [X] | [Y] | +[Z]% |
| Code Quality | [X] | [Y] | +[Z]% |
| **Overall Health** | **[X]** | **[Y]** | **+[Z]%** |

---

### Phase 7: Reporting & Continuous Improvement (10-15 min)

**Objective**: Document findings, fixes, and recommendations for preventing future issues.

**7.1 Generate Comprehensive Report**:

```markdown
# Repository Validation Report

**Date**: [ISO 8601]
**Scope**: {{VALIDATION_SCOPE}}
**Mode**: {{FIX_MODE}}
**Duration**: [X minutes]

## Executive Summary

**Health Score**: [Before] → [After] (+[X]% improvement)

**Issues Detected**: [TOTAL COUNT]
├── 🔴 Critical: [COUNT]
├── 🟠 High: [COUNT]
├── 🟡 Medium: [COUNT]
└── 🟢 Low: [COUNT]

**Issues Fixed**: [COUNT] ([X]% of total)
**Issues Remaining**: [COUNT] (require manual intervention)

**Impact**:
- [X] broken references fixed
- [Y] consistency issues resolved
- [Z] files improved
- [W] validation tests now passing

## Detailed Findings

### Reference Integrity Issues

#### Fixed
[List all fixed reference issues with details]

#### Remaining (Need Manual Review)
[List issues that couldn't be auto-fixed]

### Consistency Issues

#### Fixed
[List all fixed consistency issues]

#### Remaining
[List issues needing manual attention]

### Collaboration Artifacts

#### Cleaned Up
[List temporary files removed, dead code eliminated]

#### Preserved (Intentional)
[List items that look like artifacts but are intentional]

## Changes Made

**Files Modified**: [COUNT]
**Lines Changed**: +[additions] / -[deletions]
**Git Commits**: [COUNT]

### Detailed Change Log

[For each file modified]
- `path/to/file.md`:
  - Fixed [X] broken file references
  - Updated [Y] line number references
  - Standardized [Z] terminology instances
  - [Other changes]

## Validation Results

✅ **All Validation Tools Passing**: [YES/NO - details if no]

### Test Results

- `validate_consistency.py`: [PASS/FAIL - details]
- `validate_knowledge_base.py`: [PASS/FAIL - details]
- Manual validation checklist: [X/Y items passing]

## Recommendations for Prevention

### Process Improvements

1. **Pre-Commit Validation**: Run validation tools before every commit
   ```bash
   # Add to .git/hooks/pre-commit
   python tests/validate_consistency.py || exit 1
   ```

2. **CI/CD Integration**: Automate validation in GitHub Actions
   - Block PRs with validation failures
   - Generate validation reports automatically

3. **Regular Maintenance Schedule**:
   - Run this validation workflow: [FREQUENCY - e.g., weekly]
   - Review and update validation rules: Monthly
   - Audit repository health: Quarterly

### Tool Enhancements

1. **Improve Validation Scripts**:
   - Add more comprehensive reference checking
   - Implement auto-fix capabilities where safe
   - Generate machine-readable reports

2. **Create Pre-Commit Hooks**:
   - Validate file naming conventions
   - Check for broken references before commit
   - Standardize terminology automatically

3. **Documentation Updates**:
   - Update CONTRIBUTING.md with validation requirements
   - Add troubleshooting guide for common issues
   - Document canonical terminology

### Collaboration Best Practices

1. **Reference Management**:
   - Use relative paths consistently
   - Avoid hardcoded line numbers (use section headers instead)
   - Validate references before committing

2. **Terminology Standards**:
   - Maintain glossary in documentation
   - Use terminology consistently
   - Review for consistency in PRs

3. **Refactoring Protocols**:
   - Update all references when moving/renaming files
   - Run validation tools after refactoring
   - Document refactoring in commits

## Next Steps

**Immediate Actions** (Next 24 hours):
1. [Action item 1]
2. [Action item 2]

**Short-Term Actions** (Next week):
1. [Action item 1]
2. [Action item 2]

**Long-Term Improvements** (Next month):
1. [Action item 1]
2. [Action item 2]

## Appendices

### A. Detailed Issue List

[Complete list of all issues with severity, location, fix status]

### B. Git Commit History

[List of all commits made during this validation]

### C. Validation Tool Output

[Raw output from validation scripts]

---

**Report Generated**: [Timestamp]
**Validation Version**: [This prompt version]
**Repository Health**: [Score with trend indicator]
```

**7.2 Update Validation Tools**:

If new types of issues were discovered:

```python
# Add new validation rules to tests/validate_consistency.py
def check_new_issue_type():
    # Implementation based on newly discovered pattern
    pass

# Update validation_framework.md with new standards
```

---

## Constraints and Guidelines

**Validation Principles** (You WILL follow these):

- You MUST run existing validation tools first before manual checks
- You WILL preserve all intentional design decisions (not all "inconsistencies" are errors)
- You MUST validate fixes don't break functionality
- You WILL prioritize critical issues over cosmetic fixes
- You MUST document all changes with clear rationale
- You WILL use git commits to track all modifications
- You MUST handle ambiguous cases interactively (ask user when uncertain)
- You WILL respect {{FIX_MODE}} and {{SEVERITY_THRESHOLD}} settings

**Safety Protocols**:

- Create git commits frequently (every 5-10 fixes)
- Test validation tools after each major fix batch
- Preserve original file content before major changes
- Use precise search_replace patterns (avoid overly broad matches)
- Validate each fix individually before moving to next

**Anti-Patterns to Avoid**:

- Changing references without verifying target exists
- Over-standardizing terminology (some variation acceptable)
- Deleting files without confirming they're truly orphaned
- Breaking working references to "fix" them to ideal state
- Assuming AI-generated content is always wrong
- Fixing issues that don't exist (false positives)

## Response Format

### 1. **Discovery Summary**

```text
REPOSITORY SCAN COMPLETE
├── Total Files Analyzed: [COUNT]
├── Existing Validation Results:
│   ├── validate_consistency.py: [PASS/FAIL - X errors]
│   └── validate_knowledge_base.py: [PASS/FAIL - Y errors]
├── References Extracted: [COUNT]
├── Issues Detected: [COUNT]
└── Repository Health Score: [X/100] [🔴/��/🟢]
```

### 2. **Issue Report**

```text
ISSUES DETECTED BY CATEGORY

🔴 CRITICAL (Fix Immediately):
[COUNT] issues
├── [Issue 1]: [Description] (File: [path], Line: [X])
└── [Issue 2]: [Description] (File: [path], Line: [X])

🟠 HIGH (Fix Soon):
[COUNT] issues
├── [Issue 1]: [Description] (File: [path], Line: [X])
└── [Issue 2]: [Description] (File: [path], Line: [X])

🟡 MEDIUM (Fix When Possible):
[COUNT] issues
└── [Summary]

🟢 LOW (Cosmetic):
[COUNT] issues
└── [Summary]

TOTAL: [COUNT] issues requiring attention
```

### 3. **Fix Execution Report**

**For Analyze-Only Mode**:
```text
ANALYSIS COMPLETE - No Fixes Applied

Recommended Actions:
1. [Action 1] - Priority: [X] - Effort: [Y hours]
2. [Action 2] - Priority: [X] - Effort: [Y hours]

To apply fixes, run with {{FIX_MODE}} = "fix-minor" or "fix-all-with-approval"
```

**For Fix Modes**:
```text
FIXES APPLIED

Auto-Fixed:
✅ [X] reference errors corrected
✅ [Y] consistency issues resolved
✅ [Z] files cleaned up

Requires Manual Review:
⚠️ [A] critical issues need approval
⚠️ [B] ambiguous cases need user decision

Changes Committed:
📝 [N] git commits with detailed messages

Validation Status:
✅ All validation tools passing
OR
⚠️ [X] validation errors remaining (see report)
```

### 4. **Repository Health Dashboard**

```text
┌─────────────────────────────────────────────────┐
│         REPOSITORY HEALTH DASHBOARD             │
├─────────────────────────────────────────────────┤
│                                                 │
│  Overall Health: [XX/100] [████████░░] 🟢      │
│                                                 │
│  Reference Integrity: [XX/100] [████████░░]    │
│  Documentation Currency: [XX/100] [████████░░] │
│  Consistency Score: [XX/100] [████████░░]      │
│  Code Quality: [XX/100] [████████░░]           │
│  Validation Pass Rate: [XX/100] [████████░░]   │
│                                                 │
│  Improvement: +[X]% from last validation       │
│  Status: [EXCELLENT/GOOD/NEEDS WORK/CRITICAL]  │
│                                                 │
└─────────────────────────────────────────────────┘
```

## Tool Integration

You WILL leverage these tools efficiently:

**Existing Validation Infrastructure**:
```bash
# Always run first
python tests/validate_consistency.py --verbose
python tests/validate_knowledge_base.py --report
```

**File Operations**:
- **Parallel Reading**: Load multiple files simultaneously for efficiency
- **Pattern Matching**: Use grep to find all instances of references
- **Precise Editing**: Use search_replace with unique context for accuracy
- **Validation**: Re-read files after changes to confirm correctness

**Git Operations**:
```bash
# Frequent commits with descriptive messages
git add [files]
git commit -m "fix(scope): description

- Detail 1
- Detail 2

Validation: [status]"
```

**External Tools** (if available):
```bash
# Link checking
markdown-link-check **/*.md

# Linting
flake8 tests/*.py
eslint **/*.js

# Security scanning
safety check  # Python dependencies
npm audit     # JavaScript dependencies
```

## Continuous Improvement Integration

**After Each Validation Run**:

1. **Update Validation Tools**: Add checks for newly discovered issue patterns
2. **Enhance Documentation**: Document new standards discovered through validation
3. **Improve Prompts**: Update agent prompts with clearer reference guidelines
4. **Refine Process**: Adjust this validation workflow based on learnings

**Metrics to Track Over Time**:
```python
validation_history = {
    "2025-01-15": {"health_score": 72, "issues": 45},
    "2025-02-01": {"health_score": 85, "issues": 12},
    "2025-02-15": {"health_score": 92, "issues": 3},
    # Track improvement trends
}
```

## Example Validation Scenario

**Before Validation**:
- Health Score: 68/100 (🟡 Fair)
- Issues: 47 (12 high, 23 medium, 12 low)
- Validation tools: 2 failures
- Broken references: 15
- Inconsistent terminology: 8 instances

**After Validation**:
- Health Score: 94/100 (🟢 Excellent)
- Issues: 2 (0 high, 1 medium, 1 low)
- Validation tools: All passing
- Broken references: 0
- Inconsistent terminology: 0

**Changes**:
- 23 files modified
- 156 references fixed
- 8 terminology standardizations
- 12 orphaned sections removed
- 5 git commits
- Duration: 52 minutes

## Global Context

This validation workflow is part of the [Multi-Agent AI Development Framework](https://github.com/paulpham157/multi-agent-ai-development-framework). By maintaining repository integrity through systematic validation, we ensure the framework remains reliable and trustworthy for the global AI community.

**Success Metrics**:
- Repository health score >90
- Zero broken references
- All validation tools passing
- Documentation reflects reality
- Consistent terminology
- Clean git history

---

**Version:** 1.0.0  
**Last Updated:** 2025-10-12  
**Purpose:** Systematic validation and error correction for multi-agent AI development framework  
**Category:** Repository Maintenance & Quality Assurance  
**Agent:** Optimization Agent  
**Execution Frequency:** As needed (recommended: weekly for active development, monthly for maintenance)
