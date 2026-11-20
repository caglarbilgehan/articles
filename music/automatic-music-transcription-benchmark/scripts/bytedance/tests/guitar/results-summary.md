# 📊 ByteDance CRNN (High-Resolution Piano Transcription) — 10-Piece 5-Stage Benchmark Summary

**Date:** November 20, 2026 — 16:09  
**Model:** ByteDance CRNN (High-Resolution Piano Transcription)  
**Evaluation Dataset:** NYU MARL GuitarSet (ISMIR 2018 - 10 Tracks: 5 Solo [421 Notes] + 5 Comping [1,122 Notes], Total: 1,543 Notes)  
**Total Iterations:** 5 Independent Runs (spaced 1 minute apart, timestamped MIDI outputs)  
**Archived MIDIs:** [`midi/guitar/`](../../midi/guitar)  

---

## 📌 Consolidated Summary Metrics

* **🎸 5 Solo Tracks Average:**
  * Average Processing Time: **2.93s**
  * Onset Recall (Note Attack): **%35.3**
  * Pitch F1-Score (Note + Timing): **%38.4**
  * Strict F1-Score (With Offset/Damping): **%18.5**

* **🎼 5 Comping / Chords Average:**
  * Average Processing Time: **3.50s**
  * Onset Recall (Chord Attacks): **%48.7**
  * Pitch F1-Score (Chord Accuracy): **%53.3**
  * Strict F1-Score (Chord Damping): **%26.9**

---

## 1. 🏁 5-Run Comparison Table

| Run | Time | Solo Time | Comp Time | Solo Onset Rec. | Solo Pitch F1 | Solo Strict F1 | Comp Onset Rec. | Comp Pitch F1 | Comp Strict F1 | Report Link |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Run 1** | `14:54` | 2.85s | 3.43s | **%35.3** | **%38.4** | %18.5 | **%48.7** | **%53.3** | %26.9 | [Report 1](./tests/guitar/result-20261119-1454.md) |
| **Run 2** | `14:56` | 2.90s | 3.54s | **%35.3** | **%38.4** | %18.5 | **%48.7** | **%53.3** | %26.9 | [Report 2](./tests/guitar/result-20261119-1456.md) |
| **Run 3** | `14:58` | 2.92s | 3.49s | **%35.3** | **%38.4** | %18.5 | **%48.7** | **%53.3** | %26.9 | [Report 3](./tests/guitar/result-20261119-1458.md) |
| **Run 4** | `15:00` | 2.83s | 3.56s | **%35.3** | **%38.4** | %18.5 | **%48.7** | **%53.3** | %26.9 | [Report 4](./tests/guitar/result-20261119-1500.md) |
| **Run 5** | `15:01` | 3.15s | 3.48s | **%35.3** | **%38.4** | %18.5 | **%48.7** | **%53.3** | %26.9 | [Report 5](./tests/guitar/result-20261119-1501.md) |
| **OVERALL AVERAGE** | — | **2.93s** | **3.50s** | **%35.3** | **%38.4** | **%18.5** | **%48.7** | **%53.3** | **%26.9** | — |

---

## 2. 🔬 Evaluation & Observations

* **Reproducibility:** Each iteration was independently executed with timestamped `.mid` outputs stored in the `midi/` directory and evaluated using `mir_eval`.
* **Metric Standards:** Evaluated against NYU MARL GuitarSet JAMS ground truth with 50ms onset tolerance and 50 cent pitch tolerance.
