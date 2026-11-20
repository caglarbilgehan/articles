#!/usr/bin/env python3
"""
Spotify Basic Pitch - Audio to MIDI Transcription CLI
Usage:
    python transcribe.py --audio <input_audio.wav> [--output <output.mid>]
"""

import os
import sys
import time
import argparse
import logging

logging.getLogger().setLevel(logging.ERROR)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from basic_pitch.inference import predict_and_save
from basic_pitch import ICASSP_2022_MODEL_PATH

def transcribe(audio_path: str, output_midi_path: str = None) -> str:
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    if output_midi_path is None:
        base, _ = os.path.splitext(audio_path)
        output_midi_path = f"{base}_basic_pitch.mid"

    out_dir = os.path.dirname(os.path.abspath(output_midi_path))
    out_filename = os.path.basename(output_midi_path)
    if not out_dir:
        out_dir = "."
    os.makedirs(out_dir, exist_ok=True)

    print(f"[INFO] Transcribing: {audio_path}")
    start_time = time.time()

    predict_and_save(
        audio_path_list=[audio_path],
        output_directory=out_dir,
        save_midi=True,
        sonify_midi=False,
        save_model_outputs=False,
        save_notes=False,
        model_or_model_path=ICASSP_2022_MODEL_PATH
    )

    elapsed = time.time() - start_time
    expected_default = os.path.join(out_dir, f"{os.path.splitext(os.path.basename(audio_path))[0]}_basic_pitch.mid")
    if os.path.abspath(expected_default) != os.path.abspath(output_midi_path):
        if os.path.exists(expected_default):
            if os.path.exists(output_midi_path):
                os.remove(output_midi_path)
            os.rename(expected_default, output_midi_path)

    print(f"[OK] Transcription complete in {elapsed:.2f}s -> {output_midi_path}")
    return output_midi_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spotify Basic Pitch Audio-to-MIDI Transcription CLI")
    parser.add_argument("--audio", "-a", required=True, help="Path to input audio file (.wav, .mp3)")
    parser.add_argument("--output", "-o", default=None, help="Path to destination .mid file")
    args = parser.parse_args()
    transcribe(args.audio, args.output)
