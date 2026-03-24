# Document Conversion Scripts

Utility scripts for converting and processing document formats, primarily focused on PDF to Markdown conversion with professional-grade quality assurance.

## Scripts

### `pdf_to_markdown.py`

Converts PDF files to well-formatted Markdown with intelligent structure preservation.

**Features:**
- Table detection and preservation
- Heading hierarchy detection
- Multi-line cell handling
- Comprehensive QA validation
- Detailed progress reporting

**Installation:**
```bash
pip install pdfplumber pymupdf
```

**Usage:**
```bash
# Convert PDF to Markdown (auto-names output)
python pdf_to_markdown.py input.pdf

# Convert with custom output path
python pdf_to_markdown.py input.pdf output.md
```

**Output:**
- Detailed console output showing all conversion phases
- Phase 1: Extraction with table awareness
- Phase 2: Finalization and cleanup
- Phase 3: Validation with structure checks
- Phase 4: File generation
- Phase 5: Integrity verification

**Example:**
```
$ python pdf_to_markdown.py document.pdf

================================================================================
PDF TO MARKDOWN CONVERTER
================================================================================

[INPUT]  document.pdf
[OUTPUT] document.md

[PHASE 1] EXTRACTION
────────────────────────────────────────────────────────────────────────────────
✓ Extracted content with table awareness
  → Initial size: 5294 characters

[PHASE 2] FINALIZATION
────────────────────────────────────────────────────────────────────────────────
✓ Removed excessive whitespace
✓ Normalized line endings
  → Final size: 5293 characters, 50 lines

[PHASE 3] VALIDATION
────────────────────────────────────────────────────────────────────────────────
✓ Markdown structure: VALID

[PHASE 4] OUTPUT GENERATION
────────────────────────────────────────────────────────────────────────────────
✓ Written: document.md
  → File size: 5352 bytes

[PHASE 5] VERIFICATION
────────────────────────────────────────────────────────────────────────────────
✓ File integrity verified
✓ Content matches written output

================================================================================
✓ CONVERSION COMPLETE - READY FOR USE
================================================================================
```

## Quality Assurance

All scripts include:
- Structure validation
- Content integrity verification
- Comprehensive progress reporting
- Error handling and graceful fallbacks
- Type hints and documentation

## Requirements

- Python 3.10+
- pdfplumber (PDF extraction)
- pymupdf (fallback PDF handling)

## Contributing

Place new document conversion scripts in this directory following the same naming and documentation conventions.
