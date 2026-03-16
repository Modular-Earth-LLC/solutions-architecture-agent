#!/usr/bin/env python3
"""
Skill Independence Validator

Validates that each skill can run independently per Anthropic marketplace requirements:
  1. No cross-skill imports — no SKILL.md references another SKILL.md by path
  2. Advisory prerequisites only — every STOP also provides an alternative path
  3. Self-contained context — each SKILL.md contains its own role, workflow, and output rules
  4. No repo-specific references — no SKILL.md hardcodes "solutions-architecture-agent" in ways that break external use
  5. Tool grants are minimal — allowed-tools is not "all"
  6. Arguments enable standalone use — each SKILL.md documents $ARGUMENTS acceptance

Usage:
    python tests/test_skill_independence.py
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SKILLS_DIR = REPO_ROOT / "skills"


def get_skill_files() -> list[tuple[str, Path, str]]:
    """Return list of (skill_name, skill_path, skill_text)."""
    results = []
    for skill_dir in sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if skill_file.exists():
            text = skill_file.read_text(encoding="utf-8")
            results.append((skill_dir.name, skill_file, text))
    return results


def check_no_cross_skill_imports() -> bool:
    """Check 1: No SKILL.md references another SKILL.md by path."""
    print("\n[1/6] Checking no cross-skill imports...")

    issues = []
    # Pattern: references to other skills/ directories by path
    path_pattern = re.compile(r'skills/[\w-]+/SKILL\.md')

    for name, path, text in get_skill_files():
        matches = path_pattern.findall(text)
        if matches:
            issues.append(f"  {name}: references {matches}")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: No SKILL.md references another SKILL.md by path")
        return True


def check_advisory_prerequisites() -> bool:
    """Check 2: Every SKILL.md that mentions STOP also provides an alternative path
    (direct input, arguments, or proceed with caveats)."""
    print("\n[2/6] Checking advisory prerequisites...")

    issues = []
    stop_pattern = re.compile(r'STOP', re.IGNORECASE)
    alt_patterns = [
        re.compile(r'provide.*direct', re.IGNORECASE),
        re.compile(r'\$ARGUMENTS', re.IGNORECASE),
        re.compile(r'or\s+provide', re.IGNORECASE),
        re.compile(r'accept.*context.*directly', re.IGNORECASE),
        re.compile(r'alternatively', re.IGNORECASE),
        re.compile(r'proceed.*with.*caveat', re.IGNORECASE),
        re.compile(r'entry.point', re.IGNORECASE),
        re.compile(r'no.*upstream.*required', re.IGNORECASE),
    ]

    for name, path, text in get_skill_files():
        # Find all STOP occurrences
        stop_matches = list(stop_pattern.finditer(text))
        if not stop_matches:
            continue

        # Check if there's any alternative path language
        has_alt = any(p.search(text) for p in alt_patterns)
        if not has_alt:
            issues.append(
                f"  {name}: has {len(stop_matches)} STOP directive(s) but no "
                f"alternative path (direct input, $ARGUMENTS, or proceed with caveats)"
            )

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All skills with STOP directives also provide alternative paths")
        return True


def check_self_contained() -> bool:
    """Check 3: Each SKILL.md contains its own role, workflow, and output rules."""
    print("\n[3/6] Checking self-contained context...")

    issues = []
    required_sections = [
        (re.compile(r'ROLE|role.*context', re.IGNORECASE), "role/context"),
        (re.compile(r'WORKFLOW|OUTPUT|PROCESS|PROCEDURE', re.IGNORECASE), "workflow/output"),
    ]

    for name, path, text in get_skill_files():
        for pattern, desc in required_sections:
            if not pattern.search(text):
                issues.append(f"  {name}: missing {desc} section")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All skills contain role, workflow, and output sections")
        return True


def check_no_repo_specific_refs() -> bool:
    """Check 4: No SKILL.md hardcodes repo name in ways that break external use."""
    print("\n[4/6] Checking no repo-specific references...")

    issues = []
    # Patterns that would break if the skill is used outside this repo
    repo_patterns = [
        (re.compile(r'solutions-architecture-agent'), "repo name"),
        (re.compile(r'C:\\\\dev|C:/dev|/home/\w+/dev'), "local filesystem path"),
        (re.compile(r'\\\\wsl\.localhost'), "WSL path"),
    ]

    for name, path, text in get_skill_files():
        for pattern, desc in repo_patterns:
            if pattern.search(text):
                issues.append(f"  {name}: contains {desc}")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: No repo-specific references found")
        return True


def check_minimal_tool_grants() -> bool:
    """Check 5: Each SKILL.md allowed-tools is a specific list, not 'all'."""
    print("\n[5/6] Checking minimal tool grants...")

    issues = []

    for name, path, text in get_skill_files():
        # Extract allowed-tools from frontmatter
        match = re.search(r'^allowed-tools:\s*(.+)$', text, re.MULTILINE)
        if not match:
            issues.append(f"  {name}: no allowed-tools in frontmatter")
            continue

        tools = match.group(1).strip()
        if tools.lower() in ("all", "*", "any"):
            issues.append(f"  {name}: allowed-tools is '{tools}' (should be specific list)")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All skills have specific tool grants")
        return True


def check_arguments_enable_standalone() -> bool:
    """Check 6: Each SKILL.md documents how to accept context via $ARGUMENTS."""
    print("\n[6/6] Checking $ARGUMENTS enable standalone use...")

    issues = []
    args_pattern = re.compile(r'\$ARGUMENTS')

    for name, path, text in get_skill_files():
        if not args_pattern.search(text):
            issues.append(f"  {name}: does not reference $ARGUMENTS")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All skills document $ARGUMENTS for standalone invocation")
        return True


def main() -> None:
    print("=" * 60)
    print("Skill Independence Validation")
    print("=" * 60)

    results = [
        check_no_cross_skill_imports(),
        check_advisory_prerequisites(),
        check_self_contained(),
        check_no_repo_specific_refs(),
        check_minimal_tool_grants(),
        check_arguments_enable_standalone(),
    ]

    passed = sum(1 for r in results if r)
    failed = sum(1 for r in results if not r)

    print()
    print("=" * 60)
    print(f"Results: {passed} PASS, {failed} FAIL")
    print("=" * 60)

    if all(results):
        print("\nAll skill independence checks passed.")
        sys.exit(0)
    else:
        print("\nSome checks failed — see details above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
