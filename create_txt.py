#!/usr/bin/env python3
import re

def clean_org_to_txt(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove org mode directives and LaTeX commands
    content = re.sub(r'^#\+.*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^# .*$', '', content, flags=re.MULTILINE)
    
    # Remove LaTeX inline commands
    content = re.sub(r'@@latex:[^@]*@@', '', content)
    
    # Convert org formatting to plain text
    content = re.sub(r'\*\*([^*]+)\*\*', r'\1', content)  # Bold
    content = re.sub(r'\*([^*]+)\*', r'\1', content)      # Italics
    content = re.sub(r'/([^/]+)/', r'\1', content)        # Italics
    
    # Remove org links but keep the text
    content = re.sub(r'\[\[([^\]]+)\]\[([^\]]+)\]\]', r'\2', content)
    content = re.sub(r'\[\[([^\]]+)\]\]', r'\1', content)
    
    # Clean up multiple empty lines
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    # Remove leading/trailing whitespace from lines
    lines = [line.rstrip() for line in content.split('\n')]
    content = '\n'.join(lines)
    
    # Remove empty lines at the beginning
    content = content.lstrip('\n')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Clean text version created: {output_file}")

if __name__ == "__main__":
    clean_org_to_txt("manuscript.org", "manuscript_clean.txt")