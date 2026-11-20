#!/usr/bin/env python3
"""
Omnizart - Multi-Instrument Music Transcription Script
Transcribes acoustic guitar audio to MIDI using Omnizart's Stream inference mode.
"""

import os
import sys
import time
import argparse
import warnings

warnings.filterwarnings("ignore")
import tensorflow as tf
from omnizart.music import app as music_app

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def find_dataset_dir() -> str:
    curr = os.path.dirname(os.path.abspath(__file__))
    for _ in range(6):
        candidate = os.path.join(curr, "test_dataset")
        if os.path.isdir(candidate):
            return candidate
        parent = os.path.dirname(curr)
        if parent == curr:
            break
        curr = parent
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../test_dataset"))

DATASET_DIR = find_dataset_dir()
MIDI_DIR = os.path.join(BASE_DIR, "midi", "guitar")
os.makedirs(MIDI_DIR, exist_ok=True)
DEFAULT_AUDIO = os.path.join(DATASET_DIR, "guitar", "05_BN3-119-G_solo_mic.wav")

def main():
    parser = argparse.ArgumentParser(description="Omnizart Audio to MIDI Transcription CLI")
    parser.add_argument("--audio", "-a", default=DEFAULT_AUDIO, help="Path to input audio file")
    parser.add_argument("--output", "-o", default=None, help="Path to output .mid file")
    parser.add_argument("--mode", "-m", choices=["Stream", "Pop", "Classical"], default="Stream", help="Transcription mode")
    args = parser.parse_args()

    audio_file = args.audio
    if not os.path.isabs(audio_file):
        audio_file = os.path.abspath(audio_file)

    if not os.path.isfile(audio_file):
        print(f"[ERROR] Audio file not found: {audio_file}")
        sys.exit(1)

    print(f"[INFO] Audio file: {audio_file}")
    print(f"[INFO] Mode: {args.mode}")

    out_file = args.output
    if not out_file:
        base_name = os.path.splitext(os.path.basename(audio_file))[0]
        out_file = os.path.join(MIDI_DIR, f"{base_name}_omnizart.mid")

    out_dir = os.path.dirname(os.path.abspath(out_file))

    print("[INFO] Initializing Omnizart music transcription...")
    start_tx = time.time()
    music_app.transcribe(audio_file, model_path=args.mode, output=out_dir)
    elapsed = time.time() - start_tx

    expected_name = os.path.splitext(os.path.basename(audio_file))[0] + ".mid"
    generated_file = os.path.join(out_dir, expected_name)

    if os.path.isfile(generated_file):
        if os.path.abspath(generated_file) != os.path.abspath(out_file):
            if os.path.exists(out_file):
                os.remove(out_file)
            os.rename(generated_file, out_file)
        print(f"[OK] Transcription complete in {elapsed:.2f}s")
        print(f"--> Saved to: {out_file}")
    else:
        print("[ERROR] MIDI output could not be generated!")

if __name__ == "__main__":
    main()
