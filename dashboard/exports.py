from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from calculator.export_engine import export_xlsx, export_pptx


def export_dashboard_files():

    results = {
        "xlsx": False,
        "pptx": False,
    }

    results["xlsx"] = export_xlsx()
    results["pptx"] = export_pptx()

    return results


if __name__ == "__main__":

    results = export_dashboard_files()

    print("")
    print("Yv-Me DASHBOARD EXPORT")
    print("----------------------")
    print(
        "Excel:",
        "READY" if results["xlsx"] else "FAILED"
    )
    print(
        "PowerPoint:",
        "READY" if results["pptx"] else "FAILED"
    )
