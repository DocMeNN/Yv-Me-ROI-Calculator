from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

XLSX_SCRIPT = ROOT / "calculator" / "export_xlsx_safe.py"
PPTX_SCRIPT = ROOT / "calculator" / "export_pptx_safe.py"


def export_xlsx():
    result = subprocess.run(
        [sys.executable, str(XLSX_SCRIPT)],
        cwd=ROOT
    )
    return result.returncode == 0


def export_pptx():
    result = subprocess.run(
        [sys.executable, str(PPTX_SCRIPT)],
        cwd=ROOT
    )
    return result.returncode == 0


def export_all():
    xlsx_ok = export_xlsx()
    pptx_ok = export_pptx()

    return {
        "xlsx": xlsx_ok,
        "pptx": pptx_ok,
        "success": xlsx_ok and pptx_ok,
    }


if __name__ == "__main__":
    result = export_all()

    print("============================================================")
    print("Yv-Me EXPORT ENGINE")
    print("============================================================")
    print(f"XLSX: {'READY' if result['xlsx'] else 'FAILED'}")
    print(f"PPTX: {'READY' if result['pptx'] else 'FAILED'}")
    print(f"STATUS: {'SUCCESS' if result['success'] else 'FAILED'}")
    print("============================================================")
