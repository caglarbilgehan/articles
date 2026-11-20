#!/usr/bin/env python3
"""
YourMT3+ - Multi-Task & Multi-Track Music Transcription Script
Transcribes acoustic guitar audio into General MIDI multi-track events
using the YourMT3+ Transformer model.
"""

import os
import sys
import time
import argparse
import warnings

warnings.filterwarnings("ignore")
import torch
import torchaudio
import pretty_midi

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SPACE_DIR = os.path.join(BASE_DIR, "YourMT3-space")
sys.path.insert(0, SPACE_DIR)
sys.path.insert(0, os.path.join(SPACE_DIR, "amt/src"))
os.chdir(SPACE_DIR)

from model_helper import load_model_checkpoint, transcribe

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
    parser = argparse.ArgumentParser(description="YourMT3+ Audio to MIDI Transcription CLI")
    parser.add_argument("--audio", "-a", default=DEFAULT_AUDIO, help="Path to input audio file")
    parser.add_argument("--output", "-o", default=None, help="Path to output .mid file")
    parser.add_argument("--device", "-d", choices=["cuda", "cpu"], default="cuda", help="Inference device")
    args = parser.parse_args()

    audio_file = args.audio
    if not os.path.isabs(audio_file):
        audio_file = os.path.abspath(audio_file)

    if not os.path.isfile(audio_file):
        print(f"[ERROR] Audio file not found: {audio_file}")
        sys.exit(1)

    device = args.device if torch.cuda.is_available() else "cpu"
    print(f"[INFO] Using device: {device}")
    print(f"[INFO] Audio file: {audio_file}")

    print("[INFO] Loading YourMT3+ checkpoint...")
    start_load = time.time()
    model = load_model_checkpoint(device=device)
    print(f"[INFO] Model loaded in {time.time() - start_load:.2f}s")

    print("[INFO] Running transcription...")
    start_tx = time.time()
    out_midi_raw = transcribe(model, audio_file)
    elapsed = time.time() - start_tx

    out_file = args.output
    if not out_file:
        base_name = os.path.splitext(os.path.basename(audio_file))[0]
        out_file = os.path.join(MIDI_DIR, f"{base_name}_yourmt3.mid")

    if os.path.exists(out_midi_raw):
        import shutil
        shutil.move(out_midi_raw, out_file)
        print(f"[OK] Transcription complete in {elapsed:.2f}s")
        print(f"--> Saved to: {out_file}")
    else:
        print("[ERROR] Output MIDI could not be created!")

if __name__ == "__main__":
    main()
