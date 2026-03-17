#!/usr/bin/env python3
"""
Workflow Validation Tests

Validates v1.1 features:
  1. Depth control section exists in all 9 skills
  2. Output length constraints exist in all 9 skills
  3. Checkpoint enforcement (MANDATORY STOP) in all 9 skills
  4. Conditional agent invocation in skills that use sub-agents
  5. New canonical flows in CLAUDE.md
  6. Scope negotiation in CLAUDE.md dispatch
  7. Deliverable-first mode in CLAUDE.md
  8. Review modes in /review skill

Usage:
    python tests/test_workflow_validation.py
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
CLAUDE_MD = REPO_ROOT / "CLAUDE.md"


def get_skill_files() -> list[tuple[str, str]]:
    """Return list of (skill_name, skill_text)."""
    results = []
    for skill_dir in sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if skill_file.exists():
            text = skill_file.read_text(encoding="utf-8")
            results.append((skill_dir.name, text))
    return results


def check_depth_control_in_all_skills() -> bool:
    """Check 1: All 9 skills have a DEPTH CONTROL section."""
    print("\n[1/8] Checking depth control in all skills...")

    skills = get_skill_files()
    issues = []
    depth_pattern = re.compile(r"DEPTH CONTROL|depth tier", re.IGNORECASE)

    for name, text in skills:
        if not depth_pattern.search(text):
            issues.append(f"  {name}: missing DEPTH CONTROL section")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All {len(skills)} skills have depth control")
        return True


def check_output_length_constraints() -> bool:
    """Check 2: All 9 skills have output length constraints."""
    print("\n[2/8] Checking output length constraints...")

    skills = get_skill_files()
    issues = []
    constraint_pattern = re.compile(
        r"Output length constraints|<\d+ lines", re.IGNORECASE
    )

    for name, text in skills:
        if not constraint_pattern.search(text):
            issues.append(f"  {name}: missing output length constraints")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All {len(skills)} skills have output length constraints")
        return True


def check_mandatory_stop() -> bool:
    """Check 3: All 9 skills have MANDATORY STOP in their completion section."""
    print("\n[3/8] Checking MANDATORY STOP in all skills...")

    skills = get_skill_files()
    issues = []

    for name, text in skills:
        if "MANDATORY STOP" not in text:
            issues.append(f"  {name}: missing MANDATORY STOP directive")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All {len(skills)} skills have MANDATORY STOP")
        return True


def check_no_auto_proceed() -> bool:
    """Check 3b: No skill contains 'automatically proceed' language."""
    print("\n  ... Checking no auto-proceed language...")

    skills = get_skill_files()
    issues = []
    auto_pattern = re.compile(
        r"(?<!NOT )(?<!not )(?<!Do NOT )automatically proceed|"
        r"(?<!NOT )(?<!not )(?<!Do NOT )auto.?execute the next",
        re.IGNORECASE,
    )

    for name, text in skills:
        if auto_pattern.search(text):
            issues.append(f"  {name}: contains auto-proceed language")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: No skills contain auto-proceed language")
        return True


def check_conditional_agents() -> bool:
    """Check 4: Skills with sub-agent invocations have conditional logic based on depth."""
    print("\n[4/8] Checking conditional agent invocation...")

    agent_skills = ["architecture", "security-review", "review"]
    issues = []

    for name, text in get_skill_files():
        if name not in agent_skills:
            continue
        if "If QUICK" not in text and "QUICK depth" not in text:
            issues.append(
                f"  {name}: uses sub-agents but has no QUICK depth conditional"
            )

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All {len(agent_skills)} agent-using skills have depth conditionals")
        return True


def check_new_canonical_flows() -> bool:
    """Check 5: CLAUDE.md contains new canonical flows."""
    print("\n[5/8] Checking new canonical flows in CLAUDE.md...")

    text = CLAUDE_MD.read_text(encoding="utf-8")
    required_flows = ["Direct Delivery", "Rapid Assessment", "Custom Document"]
    issues = []

    for flow in required_flows:
        if flow not in text:
            issues.append(f"  Missing flow: {flow}")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All {len(required_flows)} new flows present")
        return True


def check_scope_negotiation() -> bool:
    """Check 6: CLAUDE.md dispatch includes scope negotiation."""
    print("\n[6/8] Checking scope negotiation in dispatch...")

    text = CLAUDE_MD.read_text(encoding="utf-8")
    required_terms = [
        "Scope Negotiation",
        "depth tier",
        "QUICK",
        "STANDARD",
        "COMPREHENSIVE",
        "--depth",
    ]
    issues = []

    for term in required_terms:
        if term not in text:
            issues.append(f"  Missing: {term}")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: Scope negotiation present with all {len(required_terms)} required terms")
        return True


def check_deliverable_first() -> bool:
    """Check 7: CLAUDE.md includes deliverable-first mode."""
    print("\n[7/8] Checking deliverable-first mode...")

    text = CLAUDE_MD.read_text(encoding="utf-8")
    required = ["Deliverable-First Mode", "deliverable specification"]
    issues = []

    for term in required:
        if term not in text:
            issues.append(f"  Missing: {term}")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: Deliverable-first mode documented")
        return True


def check_review_modes() -> bool:
    """Check 8: /review skill has review modes."""
    print("\n[8/8] Checking review modes...")

    review_file = SKILLS_DIR / "review" / "SKILL.md"
    text = review_file.read_text(encoding="utf-8")
    required_modes = ["Single-file", "Final-document", "Batch"]
    issues = []

    for mode in required_modes:
        if mode not in text:
            issues.append(f"  Missing review mode: {mode}")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All {len(required_modes)} review modes present")
        return True


def main() -> None:
    print("=" * 60)
    print("Workflow Validation (v1.1 Features)")
    print("=" * 60)

    results = [
        check_depth_control_in_all_skills(),
        check_output_length_constraints(),
        check_mandatory_stop() and check_no_auto_proceed(),
        check_conditional_agents(),
        check_new_canonical_flows(),
        check_scope_negotiation(),
        check_deliverable_first(),
        check_review_modes(),
    ]

    passed = sum(1 for r in results if r)
    failed = sum(1 for r in results if not r)

    print()
    print("=" * 60)
    print(f"Results: {passed} PASS, {failed} FAIL")
    print("=" * 60)

    if all(results):
        print("\nAll workflow validation checks passed.")
        sys.exit(0)
    else:
        print("\nSome checks failed — see details above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
