# 🎼 Omnizart — Multi-Instrument Music Transcription

## Overview
Omnizart (MCTLab) is a comprehensive music information retrieval library featuring deep convolutional networks (MusiCNN) and Combined Frequency and Periodicity (CFP) feature representations. In stream inference mode, it processes audio frame-by-frame on CPU.

## Evaluation Summary on GuitarSet (10 Pieces / 1,543 Notes)
* **5 Solo Tracks:** Time: **13.17s** | Onset Recall: **31.2%** | Pitch F1: **24.8%** | Strict F1: **1.1%**
* **5 Comping Tracks:** Time: **13.82s** | Onset Recall: **10.1%** | Pitch F1: **9.6%** | Strict F1: **1.0%**

## Usage
```bash
python transcribe.py --audio ../../test_dataset/guitar/05_BN3-119-G_solo_mic.wav --output output.mid --mode Stream
python evaluate.py --jams ../../test_dataset/guitar/05_BN3-119-G_solo.jams --midi output.mid
python benchmark.py --run-num 1 --total-runs 5 --mode Stream
```
