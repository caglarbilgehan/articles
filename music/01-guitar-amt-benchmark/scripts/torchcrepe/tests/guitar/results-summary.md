# 📊 TorchCREPE Monophonic Pitch Estimator — 10-Piece 5-Stage Benchmark Summary

**Date:** November 20, 2026 — 16:09  
**Model:** TorchCREPE Monophonic Pitch Estimator  
**Evaluation Dataset:** NYU MARL GuitarSet (ISMIR 2018 - 10 Tracks: 5 Solo [421 Notes] + 5 Comping [1,122 Notes], Total: 1,543 Notes)  
**Total Iterations:** 5 Independent Runs (spaced 1 minute apart, timestamped MIDI outputs)  
**Archived MIDIs:** [`midi/guitar/`](../../midi/guitar)  

---

## 📌 Consolidated Summary Metrics

* **🎸 5 Solo Tracks Average:**
  * Average Processing Time: **6.55s**
  * Onset Recall (Note Attack): **%84.5**
  * Pitch F1-Score (Note + Timing): **%83.0**
  * Strict F1-Score (With Offset/Damping): **%68.1**

* **🎼 5 Comping / Chords Average:**
  * Average Processing Time: **9.27s**
  * Onset Recall (Chord Attacks): **%27.0**
  * Pitch F1-Score (Chord Accuracy): **%33.1**
  * Strict F1-Score (Chord Damping): **%17.5**

---

## 1. 🏁 5-Run Comparison Table

| Run | Time | Solo Time | Comp Time | Solo Onset Rec. | Solo Pitch F1 | Solo Strict F1 | Comp Onset Rec. | Comp Pitch F1 | Comp Strict F1 | Report Link |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Run 1** | `14:21` | 27.86s | 40.67s | **%84.8** | **%82.7** | %68.4 | **%27.3** | **%33.2** | %17.6 | [Report 1](./tests/guitar/result-20261119-1421.md) |
| **Run 2** | `14:28` | 1.22s | 1.42s | **%83.8** | **%82.4** | %67.0 | **%26.9** | **%32.9** | %17.3 | [Report 2](./tests/guitar/result-20261119-1428.md) |
| **Run 3** | `14:30` | 1.23s | 1.42s | **%85.1** | **%83.0** | %68.8 | **%27.1** | **%32.9** | %17.3 | [Report 3](./tests/guitar/result-20261119-1430.md) |
| **Run 4** | `14:31` | 1.22s | 1.42s | **%83.9** | **%82.9** | %67.7 | **%26.9** | **%33.1** | %17.5 | [Report 4](./tests/guitar/result-20261119-1431.md) |
| **Run 5** | `14:33` | 1.21s | 1.43s | **%84.8** | **%83.9** | %68.7 | **%27.0** | **%33.2** | %17.6 | [Report 5](./tests/guitar/result-20261119-1433.md) |
| **OVERALL AVERAGE** | — | **6.55s** | **9.27s** | **%84.5** | **%83.0** | **%68.1** | **%27.0** | **%33.1** | **%17.5** | — |

---

## 2. 🔬 Evaluation & Observations

* **Reproducibility:** Each iteration was independently executed with timestamped `.mid` outputs stored in the `midi/` directory and evaluated using `mir_eval`.
* **Metric Standards:** Evaluated against NYU MARL GuitarSet JAMS ground truth with 50ms onset tolerance and 50 cent pitch tolerance.
