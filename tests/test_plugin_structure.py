#!/usr/bin/env python3
"""
Plugin Structure Validator

Validates the Claude Code plugin packaging:
  1. plugin.json exists, valid JSON, required fields, version matches .repo-metadata.json
  2. Every skills/*/ has SKILL.md with YAML frontmatter (name, description, allowed-tools)
  3. Skill name in frontmatter matches directory name
  4. Agent files in agents/*.md have YAML frontmatter (name, description, tools, model, maxTurns)
  5. Required directories exist
  6. No SKILL.md contains forbidden patterns
  7. No SKILL.md exceeds 500 lines
  8. .repo-metadata.json skill_names/sub_agent_names match filesystem

Usage:
    python tests/test_plugin_structure.py
"""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PLUGIN_JSON = REPO_ROOT / ".claude-plugin" / "plugin.json"
METADATA_FILE = REPO_ROOT / ".repo-metadata.json"
SKILLS_DIR = REPO_ROOT / "skills"
AGENTS_DIR = REPO_ROOT / "agents"

REQUIRED_DIRS = [
    ".claude-plugin",
    "skills",
    "agents",
    "hooks",
    "knowledge_base/schemas",
]

REQUIRED_PLUGIN_FIELDS = ["name", "version", "description"]

REQUIRED_SKILL_FRONTMATTER = ["name", "description", "allowed-tools"]
REQUIRED_AGENT_FRONTMATTER = ["name", "description", "tools", "model", "maxTurns"]

FORBIDDEN_SKILL_PATTERNS = [
    (r"context:\s*fork", "context: fork (Decision 1: no forking)"),
    (r"\$ARGUMENTS\.0", "$ARGUMENTS.0 dot syntax (use bracket syntax)"),
    (r"allowed-tools:.*\bTask\b", "Task in allowed-tools (renamed to Agent)"),
]

MAX_SKILL_LINES = 500

REQUIRED_SKILL_SECTIONS = [
    "ROLE & CONTEXT",
    "PREREQUISITES",
    "CONTEXT LOADING",
    "WORKFLOW",
    "OUTPUT",
]


def parse_yaml_frontmatter(filepath: Path) -> dict | None:
    """Parse simple YAML frontmatter (key: value pairs) from a markdown file."""
    try:
        text = filepath.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None

    if not text.startswith("---"):
        return None

    end = text.find("---", 3)
    if end == -1:
        return None

    frontmatter = {}
    for line in text[3:end].strip().split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.match(r'^([a-zA-Z_-]+):\s*(.+)$', line)
        if match:
            key = match.group(1)
            value = match.group(2).strip().strip('"').strip("'")
            frontmatter[key] = value

    return frontmatter


def check_plugin_json() -> tuple[bool, str]:
    """Check 1: plugin.json exists, valid JSON, required fields, version matches."""
    if not PLUGIN_JSON.exists():
        return False, f"{PLUGIN_JSON.relative_to(REPO_ROOT)} not found"

    try:
        with open(PLUGIN_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"

    missing = [f for f in REQUIRED_PLUGIN_FIELDS if f not in data]
    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"

    # Version must match .repo-metadata.json
    if METADATA_FILE.exists():
        with open(METADATA_FILE, "r", encoding="utf-8") as f:
            metadata = json.load(f)
        if data.get("version") != metadata.get("version"):
            return False, (
                f"Version mismatch: plugin.json={data.get('version')}, "
                f".repo-metadata.json={metadata.get('version')}"
            )

    return True, "Valid"


def check_skill_frontmatter() -> tuple[bool, list[str]]:
    """Check 2-3: Every skill has SKILL.md with required frontmatter, name matches dir."""
    issues = []
    skill_dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())

    if not skill_dirs:
        return False, ["No skill directories found"]

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        dir_name = skill_dir.name

        if not skill_file.exists():
            issues.append(f"{dir_name}/SKILL.md not found")
            continue

        fm = parse_yaml_frontmatter(skill_file)
        if fm is None:
            issues.append(f"{dir_name}/SKILL.md missing YAML frontmatter")
            continue

        missing = [f for f in REQUIRED_SKILL_FRONTMATTER if f not in fm]
        if missing:
            issues.append(f"{dir_name}: missing frontmatter fields: {', '.join(missing)}")

        # Check name matches directory
        if fm.get("name") != dir_name:
            issues.append(f"{dir_name}: frontmatter name='{fm.get('name')}' != dir name='{dir_name}'")

    return len(issues) == 0, issues


def check_agent_frontmatter() -> tuple[bool, list[str]]:
    """Check 4: Agent files have required YAML frontmatter."""
    issues = []
    agent_files = sorted(f for f in AGENTS_DIR.glob("*.md") if f.name != "README.md")

    if not agent_files:
        return False, ["No agent files found"]

    for agent_file in agent_files:
        name = agent_file.stem
        fm = parse_yaml_frontmatter(agent_file)
        if fm is None:
            issues.append(f"{name}: missing YAML frontmatter")
            continue

        missing = [f for f in REQUIRED_AGENT_FRONTMATTER if f not in fm]
        if missing:
            issues.append(f"{name}: missing frontmatter fields: {', '.join(missing)}")

    return len(issues) == 0, issues


def check_required_dirs() -> tuple[bool, list[str]]:
    """Check 5: Required directories exist."""
    missing = []
    for d in REQUIRED_DIRS:
        if not (REPO_ROOT / d).exists():
            missing.append(d)
    return len(missing) == 0, missing


def check_forbidden_patterns() -> tuple[bool, list[str]]:
    """Check 6: No SKILL.md contains forbidden patterns."""
    issues = []
    for skill_dir in sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            continue

        text = skill_file.read_text(encoding="utf-8")
        for pattern, description in FORBIDDEN_SKILL_PATTERNS:
            if re.search(pattern, text):
                issues.append(f"{skill_dir.name}: contains {description}")

    return len(issues) == 0, issues


def check_skill_line_count() -> tuple[bool, list[str]]:
    """Check 7: No SKILL.md exceeds 500 lines."""
    issues = []
    for skill_dir in sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            continue

        line_count = len(skill_file.read_text(encoding="utf-8").splitlines())
        if line_count > MAX_SKILL_LINES:
            issues.append(f"{skill_dir.name}: {line_count} lines (max {MAX_SKILL_LINES})")

    return len(issues) == 0, issues


def check_skill_section_anchors() -> tuple[bool, list[str]]:
    """Check 8: Every SKILL.md contains required section anchors."""
    issues = []
    for skill_dir in sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            continue

        text = skill_file.read_text(encoding="utf-8")
        for section in REQUIRED_SKILL_SECTIONS:
            if section not in text:
                issues.append(f"{skill_dir.name}: missing section '{section}'")

    return len(issues) == 0, issues


def check_metadata_names() -> tuple[bool, list[str]]:
    """Check 9: .repo-metadata.json skill_names/sub_agent_names match filesystem."""
    issues = []

    if not METADATA_FILE.exists():
        return True, []  # Skip if no metadata

    with open(METADATA_FILE, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    arch = metadata.get("architecture", {})

    # Skill names
    declared_skills = set(arch.get("skill_names", []))
    actual_skills = set(
        d.name for d in SKILLS_DIR.iterdir()
        if d.is_dir() and (d / "SKILL.md").exists()
    )
    if declared_skills != actual_skills:
        only_declared = declared_skills - actual_skills
        only_actual = actual_skills - declared_skills
        if only_declared:
            issues.append(f"skill_names in metadata but not on disk: {sorted(only_declared)}")
        if only_actual:
            issues.append(f"Skills on disk but not in metadata: {sorted(only_actual)}")

    # Sub-agent names
    declared_agents = set(arch.get("sub_agent_names", []))
    actual_agents = set(
        f.stem for f in AGENTS_DIR.glob("*.md") if f.name != "README.md"
    )
    if declared_agents != actual_agents:
        only_declared = declared_agents - actual_agents
        only_actual = actual_agents - declared_agents
        if only_declared:
            issues.append(f"sub_agent_names in metadata but not on disk: {sorted(only_declared)}")
        if only_actual:
            issues.append(f"Agents on disk but not in metadata: {sorted(only_actual)}")

    return len(issues) == 0, issues


def main() -> None:
    print("=" * 60)
    print("Plugin Structure Validation")
    print("=" * 60)

    checks = [
        ("plugin.json validity", check_plugin_json),
        ("Skill SKILL.md frontmatter", check_skill_frontmatter),
        ("Agent frontmatter", check_agent_frontmatter),
        ("Required directories", check_required_dirs),
        ("Forbidden patterns", check_forbidden_patterns),
        ("SKILL.md line count", check_skill_line_count),
        ("Metadata name sync", check_metadata_names),
        ("Skill section anchors", check_skill_section_anchors),
    ]

    results = []
    for i, (name, check_fn) in enumerate(checks, 1):
        print(f"\n  [{i}/{len(checks)}] {name}:")
        passed, detail = check_fn()

        if passed:
            if isinstance(detail, str):
                print(f"    [PASS] {detail}")
            else:
                print(f"    [PASS]")
        else:
            print(f"    [FAIL]")
            if isinstance(detail, str):
                print(f"    {detail}")
            elif isinstance(detail, list):
                for item in detail:
                    print(f"    - {item}")

        results.append(passed)

    passed = sum(1 for r in results if r)
    failed = sum(1 for r in results if not r)

    print()
    print("=" * 60)
    print(f"Results: {passed} PASS, {failed} FAIL")
    print("=" * 60)

    if all(results):
        print("\nAll plugin structure checks passed.")
        sys.exit(0)
    else:
        print("\nSome checks failed — see details above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
