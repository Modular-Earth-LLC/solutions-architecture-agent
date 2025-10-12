#!/usr/bin/env python3
"""
Repository Consistency Validator

Validates critical consistency requirements:
- All dates match alpha release date (2025-10-12)
- All 23 agent files exist
- Knowledge base JSON files are valid

Run: python tests/validate_consistency.py
"""

import json
import re
import sys
from pathlib import Path

# Configuration
REPO_ROOT = Path(__file__).parent.parent
EXPECTED_DATE = "2025-10-12"
EXPECTED_AGENTS = 23

def validate_dates():
    """Check all markdown files have consistent dates"""
    print(f"\n[1/3] Validating dates (expected: {EXPECTED_DATE})...")
    
    issues = []
    # Check only core files, exclude examples/outputs/archived
    core_patterns = ["*.md", "knowledge_base/*.json"]
    exclude_patterns = ["outputs/", "tmp/", "examples/"]
    
    files = []
    for pattern in core_patterns:
        files.extend(REPO_ROOT.glob(f"**/{pattern}"))
    
    files = [f for f in files if not any(ex in str(f) for ex in exclude_patterns)]
    
    date_pattern = re.compile(r'20\d{2}-\d{2}-\d{2}')
    
    for f in files:
        try:
            content = f.read_text(encoding='utf-8')
            dates = date_pattern.findall(content)
            wrong_dates = [d for d in dates if d != EXPECTED_DATE and d not in [
                '2025-12-31', '2025-11-01', '2025-12-01',  # Example project deadlines
                '2012-10-17', '2022-11-28', '2023-05-31'  # External service launch dates
            ]]
            if wrong_dates:
                issues.append(f"  {f.relative_to(REPO_ROOT)}: {', '.join(set(wrong_dates))}")
        except:
            pass
    
    if issues:
        print(f"  Found {len(issues)} files with incorrect dates:")
        for issue in issues[:10]:  # Show first 10
            print(issue)
        return False
    else:
        print(f"  OK: Checked {len(files)} core files")
        return True

def validate_agents():
    """Check all expected agent files exist"""
    print(f"\n[2/3] Validating agent files (expected: {EXPECTED_AGENTS})...")
    
    agents = [
        "supervisor_agent.system.prompt.md",
        "ai_agents/requirements_agent.system.prompt.md",
        "ai_agents/architecture_agent.system.prompt.md",
        "ai_agents/deployment_agent.system.prompt.md",
        "ai_agents/optimization_agent.system.prompt.md",
        "ai_agents/prompt_engineering_agent.system.prompt.md",
        "ai_agents/engineering_supervisor_agent.system.prompt.md",
        "ai_agents/streamlit_ui_agent.system.prompt.md",
        "ai_agents/claude_code_agent.system.prompt.md",
        "ai_agents/claude_workspaces_agent.system.prompt.md",
        "ai_agents/anthropic_agents_sdk_agent.system.prompt.md",
        "ai_agents/mcp_services_agent.system.prompt.md",
        "ai_agents/langchain_agent.system.prompt.md",
        "ai_agents/knowledge_engineering_agent.system.prompt.md",
        "ai_agents/data_engineering_agent.system.prompt.md",
        "ai_agents/aws_bedrock_agentcore_agent.system.prompt.md",
        "ai_agents/aws_bedrock_strands_agent.system.prompt.md",
        "ai_agents/aws_infrastructure_agent.system.prompt.md",
        "ai_agents/aws_security_networking_agent.system.prompt.md",
        "ai_agents/claude_projects_agent.system.prompt.md",
        "ai_agents/testing_qa_agent.system.prompt.md",
        "ai_agents/github_copilot_agent.system.prompt.md",
        "ai_agents/cursor_ide_agent.system.prompt.md",
    ]
    
    missing = [a for a in agents if not (REPO_ROOT / a).exists()]
    
    if missing:
        print(f"  ERROR: Missing {len(missing)} agent files:")
        for m in missing:
            print(f"  - {m}")
        return False
    else:
        print(f"  OK: All {len(agents)} agent files exist")
        return True

def validate_knowledge_base():
    """Check knowledge base JSON files are valid"""
    print(f"\n[3/3] Validating knowledge base...")
    
    kb_files = [
        "knowledge_base/system_config.json",
        "knowledge_base/user_requirements.json",
        "knowledge_base/design_decisions.json"
    ]
    
    issues = []
    for kb in kb_files:
        path = REPO_ROOT / kb
        if not path.exists():
            issues.append(f"  Missing: {kb}")
            continue
        try:
            with open(path, 'r', encoding='utf-8') as f:
                json.load(f)
        except json.JSONDecodeError as e:
            issues.append(f"  Invalid JSON in {kb}: {e}")
    
    if issues:
        print(f"  ERROR: Found {len(issues)} issues:")
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All {len(kb_files)} KB files are valid JSON")
        return True

def main():
    print("=" * 60)
    print("Repository Consistency Validation")
    print("=" * 60)
    
    results = [
        validate_dates(),
        validate_agents(),
        validate_knowledge_base()
    ]
    
    print("\n" + "=" * 60)
    if all(results):
        print("SUCCESS: All validations passed!")
        print("=" * 60)
        return 0
    else:
        print("FAILED: Some validations failed (see above)")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())