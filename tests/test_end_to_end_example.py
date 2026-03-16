#!/usr/bin/env python3
"""
End-to-End Example Validator

Runs schema validation end-to-end for the healthcare example package.
This verifies generated artifacts align with repository schema contracts.

Usage:
    python tests/test_end_to_end_example.py
"""

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("Error: jsonschema library not installed. Run: pip install jsonschema")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent
EXAMPLE_DIR = REPO_ROOT / "examples" / "healthcare-ibmi-migration"
SCHEMA_DIR = REPO_ROOT / "knowledge_base" / "schemas"

SCHEMA_MAP = {
    "engagement.json": "engagement.schema.json",
    "requirements.json": "requirements.schema.json",
    "architecture.json": "architecture.schema.json",
    "data_model.json": "data_model.schema.json",
    "security_review.json": "security_review.schema.json",
    "integration_plan.json": "integration_plan.schema.json",
    "estimate.json": "estimate.schema.json",
    "project_plan.json": "project_plan.schema.json",
    "reviews.json": "reviews.schema.json",
}


def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_file(file_name: str, schema_name: str) -> tuple[bool, str]:
    data_path = EXAMPLE_DIR / file_name
    schema_path = SCHEMA_DIR / schema_name

    if not data_path.exists():
        return False, f"{file_name} missing"
    if not schema_path.exists():
        return False, f"Schema {schema_name} missing"

    instance = load_json(data_path)
    schema = load_json(schema_path)

    try:
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(instance), key=lambda e: str(e.path))
        if errors:
            msg = errors[0]
            path = ".".join(str(p) for p in msg.path) or "<root>"
            return False, f"{file_name}: {path} -> {msg.message}"
    except Exception as e:
        return False, f"{file_name}: validator error ({e})"

    return True, f"{file_name}: valid"


def check_lifecycle_file_references() -> tuple[bool, str]:
    """Check that engagement.json lifecycle_state file references resolve."""
    engagement_file = EXAMPLE_DIR / "engagement.json"
    if not engagement_file.exists():
        return False, "engagement.json missing"

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
        return False, "; ".join(missing)
    return True, "lifecycle_state file references resolve"


def check_engagement_id_consistency() -> tuple[bool, str]:
    """Check that all example JSON files share one engagement_id."""
    ids = {}
    for json_file in sorted(EXAMPLE_DIR.glob("*.json")):
        data = load_json(json_file)
        eid = data.get("engagement_id")
        if eid:
            ids[json_file.name] = eid

    if len(ids) < 2:
        return True, "fewer than 2 files with engagement_id (skip)"

    unique = set(ids.values())
    if len(unique) != 1:
        details = ", ".join(f"{n}={e}" for n, e in ids.items())
        return False, f"inconsistent engagement_ids: {details}"

    return True, f"all files share engagement_id '{next(iter(unique))}'"


def check_status_version_fields() -> tuple[bool, str]:
    """Check that example JSON files include status and version envelope fields."""
    issues = []
    for json_file in sorted(EXAMPLE_DIR.glob("*.json")):
        data = load_json(json_file)
        if "status" not in data:
            issues.append(f"{json_file.name}: missing status")
        if json_file.name != "engagement.json" and "version" not in data:
            issues.append(f"{json_file.name}: missing version")

    if issues:
        return False, "; ".join(issues)
    return True, "all example files have status/version envelope fields"


def main() -> None:
    print("=" * 60)
    print("End-to-End Example Validation")
    print("=" * 60)

    print("\n[1/5] Validating healthcare example files against schemas...")
    results = []
    for file_name, schema_name in SCHEMA_MAP.items():
        ok, detail = validate_file(file_name, schema_name)
        results.append(ok)
        prefix = "OK" if ok else "FAIL"
        print(f"  [{prefix}] {detail}")

    print("\n[2/5] Checking proposal artifact presence...")
    proposal_path = EXAMPLE_DIR / "proposal.md"
    if proposal_path.exists():
        print("  [OK] proposal.md present")
        results.append(True)
    else:
        print("  [FAIL] proposal.md missing")
        results.append(False)

    extra_checks = [
        ("[3/5] Lifecycle file references", check_lifecycle_file_references),
        ("[4/5] Engagement ID consistency", check_engagement_id_consistency),
        ("[5/5] Status/version envelope fields", check_status_version_fields),
    ]

    for label, check_fn in extra_checks:
        print(f"\n{label}...")
        ok, detail = check_fn()
        results.append(ok)
        prefix = "OK" if ok else "FAIL"
        print(f"  [{prefix}] {detail}")

    passed = sum(1 for r in results if r)
    failed = sum(1 for r in results if not r)

    print("\n" + "=" * 60)
    print(f"Results: {passed} PASS, {failed} FAIL")
    print("=" * 60)

    if failed == 0:
        print("\nAll end-to-end example checks passed.")
        sys.exit(0)

    print("\nEnd-to-end validation found failures.")
    sys.exit(1)


if __name__ == "__main__":
    main()
