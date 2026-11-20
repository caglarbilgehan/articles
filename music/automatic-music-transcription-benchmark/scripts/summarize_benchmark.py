#!/usr/bin/env python3
"""
Consolidated 5-Run Benchmark Summary Generator for AMT Models
Usage:
    python summarize_benchmark.py <model_dir_name> [instrument]
"""

import os
import sys
import re
import glob
from datetime import datetime


AMT_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_TITLES = {
    "yourmt3": "YourMT3+ Multi-Track Transformer",
    "basic-pitch": "Spotify Basic Pitch (ICASSP 2022)",
    "torchcrepe": "TorchCREPE Monophonic Pitch Estimator",
    "omnizart": "Omnizart Music (Stream Mode)",
    "bytedance": "ByteDance CRNN (High-Resolution Piano Transcription)"
}

def parse_result_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    ts_match = re.search(r"result-(\d{8}-\d{4})\.md", file_path)
    ts = ts_match.group(1) if ts_match else "N/A"
    time_part = ts.split("-")[1] if "-" in ts else ts
    time_display = f"{time_part[:2]}:{time_part[2:]}" if len(time_part) == 4 else ts

    c_clean = content.replace("*", "")
    
    solo_m = re.search(
        r"5 Solo (?:Average|Ortalama):\s*(?:Time|Süre):\s*([\d\.]+)s\s*\|\s*Onset Recall:\s*%([\d\.]+)\s*\|\s*Pitch Recall:\s*%([\d\.]+)\s*\|\s*Pitch F1:\s*%([\d\.]+)\s*\|\s*Strict F1:\s*%([\d\.]+)",
        c_clean, re.IGNORECASE
    )
    comp_m = re.search(
        r"5 Comping (?:Average|Ortalama):\s*(?:Time|Süre):\s*([\d\.]+)s\s*\|\s*Onset Recall:\s*%([\d\.]+)\s*\|\s*Pitch Recall:\s*%([\d\.]+)\s*\|\s*Pitch F1:\s*%([\d\.]+)\s*\|\s*Strict F1:\s*%([\d\.]+)",
        c_clean, re.IGNORECASE
    )

    if not solo_m or not comp_m:
        return None

    return {
        "file": file_path,
        "ts": ts,
        "time_display": time_display,
        "solo_time": float(solo_m.group(1)),
        "solo_orec": float(solo_m.group(2)),
        "solo_prec": float(solo_m.group(3)),
        "solo_pf1": float(solo_m.group(4)),
        "solo_sf1": float(solo_m.group(5)),
        "comp_time": float(comp_m.group(1)),
        "comp_orec": float(comp_m.group(2)),
        "comp_prec": float(comp_m.group(3)),
        "comp_pf1": float(comp_m.group(4)),
        "comp_sf1": float(comp_m.group(5)),
    }

def generate_summary(model_name, instrument="guitar"):
    target_dir = os.path.join(AMT_DIR, model_name)
    inst_tests_dir = os.path.join(target_dir, "tests", instrument)
    tests_dir = inst_tests_dir if os.path.isdir(inst_tests_dir) else os.path.join(target_dir, "tests")
    if not os.path.isdir(tests_dir):
        print(f"[ERROR] Directory not found: {tests_dir}")
        return

    result_files = sorted(glob.glob(os.path.join(tests_dir, "result-*.md")))
    if not result_files:
        print(f"[ERROR] No result-*.md files found in {tests_dir}")
        return

    parsed = []
    for rf in result_files:
        p = parse_result_file(rf)
        if p:
            parsed.append(p)

    if not parsed:
        print(f"[WARNING] No valid benchmark results found for {model_name}")
        return

    parsed = parsed[-5:]
    model_title = MODEL_TITLES.get(model_name, model_name)
    now_str = datetime.now().strftime("%B %d, %Y — %H:%M")

    table_rows = ""
    for idx, r in enumerate(parsed, 1):
        rel_file = os.path.relpath(r['file'], target_dir)
        table_rows += (
            f"| **Run {idx}** | `{r['time_display']}` | "
            f"{r['solo_time']:.2f}s | {r['comp_time']:.2f}s | "
            f"**%{r['solo_orec']:.1f}** | **%{r['solo_pf1']:.1f}** | %{r['solo_sf1']:.1f} | "
            f"**%{r['comp_orec']:.1f}** | **%{r['comp_pf1']:.1f}** | %{r['comp_sf1']:.1f} | "
            f"[Report {idx}](./{rel_file}) |\n"
        )

    avg_st = sum(r['solo_time'] for r in parsed) / len(parsed)
    avg_ct = sum(r['comp_time'] for r in parsed) / len(parsed)
    avg_so = sum(r['solo_orec'] for r in parsed) / len(parsed)
    avg_spf = sum(r['solo_pf1'] for r in parsed) / len(parsed)
    avg_ssf = sum(r['solo_sf1'] for r in parsed) / len(parsed)
    avg_co = sum(r['comp_orec'] for r in parsed) / len(parsed)
    avg_cpf = sum(r['comp_pf1'] for r in parsed) / len(parsed)
    avg_csf = sum(r['comp_sf1'] for r in parsed) / len(parsed)

    table_rows += (
        f"| **OVERALL AVERAGE** | — | "
        f"**{avg_st:.2f}s** | **{avg_ct:.2f}s** | "
        f"**%{avg_so:.1f}** | **%{avg_spf:.1f}** | **%{avg_ssf:.1f}** | "
        f"**%{avg_co:.1f}** | **%{avg_cpf:.1f}** | **%{avg_csf:.1f}** | — |\n"
    )

    summary_content = f"""# 📊 {model_title} — 10-Piece 5-Stage Benchmark Summary

**Date:** {now_str}  
**Model:** {model_title}  
**Evaluation Dataset:** NYU MARL GuitarSet (ISMIR 2018 - 10 Tracks: 5 Solo [421 Notes] + 5 Comping [1,122 Notes], Total: 1,543 Notes)  
**Total Iterations:** {len(parsed)} Independent Runs (spaced 1 minute apart, timestamped MIDI outputs)  
**Archived MIDIs:** [`midi/{instrument}/`](../../midi/{instrument})  

---

## 📌 Consolidated Summary Metrics

* **🎸 5 Solo Tracks Average:**
  * Average Processing Time: **{avg_st:.2f}s**
  * Onset Recall (Note Attack): **%{avg_so:.1f}**
  * Pitch F1-Score (Note + Timing): **%{avg_spf:.1f}**
  * Strict F1-Score (With Offset/Damping): **%{avg_ssf:.1f}**

* **🎼 5 Comping / Chords Average:**
  * Average Processing Time: **{avg_ct:.2f}s**
  * Onset Recall (Chord Attacks): **%{avg_co:.1f}**
  * Pitch F1-Score (Chord Accuracy): **%{avg_cpf:.1f}**
  * Strict F1-Score (Chord Damping): **%{avg_csf:.1f}**

---

## 1. 🏁 5-Run Comparison Table

| Run | Time | Solo Time | Comp Time | Solo Onset Rec. | Solo Pitch F1 | Solo Strict F1 | Comp Onset Rec. | Comp Pitch F1 | Comp Strict F1 | Report Link |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
{table_rows}
---

## 2. 🔬 Evaluation & Observations

* **Reproducibility:** Each iteration was independently executed with timestamped `.mid` outputs stored in the `midi/` directory and evaluated using `mir_eval`.
* **Metric Standards:** Evaluated against NYU MARL GuitarSet JAMS ground truth with 50ms onset tolerance and 50 cent pitch tolerance.
"""
    summary_path = os.path.join(tests_dir, "results-summary.md")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary_content)

    print(f"[OK] Summary successfully generated: {summary_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python summarize_benchmark.py <model_name> [instrument]")
        sys.exit(1)
    inst = sys.argv[2] if len(sys.argv) > 2 else "guitar"
    generate_summary(sys.argv[1], inst)
