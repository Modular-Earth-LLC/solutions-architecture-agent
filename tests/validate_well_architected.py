#!/usr/bin/env python3
"""
Well-Architected Review Validator

Validates repository coverage for Well-Architected guidance:
  1. Architecture docs mention all 6 WA pillars
  2. system_config includes references to AWS WA + GenAI lens + Azure + GCP
  3. /architecture skill requires WA scoring and multi-cloud perspective
  4. parallel-wa-reviewer sub-agent supports all 6 pillar names

Usage:
    python tests/validate_well_architected.py
"""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
ARCH_DOC = REPO_ROOT / "ARCHITECTURE.md"
SYSTEM_CONFIG = REPO_ROOT / "knowledge_base" / "system_config.json"
ARCH_SKILL = REPO_ROOT / "skills" / "architecture" / "SKILL.md"
WA_AGENT = REPO_ROOT / "agents" / "parallel-wa-reviewer.md"

PILLARS = [
    "Operational Excellence",
    "Security",
    "Reliability",
    "Performance Efficiency",
    "Cost Optimization",
    "Sustainability",
]


def check_architecture_doc_pillars() -> bool:
    print("\n[1/4] Checking ARCHITECTURE.md pillar coverage...")
    if not ARCH_DOC.exists():
        print("  [FAIL] ARCHITECTURE.md not found")
        return False

    text = ARCH_DOC.read_text(encoding="utf-8")
    without_tags = re.sub(r"<[^>]+>", " ", text)
    normalized = re.sub(r"\s+", " ", without_tags)

    pillar_patterns = {
        "Operational Excellence": r"Operational\s+Excellence",
        "Security": r"Security",
        "Reliability": r"Reliability",
        "Performance Efficiency": r"Performance\s+Efficiency",
        "Cost Optimization": r"Cost\s+Optimization",
        "Sustainability": r"Sustainability",
    }
    missing = [
        pillar
        for pillar, pattern in pillar_patterns.items()
        if not re.search(pattern, normalized, re.IGNORECASE)
    ]

    if missing:
        print(f"  Missing pillars in ARCHITECTURE.md: {missing}")
        return False

    print("  OK: All 6 WA pillars referenced in ARCHITECTURE.md")
    return True


def check_system_config_framework_refs() -> bool:
    print("\n[2/4] Checking system_config framework references...")
    if not SYSTEM_CONFIG.exists():
        print("  [FAIL] knowledge_base/system_config.json not found")
        return False

    with open(SYSTEM_CONFIG, "r", encoding="utf-8") as f:
        data = json.load(f)

    refs = data.get("technical_references", {})
    aws = refs.get("aws_general", {})
    azure = refs.get("azure_openai", {})
    gcp = refs.get("google_vertex", {})

    issues = []
    if "well_architected_framework" not in aws:
        issues.append("aws_general.well_architected_framework missing")
    if "genai_lens" not in aws:
        issues.append("aws_general.genai_lens missing")
    if not azure:
        issues.append("azure_openai references missing")
    if not gcp:
        issues.append("google_vertex references missing")

    if issues:
        for issue in issues:
            print(f"  {issue}")
        return False

    print("  OK: AWS WA + GenAI lens + Azure + GCP references present")
    return True


def check_architecture_skill_wa_requirements() -> bool:
    print("\n[3/4] Checking /architecture skill WA requirements...")
    if not ARCH_SKILL.exists():
        print("  [FAIL] skills/architecture/SKILL.md not found")
        return False

    text = ARCH_SKILL.read_text(encoding="utf-8")

    checks = [
        (r"Well-Architected", "Well-Architected references"),
        (r"AWS", "AWS coverage"),
        (r"Azure", "Azure coverage"),
        (r"GCP|Google", "GCP coverage"),
        (r"0-10|score", "scoring guidance"),
    ]

    missing = []
    for pattern, label in checks:
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(label)

    if missing:
        print(f"  Missing in architecture skill: {missing}")
        return False

    print("  OK: /architecture skill includes WA multi-cloud scoring guidance")
    return True


def check_parallel_wa_agent_pillars() -> bool:
    print("\n[4/4] Checking parallel-wa-reviewer pillar support...")
    if not WA_AGENT.exists():
        print("  [FAIL] agents/parallel-wa-reviewer.md not found")
        return False

    text = WA_AGENT.read_text(encoding="utf-8")
    missing = [pillar for pillar in PILLARS if pillar not in text]

    if missing:
        print(f"  Missing pillar(s) in sub-agent prompt: {missing}")
        return False

    print("  OK: parallel-wa-reviewer enumerates all 6 pillar names")
    return True


def main() -> None:
    print("=" * 60)
    print("Well-Architected Validation")
    print("=" * 60)

    results = [
        check_architecture_doc_pillars(),
        check_system_config_framework_refs(),
        check_architecture_skill_wa_requirements(),
        check_parallel_wa_agent_pillars(),
    ]

    passed = sum(1 for r in results if r)
    failed = sum(1 for r in results if not r)

    print("\n" + "=" * 60)
    print(f"Results: {passed} PASS, {failed} FAIL")
    print("=" * 60)

    if failed == 0:
        print("\nAll Well-Architected checks passed.")
        sys.exit(0)

    print("\nSome Well-Architected checks failed.")
    sys.exit(1)


if __name__ == "__main__":
    main()
