from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parent
SUMMARY_FILE = DATA_DIR / "budget_summary.json"

with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
    BUDGET = json.load(f)

MODEL_NAME = "Yv-Me ROI Calculator"

PROGRAMME = {
    "name": BUDGET["programme"],
    "location": BUDGET["location"],
    "pilot_months": BUDGET["pilot_months"],
    "chews": BUDGET["chews"],
    "beneficiaries": BUDGET["beneficiaries"],
    "beneficiaries_per_chew": BUDGET["beneficiaries_per_chew"],
    "total_budget": BUDGET["total_budget"],
    "currency": BUDGET["currency"],
    "care_model": BUDGET["care_model"],
}

OBJECTIVES = {
    "1": "Training and Deployment",
    "2": "Community-Based Palliative and Primary Care Services",
    "3": "Advocacy Engagement and Technical Support",
    "4": "Health Governance and Public Awareness",
    "5": "Communications and Monitoring & Evaluation",
    "6": "Equipment",
    "7": "Personnel",
    "8": "Management / Indirect Cost",
}
