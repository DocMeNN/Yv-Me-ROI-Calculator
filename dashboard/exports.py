from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from calculator.export_engine import export_xlsx, export_pptx


def generate_xlsx():
    return export_xlsx()


def generate_pptx():
    return export_pptx()


def generate_all():
    return {
        "xlsx": generate_xlsx(),
        "pptx": generate_pptx(),
    }


if __name__ == "__main__":
    result = generate_all()

    print("")
    print("Yv-Me EXPORT STATUS")
    print("===================")
    print("XLSX:", "READY" if result["xlsx"] else "FAILED")
    print("PPTX:", "READY" if result["pptx"] else "FAILED")
