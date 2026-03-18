# Phase 4: CI/CD and Testing

**Goal:** Configure GitHub Actions CI/CD with lint and test on every push, write a test suite covering all pipeline modules, and verify Claude Code auto-lint hooks are working.

**Minimum state after this phase:** `git push origin main` triggers GitHub Actions — both ci.yml and deploy.yml show green checkmarks. **G-004 passed.**

---

## Prerequisites Checklist

- [ ] `phase-03-complete.md` exists with actual module paths, function signatures
- [ ] Full pipeline run produces ≥6 images in S3 (G-003 passed)
- [ ] GitHub repo is public and connected: `git remote -v` shows `github.com/praeducer/pai-take-home-exercise`
- [ ] `gh auth status` shows authenticated as `praeducer`
- [ ] Ruff installed: `ruff --version`

**Load prior context:** Read `phase-01-complete.md`, `phase-02-complete.md`, and `phase-03-complete.md` for actual function signatures, S3 bucket names, and module structure.

---

## Architecture Decisions for This Phase

| Decision | Value |
|---------|-------|
| CI tool | GitHub Actions |
| Linter | `ruff` (fast, all-in-one; replaces flake8) |
| Test framework | pytest |
| Dependency scanner | pip-audit (runs in CI, fails on high/critical CVEs) |
| Action version pinning | SHA commit hashes (not semver tags) — required for supply chain security |
| AWS credentials in CI | GitHub Secrets (simpler for PoC); OIDC is preferred but optional here |
| Integration tests | Marked `@pytest.mark.integration`, skipped in CI by default (require real AWS) |

---

## Tasks

### Task 1: Write Unit Tests

Create `tests/conftest.py` with shared fixtures:

```python
import pytest
import json

@pytest.fixture
def sample_brief():
    return {
        "sku_id": "test-product-001",
        "products": [
            {"name": "Test Product", "flavor": "Original", "description": "A test product description"},
            {"name": "Test Product", "flavor": "Vanilla", "description": "Vanilla variant description"}
        ],
        "region": "us-west",
        "audience": "test audience",
        "attributes": ["organic", "non-gmo", "test-attr"]
    }

@pytest.fixture
def sample_product(sample_brief):
    return sample_brief["products"][0]
```

---

**`tests/test_sku_parser.py`:**
```python
import pytest
import json
import jsonschema
from src.pipeline.sku_parser import parse_sku_brief, validate_sku_brief

def test_valid_brief(sample_brief, tmp_path):
    brief_file = tmp_path / "brief.json"
    brief_file.write_text(json.dumps(sample_brief))
    result = parse_sku_brief(str(brief_file))
    assert result["sku_id"] == "test-product-001"
    assert len(result["products"]) == 2

def test_invalid_brief_missing_sku_id(tmp_path):
    invalid = {"products": [{"name": "x", "description": "y"}, {"name": "z", "description": "w"}], "region": "us", "audience": "a", "attributes": []}
    brief_file = tmp_path / "invalid.json"
    brief_file.write_text(json.dumps(invalid))
    with pytest.raises(jsonschema.ValidationError):
        parse_sku_brief(str(brief_file))

def test_brief_requires_two_products(tmp_path):
    only_one = {**pytest.importorskip("src.pipeline.sku_parser") and {}, "sku_id": "x", "products": [{"name": "a", "description": "b"}], "region": "r", "audience": "a", "attributes": []}
    brief_file = tmp_path / "one_product.json"
    brief_file.write_text(json.dumps(only_one))
    with pytest.raises(jsonschema.ValidationError):
        parse_sku_brief(str(brief_file))
```

---

**`tests/test_prompt_constructor.py`:**
```python
from src.pipeline.prompt_constructor import build_image_prompt, build_text_overlay_content

def test_prompt_contains_product_name(sample_brief, sample_product):
    prompt = build_image_prompt(sample_brief, sample_product, "1:1")
    assert "Test Product" in prompt
    assert len(prompt) > 50

def test_prompt_contains_attributes(sample_brief, sample_product):
    prompt = build_image_prompt(sample_brief, sample_product, "1:1")
    assert "organic" in prompt

def test_prompt_contains_region(sample_brief, sample_product):
    prompt = build_image_prompt(sample_brief, sample_product, "1:1")
    assert "us-west" in prompt

def test_overlay_content_has_regulatory(sample_brief, sample_product):
    content = build_text_overlay_content(sample_brief, sample_product)
    assert "regulatory_text" in content
    assert len(content["regulatory_text"]) > 0

def test_overlay_content_max_four_attributes(sample_brief, sample_product):
    content = build_text_overlay_content(sample_brief, sample_product)
    assert len(content["attributes"]) <= 4
```

---

**`tests/test_image_generator.py`:**
```python
import os
from unittest.mock import patch
from src.pipeline.image_generator import generate_image, DRY_RUN_PIXEL, _cache_key, _get_cached, _save_cached

def test_dry_run_returns_placeholder():
    result = generate_image("test prompt", "1:1", "dev", dry_run=True)
    assert result == DRY_RUN_PIXEL

def test_env_dry_run_returns_placeholder(monkeypatch):
    monkeypatch.setenv("PAI_DRY_RUN", "1")
    result = generate_image("test prompt", "1:1", "dev")
    assert result == DRY_RUN_PIXEL

def test_cache_key_is_deterministic():
    k1 = _cache_key("prompt", 1024, 1024, "model")
    k2 = _cache_key("prompt", 1024, 1024, "model")
    assert k1 == k2

def test_cache_key_differs_for_different_prompts():
    k1 = _cache_key("prompt-a", 1024, 1024, "model")
    k2 = _cache_key("prompt-b", 1024, 1024, "model")
    assert k1 != k2

def test_cache_hit_returns_cached_bytes(tmp_path, monkeypatch):
    monkeypatch.setattr("src.pipeline.image_generator.CACHE_DIR", tmp_path)
    test_bytes = b"fake-image-data"
    key = _cache_key("prompt", 1024, 1024, "model")
    _save_cached(key, test_bytes)
    result = _get_cached(key)
    assert result == test_bytes
```

---

**`tests/test_text_overlay.py`:**
```python
from PIL import Image
import io
from src.pipeline.image_generator import DRY_RUN_PIXEL
from src.pipeline.text_overlay import apply_overlay

CONTENT = {
    "title": "Test Product\nOriginal",
    "attributes": ["organic", "non-gmo"],
    "regulatory_text": "Contains: nuts. See label."
}

def test_overlay_returns_bytes():
    # Use a real small test image
    img = Image.new("RGB", (1024, 1024), color=(200, 200, 200))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    image_bytes = buf.getvalue()

    result = apply_overlay(image_bytes, CONTENT, "1:1")
    assert isinstance(result, bytes)
    assert len(result) > 0

def test_overlay_correct_dimensions():
    img = Image.new("RGB", (576, 1024), color=(200, 200, 200))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    image_bytes = buf.getvalue()

    result = apply_overlay(image_bytes, CONTENT, "9:16")
    result_img = Image.open(io.BytesIO(result))
    assert result_img.size == (576, 1024)

def test_overlay_all_ratios_succeed():
    for ratio, size in [("1:1", (1024, 1024)), ("9:16", (576, 1024)), ("16:9", (1024, 576))]:
        img = Image.new("RGB", size, color=(200, 200, 200))
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        result = apply_overlay(buf.getvalue(), CONTENT, ratio)
        assert len(result) > 0, f"Empty result for ratio {ratio}"
```

---

**`tests/test_asset_manager.py`:**
```python
from src.pipeline.asset_manager import build_output_key

def test_output_key_structure():
    key = build_output_key("trail-mix", "us-west", "front_label", "original.png")
    assert key == "trail-mix/us-west/front_label/original.png"

def test_output_key_with_hyphens():
    key = build_output_key("organic-trail-mix-us", "us-west", "back_label", "dark-chocolate.png")
    parts = key.split("/")
    assert len(parts) == 4
    assert parts[0] == "organic-trail-mix-us"
    assert parts[2] == "back_label"
```

---

**`tests/test_integration.py`** (requires real AWS, skipped in CI):
```python
import pytest
import os

@pytest.mark.integration
def test_full_pipeline_dry_run(tmp_path):
    """Full pipeline in dry-run mode — zero API cost, verifies module wiring."""
    import subprocess
    result = subprocess.run(
        ["python", "-m", "src.pipeline.run_pipeline",
         "inputs/sample_sku_brief.json", "--dry-run"],
        env={**os.environ, "PAI_DRY_RUN": "1"},
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"Pipeline failed: {result.stderr}"
    assert "Pipeline complete" in result.stdout
```

**Acceptance:** `pytest tests/ -v -m "not integration"` passes with all unit tests green.

---

### Task 2: Create `.github/workflows/ci.yml`

```yaml
name: CI

on:
  push:
    branches: ["**"]
  pull_request:
    branches: [main]

jobs:
  lint-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683  # v4.2.2
      - uses: actions/setup-python@0b93645e9fea7318ecaed2b359559ac225c90a2b  # v5.3.0
        with:
          python-version: "3.12"
          cache: "pip"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Lint with ruff
        run: ruff check src/ tests/

      - name: Run unit tests
        run: pytest tests/ -v -m "not integration" --tb=short

      - name: Security audit
        run: pip-audit --requirement requirements.txt --severity high
        continue-on-error: false
```

**Important:** Replace SHA hashes above with the current actual SHAs for `actions/checkout@v4` and `actions/setup-python@v5`. Find them at:
- `github.com/actions/checkout/releases` → copy SHA for latest v4 release
- `github.com/actions/setup-python/releases` → copy SHA for latest v5 release

**Acceptance:** ci.yml is valid YAML. `git push` triggers it. Green within 2 minutes.

---

### Task 3: Create `.github/workflows/deploy.yml`

```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    needs: []  # Note: ci.yml is a separate workflow; configure branch protection to require ci
    steps:
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683  # v4.2.2

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@e3dd6a429d7300a6a4c196c26e071d42e0343502  # v4.0.2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: Deploy CloudFormation stack
        run: |
          aws cloudformation deploy \
            --stack-name pai-exercise \
            --template-file infra/cloudformation/stack.yaml \
            --capabilities CAPABILITY_IAM \
            --region us-east-1
```

**GitHub Secrets setup** (Paul human action):
1. Go to `github.com/praeducer/pai-take-home-exercise/settings/secrets/actions`
2. Add `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` for the `pai-exercise` profile

**Alternative (preferred):** OIDC federation — avoids long-lived secrets. Requires IAM Identity Provider setup in AWS console (15-minute human task). See `docs/design-decisions.md` for OIDC setup instructions.

**Acceptance:** deploy.yml is valid YAML. After secrets are set, push to main triggers deploy.yml.

---

### Task 4: Create `Makefile` for Local Development

```makefile
.PHONY: test lint audit install clean

install:
	pip install -r requirements.txt

test:
	pytest tests/ -v -m "not integration"

test-all:
	pytest tests/ -v

lint:
	ruff check src/ tests/

lint-fix:
	ruff check src/ tests/ --fix

audit:
	pip-audit --requirement requirements.txt --severity high

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
```

**Acceptance:** `make test` and `make lint` run without error.

---

### Task 5: Verify Claude Code Auto-Lint Hook

Edit any `.py` file in `src/` (add a comment, change whitespace). Observe that:
1. Within a few seconds of the edit, Claude Code shows ruff output
2. If ruff finds an issue (trailing whitespace, unused import), it auto-fixes or reports it

If hook is not triggering:
- Check `.claude/settings.json` — verify `PostToolUse` matcher is `"Edit|Write"` (not `"edit|write"`)
- Ensure ruff is on PATH in the session: `which ruff` or `ruff --version`

**Acceptance:** Editing a Python file triggers ruff without manual invocation.

---

### Task 6: Add `pyproject.toml` for Ruff Configuration

```toml
[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "W", "F", "I"]
ignore = ["E501"]  # Allow long lines in prompt strings

[tool.pytest.ini_options]
testpaths = ["tests"]
markers = [
    "integration: tests that require real AWS credentials"
]
```

**Acceptance:** `ruff check src/` uses config from `pyproject.toml`. `pytest tests/ --co` shows markers.

---

## Automated Verification

```bash
# Lint
ruff check src/ tests/
# Expected: no output (zero issues)

# Unit tests
pytest tests/ -v -m "not integration"
# Expected: all PASSED, none FAILED

# Security audit
pip-audit --requirement requirements.txt --severity high
# Expected: "No known vulnerabilities found" or specific CVE output (investigate if found)

# Push to GitHub and verify CI
git push origin main
# Then: visit github.com/praeducer/pai-take-home-exercise/actions
# Expected: ci.yml workflow shows green checkmark within 2 minutes
```

---

## Human Gate

Paul opens the GitHub Actions tab:
`github.com/praeducer/pai-take-home-exercise/actions`

Confirm:
- [ ] `ci.yml` run on main branch shows green checkmark
- [ ] All 3 jobs (lint, test, audit) show green
- [ ] `deploy.yml` ran and shows green (or shows expected failure if secrets not yet set)

**Gate question:** "CI/CD tab shows green on main branch?"

---

## Exit Protocol

1. **Save context snapshot:** Write `phase-04-complete.md`:
   ```markdown
   # Phase 4 Complete

   **CI/CD workflow URLs:**
   - ci.yml: https://github.com/praeducer/pai-take-home-exercise/actions/workflows/ci.yml
   - deploy.yml: https://github.com/praeducer/pai-take-home-exercise/actions/workflows/deploy.yml

   **Test summary:** X unit tests passing, 1 integration test skipped
   **Ruff issues fixed:** [none / list any]
   **pip-audit result:** [clean / CVEs found and addressed]
   **Actions SHA used:**
   - actions/checkout: [actual SHA]
   - actions/setup-python: [actual SHA]
   - aws-actions/configure-aws-credentials: [actual SHA]
   **Deviations:** [none / list any — e.g., used GitHub Secrets instead of OIDC]
   ```

2. **Commit:** `git commit -m "feat(phase-04): CI/CD, full test suite, auto-lint hooks complete"`

3. **Push:** `git push origin main` (triggers CI — confirm green)

4. **Signal Phase 5 ready:** "Phase 4 complete — G-004 passed. GitHub Actions green. Ready for Phase 5: Docs & Demo."
