#!/usr/bin/env python3
"""
Engagement Flow Validator

Static validation of engagement lifecycle logic:
  1. Canonical flow DAG validity — predecessors appear earlier in each flow
  2. Engagement schema lifecycle coverage — all domain KB files tracked
  3. Status enum consistency — lifecycle_entry status enum matches SKILL.md references
  4. ARCHITECTURE.md DAG cross-reference — KB ownership matches DEPENDS_ON_DAG
  5. Prerequisite directive coverage — skills with $depends_on have prerequisite language

Usage:
    python tests/test_engagement_flow.py
"""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SCHEMA_DIR = REPO_ROOT / "knowledge_base" / "schemas"
SKILLS_DIR = REPO_ROOT / "skills"

# Import DEPENDS_ON_DAG from validate_consistency.py
sys.path.insert(0, str(Path(__file__).parent))
from validate_consistency import DEPENDS_ON_DAG

# Canonical flows from CLAUDE.md — skill abbreviations mapped to KB file names
SKILL_ABBREV = {
    "req": "requirements",
    "arch": "architecture",
    "dm": "data_model",
    "sr": "security_review",
    "ip": "integration_plan",
    "est": "estimate",
    "ppl": "project_plan",
    "pro": "proposal",
    "rv": "reviews",
}

# Canonical flows (from CLAUDE.md). Brackets mean optional.
CANONICAL_FLOWS = {
    "greenfield":  ["req", "arch", "dm", "sr", "est", "ppl", "pro", "rv"],
    "migration":   ["req", "ip", "arch", "dm", "sr", "est", "ppl", "pro", "rv"],
    "streamlined": ["req", "arch", "est", "pro"],
    "assessment":  ["req", "arch", "sr", "pro"],  # sr is optional but valid
    "quick_qualify": ["req"],
}

# Skills that own KB files (proposal writes to outputs/, not KB)
SKILL_TO_KB = {
    "requirements": "requirements",
    "architecture": "architecture",
    "data-model": "data_model",
    "security-review": "security_review",
    "integration-plan": "integration_plan",
    "estimate": "estimate",
    "project-plan": "project_plan",
    "review": "reviews",
}

# Expected lifecycle_state properties in engagement.schema.json
EXPECTED_LIFECYCLE_DOMAINS = {
    "requirements", "architecture", "data_model", "security_review",
    "integration_plan", "estimate", "project_plan",
}


def check_flow_dag_validity() -> bool:
    """Check 1: For each canonical flow, verify that every skill's $depends_on
    predecessors appear earlier in the flow (or are not in the flow at all)."""
    print("\n[1/5] Checking canonical flow DAG validity...")

    issues = []

    for flow_name, flow_abbrevs in CANONICAL_FLOWS.items():
        flow_kb_names = [SKILL_ABBREV[a] for a in flow_abbrevs]

        for i, kb_name in enumerate(flow_kb_names):
            if kb_name not in DEPENDS_ON_DAG:
                continue  # proposal/reviews have dynamic deps

            deps = DEPENDS_ON_DAG[kb_name]
            predecessors_in_flow = set(flow_kb_names[:i])

            for dep in deps:
                dep_name = dep.replace(".json", "")
                # system_config is always available (not a flow step)
                if dep_name == "system_config":
                    continue
                # Dep must either appear before this skill in the flow,
                # or not be part of this flow at all (optional skip)
                if dep_name in [SKILL_ABBREV[a] for a in flow_abbrevs]:
                    if dep_name not in predecessors_in_flow:
                        issues.append(
                            f"  {flow_name}: {kb_name} depends on {dep_name}, "
                            f"but {dep_name} appears at or after {kb_name}"
                        )

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All {len(CANONICAL_FLOWS)} canonical flows have valid DAG ordering")
        return True


def check_lifecycle_coverage() -> bool:
    """Check 2: engagement.schema.json lifecycle_state covers all domain KB files."""
    print("\n[2/5] Checking engagement schema lifecycle coverage...")

    schema_file = SCHEMA_DIR / "engagement.schema.json"
    if not schema_file.exists():
        print("  [SKIP] engagement.schema.json not found")
        return True

    with open(schema_file, "r", encoding="utf-8") as f:
        schema = json.load(f)

    lifecycle_props = set(
        schema.get("properties", {})
        .get("lifecycle_state", {})
        .get("properties", {})
        .keys()
    )

    missing = EXPECTED_LIFECYCLE_DOMAINS - lifecycle_props
    extra = lifecycle_props - EXPECTED_LIFECYCLE_DOMAINS

    issues = []
    if missing:
        issues.append(f"  Missing from schema: {sorted(missing)}")
    if extra:
        issues.append(f"  Extra in schema (not expected): {sorted(extra)}")

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All {len(EXPECTED_LIFECYCLE_DOMAINS)} domain files covered in lifecycle_state")
        return True


def check_status_enum_consistency() -> bool:
    """Check 3: lifecycle_entry status enum includes all statuses referenced in SKILL.md files."""
    print("\n[3/5] Checking status enum consistency...")

    schema_file = SCHEMA_DIR / "engagement.schema.json"
    if not schema_file.exists():
        print("  [SKIP] engagement.schema.json not found")
        return True

    with open(schema_file, "r", encoding="utf-8") as f:
        schema = json.load(f)

    # Get status enum from $defs/lifecycle_entry
    lifecycle_entry = schema.get("$defs", {}).get("lifecycle_entry", {})
    status_enum = set(
        lifecycle_entry.get("properties", {}).get("status", {}).get("enum", [])
    )

    if not status_enum:
        print("  [FAIL] Could not find lifecycle_entry status enum")
        return False

    # Scan SKILL.md files for status references
    status_refs = set()
    status_pattern = re.compile(
        r'(?:status|lifecycle_state).*?(?:`|"|\')'
        r'(not_started|in_progress|draft|complete|approved)'
        r'(?:`|"|\')',
        re.IGNORECASE,
    )

    for skill_dir in sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            continue
        text = skill_file.read_text(encoding="utf-8")
        for match in status_pattern.finditer(text):
            status_refs.add(match.group(1))

    unreferenced_in_schema = status_refs - status_enum
    if unreferenced_in_schema:
        print(f"  SKILL.md references statuses not in schema enum: {sorted(unreferenced_in_schema)}")
        return False

    print(f"  OK: Schema enum {sorted(status_enum)} covers all SKILL.md references")
    return True


def check_architecture_dag_crossref() -> bool:
    """Check 4: ARCHITECTURE.md KB ownership table matches DEPENDS_ON_DAG."""
    print("\n[4/5] Checking ARCHITECTURE.md DAG cross-reference...")

    arch_file = REPO_ROOT / "ARCHITECTURE.md"
    if not arch_file.exists():
        print("  [SKIP] ARCHITECTURE.md not found")
        return True

    text = arch_file.read_text(encoding="utf-8")

    # Extract "Depends On" column from the KB File Ownership table
    # Table format: | Skill | Owns | Depends On |
    issues = []
    table_pattern = re.compile(
        r'\|\s*(\w[\w\s&]*?)\s*\|\s*`(\w+\.json)`\s*\|\s*([^|]*)\|',
    )

    found_mappings = {}
    for match in table_pattern.finditer(text):
        kb_file = match.group(2).replace(".json", "")
        deps_text = match.group(3).strip()

        if deps_text == "--" or not deps_text:
            found_mappings[kb_file] = []
        else:
            deps = [
                d.strip().strip("`").replace(".json", "")
                for d in re.split(r'[,;]|\band\b', deps_text)
                if d.strip() and d.strip() != "--"
            ]
            # Filter out parenthetical notes and empty strings
            deps = [d for d in deps if d and not d.startswith("(")]
            found_mappings[kb_file] = deps

    if not found_mappings:
        print("  [SKIP] Could not parse KB ownership table from ARCHITECTURE.md")
        return True

    # Cross-reference with DEPENDS_ON_DAG
    for kb_name, dag_deps in DEPENDS_ON_DAG.items():
        if kb_name not in found_mappings:
            continue  # Not all DAG entries need to be in the table

        dag_dep_names = sorted(d.replace(".json", "") for d in dag_deps)
        arch_dep_names = sorted(found_mappings[kb_name])

        # Loose comparison — ARCHITECTURE.md may list optional deps
        for dep in dag_dep_names:
            if dep == "system_config":
                continue  # Often omitted from the table
            if dep not in arch_dep_names:
                issues.append(
                    f"  {kb_name}: DAG requires {dep}, "
                    f"not found in ARCHITECTURE.md table"
                )

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: ARCHITECTURE.md table consistent with DEPENDS_ON_DAG ({len(found_mappings)} entries)")
        return True


def check_prerequisite_directives() -> bool:
    """Check 5: Every skill with $depends_on has prerequisite-checking language."""
    print("\n[5/5] Checking prerequisite directive coverage...")

    issues = []
    prerequisite_keywords = re.compile(
        r'prerequisit|depends.on|upstream|required.*before|validate.*before|'
        r'must.*complete|check.*exist|entry.point|no.*upstream',
        re.IGNORECASE,
    )

    for skill_dir_name, kb_name in SKILL_TO_KB.items():
        # Skip skills with no fixed dependencies
        if kb_name not in DEPENDS_ON_DAG:
            continue
        if not DEPENDS_ON_DAG[kb_name]:
            continue  # No deps (system_config only doesn't count)
        non_sysconfig_deps = [
            d for d in DEPENDS_ON_DAG[kb_name] if d != "system_config.json"
        ]
        if not non_sysconfig_deps:
            continue

        skill_file = SKILLS_DIR / skill_dir_name / "SKILL.md"
        if not skill_file.exists():
            issues.append(f"  {skill_dir_name}: SKILL.md not found")
            continue

        text = skill_file.read_text(encoding="utf-8")
        if not prerequisite_keywords.search(text):
            issues.append(
                f"  {skill_dir_name}: has dependencies {non_sysconfig_deps} "
                f"but no prerequisite-checking language in SKILL.md"
            )

    if issues:
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  OK: All skills with dependencies include prerequisite directives")
        return True


def main() -> None:
    print("=" * 60)
    print("Engagement Flow Validation")
    print("=" * 60)

    results = [
        check_flow_dag_validity(),
        check_lifecycle_coverage(),
        check_status_enum_consistency(),
        check_architecture_dag_crossref(),
        check_prerequisite_directives(),
    ]

    passed = sum(1 for r in results if r)
    failed = sum(1 for r in results if not r)

    print()
    print("=" * 60)
    print(f"Results: {passed} PASS, {failed} FAIL")
    print("=" * 60)

    if all(results):
        print("\nAll engagement flow checks passed.")
        sys.exit(0)
    else:
        print("\nSome checks failed — see details above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
