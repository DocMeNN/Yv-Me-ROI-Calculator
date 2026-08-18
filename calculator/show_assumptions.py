import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "data" / "adjustable_assumptions.csv"

print("=" * 70)
print("Yv-Me — ADJUSTABLE ASSUMPTIONS")
print("=" * 70)
print("Edit the VALUE column to change the model.")
print("Status changes automatically to ADJUSTED.")
print("")

rows = []

with open(FILE, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)

    for row in reader:
        rows.append(row)

for i, row in enumerate(rows, 1):
    print(
        f"{i:02d}. "
        f"{row['assumption']:<45} "
        f"{row['value']:>15} "
        f"{row['unit']:<20} "
        f"[{row['status']}]"
    )

print("")
print("=" * 70)
