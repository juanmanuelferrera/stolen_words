#!/usr/bin/env python3
"""
Fix line wrapping in manuscript.txt for ElevenLabs audiobook generation.
Joins wrapped lines within paragraphs while preserving paragraph breaks.
"""

def fix_line_wrap(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = []
    current_paragraph = []

    for line in lines:
        stripped = line.strip()

        # Empty line means paragraph break
        if not stripped:
            if current_paragraph:
                # Join all lines in the paragraph with a space
                result.append(' '.join(current_paragraph))
                result.append('')  # Add blank line between paragraphs
                current_paragraph = []
        else:
            # Add this line to current paragraph
            current_paragraph.append(stripped)

    # Don't forget the last paragraph
    if current_paragraph:
        result.append(' '.join(current_paragraph))

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))

    print(f"Created {output_file} with unwrapped paragraphs for ElevenLabs")

if __name__ == '__main__':
    fix_line_wrap('manuscript.txt', 'manuscript_elevenlabs.txt')
