# 🎸 Spotify Basic Pitch — Acoustic Guitar AMT Suite

## Overview
Spotify Basic Pitch is a lightweight, instrument-agnostic neural network model for Automatic Music Transcription (AMT). It leverages a Harmonic Convolutional Neural Network (CNN) architecture optimized with TensorFlow Lite (TFLite), making it exceptionally fast (~1.1s on CPU/GPU) and suitable for client-side, mobile, or serverless deployments.

## Evaluation Summary on GuitarSet (10 Pieces / 1,543 Notes)
* **5 Solo Tracks:** Time: **1.17s** | Onset Recall: **93.9%** | Pitch F1: **82.7%** | Strict F1: **64.4%**
* **5 Comping Tracks:** Time: **1.04s** | Onset Recall: **91.0%** | Pitch F1: **77.0%** | Strict F1: **51.9%**

## Usage

### 1. Transcribe
```bash
python transcribe.py --audio ../../test_dataset/guitar/05_BN3-119-G_solo_mic.wav --output output.mid
```

### 2. Evaluate with mir_eval
```bash
python evaluate.py --jams ../../test_dataset/guitar/05_BN3-119-G_solo.jams --midi output.mid
```

### 3. Run 10-Piece Benchmark
```bash
python benchmark.py --run-num 1 --total-runs 5
```
