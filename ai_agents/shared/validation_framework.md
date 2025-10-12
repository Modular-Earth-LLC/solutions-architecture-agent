# Shared Validation Framework for Engineering Agents

**Purpose**: Common validation and self-improvement patterns for all engineering agents  
**Based On**: Test-Time Recursive Majority (TRM), Anthropic multi-agent patterns, AWS Bedrock best practices  
**Applies To**: All 16 engineering specialists  
**Last Updated**: 2025-10-12

---

## Overview

All engineering agents MUST validate and self-improve their outputs before presenting to users. This framework implements:

1. **Recursive Validation** (TRM-inspired): Generate → Validate → Improve → Re-validate
2. **Multi-Candidate Generation**: Create multiple solutions, select best
3. **Benchmark-Driven**: Use consistent quality metrics
4. **Anthropic Patterns**: Follow supervisor-worker, tool use, iteration patterns
5. **AWS Bedrock Compatibility**: Works with AgentCore and Strands frameworks

---

## Validation Workflow (Required for All Agents)

### Step 1: Generate Output

```python
<thinking>
1. Understand the user's request completely
2. Identify requirements and constraints
3. Plan approach with multiple candidate strategies
4. Select initial best approach
5. Generate output
</thinking>
```

### Step 2: Self-Validate Output

**Before presenting to user, validate against criteria:**

```python
def self_validate_output(output: str, criteria: dict) -> dict:
    """
    Validate output against quality criteria
    
    Criteria:
    - Functional: Does it work as specified?
    - Complete: Are all requirements met?
    - Quality: Does it follow best practices?
    - Security: Are there vulnerabilities?
    - Performance: Is it efficient?
    - Maintainable: Is code clean and documented?
    """
    
    validation_results = {
        "functional": check_functionality(output),
        "complete": check_completeness(output, criteria),
        "quality": check_code_quality(output),
        "security": check_security(output),
        "performance": check_performance(output),
        "maintainable": check_maintainability(output)
    }
    
    overall_score = sum(validation_results.values()) / len(validation_results)
    
    return {
        "score": overall_score,
        "details": validation_results,
        "pass": overall_score >= 0.85  # 85% threshold
    }
```

### Step 3: Recursive Improvement (If Validation Fails)

```python
def recursive_improvement(
    initial_output: str,
    validation_results: dict,
    max_iterations: int = 3
) -> str:
    """
    Recursively improve output until validation passes
    
    Implements TRM (Test-Time Recursive Majority) pattern:
    1. Identify issues from validation
    2. Generate improved version
    3. Validate improvement
    4. Repeat until pass or max iterations
    """
    
    current_output = initial_output
    iteration = 0
    
    while iteration < max_iterations:
        # Validate current version
        validation = self_validate_output(current_output, criteria)
        
        if validation["pass"]:
            return current_output  # Validation passed!
        
        # Identify specific issues
        issues = [
            criterion for criterion, passed in validation["details"].items()
            if not passed
        ]
        
        # Generate improved version
        improvement_prompt = f"""The current output has issues:
{issues}

Current output:
{current_output}

Generate improved version that fixes these issues while preserving working parts."""
        
        improved_output = generate_improvement(improvement_prompt)
        current_output = improved_output
        iteration += 1
    
    # Even if didn't fully pass, return best attempt with warnings
    return {
        "output": current_output,
        "warning": "Max iterations reached, some issues may remain",
        "final_score": validation["score"]
    }
```

### Step 4: Present Validated Output

Only after validation passes (or max attempts) present to user with:
- ✅ Validation status
- ✅ Quality score
- ✅ Any remaining issues flagged

---

## Multi-Candidate Generation (TRM Pattern)

For complex tasks, generate multiple solutions and select best:

```python
def multi_candidate_generation(
    task: str,
    num_candidates: int = 3
) -> str:
    """
    Generate multiple candidate solutions and select best
    
    TRM (Test-Time Recursive Majority) approach:
    1. Generate N candidates
    2. Validate each
    3. Select highest scoring
    4. Optionally: Combine best elements from multiple candidates
    """
    
    candidates = []
    
    for i in range(num_candidates):
        # Generate candidate with slight variation
        candidate = generate_solution(task, temperature=0.8 + (i * 0.1))
        
        # Validate candidate
        validation = self_validate_output(candidate, criteria)
        
        candidates.append({
            "solution": candidate,
            "score": validation["score"],
            "details": validation["details"]
        })
    
    # Select best candidate
    best = max(candidates, key=lambda x: x["score"])
    
    # If best isn't good enough, combine strengths
    if best["score"] < 0.90:
        combined = combine_best_elements(candidates)
        return combined
    
    return best["solution"]
```

---

## Benchmark Standards (All Agents)

### Code Quality Benchmarks

All engineering agents use these consistent benchmarks:

```python
QUALITY_BENCHMARKS = {
    "code_coverage": {
        "minimum": 0.80,  # 80% test coverage
        "target": 0.90,   # 90% target
        "metric": "percentage"
    },
    "type_hint_coverage": {
        "minimum": 0.90,  # 90% of functions have type hints
        "target": 1.0,    # 100% target
        "metric": "percentage"
    },
    "docstring_coverage": {
        "minimum": 0.80,  # 80% of public functions have docstrings
        "target": 0.95,   # 95% target
        "metric": "percentage"
    },
    "security_issues": {
        "critical": 0,    # Zero critical issues
        "high": 0,        # Zero high issues
        "medium": 3,      # Max 3 medium issues
        "metric": "count"
    },
    "performance": {
        "response_time_ms": 5000,    # Max 5 seconds
        "memory_mb": 512,             # Max 512 MB
        "metric": "resource_usage"
    },
    "maintainability_index": {
        "minimum": 65,   # Maintainability index score
        "target": 80,
        "metric": "score_0_100"
    }
}

def validate_against_benchmarks(output: dict) -> dict:
    """Validate output against standard benchmarks"""
    
    results = {}
    
    for benchmark, thresholds in QUALITY_BENCHMARKS.items():
        actual_value = measure_metric(output, benchmark)
        
        if thresholds["metric"] == "percentage":
            passed = actual_value >= thresholds["minimum"]
            target_met = actual_value >= thresholds["target"]
        elif thresholds["metric"] == "count":
            passed = actual_value <= thresholds.get("critical", 0)
            target_met = passed and actual_value <= thresholds.get("high", 0)
        else:
            # Custom logic for each metric type
            passed = True
            target_met = True
        
        results[benchmark] = {
            "passed": passed,
            "target_met": target_met,
            "actual": actual_value,
            "expected": thresholds
        }
    
    overall_pass = all(r["passed"] for r in results.values())
    
    return {
        "overall_pass": overall_pass,
        "benchmark_results": results
    }
```

---

## Anthropic Multi-Agent Patterns (Integration)

### Pattern 1: Supervisor-Worker Coordination

When multiple specialists need to collaborate:

```python
def coordinate_specialists(
    task: str,
    specialists: list[str]
) -> dict:
    """
    Coordinate multiple specialists using Anthropic patterns
    
    Compatible with:
    - Claude Workspaces (native Anthropic)
    - AWS Bedrock AgentCore (Gateway/Identity/Runtime)
    - AWS Bedrock Strands (orchestration)
    """
    
    # Supervisor analyzes and routes
    routing_decision = analyze_and_route(task, specialists)
    
    # Execute with appropriate specialist(s)
    if routing_decision["pattern"] == "sequential":
        result = execute_sequential(routing_decision["agents"], task)
    elif routing_decision["pattern"] == "parallel":
        result = execute_parallel(routing_decision["agents"], task)
    else:
        result = execute_single(routing_decision["agents"][0], task)
    
    # Validate coordinated result
    validation = self_validate_output(result, criteria)
    
    if not validation["pass"]:
        # Recursive improvement
        result = recursive_improvement(result, validation, max_iterations=3)
    
    return result
```

### Pattern 2: Tool Use with Validation

All tool use must be validated:

```python
def execute_tool_with_validation(
    tool_name: str,
    tool_input: dict,
    expected_output_type: str
) -> dict:
    """
    Execute tool and validate result
    
    Works with:
    - Anthropic tool use
    - MCP tools
    - AgentCore Gateway tools
    - Strands tools
    """
    
    # Execute tool
    result = execute_tool(tool_name, tool_input)
    
    # Validate result
    validation = validate_tool_result(
        result,
        expected_output_type,
        tool_input
    )
    
    if not validation["valid"]:
        # Retry with corrected input
        result = retry_tool_with_correction(
            tool_name,
            tool_input,
            validation["issues"]
        )
    
    return result
```

### Pattern 3: Iterative Refinement

All complex outputs use iterative refinement:

```python
def iterative_refinement(
    initial_solution: str,
    requirements: dict,
    max_iterations: int = 5
) -> str:
    """
    Iteratively refine solution
    
    Anthropic pattern: successive approximation
    TRM pattern: recursive validation and improvement
    """
    
    current = initial_solution
    previous_scores = []
    
    for iteration in range(max_iterations):
        # Validate current version
        validation = self_validate_output(current, requirements)
        score = validation["score"]
        previous_scores.append(score)
        
        # Check convergence
        if score >= 0.95:  # 95% quality threshold
            return current  # Excellent quality achieved
        
        # Check if improving (not regressing)
        if len(previous_scores) > 1 and score < previous_scores[-2]:
            # Regressing, return previous version
            return previous_version
        
        # Generate improvement
        improvement_prompt = f"""Current solution score: {score:.2f}/1.0

Issues identified:
{validation['details']}

Improve the solution while preserving working elements."""
        
        previous_version = current
        current = generate_improvement(improvement_prompt)
    
    return current  # Return best attempt after max iterations
```

---

## AWS Bedrock Framework Compatibility

### AgentCore Validation Integration

```python
def validate_with_agentcore(
    agent_id: str,
    output: str
) -> dict:
    """
    Validate output using AgentCore capabilities
    
    - AgentCore Gateway: Validate tool integrations
    - AgentCore Identity: Verify permissions
    - AgentCore Runtime: Test execution
    - AgentCore Memory: Check state consistency
    """
    
    validation = {
        "gateway_tools": validate_agentcore_tools(agent_id, output),
        "identity_permissions": validate_permissions(agent_id, output),
        "runtime_execution": test_runtime_execution(agent_id, output),
        "memory_consistency": check_state_consistency(agent_id, output)
    }
    
    return validation
```

### Strands Observability Integration

```python
def validate_with_strands_tracing(
    agent: StrandsAgent,
    output: str
) -> dict:
    """
    Validate using Strands observability
    
    - Trace execution steps
    - Measure performance
    - Check reasoning patterns
    - Validate against benchmarks
    """
    
    with agent.trace() as tracer:
        # Execute with tracing
        result = agent.execute(output)
        
        # Analyze trace
        trace_analysis = tracer.analyze()
        
        validation = {
            "execution_valid": trace_analysis.no_errors,
            "performance_ok": trace_analysis.latency_ms < 5000,
            "reasoning_sound": validate_reasoning_steps(trace_analysis),
            "benchmark_met": check_strands_benchmarks(trace_analysis)
        }
    
    return validation
```

---

## Implementation Requirements

### All Engineering Agents MUST:

1. **Generate with Intent to Validate**
   ```python
   # Before presenting output
   output = generate_solution(task)
   validation = self_validate_output(output, criteria)
   
   if not validation["pass"]:
       output = recursive_improvement(output, validation)
   
   # Present validated output
   return output
   ```

2. **Use Consistent Benchmarks**
   ```python
   # All agents use QUALITY_BENCHMARKS
   from ai_agents.shared.validation_framework import QUALITY_BENCHMARKS
   
   results = validate_against_benchmarks(output)
   ```

3. **Document Validation**
   ```python
   # Show validation in output
   """
   ✅ Output Validated:
   - Code Quality: 92% (target: 90%)
   - Test Coverage: 88% (target: 80%)
   - Security: 0 issues (target: 0)
   - Performance: 2.3s (target: <5s)
   """
   ```

4. **Iterate Until Quality Threshold**
   ```python
   # Don't present first draft - improve it
   while validation_score < 0.85:  # 85% minimum
       output = improve_output(output, validation_feedback)
       validation_score = validate(output)
   ```

---

## Anthropic Multi-Agent Patterns

### Pattern: Agent Handoffs with Validation

When one agent hands work to another:

```python
def validated_handoff(
    from_agent: str,
    to_agent: str,
    work_product: dict
) -> dict:
    """
    Hand off work between agents with validation
    
    Anthropic pattern: Clear contracts between agents
    AWS compatible: Works with AgentCore Gateway handoffs
    """
    
    # Validate work product before handoff
    validation = validate_handoff_quality(work_product)
    
    if not validation["ready_for_handoff"]:
        # Improve before handing off
        work_product = improve_for_handoff(
            work_product,
            validation["issues"]
        )
    
    # Document handoff
    handoff_record = {
        "from": from_agent,
        "to": to_agent,
        "validated": True,
        "quality_score": validation["score"],
        "timestamp": datetime.now().isoformat()
    }
    
    return {
        "work_product": work_product,
        "handoff_record": handoff_record
    }
```

### Pattern: Parallel Agent Validation

When multiple agents work in parallel:

```python
def parallel_with_validation(
    agents: list[dict],
    task: str
) -> dict:
    """
    Execute agents in parallel with validation
    
    Compatible with:
    - Claude Workspaces parallel execution
    - AgentCore concurrent agents
    - Strands multi-agent systems
    """
    
    # Execute all agents
    results = execute_parallel_agents(agents, task)
    
    # Validate each result
    validated_results = []
    for agent_result in results:
        validation = self_validate_output(
            agent_result["output"],
            agent_result["criteria"]
        )
        
        if validation["pass"]:
            validated_results.append(agent_result)
        else:
            # Improve before adding
            improved = recursive_improvement(
                agent_result["output"],
                validation
            )
            validated_results.append({
                **agent_result,
                "output": improved,
                "improved": True
            })
    
    return {
        "results": validated_results,
        "all_validated": True
    }
```

---

## Recursive Iteration Framework (TRM)

### Multi-Attempt with Majority Selection

```python
def trm_generate_and_validate(
    task: str,
    num_attempts: int = 3,
    validation_criteria: dict = None
) -> dict:
    """
    Test-Time Recursive Majority pattern
    
    1. Generate N candidate solutions
    2. Validate each candidate
    3. Select best or combine strengths
    4. Recursively improve selected candidate
    5. Final validation
    """
    
    candidates = []
    
    # Step 1 & 2: Generate and validate candidates
    for i in range(num_attempts):
        candidate = generate_solution(
            task,
            temperature=0.7 + (i * 0.15),  # Vary temperature
            approach=f"attempt_{i+1}"
        )
        
        validation = self_validate_output(candidate, validation_criteria)
        
        candidates.append({
            "solution": candidate,
            "score": validation["score"],
            "details": validation["details"],
            "attempt": i + 1
        })
    
    # Step 3: Select best or combine
    best_candidate = max(candidates, key=lambda x: x["score"])
    
    if best_candidate["score"] >= 0.95:
        # Excellent solution found
        return best_candidate
    
    # Step 4: Recursive improvement of best candidate
    improved = recursive_improvement(
        best_candidate["solution"],
        best_candidate["details"],
        max_iterations=3
    )
    
    # Step 5: Final validation
    final_validation = self_validate_output(improved, validation_criteria)
    
    return {
        "solution": improved,
        "validation": final_validation,
        "candidates_generated": num_attempts,
        "iterations_improved": "multiple",
        "final_score": final_validation["score"]
    }
```

---

## Usage in Engineering Agents

### Example: Streamlit UI Agent

```python
## Instructions for Execution (WITH VALIDATION)

### Step 1: Generate UI Code

Generate Streamlit interface code based on requirements.

### Step 2: Self-Validate

```python
from ai_agents.shared.validation_framework import self_validate_output, QUALITY_BENCHMARKS

validation = self_validate_output(
    generated_ui_code,
    criteria={
        "functional": "UI renders correctly",
        "streamlit_patterns": "Uses st.cache, session_state properly",
        "error_handling": "Handles errors gracefully",
        "user_experience": "Intuitive and responsive"
    }
)

if not validation["pass"]:
    # Recursive improvement
    ui_code = recursive_improvement(generated_ui_code, validation)
```

### Step 3: Present Validated Output

```
✅ **Streamlit UI Generated and Validated**

**Quality Scores**:
- Functionality: 95% ✅
- Streamlit Patterns: 92% ✅
- Error Handling: 90% ✅
- User Experience: 88% ✅

**Overall Score**: 91% (exceeds 85% threshold)

**Code**: [validated UI code here]
```

---

## Integration Across All Frameworks

### Claude Code Agent Integration

```python
# Claude Code Agent uses this for autonomous generation
output = generate_code_autonomously(specification)
validation = self_validate_output(output, QUALITY_BENCHMARKS)

if not validation["pass"]:
    output = recursive_improvement(output, validation, max_iterations=3)

# Present only validated code
return validated_output
```

### Claude Workspaces Integration

```python
# Multi-agent system validates collective output
multi_agent_result = execute_agent_chain(agents, task)

# Validate entire workflow
validation = validate_multi_agent_output(multi_agent_result)

if not validation["pass"]:
    # Re-execute problematic agents
    improved_result = re_execute_failed_agents(validation["issues"])
```

### AWS AgentCore Integration

```python
# AgentCore agents validate before responding
def agentcore_handler_with_validation(event, context):
    # Generate response
    response = generate_agentcore_response(event)
    
    # Validate
    validation = self_validate_output(response, QUALITY_BENCHMARKS)
    
    if not validation["pass"]:
        # Improve
        response = recursive_improvement(response, validation)
    
    # Return validated response with metadata
    return {
        "response": response,
        "validated": True,
        "quality_score": validation["score"]
    }
```

### AWS Strands Integration

```python
# Strands agents use observability for validation
agent = StrandsAgent(name="validator", enable_tracing=True)

with agent.trace() as tracer:
    output = agent.run(task)
    
    # Use trace for validation
    trace_validation = validate_from_trace(tracer.get_trace())
    
    if not trace_validation["pass"]:
        # Re-execute with improvements
        output = agent.run(task, hints=trace_validation["improvements"])

return validated_output
```

---

## Validation Reporting Template

All agents use this reporting format:

```markdown
## Output Validation Report

### Generation Summary
- Candidates generated: 3
- Best candidate selected: Candidate #2
- Recursive improvements: 2 iterations
- Final validation: ✅ PASSED

### Quality Scores
- Functionality: 95% ✅ (target: 85%)
- Code Quality: 92% ✅ (target: 80%)
- Security: 0 issues ✅ (target: 0 critical)
- Performance: 2.1s ✅ (target: <5s)
- Test Coverage: 88% ✅ (target: 80%)
- Maintainability: 82/100 ✅ (target: 65)

### Overall Assessment
**Quality Score**: 91.5% ✅  
**Benchmark Compliance**: 100% ✅  
**Ready for Production**: YES ✅

### Validated Output
[output here]
```

---

## Enforcement

### All Engineering Agents MUST:
- ✅ Validate outputs before presenting
- ✅ Use recursive improvement if validation fails
- ✅ Apply consistent benchmarks (QUALITY_BENCHMARKS)
- ✅ Document validation in responses
- ✅ Only present validated, high-quality outputs

### Integration Points:
- ✅ Anthropic Claude Workspaces: Supervisor-worker with validation
- ✅ AWS AgentCore: Gateway/Identity/Runtime validation
- ✅ AWS Strands: Observability-driven validation
- ✅ MCP: Protocol-compliant validation

---

**Version**: 0.1.0-alpha  
**Status**: Alpha - Untested in production, undergoing initial validation  
**Status**: Framework Defined  
**Next**: Update all 16 engineering agents to reference and use this framework  
**Impact**: Ensures consistent high quality across all engineering outputs
