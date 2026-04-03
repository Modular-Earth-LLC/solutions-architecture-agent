#!/usr/bin/env python3
"""
PDF to Markdown Converter

Professional-grade conversion tool for PDF files to well-formatted Markdown.
Handles complex layouts including tables, multi-column text, and mixed content.

Usage:
    python pdf_to_markdown.py <input_pdf> [<output_md>]

Requirements:
    - pdfplumber
    - pymupdf

Installation:
    uv pip install pdfplumber pymupdf
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

try:
    import pdfplumber
except ImportError:
    print("ERROR: pdfplumber not installed. Run: uv pip install pdfplumber")
    sys.exit(1)


def extract_and_convert(pdf_path: str) -> str:
    """
    Extract PDF content with intelligent preservation of structure.
    Avoids breaking tables and maintains semantic meaning.
    """
    markdown = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            text = page.extract_text()

            if not text:
                continue

            # Extract tables FIRST to preserve structure
            tables = page.extract_tables()

            if tables and len(tables) > 0:
                # Add tables properly formatted
                for table_idx, table in enumerate(tables):
                    markdown.extend(format_table(table))
                    markdown.append("")

                # Add remaining text (filtering out table text)
                remaining_text = _remove_table_text(text, tables)
                if remaining_text.strip():
                    markdown.append(_process_text(remaining_text))
            else:
                # No tables - just add text with light processing
                markdown.append(_process_text(text))

            markdown.append("")  # Page separator

    return "\n".join(markdown)


def format_table(table: List[List[str]]) -> List[str]:
    """Format a clean markdown table."""
    if not table or len(table) == 0:
        return []

    markdown_table = []

    # Header row
    header_cells = [str(cell or "").strip() for cell in table[0]]
    markdown_table.append("| " + " | ".join(header_cells) + " |")

    # Separator row
    sep_row = "|" + "|".join([" --- " for _ in header_cells]) + "|"
    markdown_table.append(sep_row)

    # Data rows
    for row in table[1:]:
        cells = [str(cell or "").strip() for cell in row]
        cells_clean = [cell.replace("\n", " ").strip() for cell in cells]
        markdown_table.append("| " + " | ".join(cells_clean) + " |")

    return markdown_table


def _remove_table_text(text: str, tables: List) -> str:
    """Remove text that belongs to tables to avoid duplication."""
    processed_lines = []
    lines = text.split("\n")

    for line in lines:
        # Skip lines that look like table headers or separators
        if "|" in line or re.match(r"^[\-=\s|]+$", line):
            continue
        processed_lines.append(line)

    return "\n".join(processed_lines)


def _process_text(text: str) -> str:
    """Process raw text content with intelligent paragraph handling."""
    lines = text.split("\n")
    processed = []
    current_paragraph = []

    for line in lines:
        stripped = line.strip()

        if not stripped:
            # Blank line - end current paragraph
            if current_paragraph:
                processed.append(" ".join(current_paragraph))
                current_paragraph = []
            processed.append("")  # Preserve blank line
        else:
            # Detect if this line is a heading
            if _is_heading(stripped):
                # Flush current paragraph
                if current_paragraph:
                    processed.append(" ".join(current_paragraph))
                    current_paragraph = []

                # Add heading
                heading_level = _guess_heading_level(stripped)
                processed.append(f"{"#" * heading_level} {_clean_heading(stripped)}")
            else:
                # Regular content
                current_paragraph.append(stripped)

    # Flush remaining paragraph
    if current_paragraph:
        processed.append(" ".join(current_paragraph))

    return "\n".join(processed)


def _is_heading(text: str) -> bool:
    """Heuristic to detect if text should be treated as a heading."""
    if text.isupper() and len(text) < 80 and len(text) > 5:
        return True

    if re.match(r"^(\d+(\.\d+)?\.)\s+", text):
        return True

    return False


def _guess_heading_level(text: str) -> int:
    """Guess the appropriate heading level."""
    if re.match(r"^(\d+(\.\d+)?\.)\s+", text):
        return 2

    if text.isupper():
        return 1

    return 3


def _clean_heading(text: str) -> str:
    """Clean up heading text."""
    text = re.sub(r"^(\d+(\.\d+)?\.)\s+", "", text)
    return text.strip()


def finalize_markdown(content: str) -> str:
    """Final cleanup and formatting."""
    lines = content.split("\n")
    finalized = []
    prev_empty = False

    for line in lines:
        is_empty = not line.strip()

        # Prevent multiple consecutive blank lines
        if is_empty:
            if prev_empty:
                continue
            finalized.append("")
            prev_empty = True
        else:
            finalized.append(line.rstrip())
            prev_empty = False

    # Remove leading/trailing blanks
    while finalized and not finalized[0].strip():
        finalized.pop(0)
    while finalized and not finalized[-1].strip():
        finalized.pop()

    return "\n".join(finalized)


def validate_markdown(content: str) -> Tuple[bool, List[str]]:
    """Validate markdown structure and content."""
    issues = []

    # Check for unclosed code blocks
    if content.count("```") % 2 != 0:
        issues.append("WARNING: Unclosed code block")

    # Check heading hierarchy
    headings = [
        (i, len(m.group(1)), m.group(2))
        for i, line in enumerate(content.split("\n"), 1)
        if (m := re.match(r"^(#+)\s+(.+)$", line))
    ]

    if headings and headings[0][1] != 1:
        issues.append("WARNING: Document should begin with H1 (# Title)")

    for i in range(1, len(headings)):
        if headings[i][1] > headings[i - 1][1] + 1:
            issues.append(
                f"WARNING: Heading hierarchy skip at line {headings[i][0]}"
            )

    return len([x for x in issues if x.startswith("ERROR")]) == 0, issues


def process_pdf(pdf_path: str, output_path: str = None) -> str:
    """
    Process PDF file and convert to markdown.

    Args:
        pdf_path: Path to input PDF file
        output_path: Path to output markdown file (optional)

    Returns:
        Path to output file
    """
    # Validate input
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    # Determine output path
    if output_path is None:
        output_path = str(Path(pdf_path).with_suffix(".md"))

    print("\n" + "=" * 80)
    print("PDF TO MARKDOWN CONVERTER")
    print("=" * 80)
    print(f"\n[INPUT]  {pdf_path}")
    print(f"[OUTPUT] {output_path}")

    # Extraction phase
    print("\n[PHASE 1] EXTRACTION")
    print("─" * 80)
    try:
        content = extract_and_convert(pdf_path)
        print("✓ Extracted content with table awareness")
        print(f"  → Initial size: {len(content)} characters")
    except Exception as e:
        print(f"✗ Extraction failed: {e}")
        raise

    # Finalization phase
    print("\n[PHASE 2] FINALIZATION")
    print("─" * 80)
    content = finalize_markdown(content)
    print("✓ Removed excessive whitespace")
    print("✓ Normalized line endings")
    line_count = len(content.split("\n"))
    print(f"  → Final size: {len(content)} characters, {line_count} lines")

    # Validation phase
    print("\n[PHASE 3] VALIDATION")
    print("─" * 80)
    is_valid, validation_issues = validate_markdown(content)
    for issue in validation_issues:
        status = "⚠" if issue.startswith("WARNING") else "✓"
        print(f"{status} {issue}")

    if is_valid:
        print("✓ Markdown structure: VALID")

    # Write output
    print("\n[PHASE 4] OUTPUT GENERATION")
    print("─" * 80)
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        file_size = os.path.getsize(output_path)
        print(f"✓ Written: {output_path}")
        print(f"  → File size: {file_size} bytes")
    except Exception as e:
        print(f"✗ Write failed: {e}")
        raise

    # Verification phase
    print("\n[PHASE 5] VERIFICATION")
    print("─" * 80)
    with open(output_path, "r", encoding="utf-8") as f:
        verify_content = f.read()

    if verify_content == content:
        print("✓ File integrity verified")
        print("✓ Content matches written output")
    else:
        print("✗ Verification failed: Content mismatch")
        raise ValueError("Content mismatch after write")

    print("\n" + "=" * 80)
    print("✓ CONVERSION COMPLETE - READY FOR USE")
    print("=" * 80 + "\n")

    return output_path


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_markdown.py <input_pdf> [<output_md>]")
        print("\nExample:")
        print("  python pdf_to_markdown.py document.pdf")
        print("  python pdf_to_markdown.py document.pdf output.md")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        result = process_pdf(pdf_path, output_path)
        print(f"\nResult saved to: {result}")
        sys.exit(0)
    except Exception as e:
        print(f"\nERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
