# Benchmark 02: Comparative Analysis of Open-Source Fret-String Assignment (FSA) & MIDI-to-Score (M2S) Systems

This repository contains the publication materials, reproducible benchmark code, and experimental results for evaluating open-source guitar tablature generation and notation systems.

---

## 📌 Executive Summary

Translating symbolic polyphonic MIDI data into playable, ergonomically viable guitar tablature is an NP-hard inverse problem known as **Fret-String Assignment (FSA)**. This benchmark provides a factorial experimental comparison:

$$\text{MIDI Input} \xrightarrow{\quad\text{FSA Engine}\quad} (s_i, f_i) \xrightarrow{\quad\text{M2S Engine}\quad} \text{W3C MusicXML / Standard Tablature}$$

### Experimental Dimensions:
1. **Experiment 1 (Baseline / Control):** M2S without FSA (Quantifying error rates of default notation importers).
2. **Experiment 2 (FSA Shootout):** Comparing open-source FSA algorithms against GuitarSet physical hexaphonic pickup ground truth (`.jams`).
   - Graph Theory / HMM Viterbi (`tuttut`)
   - Heuristic Biomechanical Cost (`gtrsnipe`)
   - Genetic Algorithm / Voicer (`GuitarArranger`)
3. **Experiment 3 (Factorial M2S $\times$ FSA Matrix):** Evaluating final notation quality, MusicXML standard conformance, and sheet layout across `music21` and `MuseScore CLI`.

---

## 📁 Repository Structure

* `ARTICLE-EN.md`: Full publication-ready article in English (Medium / Research paper).
* `ARTICLE-TR.md`: Turkish translation and comprehensive draft.
* `images/`: High-resolution benchmark charts, architecture flowcharts, and generated score comparisons.
* `scores/`: 30 generated W3C MusicXML score and tablature files across all test tracks and pipelines.
* `scripts/`: Standalone reproducible evaluation scripts.
* `test_dataset/`: GuitarSet ground truth test annotations (`.jams`).
