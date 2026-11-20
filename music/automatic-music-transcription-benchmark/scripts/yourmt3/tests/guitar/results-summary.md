# 📊 YourMT3+ Multi-Track Transformer — 10-Piece 5-Stage Benchmark Summary

**Date:** November 20, 2026 — 16:09  
**Model:** YourMT3+ Multi-Track Transformer  
**Evaluation Dataset:** NYU MARL GuitarSet (ISMIR 2018 - 10 Tracks: 5 Solo [421 Notes] + 5 Comping [1,122 Notes], Total: 1,543 Notes)  
**Total Iterations:** 5 Independent Runs (spaced 1 minute apart, timestamped MIDI outputs)  
**Archived MIDIs:** [`midi/guitar/`](../../midi/guitar)  

---

## 📌 Consolidated Summary Metrics

* **🎸 5 Solo Tracks Average:**
  * Average Processing Time: **1.26s**
  * Onset Recall (Note Attack): **%89.3**
  * Pitch F1-Score (Note + Timing): **%90.8**
  * Strict F1-Score (With Offset/Damping): **%81.9**

* **🎼 5 Comping / Chords Average:**
  * Average Processing Time: **2.01s**
  * Onset Recall (Chord Attacks): **%86.3**
  * Pitch F1-Score (Chord Accuracy): **%85.9**
  * Strict F1-Score (Chord Damping): **%73.9**

---

## 1. 🏁 5-Run Comparison Table

| Run | Time | Solo Time | Comp Time | Solo Onset Rec. | Solo Pitch F1 | Solo Strict F1 | Comp Onset Rec. | Comp Pitch F1 | Comp Strict F1 | Report Link |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Run 1** | `14:02` | 1.63s | 2.15s | **%89.3** | **%90.8** | %81.9 | **%86.3** | **%85.9** | %73.9 | [Report 1](./tests/guitar/result-20261119-1402.md) |
| **Run 2** | `14:07` | 1.18s | 2.01s | **%89.3** | **%90.8** | %81.9 | **%86.3** | **%85.9** | %73.9 | [Report 2](./tests/guitar/result-20261119-1407.md) |
| **Run 3** | `14:09` | 1.17s | 1.96s | **%89.3** | **%90.8** | %81.9 | **%86.3** | **%85.9** | %73.9 | [Report 3](./tests/guitar/result-20261119-1409.md) |
| **Run 4** | `14:10` | 1.17s | 1.95s | **%89.3** | **%90.8** | %81.9 | **%86.3** | **%85.9** | %73.9 | [Report 4](./tests/guitar/result-20261119-1410.md) |
| **Run 5** | `14:12` | 1.14s | 1.97s | **%89.3** | **%90.8** | %81.9 | **%86.3** | **%85.9** | %73.9 | [Report 5](./tests/guitar/result-20261119-1412.md) |
| **OVERALL AVERAGE** | — | **1.26s** | **2.01s** | **%89.3** | **%90.8** | **%81.9** | **%86.3** | **%85.9** | **%73.9** | — |

---

## 2. 🔬 Evaluation & Observations

* **Reproducibility:** Each iteration was independently executed with timestamped `.mid` outputs stored in the `midi/` directory and evaluated using `mir_eval`.
* **Metric Standards:** Evaluated against NYU MARL GuitarSet JAMS ground truth with 50ms onset tolerance and 50 cent pitch tolerance.
