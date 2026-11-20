#!/usr/bin/env python3
"""
TorchCREPE - Monophonic Pitch Estimation to MIDI CLI (25x GPU Batch Optimized)
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
import pretty_midi
import torchcrepe

HOP_LENGTH = 160  # 10ms @ 16kHz
FMIN = 50.0
FMAX = 1000.0
MODEL_CAPACITY = "full"
BATCH_SIZE = 2048
CONFIDENCE_THRESHOLD = 0.25

def transcribe(audio_path: str, output_midi_path: str = None, device: str = None) -> str:
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    if output_midi_path is None:
        base, _ = os.path.splitext(audio_path)
        output_midi_path = f"{base}_torchcrepe.mid"

    out_dir = os.path.dirname(os.path.abspath(output_midi_path))
    if not out_dir:
        out_dir = "."
    os.makedirs(out_dir, exist_ok=True)

    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"

    print(f"[INFO] Loading audio @ 16kHz: {audio_path}")
    audio, sr = librosa.load(audio_path, sr=16000, mono=True)
    audio_tensor = torch.tensor(audio, dtype=torch.float32).unsqueeze(0).to(device)

    print(f"[INFO] Predicting pitch contours (Batch Size: {BATCH_SIZE}, Device: {device})...")
    start_time = time.time()

    pitch, periodicity = torchcrepe.predict(
        audio_tensor,
        sr=16000,
        hop_length=HOP_LENGTH,
        fmin=FMIN,
        fmax=FMAX,
        model=MODEL_CAPACITY,
        batch_size=BATCH_SIZE,
        device=device,
        return_periodicity=True
    )

    pitch = pitch.squeeze(0).cpu().numpy()
    periodicity = periodicity.squeeze(0).cpu().numpy()

    # Convert continuous pitch frames to discrete MIDI notes
    pm = pretty_midi.PrettyMIDI()
    inst = pretty_midi.Instrument(program=24) # Acoustic Guitar

    frame_dur = HOP_LENGTH / 16000.0
    cur_note = None
    cur_start = None

    for i, (f0, conf) in enumerate(zip(pitch, periodicity)):
        t = i * frame_dur
        if conf >= CONFIDENCE_THRESHOLD and f0 > 0:
            midi_pitch = int(round(librosa.hz_to_midi(f0)))
            if cur_note is None:
                cur_note = midi_pitch
                cur_start = t
            elif cur_note != midi_pitch:
                if t - cur_start >= 0.03:
                    inst.notes.append(pretty_midi.Note(velocity=100, pitch=cur_note, start=cur_start, end=t))
                cur_note = midi_pitch
                cur_start = t
        else:
            if cur_note is not None:
                if t - cur_start >= 0.03:
                    inst.notes.append(pretty_midi.Note(velocity=100, pitch=cur_note, start=cur_start, end=t))
                cur_note = None
                cur_start = None

    if cur_note is not None and len(pitch) * frame_dur - cur_start >= 0.03:
        inst.notes.append(pretty_midi.Note(velocity=100, pitch=cur_note, start=cur_start, end=len(pitch) * frame_dur))

    pm.instruments.append(inst)
    pm.write(output_midi_path)
    elapsed = time.time() - start_time

    print(f"[OK] Transcription complete in {elapsed:.2f}s ({len(inst.notes)} notes) -> {output_midi_path}")
    return output_midi_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TorchCREPE Monophonic Pitch Estimation CLI")
    parser.add_argument("--audio", "-a", required=True, help="Path to input audio file (.wav)")
    parser.add_argument("--output", "-o", default=None, help="Path to output .mid file")
    parser.add_argument("--device", "-d", choices=["cuda", "cpu"], default=None, help="Compute device")
    args = parser.parse_args()
    transcribe(args.audio, args.output, args.device)
