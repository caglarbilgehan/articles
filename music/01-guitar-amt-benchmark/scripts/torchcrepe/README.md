# 🎸 TorchCREPE — Deep Convolutional Pitch Estimator

## Overview
TorchCREPE is a PyTorch implementation of CREPE (Kim et al., 2018), a deep convolutional neural network trained on time-domain audio signals for monophonic pitch estimation. It provides 10ms frame resolution and exceptional articulation tracking (vibrato, string bends, slides). By optimizing inference with `batch_size=2048`, inference time drops from ~37s down to **1.2s (25x speedup)** on CUDA GPU.

## Evaluation Summary on GuitarSet (10 Pieces / 1,543 Notes)
* **5 Solo Tracks:** Time: **1.22s** | Onset Recall: **84.5%** | Pitch F1: **83.0%** | Strict F1: **68.1%**
* **5 Comping Tracks:** Time: **1.28s** | Onset Recall: **27.0%** | Pitch F1: **33.1%** | Strict F1: **17.5%**

## Usage
```bash
python transcribe.py --audio ../../test_dataset/guitar/03_Funk1-97-C_solo_mic.wav --output output.mid --device cuda
python evaluate.py --jams ../../test_dataset/guitar/03_Funk1-97-C_solo.jams --midi output.mid
python benchmark.py --run-num 1 --total-runs 5 --device cuda
```
