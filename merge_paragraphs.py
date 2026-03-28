#!/usr/bin/env python3
"""
Merge shorter paragraphs in manuscript to reduce paragraph count for ElevenLabs.
Keeps longer paragraphs intact, merges shorter related ones.
"""

def merge_paragraphs(input_file, output_file, max_short_length=200):
    """
    Merge consecutive short paragraphs while keeping longer ones separate.
    max_short_length: paragraphs shorter than this may be merged with adjacent ones
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into paragraphs (double newline separates them)
    paragraphs = content.split('\n\n')

    merged = []
    buffer = []

    for para in paragraphs:
        para = para.strip()

        if not para:  # Skip empty paragraphs
            continue

        # If paragraph is long enough, flush buffer and add it separately
        if len(para) > max_short_length:
            if buffer:
                merged.append(' '.join(buffer))
                buffer = []
            merged.append(para)
        else:
            # Add short paragraph to buffer
            buffer.append(para)

            # If buffer gets too long, flush it
            if len(' '.join(buffer)) > max_short_length * 2:
                merged.append(' '.join(buffer))
                buffer = []

    # Don't forget remaining buffer
    if buffer:
        merged.append(' '.join(buffer))

    # Write output with double newlines between paragraphs
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(merged))

    print(f"Original paragraphs: {len(paragraphs)}")
    print(f"Merged paragraphs: {len(merged)}")
    print(f"Reduction: {len(paragraphs) - len(merged)} paragraphs")
    print(f"Created: {output_file}")

if __name__ == '__main__':
    merge_paragraphs('manuscript_elevenlabs.txt', 'manuscript_elevenlabs_merged.txt', max_short_length=200)
