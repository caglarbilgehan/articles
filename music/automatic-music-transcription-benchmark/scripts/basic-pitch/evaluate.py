#!/usr/bin/env python3
"""
Evaluate Transcribed MIDI against JAMS Ground Truth using mir_eval
Usage:
    python evaluate.py --jams <reference.jams> --midi <transcribed.mid>
"""

import os
import sys
import argparse
import numpy as np
import pretty_midi
import jams
import mir_eval

def load_jams_notes(jams_path: str):
    jam = jams.load(jams_path)
    ref_intervals, ref_pitches = [], []
    for ann in jam.annotations:
        if ann.namespace == 'note_midi':
            for obs in ann.data:
                ref_intervals.append([obs.time, obs.time + obs.duration])
                ref_pitches.append(obs.value)
    if not ref_intervals:
        return np.empty((0, 2)), np.empty(0)
    return np.array(ref_intervals), np.array(ref_pitches)

def load_midi_notes(midi_path: str):
    pm = pretty_midi.PrettyMIDI(midi_path)
    intervals, pitches = [], []
    for inst in pm.instruments:
        if not inst.is_drum:
            for note in inst.notes:
                intervals.append([note.start, note.end])
                pitches.append(note.pitch)
    if not intervals:
        return np.empty((0, 2)), np.empty(0)
    return np.array(intervals), np.array(pitches)

def evaluate(jams_path: str, midi_path: str):
    ref_intervals, ref_pitches = load_jams_notes(jams_path)
    est_intervals, est_pitches = load_midi_notes(midi_path)

    print("=" * 60)
    print(f" mir_eval Evaluation Report")
    print("=" * 60)
    print(f"Reference JAMS: {os.path.basename(jams_path)} ({len(ref_pitches)} notes)")
    print(f"Estimated MIDI: {os.path.basename(midi_path)} ({len(est_pitches)} notes)")
    print("-" * 60)

    if len(est_pitches) == 0:
        print("[ERROR] Estimated MIDI contains 0 notes!")
        return

    onset_prec, onset_rec, onset_f, _ = mir_eval.transcription.onset_precision_recall_f1(
        ref_intervals, est_intervals, onset_tolerance=0.05
    )
    pitch_prec, pitch_rec, pitch_f, _ = mir_eval.transcription.precision_recall_f1(
        ref_intervals, ref_pitches, est_intervals, est_pitches,
        onset_tolerance=0.05, pitch_tolerance=50.0, offset_ratio=None
    )
    strict_prec, strict_rec, strict_f, _ = mir_eval.transcription.precision_recall_f1(
        ref_intervals, ref_pitches, est_intervals, est_pitches,
        onset_tolerance=0.05, pitch_tolerance=50.0, offset_ratio=0.2, offset_min_tolerance=0.05
    )

    print(f"Onset Detection (±50ms)  : Precision: %{onset_prec*100:.1f} | Recall: %{onset_rec*100:.1f} | F1: %{onset_f*100:.1f}")
    print(f"Pitch Accuracy (±50cent) : Precision: %{pitch_prec*100:.1f} | Recall: %{pitch_rec*100:.1f} | F1: %{pitch_f*100:.1f}")
    print(f"Strict Note (With Offset): Precision: %{strict_prec*100:.1f} | Recall: %{strict_rec*100:.1f} | F1: %{strict_f*100:.1f}")
    print("=" * 60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate MIDI against JAMS ground truth")
    parser.add_argument("--jams", "-j", required=True, help="Path to reference .jams file")
    parser.add_argument("--midi", "-m", required=True, help="Path to transcribed .mid file")
    args = parser.parse_args()
    evaluate(args.jams, args.midi)
