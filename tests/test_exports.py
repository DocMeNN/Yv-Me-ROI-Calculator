from pathlib import Path
from calculator.export_engine import export_xlsx, export_pptx


ROOT = Path(__file__).resolve().parents[1]


def test_xlsx_export():
    assert export_xlsx()
    assert (
        ROOT /
        "exports" /
        "xlsx" /
        "Yv-Me_ROI_Calculator.xlsx"
    ).exists()


def test_pptx_export():
    assert export_pptx()
    assert (
        ROOT /
        "exports" /
        "pptx" /
        "Yv-Me_Investor_Donor_Grant_Presentation.pptx"
    ).exists()
