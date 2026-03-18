# Phase 6: Enhancements (Optional)

**Goal:** Implement nice-to-have features: brand compliance checks, regulatory content checks, and approval status tracking in pipeline manifests.

**This phase is OPTIONAL.** Only start if Phase 5 is fully complete and there is at least 2 hours of work time remaining before the interview.

**Minimum state after this phase:** Brand and regulatory compliance sections present in pipeline manifest. `/pipeline-status` shows compliance column.

---

## Prerequisites Checklist

- [ ] `phase-05-complete.md` exists — repo published, README complete, CI/CD green, v1.0.0 tagged
- [ ] `github.com/praeducer/pai-take-home-exercise` is demo-ready (verified by Paul)
- [ ] At least 2 hours of time before interview
- [ ] All Phase 1-5 tests still passing: `pytest tests/ -v -m "not integration"`

**Load prior context:** Read `phase-01-complete.md` through `phase-05-complete.md`. Phase 6 enhancements should not break any existing functionality.

---

## Architecture Decisions for This Phase

| Decision | Value |
|---------|-------|
| Brand checks | Claude Sonnet 4.6 (LLM-as-judge) via AnthropicBedrock — evaluates image against brand rules in SKU brief |
| Regulatory checks | Synthesized JSON lookup table in `data/regulatory_requirements.json` by region — no real compliance DB |
| Approval tracking | Appended to `manifest.json` (E-006) — no separate database |
| Honesty | Document clearly in README that regulatory data is synthesized/illustrative, not authoritative |

---

## Tasks

### Task 1: Brand Compliance Check (`src/pipeline/brand_checker.py`)

```python
import json
import io
import base64
from anthropic import AnthropicBedrock

def check_brand_compliance(
    image_bytes: bytes,
    brief: dict,
    client: AnthropicBedrock,
    dry_run: bool = False
) -> dict:
    """
    Use Claude Sonnet 4.6 as LLM-as-judge to evaluate brand compliance.
    Returns: {compliant: bool, issues: list[str], confidence: float}
    """
    if dry_run:
        return {"compliant": True, "issues": [], "confidence": 0.0, "dry_run": True}

    # Encode image for multimodal input
    image_b64 = base64.standard_b64encode(image_bytes).decode("utf-8")
    product_name = brief.get("products", [{}])[0].get("name", "Unknown Product")
    attributes = ", ".join(brief.get("attributes", []))

    try:
        message = client.messages.create(
            model="anthropic.claude-sonnet-4-6",
            max_tokens=512,
            system=(
                "You are a brand compliance reviewer. Evaluate the packaging image against "
                "the brand requirements. Return ONLY a JSON object with keys: "
                "'compliant' (bool), 'issues' (list of strings), 'confidence' (float 0-1). "
                "Do not include any text outside the JSON."
            ),
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": image_b64
                        }
                    },
                    {
                        "type": "text",
                        "text": (
                            f"Brand requirements:\n"
                            f"- Product: {product_name}\n"
                            f"- Required attributes visible: {attributes}\n"
                            f"- Background should be clean (white or light)\n"
                            f"- Text must be legible\n\n"
                            f"Evaluate this packaging image for brand compliance."
                        )
                    }
                ]
            }]
        )
        result = json.loads(message.content[0].text)
        return {
            "compliant": bool(result.get("compliant", False)),
            "issues": result.get("issues", []),
            "confidence": float(result.get("confidence", 0.5))
        }
    except Exception as e:
        return {"compliant": None, "issues": [str(e)], "confidence": 0.0, "error": True}
```

**Acceptance:** `check_brand_compliance(image_bytes, brief, client, dry_run=True)` returns `{compliant: True, issues: [], confidence: 0.0}`. Real call returns structured JSON with `compliant`, `issues`, `confidence` keys.

---

### Task 2: Regulatory Content Check (`src/pipeline/regulatory_checker.py`)

Create `data/regulatory_requirements.json`:

```json
{
  "us-west": {
    "required_disclosures": ["allergen_statement", "nutrition_facts"],
    "required_certifications": ["USDA Organic"],
    "mandatory_languages": ["en"],
    "notes": "FDA regulations apply. Synthesized for PoC — not authoritative."
  },
  "latam": {
    "required_disclosures": ["allergen_statement", "nutrition_facts", "country_of_origin"],
    "required_certifications": [],
    "mandatory_languages": ["es"],
    "notes": "Synthesized LATAM regulatory requirements. Not authoritative."
  },
  "apac": {
    "required_disclosures": ["allergen_statement", "nutrition_facts", "expiry_date"],
    "required_certifications": [],
    "mandatory_languages": ["en"],
    "notes": "Synthesized APAC requirements. Not authoritative."
  },
  "eu": {
    "required_disclosures": ["allergen_statement", "nutrition_facts", "country_of_origin", "recycling_info"],
    "required_certifications": [],
    "mandatory_languages": ["en", "de", "fr"],
    "notes": "Synthesized EU regulations (not real EU Regulation 1169/2011). Not authoritative."
  }
}
```

```python
import json
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent.parent / "data" / "regulatory_requirements.json"

def check_regulatory_content(text_content: dict, region: str) -> dict:
    """
    Check if text overlay content includes required regulatory elements for the region.
    Returns: {compliant: bool, missing_items: list[str], region: str}
    """
    try:
        requirements = json.loads(DATA_PATH.read_text())
    except FileNotFoundError:
        return {"compliant": None, "missing_items": ["regulatory_requirements.json not found"], "region": region}

    region_reqs = requirements.get(region, requirements.get("us-west", {}))
    required = region_reqs.get("required_disclosures", [])

    regulatory_text = text_content.get("regulatory_text", "").lower()
    missing = []

    if "allergen_statement" in required:
        if not any(word in regulatory_text for word in ["contains", "allergen", "nuts", "wheat", "dairy", "soy"]):
            missing.append("allergen_statement — text should mention allergen information")

    if "nutrition_facts" in required:
        if not any(word in regulatory_text for word in ["nutrition", "calories", "ingredients", "see", "information"]):
            missing.append("nutrition_facts — text should reference nutrition information")

    return {
        "compliant": len(missing) == 0,
        "missing_items": missing,
        "region": region,
        "requirements_checked": required,
        "disclaimer": region_reqs.get("notes", "Synthesized data — not authoritative.")
    }
```

**Acceptance:** `check_regulatory_content(content, "eu")` returns `missing_items` listing unchecked requirements when regulatory text is minimal. For content with "Contains: See ingredients list", allergen_statement check passes.

---

### Task 3: Add Compliance Checks to Pipeline

Update `run_pipeline.py` to run compliance checks after text overlay:

```python
from .brand_checker import check_brand_compliance
from .regulatory_checker import check_regulatory_content

# In the per-product × per-ratio loop, after apply_overlay:
overlay_content = build_text_overlay_content(brief, product)
composited = apply_overlay(image_bytes, overlay_content, aspect_ratio)

# Compliance checks
brand_result = check_brand_compliance(composited, brief, text_client, dry_run)
regulatory_result = check_regulatory_content(overlay_content, region)

# Store compliance results per image
compliance_results.append({
    "product": product["name"],
    "aspect_ratio": aspect_ratio,
    "brand": brand_result,
    "regulatory": regulatory_result
})
```

Update `write_manifest` to include compliance section:
```python
manifest["compliance"] = {
    "results": compliance_results,
    "overall_brand_compliant": all(r["brand"].get("compliant") for r in compliance_results),
    "overall_regulatory_compliant": all(r["regulatory"]["compliant"] for r in compliance_results)
}
```

**Acceptance:** Pipeline run manifest includes `compliance` key with `results` array and overall status flags.

---

### Task 4: Update `/pipeline-status` Skill to Show Compliance

Update the pipeline-status skill to display a compliance column:

```
2026-03-18T14:30:00 | organic-trail-mix-us          | 6 imgs | REAL | ✓ | BRAND: PASS | REG: PASS
2026-03-18T14:00:00 | granola-bar-latam              | 6 imgs | REAL | ✓ | BRAND: PASS | REG: WARN(1)
```

**Acceptance:** `/pipeline-status` output includes brand and regulatory status columns.

---

### Task 5: Write Tests for New Modules

**`tests/test_brand_checker.py`:**
```python
from src.pipeline.brand_checker import check_brand_compliance
from src.pipeline.image_generator import DRY_RUN_PIXEL

def test_dry_run_returns_compliant(sample_brief):
    result = check_brand_compliance(DRY_RUN_PIXEL, sample_brief, None, dry_run=True)
    assert result["compliant"] is True
    assert result["dry_run"] is True

def test_handles_client_error_gracefully(sample_brief):
    """Should not raise even if client is None in non-dry-run mode."""
    # With a None client, should catch exception and return error result
    result = check_brand_compliance(DRY_RUN_PIXEL, sample_brief, None, dry_run=False)
    assert "error" in result or result["compliant"] is None
```

**`tests/test_regulatory_checker.py`:**
```python
from src.pipeline.regulatory_checker import check_regulatory_content

CONTENT_WITH_ALLERGEN = {
    "title": "Test",
    "attributes": ["organic"],
    "regulatory_text": "Contains: nuts and seeds. See label for nutrition information."
}

CONTENT_MINIMAL = {
    "title": "Test",
    "attributes": [],
    "regulatory_text": "For more info visit website."
}

def test_passes_with_allergen_info():
    result = check_regulatory_content(CONTENT_WITH_ALLERGEN, "us-west")
    assert result["compliant"] is True

def test_fails_for_eu_with_minimal_text():
    result = check_regulatory_content(CONTENT_MINIMAL, "eu")
    assert result["compliant"] is False
    assert len(result["missing_items"]) > 0

def test_unknown_region_defaults_to_us_west():
    result = check_regulatory_content(CONTENT_WITH_ALLERGEN, "unknown-region")
    assert "region" in result
```

**Acceptance:** `pytest tests/test_brand_checker.py tests/test_regulatory_checker.py -v` passes.

---

## Automated Verification

```bash
# New tests
pytest tests/test_brand_checker.py tests/test_regulatory_checker.py -v

# All tests still passing
pytest tests/ -v -m "not integration"

# Dry-run pipeline with compliance checks
PAI_DRY_RUN=1 python -m src.pipeline.run_pipeline inputs/sample_sku_brief.json --dry-run
# Manifest should include "compliance" key

# Real pipeline with compliance
PAI_OUTPUT_BUCKET={output-bucket} \
  python -m src.pipeline.run_pipeline inputs/sample_sku_brief.json --model-tier dev
cat outputs/runs/*.json | python -m json.tool | grep -A 5 '"compliance"'
```

---

## Human Gate

Paul reviews:

1. **Brand compliance results** — at least 1 image evaluated by Claude Sonnet 4.6 with meaningful output (not just True/False with no reasoning)
2. **Regulatory check** — at least 1 region (`eu` with multilingual requirement) triggers a warning for minimal text
3. **Manifest** — `cat outputs/runs/*.json` shows `compliance` section with `results` array

**Gate question:** "Do the compliance results look meaningful (not all empty/trivial)?"

---

## Exit Protocol

1. **Save context snapshot:** Write `phase-06-complete.md`:
   ```markdown
   # Phase 6 Complete — Enhancements

   **New modules:** brand_checker.py, regulatory_checker.py
   **Test coverage:** brand (2 tests), regulatory (3 tests)
   **Brand check approach:** LLM-as-judge via Claude Sonnet 4.6 multimodal
   **Regulatory data:** synthesized JSON in data/regulatory_requirements.json (NOT authoritative)
   **Deviations:** [none / list any]
   ```

2. **Update README** to mention brand compliance and regulatory checks as Phase 6 bonus features.

3. **Commit:** `git commit -m "feat(phase-06): brand compliance, regulatory checks, approval tracking"`

4. **Push:** `git push origin main` (triggers CI — confirm still green)

5. **Signal complete:** "Phase 6 complete. All bonus features implemented. Repo ready for interview submission."
