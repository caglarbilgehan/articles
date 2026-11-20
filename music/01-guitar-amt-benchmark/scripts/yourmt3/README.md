# 🏆 YourMT3+ — Multi-Track Music Transcription Transformer

## Overview
YourMT3+ (Gardner et al., 2024) is a next-generation sequence-to-sequence music transcription model based on the T5 Transformer architecture. It processes 16kHz audio through a convolutional front-end and a T5 encoder-decoder backbone to output tokenized multi-track MIDI events. It automatically identifies the acoustic guitar channel and assigns General MIDI Program 24 (Acoustic Guitar), achieving state-of-the-art results across both solo and polyphonic comping tracks.

## Evaluation Summary on GuitarSet (10 Pieces / 1,543 Notes)
* **5 Solo Tracks:** Time: **1.26s** | Onset Recall: **89.3%** | Pitch F1: **90.8%** | Strict F1: **81.9%**
* **5 Comping Tracks:** Time: **2.01s** | Onset Recall: **86.3%** | Pitch F1: **85.9%** | Strict F1: **73.9%**

## Usage
```bash
python transcribe.py --audio ../../test_dataset/guitar/05_BN3-119-G_solo_mic.wav --output output.mid --device cuda
python evaluate.py --jams ../../test_dataset/guitar/05_BN3-119-G_solo.jams --midi output.mid
python benchmark.py --run-num 1 --total-runs 5 --device cuda
```
