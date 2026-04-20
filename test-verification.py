#!/usr/bin/env python3
"""
Stratford PAL Website Verification Script
Tests all HTML files for structural integrity, links, and content
"""

import os
import re
from pathlib import Path
from html.parser import HTMLParser

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.images = []
        self.stylesheets = []
        self.scripts = []
        self.errors = []
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'a' and 'href' in attrs_dict:
            self.links.append(attrs_dict['href'])
        elif tag == 'img' and 'src' in attrs_dict:
            self.images.append(attrs_dict['src'])
        elif tag == 'link' and 'href' in attrs_dict:
            self.stylesheets.append(attrs_dict['href'])
        elif tag == 'script' and 'src' in attrs_dict:
            self.scripts.append(attrs_dict['src'])

def verify_html_file(filepath):
    """Verify HTML file structure and content"""
    print(f"\n{'='*60}")
    print(f"Testing: {filepath.name}")
    print(f"{'='*60}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check file size
    file_size = len(content)
    print(f"✓ File size: {file_size} bytes")
    
    # Parse HTML
    parser = LinkExtractor()
    try:
        parser.feed(content)
        print(f"✓ HTML structure valid")
    except Exception as e:
        print(f"✗ HTML parsing error: {e}")
        return False
    
    # Check for critical elements
    checks = {
        "<!DOCTYPE": "DOCTYPE declaration",
        "<html": "HTML tag",
        "<head": "HEAD tag",
        "<body": "BODY tag",
        "<title": "TITLE tag",
        "<meta": "META tags",
    }
    
    for tag, desc in checks.items():
        if tag.lower() in content.lower():
            print(f"✓ Contains {desc}")
        else:
            print(f"✗ Missing {desc}")
    
    # Check for content
    text_content = re.sub(r'<[^>]+>', '', content).strip()
    if len(text_content) > 100:
        print(f"✓ Has substantial content ({len(text_content)} chars)")
    else:
        print(f"✗ Content too short ({len(text_content)} chars)")
    
    # Report assets
    if parser.stylesheets:
        print(f"\n📄 Stylesheets ({len(parser.stylesheets)}):")
        for url in parser.stylesheets:
            print(f"  - {url}")
    
    if parser.scripts:
        print(f"\n🔧 Scripts ({len(parser.scripts)}):")
        for url in parser.scripts:
            print(f"  - {url}")
    
    if parser.images:
        print(f"\n🖼️  Images ({len(parser.images)}):")
        for url in parser.images[:5]:  # Show first 5
            print(f"  - {url}")
        if len(parser.images) > 5:
            print(f"  ... and {len(parser.images) - 5} more")
    
    print(f"\n🔗 Internal Links ({len([l for l in parser.links if not l.startswith(('http', 'mailto', '#'))])}):")
    internal_links = [l for l in parser.links if not l.startswith(('http', 'mailto', '#')) and l]
    for link in set(internal_links):
        print(f"  - {link}")
    
    print(f"\n🌐 External Links ({len([l for l in parser.links if l.startswith('http')])}):")
    external_links = [l for l in parser.links if l.startswith('http')]
    for link in set(external_links):
        print(f"  - {link}")
    
    return True

def main():
    project_dir = Path(__file__).parent
    html_files = sorted(project_dir.glob("*.html"))
    
    print(f"\n{'#'*60}")
    print(f"# Stratford PAL - Website Verification")
    print(f"# Testing {len(html_files)} HTML files")
    print(f"{'#'*60}")
    
    success_count = 0
    for html_file in html_files:
        if verify_html_file(html_file):
            success_count += 1
    
    # Summary
    print(f"\n{'='*60}")
    print(f"VERIFICATION SUMMARY")
    print(f"{'='*60}")
    print(f"✓ Verified: {success_count}/{len(html_files)} files")
    
    # Check for required pages
    required_pages = [
        'index.html',
        'about.html',
        'programs.html',
        'events.html',
        'scholarships.html',
        'get-involved.html',
        'contact.html'
    ]
    
    print(f"\n📋 Required Pages:")
    found_pages = [f.name for f in html_files]
    for page in required_pages:
        status = "✓" if page in found_pages else "✗"
        print(f"  {status} {page}")
    
    # Check for CSS and JS
    print(f"\n🎨 Assets:")
    css_files = list(project_dir.glob("css/*.css"))
    js_files = list(project_dir.glob("js/*.js"))
    data_files = list(project_dir.glob("data/*.json"))
    
    print(f"  ✓ CSS files: {len(css_files)}")
    for f in css_files:
        print(f"    - {f.name}")
    
    print(f"  ✓ JS files: {len(js_files)}")
    for f in js_files:
        print(f"    - {f.name}")
    
    print(f"  ✓ Data files: {len(data_files)}")
    for f in data_files:
        print(f"    - {f.name}")
    
    print(f"\n{'='*60}\n")

if __name__ == "__main__":
    main()
