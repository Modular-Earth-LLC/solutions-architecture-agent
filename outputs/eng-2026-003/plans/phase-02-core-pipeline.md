# Phase 2: Core Pipeline

**Goal:** Build a working end-to-end pipeline that accepts an SKU brief JSON and produces at least one packaged image (1:1 ratio) per product in S3 with text overlay. This is the **minimum demo state**.

**Minimum state after this phase:** `/run-pipeline inputs/sample_sku_brief.json` produces ≥2 images in S3. Human confirms text overlay is readable. **G-002 passed.**

---

## Prerequisites Checklist

- [ ] `phase-01-complete.md` exists with: input bucket name, output bucket name, region, models confirmed
- [ ] `aws cloudformation describe-stacks --stack-name pai-exercise --profile pai-exercise --query 'Stacks[0].StackStatus'` returns `"CREATE_COMPLETE"`
- [ ] `python -c "import boto3, PIL, anthropic, jsonschema"` succeeds in `.venv`
- [ ] G-001 passed — Bedrock model access confirmed for nova-canvas-v1:0 and claude-sonnet-4-6

**Load prior context:** Read `phase-01-complete.md` and extract: S3 bucket names, region (`us-east-1`), confirmed model IDs, profile name (`pai-exercise`).

---

## Architecture Decisions for This Phase

| Decision | Value |
|---------|-------|
| Orchestration | Direct Python function calls — no LangChain, no frameworks |
| Image generation (default) | `amazon.nova-canvas-v1:0` (primary); `amazon.titan-image-generator-v2:0` (dev tier, cheaper) |
| Text reasoning | `anthropic.AnthropicBedrock(aws_region='us-east-1')` — explicit region required |
| Text overlay | Pillow only — `PIL.Image`, `PIL.ImageDraw`, `PIL.ImageFont` |
| Interface | `/run-pipeline` skill (not argparse) |
| dry-run | `PAI_DRY_RUN=1` env var skips all Bedrock calls; returns 1×1 pixel placeholder |
| Cache | `~/.cache/pai-pipeline/` keyed by SHA-256 hash of (prompt + dimensions + model_id) |
| Retry | 3 attempts, exponential backoff: 2^n seconds between attempts |
| Manifest | E-006: written to both S3 `{SKU}/{region}/manifest.json` and local `outputs/runs/{timestamp}_{sku_id}.json` |

---

## Tasks

### Task 1: Define SKU Brief JSON Schema (`src/schemas/sku_brief_schema.json`)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "SKU Brief",
  "type": "object",
  "required": ["sku_id", "products", "region", "audience", "attributes"],
  "properties": {
    "sku_id": { "type": "string", "maxLength": 64 },
    "products": {
      "type": "array",
      "minItems": 2,
      "items": {
        "type": "object",
        "required": ["name", "description"],
        "properties": {
          "name": { "type": "string", "maxLength": 100 },
          "flavor": { "type": "string", "maxLength": 100 },
          "description": { "type": "string", "maxLength": 500 }
        }
      }
    },
    "region": { "type": "string", "maxLength": 64 },
    "audience": { "type": "string", "maxLength": 200 },
    "attributes": { "type": "array", "items": { "type": "string", "maxLength": 50 } }
  }
}
```

**Acceptance:** Schema validates sample brief. Invalid brief (missing `sku_id`) raises `jsonschema.ValidationError`.

---

### Task 2: Write Sample SKU Brief (`inputs/sample_sku_brief.json`)

```json
{
  "sku_id": "organic-trail-mix-us",
  "products": [
    {
      "name": "Organic Trail Mix",
      "flavor": "Original",
      "description": "Classic blend of nuts, seeds, and dried fruit for sustained energy"
    },
    {
      "name": "Organic Trail Mix",
      "flavor": "Dark Chocolate",
      "description": "Premium trail mix with fair-trade dark chocolate chips and antioxidant-rich berries"
    }
  ],
  "region": "us-west",
  "audience": "health-conscious adults 25-40",
  "attributes": ["organic", "non-gmo", "high-protein", "gluten-free"]
}
```

**Acceptance:** `python -c "import json, jsonschema; s=json.load(open('src/schemas/sku_brief_schema.json')); jsonschema.validate(json.load(open('inputs/sample_sku_brief.json')), s); print('valid')"` prints `valid`.

---

### Task 3: Implement `src/pipeline/sku_parser.py`

```python
import json
import jsonschema
from pathlib import Path

SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "sku_brief_schema.json"

def parse_sku_brief(file_path: str) -> dict:
    """Load and validate SKU brief JSON. Raises jsonschema.ValidationError on invalid."""
    with open(file_path) as f:
        brief = json.load(f)
    validate_sku_brief(brief)
    return brief

def validate_sku_brief(brief: dict) -> bool:
    schema = json.loads(SCHEMA_PATH.read_text())
    jsonschema.validate(brief, schema)
    return True
```

**Acceptance:** Parses `inputs/sample_sku_brief.json` without error. Raises on missing `sku_id`.

---

### Task 4: Implement `src/pipeline/asset_manager.py`

Functions:
- `check_s3_asset(bucket: str, key: str, profile: str = "pai-exercise") -> bool`
- `download_s3_asset(bucket: str, key: str, local_path: str, profile: str = "pai-exercise") -> str`
- `upload_output(bucket: str, key: str, image_bytes: bytes, profile: str = "pai-exercise") -> None`
- `build_output_key(sku_id: str, region: str, format_name: str, filename: str) -> str`

`build_output_key` must produce: `{sku_id}/{region}/{format_name}/{filename}`

Use `boto3.Session(profile_name=profile).client("s3")` for credential isolation.

**Acceptance:** `build_output_key("trail-mix", "us-west", "front_label", "original.png")` returns `"trail-mix/us-west/front_label/original.png"`.

---

### Task 5: Implement `src/pipeline/prompt_constructor.py`

```python
def build_image_prompt(brief: dict, product: dict, aspect_ratio: str) -> str:
    """Build Bedrock image generation prompt from SKU brief and product."""
    name = product["name"]
    flavor = product.get("flavor", "")
    description = product["description"]
    attributes = ", ".join(brief.get("attributes", []))
    region = brief.get("region", "")
    audience = brief.get("audience", "")

    product_display = f"{name} — {flavor}" if flavor else name

    return (
        f"Professional product packaging label design for {product_display}. "
        f"{description}. "
        f"Key attributes: {attributes}. "
        f"Target market: {audience} in {region}. "
        f"Clean, modern packaging design with clear typography. "
        f"High quality commercial product photography style. "
        f"White or light background. Aspect ratio: {aspect_ratio}."
    )

def build_text_overlay_content(brief: dict, product: dict) -> dict:
    """Return structured text content for Pillow overlay."""
    name = product["name"]
    flavor = product.get("flavor", "")
    title = f"{name}\n{flavor}" if flavor else name
    attributes = brief.get("attributes", [])
    regulatory_text = "Contains: See ingredients list. For more information visit our website."
    return {
        "title": title,
        "attributes": attributes[:4],  # Max 4 attribute tags
        "regulatory_text": regulatory_text
    }
```

Sanitize all string fields before use: `field.replace('\n', ' ').replace('\r', '').strip()[:max_len]`

**Acceptance:** `build_image_prompt(brief, product, "1:1")` returns a non-empty string containing the product name and at least one attribute.

---

### Task 6: Implement `src/pipeline/text_reasoning.py`

```python
import os
from anthropic import AnthropicBedrock

def get_bedrock_client() -> AnthropicBedrock:
    """Return AnthropicBedrock client. aws_region must be explicit — does not read ~/.aws/config."""
    return AnthropicBedrock(
        aws_region="us-east-1"
        # Uses same credential chain as boto3: env vars, ~/.aws/credentials, instance profile
    )

def enhance_prompt_with_reasoning(
    client: AnthropicBedrock,
    base_prompt: str,
    product: dict,
    dry_run: bool = False
) -> str:
    """Optionally enhance image prompt via Claude Sonnet 4.6. Falls back to base_prompt on error."""
    if dry_run:
        return base_prompt
    try:
        message = client.messages.create(
            model="anthropic.claude-sonnet-4-6",
            max_tokens=256,
            system="You are a packaging design expert. Improve the following image generation prompt for better visual quality. Return ONLY the improved prompt text, nothing else.",
            messages=[{"role": "user", "content": base_prompt}]
        )
        enhanced = message.content[0].text.strip()
        return enhanced if enhanced else base_prompt
    except Exception:
        return base_prompt  # Always fall back — text reasoning is enhancement, not critical path
```

**Acceptance:** With dry_run=True, returns `base_prompt` unchanged. Client initializes without error.

---

### Task 7: Implement `src/pipeline/image_generator.py`

```python
import os
import json
import time
import hashlib
from pathlib import Path
import boto3
from botocore.exceptions import ClientError

CACHE_DIR = Path.home() / ".cache" / "pai-pipeline"
MODEL_TIERS = {
    "dev": "amazon.titan-image-generator-v2:0",
    "iterate": "amazon.nova-canvas-v1:0",
    "final": "amazon.nova-canvas-v1:0"
}
ASPECT_RATIO_DIMS = {
    "1:1": (1024, 1024),
    "9:16": (576, 1024),
    "16:9": (1024, 576)
}
DRY_RUN_PIXEL = bytes([
    0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A,  # PNG header
    0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52,  # IHDR chunk
    0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01,  # 1x1
    0x08, 0x02, 0x00, 0x00, 0x00, 0x90, 0x77, 0x53,
    0xDE, 0x00, 0x00, 0x00, 0x0C, 0x49, 0x44, 0x41,
    0x54, 0x08, 0xD7, 0x63, 0xF8, 0xFF, 0xFF, 0x3F,
    0x00, 0x05, 0xFE, 0x02, 0xFE, 0xDC, 0xCC, 0x59,
    0xE7, 0x00, 0x00, 0x00, 0x00, 0x49, 0x45, 0x4E,
    0x44, 0xAE, 0x42, 0x60, 0x82
])

def _cache_key(prompt: str, width: int, height: int, model_id: str) -> str:
    content = f"{prompt}|{width}|{height}|{model_id}"
    return hashlib.sha256(content.encode()).hexdigest()

def _get_cached(cache_key: str) -> bytes | None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_file = CACHE_DIR / f"{cache_key}.png"
    return cache_file.read_bytes() if cache_file.exists() else None

def _save_cached(cache_key: str, image_bytes: bytes) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    (CACHE_DIR / f"{cache_key}.png").write_bytes(image_bytes)

def generate_image(
    prompt: str,
    aspect_ratio: str = "1:1",
    model_tier: str = "dev",
    dry_run: bool = False,
    profile: str = "pai-exercise"
) -> bytes:
    """Generate image via Bedrock. Returns PNG bytes. Falls back to lower tier on throttling."""
    if dry_run or os.environ.get("PAI_DRY_RUN"):
        return DRY_RUN_PIXEL

    width, height = ASPECT_RATIO_DIMS.get(aspect_ratio, (1024, 1024))
    model_id = MODEL_TIERS.get(model_tier, MODEL_TIERS["dev"])

    key = _cache_key(prompt, width, height, model_id)
    cached = _get_cached(key)
    if cached:
        return cached

    session = boto3.Session(profile_name=profile, region_name="us-east-1")
    client = session.client("bedrock-runtime")

    for attempt in range(3):
        try:
            if "nova-canvas" in model_id:
                body = json.dumps({
                    "taskType": "TEXT_IMAGE",
                    "textToImageParams": {"text": prompt},
                    "imageGenerationConfig": {
                        "width": width, "height": height,
                        "quality": "standard", "numberOfImages": 1
                    }
                })
                response = client.invoke_model(modelId=model_id, body=body)
                result = json.loads(response["body"].read())
                import base64
                image_bytes = base64.b64decode(result["images"][0])
            else:
                # Titan Image Generator V2
                body = json.dumps({
                    "taskType": "TEXT_IMAGE",
                    "textToImageParams": {"text": prompt},
                    "imageGenerationConfig": {
                        "width": width, "height": height,
                        "quality": "standard", "numberOfImages": 1
                    }
                })
                response = client.invoke_model(modelId=model_id, body=body)
                result = json.loads(response["body"].read())
                import base64
                image_bytes = base64.b64decode(result["images"][0])

            _save_cached(key, image_bytes)
            return image_bytes

        except ClientError as e:
            error_code = e.response["Error"]["Code"]
            if error_code in ("ThrottlingException", "ServiceUnavailableException") and attempt < 2:
                time.sleep(2 ** (attempt + 1))
                continue
            if attempt == 2:
                # Fall back to dev tier if final/iterate tier throttled
                if model_tier != "dev":
                    return generate_image(prompt, aspect_ratio, "dev", False, profile)
                raise
            raise
    raise RuntimeError(f"Image generation failed after 3 attempts for model {model_id}")
```

**Acceptance:** With `PAI_DRY_RUN=1`, returns `DRY_RUN_PIXEL`. With real credentials and dev tier, generates a PNG for a test prompt. ThrottlingException triggers retry with exponential backoff.

---

### Task 8: Implement `src/pipeline/text_overlay.py`

```python
from PIL import Image, ImageDraw, ImageFont
import io

LAYOUT_1_1 = {
    "title_y_pct": 0.05, "title_font_size": 48,
    "attrs_y_pct": 0.70, "attr_font_size": 28,
    "regulatory_y_pct": 0.90, "reg_font_size": 18
}
LAYOUT_9_16 = {
    "title_y_pct": 0.05, "title_font_size": 44,
    "attrs_y_pct": 0.65, "attr_font_size": 26,
    "regulatory_y_pct": 0.90, "reg_font_size": 16
}
LAYOUT_16_9 = {
    "title_y_pct": 0.05, "title_font_size": 40,
    "attrs_y_pct": 0.60, "attr_font_size": 24,
    "regulatory_y_pct": 0.88, "reg_font_size": 16
}
LAYOUTS = {"1:1": LAYOUT_1_1, "9:16": LAYOUT_9_16, "16:9": LAYOUT_16_9}

def apply_overlay(image_bytes: bytes, content: dict, aspect_ratio: str = "1:1") -> bytes:
    """Apply text overlay to image. Returns PNG bytes."""
    img = Image.open(io.BytesIO(image_bytes)).convert("RGBA")
    width, height = img.size

    # Create overlay layer for semi-transparent text backgrounds
    overlay = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    layout = LAYOUTS.get(aspect_ratio, LAYOUT_1_1)

    # Try to load a system font, fall back to default
    try:
        title_font = ImageFont.truetype("arial.ttf", layout["title_font_size"])
        attr_font = ImageFont.truetype("arial.ttf", layout["attr_font_size"])
        reg_font = ImageFont.truetype("arial.ttf", layout["reg_font_size"])
    except (OSError, IOError):
        title_font = ImageFont.load_default()
        attr_font = ImageFont.load_default()
        reg_font = ImageFont.load_default()

    # Title with semi-transparent background strip
    title_y = int(height * layout["title_y_pct"])
    draw.rectangle([(0, title_y - 5), (width, title_y + layout["title_font_size"] * 2 + 10)],
                   fill=(0, 0, 0, 160))
    draw.text((width // 2, title_y + layout["title_font_size"] // 2),
              content.get("title", ""), fill=(255, 255, 255, 255),
              font=title_font, anchor="mm", align="center")

    # Attribute tags
    attrs = content.get("attributes", [])
    attrs_y = int(height * layout["attrs_y_pct"])
    tag_x = 20
    for attr in attrs[:4]:
        tag_text = f"  {attr.upper()}  "
        draw.rectangle([(tag_x - 5, attrs_y - 5),
                        (tag_x + len(tag_text) * (layout["attr_font_size"] // 2) + 5,
                         attrs_y + layout["attr_font_size"] + 5)],
                       fill=(255, 255, 255, 200))
        draw.text((tag_x, attrs_y), tag_text, fill=(0, 0, 0, 255), font=attr_font)
        tag_x += len(tag_text) * (layout["attr_font_size"] // 2) + 20
        if tag_x > width * 0.85:
            break

    # Regulatory text footer
    reg_y = int(height * layout["regulatory_y_pct"])
    reg_text = content.get("regulatory_text", "")
    draw.rectangle([(0, reg_y - 3), (width, height)], fill=(0, 0, 0, 180))
    draw.text((width // 2, reg_y + layout["reg_font_size"] // 2),
              reg_text, fill=(255, 255, 255, 220),
              font=reg_font, anchor="mm")

    # Composite and return
    composited = Image.alpha_composite(img, overlay).convert("RGB")
    output_buf = io.BytesIO()
    composited.save(output_buf, format="PNG")
    return output_buf.getvalue()
```

**Note:** Font availability varies by OS. On Windows, `arial.ttf` is typically available. If not found, the default Pillow bitmap font is used as fallback — text will be readable but smaller. For portability, bundle a `.ttf` file (e.g., `src/fonts/DejaVuSans.ttf`) as an enhancement in P-003.

**Acceptance:** `apply_overlay(image_bytes, content, "1:1")` returns bytes longer than input. Output PNG opens in image viewer with readable product name.

---

### Task 9: Implement `src/pipeline/output_manager.py`

```python
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
import boto3

def write_manifest(run_data: dict, bucket: str, sku_id: str, region: str,
                   profile: str = "pai-exercise") -> None:
    """Write pipeline run manifest to S3 and local outputs/runs/."""
    manifest = {
        "run_id": run_data.get("run_id", str(uuid.uuid4())),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "sku_id": sku_id,
        "region": region,
        "models_used": run_data.get("models_used", []),
        "images_generated": run_data.get("images_generated", 0),
        "dry_run": run_data.get("dry_run", False),
        "errors": run_data.get("errors", []),
        "duration_seconds": run_data.get("duration_seconds", 0)
    }

    manifest_json = json.dumps(manifest, indent=2)

    # Write to S3
    s3 = boto3.Session(profile_name=profile, region_name="us-east-1").client("s3")
    s3_key = f"{sku_id}/{region}/manifest.json"
    s3.put_object(Bucket=bucket, Key=s3_key, Body=manifest_json.encode(),
                  ContentType="application/json")

    # Write locally
    local_dir = Path("outputs/runs")
    local_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    local_file = local_dir / f"{ts}_{sku_id}.json"
    local_file.write_text(manifest_json)
```

**Acceptance:** After a pipeline run, `outputs/runs/` contains a valid JSON manifest with `run_id`, `timestamp`, `sku_id`, `images_generated`.

---

### Task 10: Implement `src/pipeline/run_pipeline.py` (Orchestrator)

```python
import os
import time
import uuid
from pathlib import Path

from .sku_parser import parse_sku_brief
from .asset_manager import upload_output, build_output_key
from .prompt_constructor import build_image_prompt, build_text_overlay_content
from .image_generator import generate_image
from .text_overlay import apply_overlay
from .output_manager import write_manifest
from .text_reasoning import get_bedrock_client, enhance_prompt_with_reasoning

OUTPUT_BUCKET = os.environ.get("PAI_OUTPUT_BUCKET", "")  # Set from CF outputs

def run_pipeline(
    sku_brief_path: str,
    model_tier: str = "dev",
    dry_run: bool = False,
    output_bucket: str = None,
    profile: str = "pai-exercise"
) -> list[str]:
    """Run full pipeline for all products × 1:1 ratio. Returns list of S3 output keys."""
    start_time = time.time()
    run_id = str(uuid.uuid4())
    bucket = output_bucket or OUTPUT_BUCKET
    dry_run = dry_run or bool(os.environ.get("PAI_DRY_RUN"))

    brief = parse_sku_brief(sku_brief_path)
    sku_id = brief["sku_id"]
    region = brief.get("region", "us-east")

    text_client = None if dry_run else get_bedrock_client()

    output_keys = []
    errors = []
    models_used = set()

    for product in brief["products"]:
        product_slug = (product.get("flavor") or product["name"]).lower().replace(" ", "-")
        try:
            base_prompt = build_image_prompt(brief, product, "1:1")
            if text_client:
                prompt = enhance_prompt_with_reasoning(text_client, base_prompt, product, dry_run)
            else:
                prompt = base_prompt

            image_bytes = generate_image(prompt, "1:1", model_tier, dry_run, profile)
            models_used.add(f"{model_tier}:{__import__('src.pipeline.image_generator', fromlist=['MODEL_TIERS']).MODEL_TIERS.get(model_tier, 'unknown')}")

            overlay_content = build_text_overlay_content(brief, product)
            composited = apply_overlay(image_bytes, overlay_content, "1:1")

            if not dry_run:
                s3_key = build_output_key(sku_id, region, "front_label", f"{product_slug}.png")
                upload_output(bucket, s3_key, composited, profile)
                output_keys.append(s3_key)

            print(f"  ✓ {product['name']} ({product.get('flavor', '')}) — 1:1 {'[dry-run]' if dry_run else s3_key}")

        except Exception as e:
            errors.append({"product": product["name"], "error": str(e)})
            print(f"  ✗ {product['name']}: {e}")

    duration = round(time.time() - start_time, 2)
    write_manifest(
        {"run_id": run_id, "models_used": list(models_used), "images_generated": len(output_keys),
         "dry_run": dry_run, "errors": errors, "duration_seconds": duration},
        bucket, sku_id, region, profile
    )

    print(f"\nPipeline complete: {len(output_keys)} images, {duration}s")
    return output_keys

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "inputs/sample_sku_brief.json"
    tier = sys.argv[2] if len(sys.argv) > 2 else "dev"
    run_pipeline(path, tier)
```

**Acceptance:** `PAI_DRY_RUN=1 python -m src.pipeline.run_pipeline inputs/sample_sku_brief.json` completes without error. `python -m src.pipeline.run_pipeline inputs/sample_sku_brief.json dev` generates ≥2 images in S3.

---

### Task 11: Update `/run-pipeline` Skill

Update `.claude/skills/run-pipeline.md` to a functional skill that invokes `run_pipeline.py`:

```markdown
---
name: run-pipeline
description: Run the PAI packaging image generation pipeline with a given SKU brief JSON file
---

# /run-pipeline

Runs the full PAI packaging automation pipeline.

## Usage

`/run-pipeline <sku-brief-path> [model-tier]`

- `sku-brief-path`: Path to SKU brief JSON file (required)
- `model-tier`: `dev` | `iterate` | `final` (default: `dev`)

## What it does

1. Parses and validates the SKU brief JSON
2. Constructs image prompts for each product
3. Generates packaging images via Bedrock (Nova Canvas or Titan V2)
4. Applies text overlay via Pillow
5. Uploads to S3 organized by `{sku_id}/{region}/front_label/`
6. Writes pipeline run manifest to S3 and local `outputs/runs/`

## Example

```bash
/run-pipeline inputs/sample_sku_brief.json dev
/run-pipeline inputs/sample_sku_brief.json final
```

To run without Bedrock calls (zero cost): `PAI_DRY_RUN=1 /run-pipeline inputs/sample_sku_brief.json`
```

**Acceptance:** The skill file is clear and self-documenting.

---

## Automated Verification

```bash
# Zero-cost validation
PAI_DRY_RUN=1 python -m src.pipeline.run_pipeline inputs/sample_sku_brief.json
# Expected: "Pipeline complete: 0 images, X.Xs" (no S3 uploads in dry-run)

# Real dev tier run (costs ~$0.02 for 2 images via Titan V2)
PAI_OUTPUT_BUCKET={output-bucket-from-phase-01} \
  python -m src.pipeline.run_pipeline inputs/sample_sku_brief.json dev
# Expected: "Pipeline complete: 2 images, Xs"

# Verify S3 output
aws s3 ls s3://{output-bucket}/organic-trail-mix-us/ --recursive --profile pai-exercise
# Expected: 2 .png files under organic-trail-mix-us/us-west/front_label/

# Verify manifest
cat outputs/runs/*.json | python -m json.tool
# Expected: valid JSON with run_id, timestamp, images_generated: 2
```

---

## Human Gate

After automated verification, Paul:

1. Downloads and opens the generated images: `aws s3 cp s3://{output-bucket}/organic-trail-mix-us/us-west/front_label/ ./tmp/ --recursive --profile pai-exercise`
2. Opens both PNG files and confirms:
   - Product name is visible and readable
   - At least one attribute tag is visible
   - Regulatory footer text is present (even if small)
3. Quality bar: **"Does this look like a product label?" not "Is this production-ready?"**

**THIS IS THE MINIMUM DEMO STATE.** If you can show this to an interviewer, Phase 2 is complete.

**Gate question:** "Images visible with readable product name and attribute text?"

---

## Exit Protocol

1. **Save context snapshot:** Write `phase-02-complete.md` in repo root:
   ```markdown
   # Phase 2 Complete

   **Output bucket:** [actual name from CF outputs]
   **Input bucket:** [actual name]
   **Sample SKU ID:** organic-trail-mix-us
   **Models used:** [actual model IDs]
   **S3 output key pattern:** {sku_id}/{region}/front_label/{product_slug}.png
   **Function signatures confirmed:**
   - run_pipeline(sku_brief_path, model_tier="dev", dry_run=False, output_bucket=None, profile="pai-exercise")
   - generate_image(prompt, aspect_ratio="1:1", model_tier="dev", dry_run=False, profile="pai-exercise")
   - apply_overlay(image_bytes, content, aspect_ratio="1:1")
   **Pillow insights:** [any coordinate tuning notes]
   **Deviations:** [none / list any]
   ```

2. **Commit:** `git commit -m "feat(phase-02): core pipeline — SKU parser to S3 upload, 1:1 ratio working"`

3. **Push:** `git push origin main`

4. **Signal Phase 3 ready:** "Phase 2 complete — G-002 passed. MINIMUM DEMO STATE ACHIEVED. Ready for Phase 3: Output Quality."
