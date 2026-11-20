# 📊 Omnizart Music (Stream Mode) — 10-Piece 5-Stage Benchmark Summary

**Date:** November 20, 2026 — 16:09  
**Model:** Omnizart Music (Stream Mode)  
**Evaluation Dataset:** NYU MARL GuitarSet (ISMIR 2018 - 10 Tracks: 5 Solo [421 Notes] + 5 Comping [1,122 Notes], Total: 1,543 Notes)  
**Total Iterations:** 5 Independent Runs (spaced 1 minute apart, timestamped MIDI outputs)  
**Archived MIDIs:** [`midi/guitar/`](../../midi/guitar)  

---

## 📌 Consolidated Summary Metrics

* **🎸 5 Solo Tracks Average:**
  * Average Processing Time: **13.17s**
  * Onset Recall (Note Attack): **%31.2**
  * Pitch F1-Score (Note + Timing): **%24.8**
  * Strict F1-Score (With Offset/Damping): **%1.1**

* **🎼 5 Comping / Chords Average:**
  * Average Processing Time: **14.66s**
  * Onset Recall (Chord Attacks): **%10.1**
  * Pitch F1-Score (Chord Accuracy): **%9.6**
  * Strict F1-Score (Chord Damping): **%1.0**

---

## 1. 🏁 5-Run Comparison Table

| Run | Time | Solo Time | Comp Time | Solo Onset Rec. | Solo Pitch F1 | Solo Strict F1 | Comp Onset Rec. | Comp Pitch F1 | Comp Strict F1 | Report Link |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Run 1** | `14:34` | 11.34s | 12.39s | **%31.2** | **%24.8** | %1.1 | **%10.1** | **%9.6** | %1.0 | [Report 1](./tests/guitar/result-20261119-1434.md) |
| **Run 2** | `14:38` | 11.47s | 13.79s | **%31.2** | **%24.8** | %1.1 | **%10.1** | **%9.6** | %1.0 | [Report 2](./tests/guitar/result-20261119-1438.md) |
| **Run 3** | `14:42` | 13.30s | 14.60s | **%31.2** | **%24.8** | %1.1 | **%10.1** | **%9.6** | %1.0 | [Report 3](./tests/guitar/result-20261119-1442.md) |
| **Run 4** | `14:45` | 13.05s | 13.86s | **%31.2** | **%24.8** | %1.1 | **%10.1** | **%9.6** | %1.0 | [Report 4](./tests/guitar/result-20261119-1445.md) |
| **Run 5** | `14:49` | 16.67s | 18.64s | **%31.2** | **%24.8** | %1.1 | **%10.1** | **%9.6** | %1.0 | [Report 5](./tests/guitar/result-20261119-1449.md) |
| **OVERALL AVERAGE** | — | **13.17s** | **14.66s** | **%31.2** | **%24.8** | **%1.1** | **%10.1** | **%9.6** | **%1.0** | — |

---

## 2. 🔬 Evaluation & Observations

* **Reproducibility:** Each iteration was independently executed with timestamped `.mid` outputs stored in the `midi/` directory and evaluated using `mir_eval`.
* **Metric Standards:** Evaluated against NYU MARL GuitarSet JAMS ground truth with 50ms onset tolerance and 50 cent pitch tolerance.
