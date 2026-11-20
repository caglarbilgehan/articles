# 🎸 Guitar Fret-String Assignment (FSA) & MIDI-to-Score (M2S) Benchmark
## Biomechanical Viterbi vs. Graph Theory & Voicing Evaluated on NYU MARL GuitarSet

This project contains the complete research, benchmark suite, evaluation pipelines, MusicXML generation engines, and publication-ready articles for investigating the guitar's inverse 1-to-many fretboard mapping problem—**Fret-String Assignment (FSA)** and **MIDI-to-Score (M2S)**.

I evaluated leading open-source FSA algorithms (**gtrsnipe**, **GuitarArranger**, **tuttut**, and a naive greedy baseline) across 10 diverse musical tracks (5 solo melodies + 5 polyphonic chord comping tracks) comprising **1,489 physical hexaphonic ground-truth notes** from the **NYU MARL GuitarSet (ISMIR 2018)**. In addition, I coupled the winning FSA solver with `music21` to generate production dual-stave **W3C MusicXML 4.0** scores (Standard Staff + 6-line TAB) directly from the transcribed audio stream.

---

## 📄 Article Versions

* 🇬🇧 [**ARTICLE-EN.md**](./ARTICLE-EN.md) — Complete English technical article prepared for Medium publication.
* 🇹🇷 [**ARTICLE-TR.md**](./ARTICLE-TR.md) — Tam kapsamlı Türkçe teknik makale taslağı.

---

## 💻 Hardware & System Specifications

* **Processor (CPU):** 13th Gen Intel(R) Core(TM) i7-13700HX (16 Cores, 24 Threads)
* **Graphics (GPU):** NVIDIA GeForce RTX 4060 Laptop GPU (8 GB GDDR6 VRAM, Driver 537.53)
* **Memory (RAM):** 48 GB DDR5 RAM
* **Operating System:** Ubuntu 26.04.1 LTS on Linux WSL2 (Kernel 6.6.114)
* **Software Stack:** Python 3.10, music21 v9.1.0, pretty_midi 0.2.10, jams 0.3.4, gtrsnipe, tuttut, GuitarArranger

---

## 📂 Directory Structure

```
02-guitar-m2s-fsa-benchmark/
├── README.md               # Project overview and documentation
├── ARTICLE-EN.md           # Full English technical article
├── ARTICLE-TR.md           # Full Turkish technical article
├── images/                 # High-resolution visual cards, pipeline diagrams & cover art
│   ├── article-image.jpg   # Publication cover hero image
│   ├── figure-01-fsa-pipeline-en.png / .tr.png
│   ├── table-01-fsa-leaderboard-en.png / .tr.png
│   └── table-02-m2s-matrix-en.png / .tr.png
├── scores/                 # 30 production W3C MusicXML scores (Standard Notation + 6-Line TAB)
├── test_dataset/           # 10 GuitarSet ground-truth hexaphonic sensor annotations (.jams)
└── scripts/                # Standalone reproducible evaluation & metric calculation scripts
    └── evaluation/
        ├── jams_reader.py  # Hexaphonic pickup ground-truth parser
        └── fsa_metrics.py  # String Accuracy, Fret MAE, and ergonomic shift calculators
```

---

## 🔗 Internal Resources & Scores

* 🎼 **W3C MusicXML Scores:** [`scores/`](./scores/)
* 🎸 **Reference GuitarSet Ground Truth:** [`test_dataset/`](./test_dataset/)
* 📊 **Evaluation & Metric Scripts:** [`scripts/evaluation/`](./scripts/evaluation/)
