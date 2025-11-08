#!/usr/bin/env python3
"""
Script to analyze and suggest fixes for common layout problems in the manuscript
"""
import re

def analyze_layout_issues(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    lines = content.split('\n')
    
    print("📝 LAYOUT ANALYSIS FOR MANUSCRIPT.ORG")
    print("=" * 50)
    
    # 1. Check for excessive spacing
    for i, line in enumerate(lines, 1):
        if re.match(r'^\+LATEX: \\vspace\{[0-9.]+cm\}$', line):
            spacing = re.search(r'\{([0-9.]+)cm\}', line).group(1)
            if float(spacing) > 1.0:
                print(f"⚠️  Line {i}: Large spacing {spacing}cm - consider reducing")
    
    # 2. Look for potential widow/orphan problems
    section_headers = []
    for i, line in enumerate(lines, 1):
        if re.match(r'^\*\*.*\*\*$', line) or '@@latex:\\textbf{' in line:
            section_headers.append((i, line.strip()))
    
    print(f"\n📋 Found {len(section_headers)} section headers")
    print("Checking for headers that might need \\needspace protection:")
    
    for line_num, header in section_headers:
        # Check if header already has needspace
        prev_lines = lines[max(0, line_num-3):line_num-1]
        has_needspace = any('needspace' in l for l in prev_lines)
        
        if not has_needspace:
            print(f"📍 Line {line_num}: {header[:50]}... (needs \\needspace)")
    
    # 3. Check for very short paragraphs that might cause layout issues
    print(f"\n📏 PARAGRAPH LENGTH ANALYSIS")
    print("-" * 30)
    
    paragraphs = content.split('\n\n')
    short_paras = []
    
    for i, para in enumerate(paragraphs):
        # Skip LaTeX commands and headers
        if para.startswith('#+') or para.startswith('#'):
            continue
        if len(para.strip()) > 0 and len(para.strip()) < 100:
            words = len(para.split())
            if words < 15 and words > 0:
                short_paras.append((i, para.strip()[:50], words))
    
    print(f"Found {len(short_paras)} very short paragraphs (might cause layout issues):")
    for i, (para_num, text, word_count) in enumerate(short_paras[:10]):
        print(f"  {word_count} words: {text}...")
    
    # 4. Suggest specific fixes
    print(f"\n🔧 SUGGESTED FIXES")
    print("-" * 20)
    
    fixes = [
        "1. Add \\needspace{3\\baselineskip} before unprotected headers",
        "2. Consider combining very short paragraphs",
        "3. Reduce spacing larger than 1cm to 0.5cm or less",
        "4. Add \\raggedbottom in preamble for flexible page endings",
        "5. Use \\enlargethispage{\\baselineskip} for pages with too much white space"
    ]
    
    for fix in fixes:
        print(fix)

if __name__ == "__main__":
    analyze_layout_issues("manuscript.org")