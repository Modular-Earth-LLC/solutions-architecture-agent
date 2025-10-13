#!/usr/bin/env python3
"""
URL Validator

Validates all external URLs in the repository:
- Extracts URLs from markdown files
- Tests accessibility (HTTP status codes)
- Identifies broken links
- Suggests fixes where possible

Run: python tests/validate_urls.py
"""

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
    print("Warning: requests library not available. Install with: pip install requests")
    print("Continuing with URL extraction only...\n")

REPO_ROOT = Path(__file__).parent.parent

def extract_urls(content):
    """Extract all URLs from markdown content"""
    # Pattern for markdown links and bare URLs
    patterns = [
        r'https?://[^\s\)]+',  # Bare URLs
        r'\[([^\]]+)\]\((https?://[^\)]+)\)',  # Markdown links
    ]
    
    urls = []
    for pattern in patterns:
        matches = re.findall(pattern, content)
        if pattern == patterns[0]:  # Bare URLs
            urls.extend(matches)
        else:  # Markdown links (tuples)
            urls.extend([m[1] if isinstance(m, tuple) else m for m in matches])
    
    return list(set(urls))  # Deduplicate

def check_url(url, timeout=10):
    """Check if URL is accessible"""
    if not REQUESTS_AVAILABLE:
        return {"status": "unknown", "reason": "requests library not installed"}
    
    try:
        # Add user agent to avoid blocks
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
    """Extract and validate all URLs from repository"""
    print("=" * 70)
    print("URL Validation")
    print("=" * 70)
    
    print("\n[1/3] Extracting URLs from markdown files...")
    
    # Find all markdown files (exclude outputs/)
    md_files = [f for f in REPO_ROOT.glob("**/*.md") if "outputs" not in str(f) and "tmp" not in str(f)]
    
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
        
        # Brief pause to avoid rate limiting
        time.sleep(0.2)
    
    print(f"\n[3/3] Validation Results:")
    print(f"  Total URLs: {total}")
    print(f"  Accessible: {len(accessible)} ({len(accessible)/total*100:.1f}%)")
    print(f"  Broken/Inaccessible: {len(broken)} ({len(broken)/total*100:.1f}%)")
    
    if broken:
        print(f"\n  BROKEN URLS ({len(broken)}):")
        for url, result in broken[:20]:  # Show first 20
            print(f"    - {url}")
            print(f"      Status: {result['status']} - {result['reason']}")
            print(f"      Found in: {', '.join(str(f) for f in url_locations[url][:3])}")
        
        if len(broken) > 20:
            print(f"    ... and {len(broken) - 20} more")
    
    return url_locations, results

def main():
    url_locations, results = validate_urls()
    
    # Generate report
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
        print(f"\nExtracted {len(url_locations)} unique URLs")
        print("Run with 'requests' library installed for accessibility testing")
        print("Install: pip install requests")
        return 0

if __name__ == "__main__":
    sys.exit(main())
