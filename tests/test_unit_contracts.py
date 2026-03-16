#!/usr/bin/env python3
"""
Unit Contract Validator

Validates local, file-level contracts without cross-file orchestration:
  1. plugin.json contains required manifest fields
  2. every SKILL.md includes required frontmatter keys
  3. every SKILL.md contains required section anchors
  4. every schema file is valid JSON

Usage:
    python tests/test_unit_contracts.py
"""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PLUGIN = REPO_ROOT / ".claude-plugin" / "plugin.json"
SKILLS_DIR = REPO_ROOT / "skills"
SCHEMA_DIR = REPO_ROOT / "knowledge_base" / "schemas"

REQUIRED_PLUGIN_FIELDS = ["name", "version", "description", "author", "license"]
REQUIRED_SKILL_FRONTMATTER = ["name", "description", "argument-hint", "allowed-tools"]
REQUIRED_SECTIONS = [
    "ROLE & CONTEXT",
    "PREREQUISITES",
    "CONTEXT LOADING",
    "WORKFLOW",
    "OUTPUT",
]


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}

    end = text.find("---", 3)
    if end == -1:
        return {}

    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([a-zA-Z_-]+):\s*(.+)$", line.strip())
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return fm


def check_plugin_manifest() -> bool:
    print("\n[1/4] Checking plugin manifest fields...")
    if not PLUGIN.exists():
        print("  [FAIL] .claude-plugin/plugin.json not found")
        return False

    with open(PLUGIN, "r", encoding="utf-8") as f:
        data = json.load(f)

    missing = [k for k in REQUIRED_PLUGIN_FIELDS if k not in data]
    if missing:
        print(f"  Missing plugin fields: {missing}")
        return False

    print("  OK: plugin.json required fields present")
    return True


def check_skill_frontmatter() -> bool:
    print("\n[2/4] Checking skill frontmatter keys...")
    issues = []

    for skill_dir in sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            issues.append(f"{skill_dir.name}: missing SKILL.md")
            continue

        fm = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
        missing = [k for k in REQUIRED_SKILL_FRONTMATTER if k not in fm]
        if missing:
            issues.append(f"{skill_dir.name}: missing frontmatter keys {missing}")

    if issues:
        for issue in issues:
            print(f"  {issue}")
        return False

    print("  OK: all skills include required frontmatter keys")
    return True


def check_skill_sections() -> bool:
    print("\n[3/4] Checking skill section anchors...")
    issues = []

    for skill_dir in sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            continue

        text = skill_file.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                issues.append(f"{skill_dir.name}: missing section containing '{section}'")

    if issues:
        for issue in issues:
            print(f"  {issue}")
        return False

    print("  OK: skill section anchors present")
    return True


def check_schema_json_validity() -> bool:
    print("\n[4/4] Checking schema file JSON validity...")
    issues = []

    for schema_file in sorted(SCHEMA_DIR.glob("*.json")):
        try:
            with open(schema_file, "r", encoding="utf-8") as f:
                json.load(f)
        except json.JSONDecodeError as e:
            issues.append(f"{schema_file.name}: invalid JSON ({e})")

    if issues:
        for issue in issues:
            print(f"  {issue}")
        return False

    print("  OK: all schema files are valid JSON")
    return True


def main() -> None:
    print("=" * 60)
    print("Unit Contract Validation")
    print("=" * 60)

    results = [
        check_plugin_manifest(),
        check_skill_frontmatter(),
        check_skill_sections(),
        check_schema_json_validity(),
    ]

    passed = sum(1 for r in results if r)
    failed = sum(1 for r in results if not r)

    print("\n" + "=" * 60)
    print(f"Results: {passed} PASS, {failed} FAIL")
    print("=" * 60)

    if failed == 0:
        print("\nAll unit contract checks passed.")
        sys.exit(0)

    print("\nSome unit contract checks failed.")
    sys.exit(1)


if __name__ == "__main__":
    main()
