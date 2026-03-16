#!/usr/bin/env python3
"""
Integration Flow Validator

Validates cross-artifact integration semantics:
  1. .repo-metadata counts match filesystem
  2. skills in metadata match skills directory
  3. sub-agents in metadata match agents directory
  4. example engagement lifecycle references existing files
  5. example domain files share one engagement_id

Usage:
    python tests/test_integration_flow.py
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
METADATA = REPO_ROOT / ".repo-metadata.json"
SKILLS_DIR = REPO_ROOT / "skills"
AGENTS_DIR = REPO_ROOT / "agents"
EXAMPLE_DIR = REPO_ROOT / "examples" / "healthcare-ibmi-migration"


def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def check_metadata_counts() -> bool:
    print("\n[1/5] Checking metadata count integration...")
    data = load_json(METADATA)

    actual_skills = sorted(
        d.name for d in SKILLS_DIR.iterdir() if d.is_dir() and (d / "SKILL.md").exists()
    )
    actual_agents = sorted(
        f.stem for f in AGENTS_DIR.glob("*.md") if f.name != "README.md"
    )

    declared_skill_count = data.get("architecture", {}).get("skills")
    declared_agent_count = data.get("architecture", {}).get("sub_agents")

    if declared_skill_count != len(actual_skills):
        print(f"  Skill count mismatch: metadata={declared_skill_count}, fs={len(actual_skills)}")
        return False
    if declared_agent_count != len(actual_agents):
        print(f"  Agent count mismatch: metadata={declared_agent_count}, fs={len(actual_agents)}")
        return False

    print("  OK: metadata counts match filesystem")
    return True


def check_metadata_names() -> bool:
    print("\n[2/5] Checking metadata name integration...")
    data = load_json(METADATA)

    declared_skills = sorted(data.get("architecture", {}).get("skill_names", []))
    declared_agents = sorted(data.get("architecture", {}).get("sub_agent_names", []))

    actual_skills = sorted(
        d.name for d in SKILLS_DIR.iterdir() if d.is_dir() and (d / "SKILL.md").exists()
    )
    actual_agents = sorted(
        f.stem for f in AGENTS_DIR.glob("*.md") if f.name != "README.md"
    )

    ok = True
    if declared_skills != actual_skills:
        print(f"  Skill names mismatch:\n    metadata={declared_skills}\n    fs={actual_skills}")
        ok = False
    if declared_agents != actual_agents:
        print(f"  Agent names mismatch:\n    metadata={declared_agents}\n    fs={actual_agents}")
        ok = False

    if ok:
        print("  OK: metadata name lists match filesystem")
    return ok


def check_example_lifecycle_files() -> bool:
    print("\n[3/5] Checking example lifecycle references...")
    engagement_file = EXAMPLE_DIR / "engagement.json"
    if not engagement_file.exists():
        print("  [FAIL] examples/healthcare-ibmi-migration/engagement.json not found")
        return False

    engagement = load_json(engagement_file)
    lifecycle = engagement.get("lifecycle_state", {})
    missing = []

    for domain, entry in lifecycle.items():
        file_name = entry.get("file")
        if not file_name:
            missing.append(f"{domain}: missing file field")
            continue
        if not (EXAMPLE_DIR / file_name).exists():
            missing.append(f"{domain}: file '{file_name}' not found")

    if missing:
        for issue in missing:
            print(f"  {issue}")
        return False

    print("  OK: lifecycle_state file references resolve")
    return True


def check_example_engagement_ids() -> bool:
    print("\n[4/5] Checking example engagement_id consistency...")
    ids = {}
    for json_file in sorted(EXAMPLE_DIR.glob("*.json")):
        data = load_json(json_file)
        eid = data.get("engagement_id")
        if eid:
            ids[json_file.name] = eid

    if len(ids) < 2:
        print("  [SKIP] fewer than 2 files contain engagement_id")
        return True

    unique = set(ids.values())
    if len(unique) != 1:
        print("  Inconsistent engagement_id values:")
        for name, eid in ids.items():
            print(f"    {name}: {eid}")
        return False

    print(f"  OK: all example JSON files share engagement_id '{next(iter(unique))}'")
    return True


def check_example_status_presence() -> bool:
    print("\n[5/5] Checking example status/version fields...")
    issues = []

    for json_file in sorted(EXAMPLE_DIR.glob("*.json")):
        data = load_json(json_file)
        if "status" not in data:
            issues.append(f"{json_file.name}: missing status")
        if json_file.name != "engagement.json" and "version" not in data:
            issues.append(f"{json_file.name}: missing version")

    if issues:
        for issue in issues:
            print(f"  {issue}")
        return False

    print("  OK: example JSON files include status/version envelope fields")
    return True


def main() -> None:
    print("=" * 60)
    print("Integration Flow Validation")
    print("=" * 60)

    results = [
        check_metadata_counts(),
        check_metadata_names(),
        check_example_lifecycle_files(),
        check_example_engagement_ids(),
        check_example_status_presence(),
    ]

    passed = sum(1 for r in results if r)
    failed = sum(1 for r in results if not r)

    print("\n" + "=" * 60)
    print(f"Results: {passed} PASS, {failed} FAIL")
    print("=" * 60)

    if failed == 0:
        print("\nAll integration flow checks passed.")
        sys.exit(0)

    print("\nSome integration flow checks failed.")
    sys.exit(1)


if __name__ == "__main__":
    main()
