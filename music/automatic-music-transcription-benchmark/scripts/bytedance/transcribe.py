#!/usr/bin/env python3
"""
ByteDance CRNN - Audio to MIDI Transcription CLI
Usage:
    python transcribe.py --audio <input_audio.wav> [--output <output.mid>] [--device cuda/cpu]
"""

import os
import sys
import time
import argparse
import warnings
warnings.filterwarnings("ignore")

import torch
import librosa
from piano_transcription_inference import PianoTranscription, sample_rate

def transcribe(audio_path: str, output_midi_path: str = None, device: str = None) -> str:
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    if output_midi_path is None:
        base, _ = os.path.splitext(audio_path)
        output_midi_path = f"{base}_bytedance.mid"

    out_dir = os.path.dirname(os.path.abspath(output_midi_path))
    if not out_dir:
        out_dir = "."
    os.makedirs(out_dir, exist_ok=True)

    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"

    print(f"[INFO] Initializing ByteDance CRNN (Device: {device})...")
    transcriptor = PianoTranscription(device=device, checkpoint_path=None)

    print(f"[INFO] Loading audio: {audio_path}")
    audio, _ = librosa.load(audio_path, sr=sample_rate, mono=True)

    print(f"[INFO] Transcribing with high-resolution regression...")
    start_time = time.time()
    transcriptor.transcribe(audio, output_midi_path)
    elapsed = time.time() - start_time

    print(f"[OK] Transcription complete in {elapsed:.2f}s -> {output_midi_path}")
    return output_midi_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ByteDance CRNN Audio-to-MIDI Transcription CLI")
    parser.add_argument("--audio", "-a", required=True, help="Path to input audio file (.wav, .mp3)")
    parser.add_argument("--output", "-o", default=None, help="Path to destination .mid file")
    parser.add_argument("--device", "-d", choices=["cuda", "cpu"], default=None, help="Compute device")
    args = parser.parse_args()
    transcribe(args.audio, args.output, args.device)
