#!/usr/bin/env python3
"""
URL Validator

Validates external URLs in repository documentation:
- Extracts URLs from scoped markdown files (docs, README, guides)
- Tests accessibility (HTTP status codes) when requests is installed
- Identifies broken links
- Configurable scope via tests/url_validation_scope.json

Run: python tests/validate_urls.py
"""

import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse
from collections import defaultdict

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("Note: requests library not available. Running extraction-only mode.")
    print("Install with: pip install requests\n")

REPO_ROOT = Path(__file__).parent.parent
SCOPE_CONFIG = Path(__file__).parent / "url_validation_scope.json"


def load_scope_config() -> dict:
    """Load include/exclude paths from scope config file."""
    if SCOPE_CONFIG.exists():
        with open(SCOPE_CONFIG, "r", encoding="utf-8") as f:
            return json.load(f)
    # Default scope if config missing
    return {
        "include_paths": [
            "README.md",
            "ARCHITECTURE.md",
            "CONTRIBUTING.md",
            "DESIGN_RATIONALE.md",
            "CODE_OF_CONDUCT.md",
            "SECURITY.md",
            "docs/",
            "tests/README.md",
            "knowledge_base/README.md",
            "examples/README.md"
        ],
        "exclude_paths": [
            ".claude/plans/",
            "archive/",
            "templates/",
            "outputs/",
            "tmp/"
        ]
    }


def get_scoped_files(config: dict) -> list[Path]:
    """Return markdown files matching the configured scope."""
    include_paths = config.get("include_paths", [])
    exclude_paths = config.get("exclude_paths", [])

    files = []
    for inc in include_paths:
        target = REPO_ROOT / inc
        if target.is_file() and target.suffix == ".md":
            files.append(target)
        elif target.is_dir():
            files.extend(target.glob("**/*.md"))

    # Apply exclusions
    filtered = []
    for f in files:
        rel = str(f.relative_to(REPO_ROOT)).replace("\\", "/")
        excluded = any(rel.startswith(ex) for ex in exclude_paths)
        if not excluded:
            filtered.append(f)

    return sorted(set(filtered))


def extract_urls(content: str) -> list[str]:
    """Extract URLs from markdown content with proper boundary handling."""
    urls = set()

    # Markdown links: [text](url)
    for match in re.finditer(r'\[([^\]]*)\]\((https?://[^\)]+)\)', content):
        urls.add(match.group(2).strip())

    # Bare URLs (not inside markdown link parens)
    for match in re.finditer(r'(?<!\()(https?://[^\s<>\[\]]+)', content):
        url = match.group(0)
        # Strip trailing punctuation that's not part of the URL
        url = url.rstrip('",`\')>;.')
        # Strip trailing ) only if there's no matching ( in the URL
        while url.endswith(')') and url.count('(') < url.count(')'):
            url = url[:-1]
        if url:
            urls.add(url)

    return list(urls)


def check_url(url: str, timeout: int = 10) -> dict:
    """Check if URL is accessible."""
    if not REQUESTS_AVAILABLE:
        return {"status": "unknown", "reason": "requests library not installed"}

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.head(url, timeout=timeout, headers=headers, allow_redirects=True)

        # Some servers don't support HEAD, try GET
        if response.status_code == 405:
            response = requests.get(url, timeout=timeout, headers=headers, allow_redirects=True, stream=True)

        return {
            "status": response.status_code,
            "reason": response.reason,
            "accessible": response.status_code < 400
        }
    except requests.exceptions.Timeout:
        return {"status": "timeout", "reason": "Request timed out", "accessible": False}
    except requests.exceptions.ConnectionError:
        return {"status": "connection_error", "reason": "Could not connect", "accessible": False}
    except requests.exceptions.TooManyRedirects:
        return {"status": "redirect_error", "reason": "Too many redirects", "accessible": False}
    except Exception as e:
        return {"status": "error", "reason": str(e), "accessible": False}


def validate_urls():
    """Extract and validate all URLs from scoped repository files."""
    print("=" * 70)
    print("URL Validation")
    print("=" * 70)

    config = load_scope_config()
    print(f"\n[1/3] Extracting URLs from scoped markdown files...")

    md_files = get_scoped_files(config)
    print(f"  Scanning {len(md_files)} files (scope: {len(config.get('include_paths', []))} include paths)")

    url_locations = defaultdict(list)

    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
            urls = extract_urls(content)
            for url in urls:
                url_locations[url].append(md_file.relative_to(REPO_ROOT))
        except Exception as e:
            print(f"  Error reading {md_file}: {e}")

    print(f"  Found {len(url_locations)} unique URLs across {len(md_files)} files")

    # Categorize by domain
    domains = defaultdict(list)
    for url in url_locations.keys():
        domain = urlparse(url).netloc
        domains[domain].append(url)

    print(f"  Domains: {len(domains)}")
    for domain, urls in sorted(domains.items(), key=lambda x: len(x[1]), reverse=True)[:10]:
        print(f"    - {domain}: {len(urls)} URLs")

    print("\n[2/3] Testing URL accessibility...")

    if not REQUESTS_AVAILABLE:
        print("  Skipping accessibility checks (requests not installed)")
        print("  Install with: pip install requests")
        return url_locations, {}

    results = {}
    broken = []
    accessible = []

    total = len(url_locations)
    for i, url in enumerate(url_locations.keys(), 1):
        if i % 20 == 0:
            print(f"  Progress: {i}/{total} URLs checked...")
            time.sleep(1)  # Rate limiting

        result = check_url(url)
        results[url] = result

        if result["accessible"]:
            accessible.append(url)
        else:
            broken.append((url, result))

        time.sleep(0.2)

    print(f"\n[3/3] Validation Results:")
    print(f"  Total URLs: {total}")
    print(f"  Accessible: {len(accessible)} ({len(accessible)/total*100:.1f}%)")
    print(f"  Broken/Inaccessible: {len(broken)} ({len(broken)/total*100:.1f}%)")

    if broken:
        print(f"\n  BROKEN URLS ({len(broken)}):")
        for url, result in broken[:20]:
            print(f"    - {url}")
            print(f"      Status: {result['status']} - {result['reason']}")
            print(f"      Found in: {', '.join(str(f) for f in url_locations[url][:3])}")

        if len(broken) > 20:
            print(f"    ... and {len(broken) - 20} more")

    return url_locations, results


def main():
    url_locations, results = validate_urls()

    print("\n" + "=" * 70)
    print("URL Validation Report")
    print("=" * 70)

    if results:
        broken = [(url, res) for url, res in results.items() if not res["accessible"]]

        if broken:
            print(f"\nACTION REQUIRED: {len(broken)} broken/inaccessible URLs found")
            print("Review and fix or remove broken links")
            return 1
        else:
            print("\nSUCCESS: All URLs are accessible!")
            return 0
    else:
        print(f"\nExtracted {len(url_locations)} unique URLs (extraction-only mode)")
        if not REQUESTS_AVAILABLE:
            print("Install requests for accessibility testing: pip install requests")
        return 0


if __name__ == "__main__":
    sys.exit(main())
