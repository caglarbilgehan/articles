# 🎸 Automatic Music Transcription (AMT) Benchmark Project
## 5 Deep Learning Architectures Evaluated on NYU MARL GuitarSet (250 Benchmark Runs)

This project contains the complete research, benchmark suite, evaluation pipelines, and final article for my comprehensive scientific study on **Automatic Music Transcription (AMT)** applied to acoustic guitar.

I evaluated **5 state-of-the-art deep learning architectures** across 10 diverse acoustic guitar tracks (5 single-note solo melodies + 5 polyphonic chord comping tracks) comprising **1,543 reference ground-truth notes** from the **NYU MARL GuitarSet (ISMIR 2018)**. Each model underwent 5 independent runs (250 total benchmark evaluations) on local hardware.

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
* **Deep Learning Stack:** Python 3.10, PyTorch 2.5.1 + CUDA 12.1, mir_eval 0.7

---

## 📂 Directory Structure

```
01-guitar-amt-benchmark/
├── README.md               # Project overview and documentation
├── ARTICLE-EN.md           # Full English technical article
├── ARTICLE-TR.md           # Full Turkish technical article
├── test_dataset/
│   └── guitar/             # 10 audio WAV files & JAMS sensor annotations (GuitarSet)
└── scripts/
    ├── MASTER_BENCHMARK_COMPARISON.md  # Consolidated master comparison report
    ├── summarize_benchmark.py          # Summary generator script
    ├── basic-pitch/        # Spotify Basic Pitch inference & benchmark suite
    ├── bytedance/          # ByteDance CRNN inference & benchmark suite
    ├── torchcrepe/         # TorchCREPE 25x GPU-optimized benchmark suite
    ├── yourmt3/            # YourMT3+ Transformer benchmark suite
    └── omnizart/           # Omnizart Music Stream benchmark suite
```

---

## 🔗 Internal Benchmark Reports

* 🏆 **Master Comparison Report:** [`scripts/MASTER_BENCHMARK_COMPARISON.md`](./scripts/MASTER_BENCHMARK_COMPARISON.md)
* 🎸 **Reference Guitar Dataset:** [`test_dataset/guitar/`](./test_dataset/guitar/)
* 📊 **5-Run Model Summaries:**
  * [`Spotify Basic Pitch (TFLite)`](./scripts/basic-pitch/tests/guitar/results-summary.md)
  * [`YourMT3+ (Transformer)`](./scripts/yourmt3/tests/guitar/results-summary.md)
  * [`ByteDance CRNN`](./scripts/bytedance/tests/guitar/results-summary.md)
  * [`TorchCREPE (Deep Conv)`](./scripts/torchcrepe/tests/guitar/results-summary.md)
  * [`Omnizart (Stream)`](./scripts/omnizart/tests/guitar/results-summary.md)
