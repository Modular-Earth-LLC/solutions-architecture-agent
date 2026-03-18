# Phase 3: Output Quality

**Goal:** Extend the pipeline to all three aspect ratios (1:1, 9:16, 16:9), enable output caching and --dry-run, and ensure 2+ products × 3 ratios = 6+ images per run, organized in S3.

**Minimum state after this phase:** Full pipeline run produces ≥6 organized images. Human confirms all 3 aspect ratios are visually correct. **G-003 passed.** All exercise core requirements are met.

---

## Prerequisites Checklist

- [ ] `phase-02-complete.md` exists with: function signatures, actual bucket names, model IDs used
- [ ] `/run-pipeline inputs/sample_sku_brief.json dev` completes successfully (G-002 passed)
- [ ] At least 2 images visible in S3 from Phase 2 run
- [ ] `outputs/runs/` contains at least 1 valid manifest JSON

**Load prior context:** Read `phase-01-complete.md` and `phase-02-complete.md`. Extract: S3 bucket names, actual function signatures, any Pillow coordinate insights.

---

## Architecture Decisions for This Phase

| Decision | Value |
|---------|-------|
| Aspect ratios | `1:1` → 1024×1024 (front label), `9:16` → 576×1024 (back label), `16:9` → 1024×576 (wraparound) |
| S3 key structure | `{sku_id}/{region}/front_label/`, `back_label/`, `wraparound/` |
| Cache | `~/.cache/pai-pipeline/` keyed by SHA-256(prompt+dims+model_id). Second run with same brief = $0 for cached images |
| Dry-run | `PAI_DRY_RUN=1` or `--dry-run` flag; 1×1 placeholder; manifest writes `dry_run: true`; no S3 image uploads |
| Manifest | Overwritten per run at `{sku_id}/{region}/manifest.json` in S3; new timestamped file in local `outputs/runs/` |
| Total images per full run | 2 products × 3 ratios = 6 images minimum |

---

## Tasks

### Task 1: Update `image_generator.py` for All 3 Aspect Ratios

The `ASPECT_RATIO_DIMS` dict and `generate_image` function are already set up from Phase 2. Verify these dimensions produce valid Bedrock responses:

| Ratio | Width | Height | Format name |
|-------|-------|--------|-------------|
| 1:1 | 1024 | 1024 | front_label |
| 9:16 | 576 | 1024 | back_label |
| 16:9 | 1024 | 576 | wraparound |

**Note for Nova Canvas:** Supported dimensions include 1024×1024, 576×1024, and 1024×576. Titan V2 supports 1024×1024, 512×512, and 768×768 — for 9:16 and 16:9 with Titan, use 512×512 and crop/pad, or stick with 1024×1024 and crop.

**Acceptance:** `generate_image(prompt, "9:16", "dev", False)` returns PNG bytes with dimensions 576×1024 (verify with `PIL.Image.open(io.BytesIO(bytes)).size`).

---

### Task 2: Update `text_overlay.py` for All 3 Aspect Ratios

The `LAYOUTS` dict already has all 3 ratio configurations from Phase 2. Verify and refine the layouts:

**1:1 layout (front_label):**
- Title centered, top-third of image (y ≈ 5-15%)
- Attributes as tag pills, center-bottom (y ≈ 70-80%)
- Regulatory footer strip, bottom (y ≈ 90-95%)

**9:16 layout (back_label):**
- Product name at top (y ≈ 5-10%)
- Longer product description in mid-section (y ≈ 40-60%)
- Attribute tags (y ≈ 65-75%)
- Regulatory footer (y ≈ 88-95%)

**16:9 layout (wraparound):**
- Product name left-aligned, upper-left quadrant (x ≈ 5%, y ≈ 10%)
- Attributes as vertical stack on right side (x ≈ 75%, y ≈ 20-60%)
- Regulatory footer full-width strip at bottom (y ≈ 88-92%)

**Pillow coordinate tuning tips:**
- Use `draw.textlength(text, font=font)` to measure text width before drawing
- Semi-transparent overlays (alpha 160-200) preserve image visibility while making text readable
- `anchor="mm"` for centered text, `anchor="lm"` for left-aligned
- For wrapping: use `textwrap.wrap(text, width=char_width)` where `char_width = width // (font_size // 2)`

**Acceptance:** apply_overlay returns PNG where text is legible across all 3 ratios. No IndexError or division-by-zero errors.

---

### Task 3: Update `run_pipeline.py` to Iterate All 3 Ratios

```python
RATIO_FORMAT_MAP = {
    "1:1": "front_label",
    "9:16": "back_label",
    "16:9": "wraparound"
}

def run_pipeline(sku_brief_path, model_tier="dev", dry_run=False, output_bucket=None, profile="pai-exercise"):
    # ... (existing setup) ...

    for product in brief["products"]:
        product_slug = (product.get("flavor") or product["name"]).lower().replace(" ", "-")
        for aspect_ratio, format_name in RATIO_FORMAT_MAP.items():
            try:
                prompt = build_image_prompt(brief, product, aspect_ratio)
                if text_client:
                    prompt = enhance_prompt_with_reasoning(text_client, prompt, product, dry_run)

                image_bytes = generate_image(prompt, aspect_ratio, model_tier, dry_run, profile)
                overlay_content = build_text_overlay_content(brief, product)
                composited = apply_overlay(image_bytes, overlay_content, aspect_ratio)

                if not dry_run:
                    s3_key = build_output_key(sku_id, region, format_name, f"{product_slug}.png")
                    upload_output(bucket, s3_key, composited, profile)
                    output_keys.append(s3_key)

            except Exception as e:
                errors.append({"product": product["name"], "ratio": aspect_ratio, "error": str(e)})
```

**Acceptance:** Full run with 2 products produces 6 S3 keys (2 × 3 ratios). Each key under correct format directory.

---

### Task 4: Implement Image Caching in `image_generator.py`

The cache skeleton was written in Phase 2. Verify it works end-to-end:

1. First run: no cache → Bedrock API called → image saved to `~/.cache/pai-pipeline/{hash}.png`
2. Second run (same brief): cache hit → Bedrock NOT called → cached bytes returned immediately

To verify cache is working:
```python
import time
start = time.time()
img1 = generate_image(prompt, "1:1", "dev", False)
first_time = time.time() - start

start = time.time()
img2 = generate_image(prompt, "1:1", "dev", False)
second_time = time.time() - start

assert second_time < first_time * 0.1  # Cache hit should be >10x faster
assert img1 == img2  # Same content
```

**Acceptance:** Second run with identical brief is measurably faster (cache hit logged to console). `~/.cache/pai-pipeline/` directory exists with PNG files.

---

### Task 5: Implement `--dry-run` Mode End-to-End

Add CLI argument handling to `run_pipeline.py` main block:

```python
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("sku_brief_path")
    parser.add_argument("--model-tier", default="dev")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output-bucket", default=None)
    args = parser.parse_args()
    run_pipeline(args.sku_brief_path, args.model_tier, args.dry_run, args.output_bucket)
```

Verify dry-run behavior:
- All `generate_image` calls return `DRY_RUN_PIXEL` (1×1 PNG)
- NO S3 image uploads (images_generated = 0)
- Manifest still written with `dry_run: true`
- Console output shows `[dry-run]` annotations

**Acceptance:** `python -m src.pipeline.run_pipeline inputs/sample_sku_brief.json --dry-run` completes in <2 seconds with zero API costs. Manifest shows `"dry_run": true`.

---

### Task 6: Write Pipeline Run Manifest to S3 and Local

Verify `output_manager.write_manifest()` produces a complete E-006 manifest:

Required fields (from data_model.json E-006):
```json
{
  "run_id": "uuid4-string",
  "timestamp": "2026-03-18T12:00:00Z",
  "sku_id": "organic-trail-mix-us",
  "region": "us-west",
  "models_used": ["dev:amazon.titan-image-generator-v2:0"],
  "images_generated": 6,
  "dry_run": false,
  "errors": [],
  "duration_seconds": 45.2
}
```

**Acceptance:** `cat outputs/runs/*.json | python -m json.tool` shows valid JSON with all 9 required fields. S3 key `{sku_id}/{region}/manifest.json` exists in output bucket.

---

### Task 7: Update `/pipeline-status` Skill

Update `.claude/skills/pipeline-status.md` to a functional skill:

```python
# The skill should run this when invoked:
import json, glob
manifests = sorted(glob.glob("outputs/runs/*.json"))
for path in manifests[-10:]:  # Show last 10 runs
    data = json.load(open(path))
    status = "DRY" if data.get("dry_run") else "REAL"
    errors = len(data.get("errors", []))
    print(f"{data['timestamp'][:19]} | {data['sku_id']:<30} | {data['images_generated']} imgs | {status} | {'✓' if errors==0 else f'{errors} errors'}")
```

**Acceptance:** `/pipeline-status` in Claude Code shows a readable table of recent runs without errors.

---

### Task 8: Update `/view-results` Skill

Update `.claude/skills/view-results.md`:

```bash
# The skill should run this when invoked with sku_id argument:
aws s3 ls s3://{output-bucket}/{sku_id}/ --recursive --profile pai-exercise

# Optionally download and open (Windows):
aws s3 cp s3://{output-bucket}/{sku_id}/ ./tmp/preview/ --recursive --profile pai-exercise
start tmp/preview/{sku_id}/us-west/front_label/*.png
```

**Acceptance:** `/view-results organic-trail-mix-us` shows the S3 listing with all 6 image paths.

---

## Automated Verification

```bash
# Dry-run (zero cost)
python -m src.pipeline.run_pipeline inputs/sample_sku_brief.json --dry-run
# Expected: "Pipeline complete: 0 images" (dry-run)

# Real run with dev tier (costs ~$0.06 for 6 images via Titan V2)
PAI_OUTPUT_BUCKET={output-bucket} \
  python -m src.pipeline.run_pipeline inputs/sample_sku_brief.json --model-tier dev
# Expected: "Pipeline complete: 6 images, ~Xs"

# Verify S3 structure
aws s3 ls s3://{output-bucket}/ --recursive --profile pai-exercise | grep "organic-trail-mix"
# Expected: 6 lines with front_label/, back_label/, wraparound/ directories

# Verify manifest
aws s3 cp s3://{output-bucket}/organic-trail-mix-us/us-west/manifest.json - --profile pai-exercise | python -m json.tool
# Expected: images_generated: 6

# Cache verification
python -m src.pipeline.run_pipeline inputs/sample_sku_brief.json --dry-run  # fast
python -m src.pipeline.run_pipeline inputs/sample_sku_brief.json --model-tier dev  # first real run
python -m src.pipeline.run_pipeline inputs/sample_sku_brief.json --model-tier dev  # second run = faster (cache)
```

---

## Human Gate

Paul downloads and inspects all 6 generated images:

```bash
mkdir -p tmp/preview
aws s3 cp s3://{output-bucket}/organic-trail-mix-us/ tmp/preview/ --recursive --profile pai-exercise
```

Open and inspect:
1. **Front label (1:1):** Product name centered, attribute tags visible, regulatory footer present
2. **Back label (9:16):** Tall format — product name at top, description readable, footer at bottom
3. **Wraparound (16:9):** Wide format — name left-aligned, right panel content, footer strip

**Quality bar:** Text overlay is readable on ALL 3 formats. Images look like product packaging. "Would an interviewer understand what this is in 3 seconds?"

**THIS PHASE COMPLETES ALL CORE EXERCISE REQUIREMENTS.**

---

## Exit Protocol

1. **Save context snapshot:** Write `phase-03-complete.md`:
   ```markdown
   # Phase 3 Complete

   **Aspect ratio dimensions used:**
   - 1:1: 1024×1024 ✓
   - 9:16: 576×1024 ✓
   - 16:9: 1024×576 ✓

   **Pillow coordinate decisions:**
   - 1:1: title_y=52px, attrs_y=717px, reg_y=921px
   - 9:16: title_y=51px, attrs_y=665px, reg_y=921px
   - 16:9: title_y=58px, attrs_y=346px (right panel), reg_y=507px
   [UPDATE WITH ACTUAL VALUES]

   **S3 key pattern confirmed:** {sku_id}/{region}/{format_name}/{product_slug}.png
   **Cache location:** ~/.cache/pai-pipeline/
   **Full run duration:** ~Xs for 6 images (dev tier)
   **Deviations:** [none / list any]
   ```

2. **Commit:** `git commit -m "feat(phase-03): all 3 aspect ratios, caching, dry-run, manifest complete"`

3. **Push:** `git push origin main`

4. **Signal Phase 4 ready:** "Phase 3 complete — G-003 passed. All exercise requirements met. Ready for Phase 4: CI/CD & Testing."
