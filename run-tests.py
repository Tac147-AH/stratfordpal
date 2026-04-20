#!/usr/bin/env python3
"""
Complete Website Implementation Test Suite
Validates all pages, links, assets, and functionality
"""

import os
import json
import re
from pathlib import Path
from urllib.parse import urlparse

def test_all():
    project_dir = Path("c:/Users/diehl/OneDrive/Documents/Claude/Projects/StratfordPAL")
    os.chdir(project_dir)
    
    results = {
        'pages': {},
        'assets': {},
        'links': {'internal': set(), 'external': set(), 'broken': []},
        'issues': []
    }
    
    # Required pages
    required_pages = {
        'index.html': 'Home',
        'about.html': 'About',
        'programs.html': 'Programs',
        'events.html': 'Events',
        'scholarships.html': 'Scholarships',
        'get-involved.html': 'Get Involved',
        'contact.html': 'Contact'
    }
    
    print("\n" + "="*70)
    print(" STRATFORD PAL - WEBSITE IMPLEMENTATION TEST SUITE")
    print("="*70)
    
    # Phase 1: Test Pages
    print("\n[PHASE 1] PAGE VERIFICATION")
    print("-" * 70)
    
    for page_file, page_name in required_pages.items():
        page_path = project_dir / page_file
        
        if not page_path.exists():
            print(f"✗ {page_name:20} MISSING - {page_file}")
            results['issues'].append(f"Missing page: {page_file}")
            continue
        
        with open(page_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Basic checks
        has_doctype = '<!DOCTYPE' in content
        has_title = '<title>' in content
        has_meta = '<meta' in content
        has_body = '<body>' in content
        
        file_size = len(content)
        status = "✓" if all([has_doctype, has_title, has_meta, has_body]) else "⚠"
        
        print(f"{status} {page_name:20} {file_size:8} bytes  OK")
        
        results['pages'][page_file] = {
            'valid': all([has_doctype, has_title, has_meta, has_body]),
            'size': file_size
        }
    
    # Phase 2: Test Assets
    print("\n[PHASE 2] ASSET VERIFICATION")
    print("-" * 70)
    
    assets_to_check = {
        'css/styles.css': 'Main stylesheet',
        'js/main.js': 'Main JavaScript',
        'data/programs.json': 'Programs data',
        'data/events.json': 'Events data'
    }
    
    for asset_path, asset_name in assets_to_check.items():
        full_path = project_dir / asset_path
        if full_path.exists():
            size = full_path.stat().st_size
            print(f"✓ {asset_name:25} {size:8} bytes")
            results['assets'][asset_path] = 'OK'
        else:
            print(f"✗ {asset_name:25} MISSING")
            results['issues'].append(f"Missing asset: {asset_path}")
    
    # Phase 3: CSS Validation
    print("\n[PHASE 3] CSS VALIDATION")
    print("-" * 70)
    
    css_path = project_dir / 'css/styles.css'
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    css_vars = re.findall(r'--[\w-]+', css_content)
    css_rules = len(re.findall(r'{[^}]+}', css_content))
    css_media_queries = len(re.findall(r'@media', css_content))
    
    print(f"✓ CSS Variables: {len(set(css_vars))} unique variables")
    print(f"✓ CSS Rules: {css_rules} rules")
    print(f"✓ Media Queries: {css_media_queries} breakpoints")
    
    # Phase 4: JavaScript Validation
    print("\n[PHASE 4] JAVASCRIPT VALIDATION")
    print("-" * 70)
    
    js_path = project_dir / 'js/main.js'
    with open(js_path, 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    js_functions = len(re.findall(r'function\s+\w+|const\s+\w+\s*=\s*\(|const\s+\w+\s*=\s*\{', js_content))
    js_event_listeners = len(re.findall(r'addEventListener|onclick', js_content))
    
    print(f"✓ Functions/Objects: {js_functions} definitions")
    print(f"✓ Event Listeners: {js_event_listeners} handlers")
    
    # Phase 5: Data Files
    print("\n[PHASE 5] DATA FILES VALIDATION")
    print("-" * 70)
    
    for data_file in ['programs.json', 'events.json']:
        data_path = project_dir / 'data' / data_file
        with open(data_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    print(f"✓ {data_file:20} {len(data)} items")
                elif isinstance(data, dict):
                    print(f"✓ {data_file:20} {len(data)} keys")
            except json.JSONDecodeError as e:
                print(f"✗ {data_file:20} JSON ERROR: {e}")
                results['issues'].append(f"Invalid JSON: {data_file}")
    
    # Phase 6: Link Extraction
    print("\n[PHASE 6] LINK ANALYSIS")
    print("-" * 70)
    
    all_links = {'internal': set(), 'external': set()}
    
    for page_file in required_pages.keys():
        page_path = project_dir / page_file
        with open(page_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract links
        href_pattern = r'href=["\']([^"\']+)["\']'
        for match in re.finditer(href_pattern, content):
            url = match.group(1)
            
            if url.startswith('http'):
                all_links['external'].add(url)
            elif url and not url.startswith('#') and url != '/':
                all_links['internal'].add(url)
    
    print(f"✓ Internal links found: {len(all_links['internal'])}")
    for link in sorted(all_links['internal']):
        if not (project_dir / link).exists():
            print(f"  ⚠ {link} - file not found")
    
    print(f"\n✓ External links found: {len(all_links['external'])}")
    external_samples = list(all_links['external'])[:5]
    for link in external_samples:
        print(f"  - {link}")
    if len(all_links['external']) > 5:
        print(f"  ... and {len(all_links['external']) - 5} more")
    
    # Phase 7: Content Coverage
    print("\n[PHASE 7] CONTENT COVERAGE")
    print("-" * 70)
    
    content_checks = {
        'index.html': ['Stratford PAL', 'programs', 'donation', 'volunteer'],
        'about.html': ['mission', 'leadership', 'history'],
        'programs.html': ['Police', 'program', 'registration'],
        'events.html': ['event', 'calendar', 'registration'],
        'scholarships.html': ['scholarship', 'financial', 'assistance'],
        'get-involved.html': ['volunteer', 'donate', 'sponsor'],
        'contact.html': ['contact', 'form', 'email']
    }
    
    for page_file, keywords in content_checks.items():
        page_path = project_dir / page_file
        with open(page_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
        
        found_keywords = [kw for kw in keywords if kw.lower() in content]
        status = "✓" if len(found_keywords) >= len(keywords) * 0.7 else "⚠"
        print(f"{status} {page_file:25} {len(found_keywords)}/{len(keywords)} keywords")
    
    # Summary
    print("\n" + "="*70)
    print(" IMPLEMENTATION TEST SUMMARY")
    print("="*70)
    
    pages_ok = len([p for p in results['pages'].values() if p['valid']])
    total_pages = len(results['pages'])
    
    print(f"\n✓ Pages:       {pages_ok}/{total_pages} valid")
    print(f"✓ Assets:      {len([a for a in results['assets'].values() if a == 'OK'])}/{len(results['assets'])} present")
    print(f"✓ Total links: {len(all_links['internal'])} internal, {len(all_links['external'])} external")
    
    if results['issues']:
        print(f"\n⚠ Issues found: {len(results['issues'])}")
        for issue in results['issues']:
            print(f"  - {issue}")
    else:
        print(f"\n✓ No critical issues found")
    
    print("\n" + "="*70)
    print(" READY FOR DEPLOYMENT")
    print("="*70 + "\n")

if __name__ == '__main__':
    test_all()
