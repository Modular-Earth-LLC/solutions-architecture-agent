#!/usr/bin/env python3
"""
Output Quality Tests

Validates output quality standards:
  1. Name consistency — no hardcoded personal names in skills or templates
  2. Length constraint presence — every skill declares per-tier limits
  3. Section completeness — required sections in templates
  4. Cross-reference ID format — skills reference consistent ID patterns
  5. No hardcoded filesystem paths in skills

Usage:
    python tests/test_output_quality.py
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
TEMPLATES_DIR = REPO_ROOT / "templates"


def get_skill_files() -> list[tuple[str, Path, str]]:
    """Return list of (skill_name, skill_path, skill_text)."""
    results = []
    for skill_dir in sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if skill_file.exists():
            text = skill_file.read_text(encoding="utf-8")
            results.append((skill_dir.name, skill_file, text))
    return results


def check_no_hardcoded_names() -> bool:
    """Check 1: No hardcoded personal names in skills or templates."""
    print("\n[1/5] Checking no hardcoded personal names...")

    # Names that should not appear in reusable components
    # These are common hallucination targets from the CVS engagement
    forbidden_names = re.compile(
        r"\bPaul Pham\b|\bPaul Praeder\b|\bPaul P\b",
        re.IGNORECASE,
    )

    issues = []

    for name, path, text in get_skill_files():
        matches = forbidden_names.findall(text)
        if matches:
            issues.append(f"  {name}/SKILL.md: contains hardcoded name(s): {matches}")

    # Check templates
    if TEMPLATES_DIR.exists():
        for template in TEMPLATES_DIR.glob("*.md"):
            text = template.read_text(encoding="utf-8")
            matches = forbidden_names.findall(text)
            if matches:
                issues.append(f"  templates/{template.name}: contains hardcoded name(s): {matches}")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: No hardcoded personal names found in skills or templates")
        return True


def check_length_constraints() -> bool:
    """Check 2: Every skill declares per-tier line limits."""
    print("\n[2/5] Checking per-tier length constraints...")

    issues = []
    limit_pattern = re.compile(r"<\d+ lines")

    for name, path, text in get_skill_files():
        matches = limit_pattern.findall(text)
        if not matches:
            issues.append(f"  {name}: no line count limits found")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All skills have per-tier line limits")
        return True


def check_template_sections() -> bool:
    """Check 3: Templates have required structural sections."""
    print("\n[3/5] Checking template section completeness...")

    issues = []
    required_templates = {
        "single-document-template.md": ["Executive Summary", "Proposed Solution", "Recommendations"],
        "presentation-template.md": ["Title", "Challenge", "Solution", "Next Steps"],
    }

    for template_name, required_sections in required_templates.items():
        template_path = TEMPLATES_DIR / template_name
        if not template_path.exists():
            issues.append(f"  Missing template: {template_name}")
            continue

        text = template_path.read_text(encoding="utf-8")
        for section in required_sections:
            if section not in text:
                issues.append(f"  {template_name}: missing section '{section}'")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All templates have required sections")
        return True


def check_id_patterns() -> bool:
    """Check 4: Skills reference consistent ID format patterns."""
    print("\n[4/5] Checking ID pattern consistency...")

    # Skills that define ID patterns in their output spec
    expected_patterns = {
        "requirements": "FR-",
        "architecture": "C-",
        "security-review": "T-",
        "integration-plan": "API-",
        "review": "R-",
    }

    issues = []
    for skill_name, expected_prefix in expected_patterns.items():
        skill_file = SKILLS_DIR / skill_name / "SKILL.md"
        if not skill_file.exists():
            issues.append(f"  {skill_name}: SKILL.md not found")
            continue

        text = skill_file.read_text(encoding="utf-8")
        if expected_prefix not in text:
            issues.append(f"  {skill_name}: missing expected ID prefix '{expected_prefix}'")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All skills use consistent ID patterns")
        return True


def check_no_hardcoded_paths() -> bool:
    """Check 5: No hardcoded filesystem paths in skills."""
    print("\n[5/5] Checking no hardcoded filesystem paths...")

    path_patterns = [
        (re.compile(r"C:\\\\dev|C:/dev|C:\\dev"), "Windows dev path"),
        (re.compile(r"\\\\wsl\.localhost"), "WSL path"),
        (re.compile(r"/home/\w+/dev"), "Linux home path"),
        (re.compile(r"paulprae-com|paulprae\.com"), "personal site reference"),
    ]

    issues = []
    for name, path, text in get_skill_files():
        for pattern, desc in path_patterns:
            if pattern.search(text):
                issues.append(f"  {name}: contains {desc}")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: No hardcoded filesystem paths in skills")
        return True


def main() -> None:
    print("=" * 60)
    print("Output Quality Validation")
    print("=" * 60)

    results = [
        check_no_hardcoded_names(),
        check_length_constraints(),
        check_template_sections(),
        check_id_patterns(),
        check_no_hardcoded_paths(),
    ]

    passed = sum(1 for r in results if r)
    failed = sum(1 for r in results if not r)

    print()
    print("=" * 60)
    print(f"Results: {passed} PASS, {failed} FAIL")
    print("=" * 60)

    if all(results):
        print("\nAll output quality checks passed.")
        sys.exit(0)
    else:
        print("\nSome checks failed — see details above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
