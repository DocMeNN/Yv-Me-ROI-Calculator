from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

MODULES = {
    "Executive": "executive",
    "Investment Case": "investment",
    "Scenarios": "scenarios",
    "Partnership": "partnership",
    "Cash Flow": "cash_flow",
    "Sensitivity": "sensitivity",
    "Funding Mix": "funding",
    "Assumptions": "assumptions",
    "Exports": "exports",
}


def dashboard_modules():
    return MODULES.copy()
