from pathlib import Path
import json
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

ASSUMPTIONS_FILE = DATA / "adjustable_assumptions.csv"
BUDGET_FILE = DATA / "budget_summary.json"

def load_budget():
    with open(BUDGET_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_assumptions():
    assumptions = {}

    with open(ASSUMPTIONS_FILE, "r", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            assumptions[row["assumption_code"]] = {
                "name": row["assumption"],
                "value": float(row["value"]),
                "unit": row["unit"],
                "status": row["status"],
                "source": row["source"],
            }

    return assumptions

def calculate(values):
    chews = values["CHEW_COUNT"]
    beneficiaries_per_chew = values["BENEFICIARIES_PER_CHEW"]

    beneficiaries = chews * beneficiaries_per_chew

    programme_months = values["PILOT_DURATION"]
    total_budget = values["TOTAL_BUDGET"]

    monthly_cost = (
        total_budget / programme_months
        if programme_months else 0
    )

    cost_per_chew = (
        total_budget / chews
        if chews else 0
    )

    cost_per_beneficiary = (
        total_budget / beneficiaries
        if beneficiaries else 0
    )

    monthly_subscription = values["SUBSCRIPTION_PER_BENEFICIARY"]

    monthly_revenue = beneficiaries * monthly_subscription
    annual_revenue = monthly_revenue * 12

    investment = values["INVESTMENT_AMOUNT"]

    if investment > 0:
        roi = (annual_revenue - investment) / investment
    else:
        roi = 0

    return {
        "chews": chews,
        "beneficiaries": beneficiaries,
        "beneficiaries_per_chew": beneficiaries_per_chew,
        "programme_months": programme_months,
        "total_budget": total_budget,
        "monthly_cost": monthly_cost,
        "cost_per_chew": cost_per_chew,
        "cost_per_beneficiary": cost_per_beneficiary,
        "monthly_revenue": monthly_revenue,
        "annual_revenue": annual_revenue,
        "investment": investment,
        "roi": roi,
    }

def update_assumption(code, value):
    rows = []

    with open(ASSUMPTIONS_FILE, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        for row in reader:
            if row["assumption_code"] == code:
                row["value"] = value
                row["status"] = "ADJUSTED"

            rows.append(row)

    with open(
        ASSUMPTIONS_FILE,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def run():
    assumptions = load_assumptions()

    values = {
        code: item["value"]
        for code, item in assumptions.items()
    }

    results = calculate(values)

    print("=" * 60)
    print("Yv-Me ASSUMPTIONS ENGINE")
    print("=" * 60)
    print(f"CHEWs:                 {results['chews']:,.0f}")
    print(f"Beneficiaries/CHEW:    {results['beneficiaries_per_chew']:,.0f}")
    print(f"Beneficiaries:         {results['beneficiaries']:,.0f}")
    print(f"Programme Budget:      NGN {results['total_budget']:,.2f}")
    print(f"Monthly Programme Cost:NGN {results['monthly_cost']:,.2f}")
    print(f"Cost/CHEW:             NGN {results['cost_per_chew']:,.2f}")
    print(f"Cost/Beneficiary:      NGN {results['cost_per_beneficiary']:,.2f}")
    print(f"Monthly Revenue:       NGN {results['monthly_revenue']:,.2f}")
    print(f"Annual Revenue:        NGN {results['annual_revenue']:,.2f}")
    print(f"ROI:                   {results['roi']:.2%}")
    print("=" * 60)

if __name__ == "__main__":
    run()
