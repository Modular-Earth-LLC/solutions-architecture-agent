#!/usr/bin/env python3
"""
Repository Consistency Validator

Validates cross-file consistency for the Solutions Architecture Agent:
  1. Metadata sync: skill/agent counts match .repo-metadata.json
  2. Schema completeness: every KB file has a corresponding schema
  3. $depends_on validation: verify dependency chains match authoritative DAG
  4. engagement_id consistency: all KB files use the same engagement_id
  5. ID uniqueness: no duplicate PREFIX-NNN IDs within each KB file

Usage:
    python tests/validate_consistency.py
"""

import json
import re
import sys
from pathlib import Path

# tests/ -> repo root
REPO_ROOT = Path(__file__).parent.parent
METADATA_FILE = REPO_ROOT / ".repo-metadata.json"
SCHEMA_DIR = REPO_ROOT / "knowledge_base" / "schemas"
KB_DIR = REPO_ROOT / "knowledge_base"

# Authoritative $depends_on DAG — minimum REQUIRED dependencies per skill.
# Skills may declare additional optional dependencies beyond these.
# The test validates that all required deps are present (superset check).
DEPENDS_ON_DAG = {
    "system_config": [],
    "engagement": [],  # entry point — reads system_config optionally but no hard deps
    "requirements": [],  # entry point — reads system_config optionally but no hard deps
    "architecture": ["requirements.json"],
    "data_model": ["requirements.json", "architecture.json"],
    "security_review": ["requirements.json", "architecture.json"],
    "integration_plan": ["requirements.json"],  # architecture.json optional (migration flow runs before architecture)
    "estimate": ["requirements.json", "architecture.json"],
    "project_plan": ["requirements.json", "architecture.json", "estimate.json"],
    # reviews has dynamic $depends_on — no fixed validation
}

# ID patterns to check for uniqueness
ID_PATTERNS = {
    "requirements": [r"SC-\d{3}", r"FR-\d{3}"],
    "architecture": [r"C-\d{3}", r"DF-\d{3}"],
    "data_model": [r"E-\d{3}"],
    "security_review": [r"T-\d{3}", r"F-\d{3}"],
    "integration_plan": [r"API-\d{3}", r"DFM-\d{3}"],
    "project_plan": [r"P-\d{3}", r"M-\d{3}"],
    "reviews": [r"R-\d{3}", r"RF-\d{3}"],
}


def check_metadata_sync() -> bool:
    """Check 1: Verify skill/agent counts match .repo-metadata.json."""
    print("\n[1/5] Checking metadata sync...")

    if not METADATA_FILE.exists():
        print("  [SKIP] .repo-metadata.json not found")
        return True

    with open(METADATA_FILE, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    issues = []

    # Count skills
    skills_dir = REPO_ROOT / "skills"
    skill_count = 0
    if skills_dir.exists():
        skill_count = sum(1 for d in skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists())

    expected_skills = metadata.get("architecture", {}).get("skills", 0)
    if skill_count != expected_skills:
        issues.append(f"  Skills: expected {expected_skills}, found {skill_count}")

    # Count sub-agents
    agents_dir = REPO_ROOT / "agents"
    agent_count = 0
    if agents_dir.exists():
        agent_count = sum(1 for f in agents_dir.glob("*.md") if f.name != "README.md")

    expected_agents = metadata.get("architecture", {}).get("sub_agents", 0)
    if agent_count != expected_agents:
        issues.append(f"  Sub-agents: expected {expected_agents}, found {agent_count}")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: {skill_count} skills, {agent_count} sub-agents match metadata")
        return True


def check_schema_completeness() -> bool:
    """Check 2: Verify every KB domain file has a corresponding schema."""
    print("\n[2/5] Checking schema completeness...")

    # Expected KB files (10 domain files)
    expected_kb = [
        "engagement", "requirements", "architecture", "data_model",
        "security_review", "integration_plan", "estimate", "project_plan",
        "reviews", "system_config"
    ]

    missing = []
    for name in expected_kb:
        schema_file = SCHEMA_DIR / f"{name}.schema.json"
        if not schema_file.exists():
            missing.append(name)

    # Also check .repo-metadata
    if not (SCHEMA_DIR / ".repo-metadata.schema.json").exists():
        missing.append(".repo-metadata")

    if missing:
        print(f"  Missing schemas: {', '.join(missing)}")
        return False
    else:
        print(f"  OK: All {len(expected_kb) + 1} schemas present")
        return True


def check_depends_on() -> bool:
    """Check 3: Verify $depends_on in existing KB files matches authoritative DAG."""
    print("\n[3/5] Checking $depends_on chains...")

    issues = []
    checked = 0

    # reviews.json has dynamic $depends_on — skip DAG check but log it
    for kb_file_candidate in [KB_DIR / "reviews.json"]:
        if kb_file_candidate.exists():
            print("  [INFO] reviews.json $depends_on is dynamic — skipping DAG check")

    for name, expected_deps in DEPENDS_ON_DAG.items():
        kb_file = KB_DIR / f"{name}.json"
        if not kb_file.exists():
            continue

        checked += 1
        try:
            with open(kb_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            issues.append(f"  {name}.json: failed to parse")
            continue

        actual_deps = data.get("$depends_on", [])

        # system_config has no $depends_on (it's the root)
        if name == "system_config":
            if actual_deps:
                issues.append(f"  system_config.json: should have no $depends_on, found {actual_deps}")
            continue

        # Superset check: actual deps must include all required deps (may include extras)
        actual_set = set(actual_deps)
        expected_set = set(expected_deps)
        missing_deps = expected_set - actual_set
        if missing_deps:
            issues.append(f"  {name}.json: missing required deps {sorted(missing_deps)}, found {actual_deps}")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: Checked {checked} existing KB files")
        return True


def check_engagement_id_consistency() -> bool:
    """Check 4: If 2+ KB files exist, verify they share the same engagement_id."""
    print("\n[4/5] Checking engagement_id consistency...")

    engagement_ids = {}
    kb_files = [
        "engagement", "requirements", "architecture", "data_model",
        "security_review", "integration_plan", "estimate", "project_plan",
        "reviews"
    ]

    for name in kb_files:
        kb_file = KB_DIR / f"{name}.json"
        if not kb_file.exists():
            continue

        try:
            with open(kb_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            continue

        eid = data.get("engagement_id")
        if eid:
            engagement_ids[name] = eid

    if len(engagement_ids) < 2:
        print(f"  [SKIP] Fewer than 2 KB files with engagement_id ({len(engagement_ids)} found)")
        return True

    unique_ids = set(engagement_ids.values())
    if len(unique_ids) > 1:
        print(f"  Inconsistent engagement_ids found:")
        for name, eid in engagement_ids.items():
            print(f"    {name}.json: {eid}")
        return False
    else:
        print(f"  OK: All {len(engagement_ids)} files share engagement_id '{list(unique_ids)[0]}'")
        return True


def _collect_id_values(obj: object, id_field_names: set[str]) -> list[str]:
    """Walk a parsed JSON structure and collect values from fields matching id_field_names."""
    results: list[str] = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in id_field_names and isinstance(value, str):
                results.append(value)
            else:
                results.extend(_collect_id_values(value, id_field_names))
    elif isinstance(obj, list):
        for item in obj:
            results.extend(_collect_id_values(item, id_field_names))
    return results


def check_id_uniqueness() -> bool:
    """Check 5: Within each KB file, verify no duplicate PREFIX-NNN IDs."""
    print("\n[5/5] Checking ID uniqueness...")

    issues = []
    checked = 0

    # Map each pattern to the JSON field names that hold those IDs
    id_field_for_pattern: dict[str, set[str]] = {
        r"SC-\d{3}": {"id"},
        r"FR-\d{3}": {"id"},
        r"C-\d{3}": {"id"},
        r"DF-\d{3}": {"id"},
        r"E-\d{3}": {"id"},
        r"T-\d{3}": {"id"},
        r"F-\d{3}": {"id"},
        r"API-\d{3}": {"id"},
        r"DFM-\d{3}": {"id"},
        r"P-\d{3}": {"id"},
        r"M-\d{3}": {"id"},
        r"R-\d{3}": {"review_id"},
        r"RF-\d{3}": {"id"},
    }

    for name, patterns in ID_PATTERNS.items():
        kb_file = KB_DIR / f"{name}.json"
        if not kb_file.exists():
            continue

        checked += 1
        try:
            with open(kb_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            continue

        for pattern in patterns:
            field_names = id_field_for_pattern.get(pattern, {"id"})
            all_ids = _collect_id_values(data, field_names)
            # Filter to only IDs matching this pattern
            compiled = re.compile(f"^{pattern}$")
            ids = [v for v in all_ids if compiled.match(v)]

            seen: dict[str, int] = {}
            for id_val in ids:
                seen[id_val] = seen.get(id_val, 0) + 1

            duplicates = {k: v for k, v in seen.items() if v > 1}
            if duplicates:
                for dup_id, count in duplicates.items():
                    issues.append(f"  {name}.json: duplicate ID '{dup_id}' ({count} occurrences)")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: Checked {checked} existing KB files, no duplicate IDs")
        return True


def main() -> None:
    print("=" * 60)
    print("Repository Consistency Validation")
    print("=" * 60)

    results = [
        check_metadata_sync(),
        check_schema_completeness(),
        check_depends_on(),
        check_engagement_id_consistency(),
        check_id_uniqueness(),
    ]

    print()
    print("=" * 60)
    passed = sum(1 for r in results if r)
    failed = sum(1 for r in results if not r)
    print(f"Results: {passed} PASS, {failed} FAIL")
    print("=" * 60)

    if all(results):
        print("All consistency checks passed.")
        sys.exit(0)
    else:
        print("Some checks failed — see details above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
