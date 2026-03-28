#!/usr/bin/env python3
"""
Unwrap text from PDF extraction to create continuous paragraphs.
Joins lines that are part of the same paragraph while preserving intentional breaks.
"""

def unwrap_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = []
    current_paragraph = []

    for line in lines:
        stripped = line.rstrip()

        # Empty line or very short line indicates paragraph break
        if len(stripped) == 0:
            if current_paragraph:
                result.append(' '.join(current_paragraph))
                result.append('')
                current_paragraph = []
        # Line with very few characters might be a heading or intentional break
        elif len(stripped) < 20 and current_paragraph:
            result.append(' '.join(current_paragraph))
            result.append(stripped)
            result.append('')
            current_paragraph = []
        else:
            # Add to current paragraph
            current_paragraph.append(stripped)

    # Don't forget the last paragraph
    if current_paragraph:
        result.append(' '.join(current_paragraph))

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))

if __name__ == '__main__':
    unwrap_text('manuscript.txt', 'manuscript_unwrapped.txt')
    print("Created manuscript_unwrapped.txt")
