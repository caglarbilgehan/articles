"""
Açık Kaynak Gitar Fret-String Assignment (FSA) Benchmark Doğrulama Betiği.
YourMT3+ ile akustik gitar sesinden transkribe edilmiş 10 parçayı
GuitarSet fiziksel hexaphonic manyetik zemin gerçeğine karşı test eder.
"""

import sys
from pathlib import Path

script_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(script_dir / "evaluation"))

from jams_reader import GuitarSetJamsReader
from fsa_metrics import evaluate_fsa_predictions
from baseline_m2s import NaiveM2SConverter


TEST_TRACKS = [
    # Sololar
    ("05_BN3-119-G_solo", "Bossa Nova", "Solo"),
    ("03_Funk1-97-C_solo", "Funk", "Solo"),
    ("04_Jazz1-200-B_solo", "Jazz", "Solo"),
    ("00_Rock2-142-D_solo", "Rock", "Solo"),
    ("02_SS1-100-C#_solo", "Singer-Songwriter", "Solo"),
    # Eşlikler (Comping)
    ("04_BN2-131-B_comp", "Bossa Nova", "Comping"),
    ("02_Funk1-97-C_comp", "Funk", "Comping"),
    ("01_Jazz3-150-C_comp", "Jazz", "Comping"),
    ("05_Rock3-117-Bb_comp", "Rock", "Comping"),
    ("00_SS3-84-Bb_comp", "Singer-Songwriter", "Comping"),
]


def main():
    repo_dir = script_dir.parent
    jams_dir = repo_dir / "test_dataset" / "ground_truth_jams"
    midi_dir = repo_dir / "test_dataset" / "yourmt3_midi"

    print("=" * 80)
    print("🎸 GUITAR M2S & FSA BENCHMARK DOĞRULAMA KOŞUMU")
    print(f"   Test Veri Seti: test_dataset/yourmt3_midi/ (YourMT3+ Ses Transkripsiyonu)")
    print(f"   Zemin Gerçeği: test_dataset/ground_truth_jams/ (GuitarSet Manyetik Sensörleri)")
    print("=" * 80)

    converter = NaiveM2SConverter()
    baseline_accs = []
    baseline_maes = []

    for track_name, genre, style in TEST_TRACKS:
        jams_path = jams_dir / f"{track_name}.jams"
        midi_path = midi_dir / f"{track_name}_yourmt3.mid"

        if not jams_path.exists() or not midi_path.exists():
            print(f"⚠️ Eksik dosya: {track_name}")
            continue

        reader = GuitarSetJamsReader(str(jams_path))
        gt_notes_raw = reader.extract_notes()
        gt_notes = [
            {"start": n.start, "end": n.end, "pitch": n.rounded_pitch, "string_number": n.string_number, "fret": n.fret}
            for n in gt_notes_raw
        ]

        preds = converter.convert_midi_to_predictions(str(midi_path))
        report = evaluate_fsa_predictions(gt_notes, preds, time_tolerance=0.08)
        
        baseline_accs.append(report.string_accuracy)
        baseline_maes.append(report.fret_mae)
        print(f"[{style:7s}] {genre:17s} | {track_name:22s} -> Naive Doğruluk: %{report.string_accuracy:5.1f} | MAE: {report.fret_mae:.2f}")

    avg_acc = sum(baseline_accs) / len(baseline_accs) if baseline_accs else 0
    avg_mae = sum(baseline_maes) / len(baseline_maes) if baseline_maes else 0
    print("=" * 80)
    print(f"📊 Kontrol Grubu (FSA Yok / Naive Baseline) Ortalaması:")
    print(f"   Ortalama Tel Doğruluğu: %{avg_acc:.1f}")
    print(f"   Ortalama Perde Hatası (MAE): {avg_mae:.2f} perde")
    print("=" * 80)


if __name__ == "__main__":
    main()
