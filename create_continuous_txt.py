#!/usr/bin/env python3
import re

def org_to_continuous_txt(input_file, output_file):
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
    
    # Remove bullet points and list markers
    content = re.sub(r'^- ', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\* ', '', content, flags=re.MULTILINE)
    
    # Replace all line breaks with spaces to create continuous text
    content = re.sub(r'\n+', ' ', content)
    
    # Clean up multiple spaces
    content = re.sub(r' +', ' ', content)
    
    # Clean up the beginning and end
    content = content.strip()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Continuous text version created: {output_file}")

if __name__ == "__main__":
    org_to_continuous_txt("manuscript.org", "manuscript_continuous.txt")