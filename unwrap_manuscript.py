#!/usr/bin/env python3
"""
Convert manuscript.txt to continuous paragraphs
Removes line breaks within paragraphs, keeps paragraph breaks
"""

def unwrap_text(input_file, output_file):
    """
    Read text file and unwrap lines within paragraphs.
    Paragraphs are separated by blank lines.
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into paragraphs (separated by one or more blank lines)
    paragraphs = []
    current_para = []

    for line in content.split('\n'):
        line = line.strip()

        if line:  # Non-empty line
            current_para.append(line)
        else:  # Empty line - end of paragraph
            if current_para:
                # Join lines in paragraph with a space
                paragraphs.append(' '.join(current_para))
                current_para = []

    # Don't forget the last paragraph if file doesn't end with blank line
    if current_para:
        paragraphs.append(' '.join(current_para))

    # Join paragraphs with double newline
    unwrapped_text = '\n\n'.join(paragraphs)

    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(unwrapped_text)

    print(f"Unwrapped {len(paragraphs)} paragraphs")
    print(f"Output written to: {output_file}")

if __name__ == "__main__":
    unwrap_text('manuscript.txt', 'manuscript_unwrapped.txt')
