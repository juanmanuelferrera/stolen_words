#!/usr/bin/env python3
"""
More aggressive paragraph merging for ElevenLabs.
"""

def merge_paragraphs_aggressive(input_file, output_file, max_short_length=400):
    """
    Merge consecutive paragraphs more aggressively.
    max_short_length: paragraphs shorter than this may be merged with adjacent ones
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into paragraphs
    paragraphs = content.split('\n\n')

    merged = []
    buffer = []

    for para in paragraphs:
        para = para.strip()

        if not para:  # Skip empty
            continue

        # If paragraph is very long, flush buffer and add it separately
        if len(para) > max_short_length:
            if buffer:
                merged.append(' '.join(buffer))
                buffer = []
            merged.append(para)
        else:
            # Add to buffer
            buffer.append(para)

            # Flush buffer when it gets reasonably large
            if len(' '.join(buffer)) > max_short_length * 3:
                merged.append(' '.join(buffer))
                buffer = []

    # Flush remaining
    if buffer:
        merged.append(' '.join(buffer))

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(merged))

    print(f"Original paragraphs: {len(paragraphs)}")
    print(f"Merged paragraphs: {len(merged)}")
    print(f"Reduction: {len(paragraphs) - len(merged)} paragraphs ({100*(len(paragraphs)-len(merged))//len(paragraphs)}% reduction)")
    print(f"Created: {output_file}")

if __name__ == '__main__':
    merge_paragraphs_aggressive('manuscript_elevenlabs.txt', 'manuscript_elevenlabs_merged.txt', max_short_length=400)
