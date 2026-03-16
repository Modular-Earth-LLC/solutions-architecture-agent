#!/usr/bin/env python3
"""
Validate Knowledge Base JSON Files Against Schemas

Auto-discovers all .schema.json files in knowledge_base/schemas/ and validates
corresponding KB files against them. Uses Draft 2020-12 JSON Schema.

Usage:
    python tests/validate_knowledge_base.py
    python tests/validate_knowledge_base.py --file system_config
    python tests/validate_knowledge_base.py --verbose
"""

import argparse
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, ValidationError
except ImportError:
    print("[ERROR] jsonschema library not installed or version too old")
    print("Install with: pip install 'jsonschema>=4.17'")
    sys.exit(1)


# tests/ -> repo root
REPO_ROOT = Path(__file__).parent.parent
SCHEMA_DIR = REPO_ROOT / "knowledge_base" / "schemas"
KB_DIR = REPO_ROOT / "knowledge_base"


def discover_schemas() -> list[dict]:
    """Auto-discover all .schema.json files and map to their data files."""
    mappings: list[dict] = []
    for schema_file in sorted(SCHEMA_DIR.glob("*.schema.json")):
        stem = schema_file.stem  # e.g., "system_config.schema"
        name = stem.replace(".schema", "")  # e.g., "system_config"

        # Special case: .repo-metadata.schema.json -> .repo-metadata.json in repo root
        if name == ".repo-metadata":
            data_file = REPO_ROOT / ".repo-metadata.json"
        else:
            data_file = KB_DIR / f"{name}.json"

        mappings.append({
            "name": name,
            "schema_file": schema_file,
            "data_file": data_file,
        })

    return mappings


def validate_file(data_file: Path, schema_file: Path, verbose: bool = False) -> tuple[str, str]:
    """Validate a JSON data file against its schema using Draft202012Validator."""
    # Load schema
    try:
        with open(schema_file, "r", encoding="utf-8") as f:
            schema = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        return "FAIL", f"Failed to load schema: {e}"

    # Load data
    try:
        with open(data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return "FAIL", f"Invalid JSON: {e}"
    except FileNotFoundError:
        return "FAIL", f"Data file not found: {data_file}"

    # Validate with Draft 2020-12
    validator = Draft202012Validator(schema)
    errors = list(validator.iter_errors(data))

    if not errors:
        return "PASS", "Valid"

    # Format errors
    messages = []
    for err in errors:
        path = " -> ".join(str(p) for p in err.absolute_path) or "(root)"
        if verbose:
            messages.append(f"  Path: {path}\n  Error: {err.message}")
        else:
            messages.append(f"  [{path}] {err.message}")

    return "FAIL", "\n".join(messages)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate KB files against schemas")
    parser.add_argument("--file", help="Validate single file (e.g., --file system_config)")
    parser.add_argument("--verbose", action="store_true", help="Show detailed JSON paths")
    args = parser.parse_args()

    # Check we're in the right place
    if not SCHEMA_DIR.exists():
        print("[ERROR] Cannot find knowledge_base/schemas/ directory")
        print("Run from the project root directory.")
        sys.exit(1)

    all_mappings = discover_schemas()
    mappings = all_mappings

    # Filter if --file specified
    if args.file:
        mappings = [m for m in all_mappings if m["name"] == args.file]
        if not mappings:
            print(f"[ERROR] No schema found for '{args.file}'")
            print(f"Available: {', '.join(m['name'] for m in all_mappings)}")
            sys.exit(1)

    print("=" * 60)
    print("Knowledge Base Validation (Draft 2020-12)")
    print("=" * 60)
    print()

    results = []

    for mapping in mappings:
        name = mapping["name"]
        schema_file = mapping["schema_file"]
        data_file = mapping["data_file"]

        print(f"  {name}:")

        # Check if data file exists — SKIP gracefully if not
        if not data_file.exists():
            print(f"    [SKIP] {data_file.name} does not exist (created at runtime)")
            results.append(("SKIP", name))
            print()
            continue

        status, message = validate_file(data_file, schema_file, args.verbose)
        if status == "PASS":
            print(f"    [PASS] {message}")
        else:
            print(f"    [FAIL]")
            for line in message.split("\n"):
                print(f"    {line}")

        results.append((status, name))
        print()

    # Summary
    passed = sum(1 for s, _ in results if s == "PASS")
    failed = sum(1 for s, _ in results if s == "FAIL")
    skipped = sum(1 for s, _ in results if s == "SKIP")

    print("=" * 60)
    print(f"Results: {passed} PASS, {failed} FAIL, {skipped} SKIP")
    print("=" * 60)

    if failed > 0:
        print("\nFailed files:")
        for status, name in results:
            if status == "FAIL":
                print(f"  - {name}")
        sys.exit(1)
    else:
        print("\nAll validated files passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
