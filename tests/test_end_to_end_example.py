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


def main() -> None:
    print("=" * 60)
    print("End-to-End Example Validation")
    print("=" * 60)

    print("\n[1/2] Validating healthcare example files against schemas...")
    results = []
    for file_name, schema_name in SCHEMA_MAP.items():
        ok, detail = validate_file(file_name, schema_name)
        results.append(ok)
        prefix = "OK" if ok else "FAIL"
        print(f"  [{prefix}] {detail}")

    print("\n[2/2] Checking proposal artifact presence...")
    proposal_path = EXAMPLE_DIR / "proposal.md"
    if proposal_path.exists():
        print("  [OK] proposal.md present")
        results.append(True)
    else:
        print("  [FAIL] proposal.md missing")
        results.append(False)

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
