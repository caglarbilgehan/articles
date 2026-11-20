# 📊 Spotify Basic Pitch (ICASSP 2022) — 10-Piece 5-Stage Benchmark Summary

**Date:** November 20, 2026 — 16:09  
**Model:** Spotify Basic Pitch (ICASSP 2022)  
**Evaluation Dataset:** NYU MARL GuitarSet (ISMIR 2018 - 10 Tracks: 5 Solo [421 Notes] + 5 Comping [1,122 Notes], Total: 1,543 Notes)  
**Total Iterations:** 5 Independent Runs (spaced 1 minute apart, timestamped MIDI outputs)  
**Archived MIDIs:** [`midi/guitar/`](../../midi/guitar)  

---

## 📌 Consolidated Summary Metrics

* **🎸 5 Solo Tracks Average:**
  * Average Processing Time: **1.17s**
  * Onset Recall (Note Attack): **%93.9**
  * Pitch F1-Score (Note + Timing): **%82.7**
  * Strict F1-Score (With Offset/Damping): **%64.4**

* **🎼 5 Comping / Chords Average:**
  * Average Processing Time: **1.04s**
  * Onset Recall (Chord Attacks): **%91.0**
  * Pitch F1-Score (Chord Accuracy): **%77.0**
  * Strict F1-Score (Chord Damping): **%51.9**

---

## 1. 🏁 5-Run Comparison Table

| Run | Time | Solo Time | Comp Time | Solo Onset Rec. | Solo Pitch F1 | Solo Strict F1 | Comp Onset Rec. | Comp Pitch F1 | Comp Strict F1 | Report Link |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Run 1** | `14:14` | 1.25s | 1.04s | **%93.9** | **%82.7** | %64.4 | **%91.0** | **%77.0** | %51.9 | [Report 1](./tests/guitar/result-20261119-1414.md) |
| **Run 2** | `14:15` | 1.19s | 1.08s | **%93.9** | **%82.7** | %64.4 | **%91.0** | **%77.0** | %51.9 | [Report 2](./tests/guitar/result-20261119-1415.md) |
| **Run 3** | `14:16` | 1.14s | 1.01s | **%93.9** | **%82.7** | %64.4 | **%91.0** | **%77.0** | %51.9 | [Report 3](./tests/guitar/result-20261119-1416.md) |
| **Run 4** | `14:18` | 1.09s | 1.03s | **%93.9** | **%82.7** | %64.4 | **%91.0** | **%77.0** | %51.9 | [Report 4](./tests/guitar/result-20261119-1418.md) |
| **Run 5** | `14:19` | 1.19s | 1.05s | **%93.9** | **%82.7** | %64.4 | **%91.0** | **%77.0** | %51.9 | [Report 5](./tests/guitar/result-20261119-1419.md) |
| **OVERALL AVERAGE** | — | **1.17s** | **1.04s** | **%93.9** | **%82.7** | **%64.4** | **%91.0** | **%77.0** | **%51.9** | — |

---

## 2. 🔬 Evaluation & Observations

* **Reproducibility:** Each iteration was independently executed with timestamped `.mid` outputs stored in the `midi/` directory and evaluated using `mir_eval`.
* **Metric Standards:** Evaluated against NYU MARL GuitarSet JAMS ground truth with 50ms onset tolerance and 50 cent pitch tolerance.
