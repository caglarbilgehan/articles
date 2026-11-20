# 🎹 ByteDance CRNN — High-Resolution Piano Transcription

## Overview
ByteDance CRNN (Kong et al., 2021) is a state-of-the-art neural architecture combining ResNet convolutional layers with Bidirectional Gated Recurrent Units (BiGRU). Designed specifically for acoustic pianos (regressing onsets, offsets, and sustain pedals), it serves in this benchmark as a representative of piano-tailored inductive bias when applied to acoustic guitar.

## Evaluation Summary on GuitarSet (10 Pieces / 1,543 Notes)
* **5 Solo Tracks:** Time: **2.93s** | Onset Recall: **35.3%** | Pitch F1: **38.4%** | Strict F1: **18.5%**
* **5 Comping Tracks:** Time: **3.47s** | Onset Recall: **48.7%** | Pitch F1: **53.3%** | Strict F1: **26.9%**

## Usage
```bash
python transcribe.py --audio ../../test_dataset/guitar/00_Rock2-142-D_solo_mic.wav --output output.mid --device cuda
python evaluate.py --jams ../../test_dataset/guitar/00_Rock2-142-D_solo.jams --midi output.mid
python benchmark.py --run-num 1 --total-runs 5 --device cuda
```
