#!/usr/bin/env python3
"""
Generate audiobook from manuscript.txt using ElevenLabs API
"""

import os
import sys
from pathlib import Path
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

def split_text_into_chunks(text, max_chars=5000):
    """
    Split text into chunks at paragraph boundaries.
    ElevenLabs has a character limit per request.
    """
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        # If adding this paragraph would exceed the limit
        if len(current_chunk) + len(para) + 2 > max_chars:
            if current_chunk:
                chunks.append(current_chunk.strip())
                current_chunk = para
            else:
                # Single paragraph is too long, split by sentences
                sentences = para.split('. ')
                for sentence in sentences:
                    if len(current_chunk) + len(sentence) + 2 > max_chars:
                        if current_chunk:
                            chunks.append(current_chunk.strip())
                        current_chunk = sentence + '.'
                    else:
                        current_chunk += sentence + '. '
        else:
            current_chunk += para + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def generate_audiobook(manuscript_path, output_dir="audiobook_output", api_key=None, voice_id=None):
    """
    Generate audiobook from manuscript using ElevenLabs

    Args:
        manuscript_path: Path to manuscript.txt
        output_dir: Directory to save audio files
        api_key: ElevenLabs API key (or set ELEVEN_API_KEY env var)
        voice_id: ElevenLabs voice ID (optional, defaults to Rachel)
    """

    # Initialize ElevenLabs client
    if api_key:
        client = ElevenLabs(api_key=api_key)
    else:
        # Will use ELEVEN_API_KEY environment variable
        client = ElevenLabs()

    # Default voice (Rachel) if not specified
    if not voice_id:
        voice_id = "21m00Tcm4TlvDq8ikWAM"  # Rachel voice

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # Read manuscript
    print(f"Reading manuscript from {manuscript_path}...")
    with open(manuscript_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Split into chunks
    print("Splitting text into chunks...")
    chunks = split_text_into_chunks(text, max_chars=4500)
    print(f"Created {len(chunks)} chunks")

    # Generate audio for each chunk
    audio_files = []
    for i, chunk in enumerate(chunks, 1):
        print(f"Generating audio for chunk {i}/{len(chunks)}...")

        try:
            audio = client.generate(
                text=chunk,
                voice=voice_id,
                model="eleven_turbo_v2_5",
                voice_settings=VoiceSettings(
                    stability=0.5,
                    similarity_boost=0.75,
                    style=0.0,
                    use_speaker_boost=True
                )
            )

            # Save chunk audio
            chunk_file = output_path / f"chunk_{i:04d}.mp3"
            with open(chunk_file, 'wb') as f:
                for audio_chunk in audio:
                    f.write(audio_chunk)

            audio_files.append(chunk_file)
            print(f"  Saved to {chunk_file}")

        except Exception as e:
            print(f"Error generating chunk {i}: {e}")
            continue

    print(f"\nGenerated {len(audio_files)} audio files in {output_dir}/")
    print("\nTo combine them into a single audiobook, run:")
    print(f"  ffmpeg -f concat -safe 0 -i <(for f in {output_dir}/chunk_*.mp3; do echo \"file '$PWD/$f'\"; done) -c copy {output_dir}/stolen_words_audiobook.mp3")

    # Create a file list for ffmpeg
    filelist_path = output_path / "filelist.txt"
    with open(filelist_path, 'w') as f:
        for audio_file in audio_files:
            f.write(f"file '{audio_file.absolute()}'\n")

    print(f"\nOr use the generated file list:")
    print(f"  ffmpeg -f concat -safe 0 -i {filelist_path} -c copy {output_dir}/stolen_words_audiobook.mp3")

    return audio_files

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate audiobook from manuscript using ElevenLabs")
    parser.add_argument("--manuscript", default="manuscript.txt", help="Path to manuscript file")
    parser.add_argument("--output-dir", default="audiobook_output", help="Output directory for audio files")
    parser.add_argument("--api-key", help="ElevenLabs API key (or set ELEVEN_API_KEY env var)")
    parser.add_argument("--voice-id", help="ElevenLabs voice ID (default: Rachel)")
    parser.add_argument("--list-voices", action="store_true", help="List available voices")

    args = parser.parse_args()

    if args.list_voices:
        client = ElevenLabs(api_key=args.api_key) if args.api_key else ElevenLabs()
        print("Available voices:")
        voices = client.voices.get_all()
        for voice in voices.voices:
            print(f"  {voice.name}: {voice.voice_id}")
        sys.exit(0)

    generate_audiobook(
        manuscript_path=args.manuscript,
        output_dir=args.output_dir,
        api_key=args.api_key,
        voice_id=args.voice_id
    )
