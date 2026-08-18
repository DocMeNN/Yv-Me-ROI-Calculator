from pathlib import Path
import json
import csv
import math

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

BUDGET_FILE = DATA / "budget_summary.json"
ASSUMPTIONS_FILE = DATA / "adjustable_assumptions.csv"


def load_budget():
    with open(BUDGET_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_assumptions():
    values = {}

    with open(ASSUMPTIONS_FILE, "r", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            values[row["assumption_code"]] = float(row["value"])

    return values


def calculate_roi(
    revenue,
    investment
):
    if investment <= 0:
        return 0

    return (revenue - investment) / investment


def calculate_break_even_months(
    investment,
    monthly_revenue,
    monthly_operating_cost
):
    contribution = monthly_revenue - monthly_operating_cost

    if contribution <= 0:
        return math.inf

    return investment / contribution


def calculate_payback_months(
    investment,
    monthly_revenue,
    monthly_operating_cost
):
    return calculate_break_even_months(
        investment,
        monthly_revenue,
        monthly_operating_cost
    )


def calculate(
    chews,
    beneficiaries_per_chew,
    programme_months,
    total_budget,
    subscription_per_beneficiary,
    investment_amount,
    revenue_share
):

    beneficiaries = chews * beneficiaries_per_chew

    monthly_operating_cost = (
        total_budget / programme_months
        if programme_months > 0
        else 0
    )

    annual_operating_cost = monthly_operating_cost * 12

    monthly_gross_revenue = (
        beneficiaries * subscription_per_beneficiary
    )

    annual_gross_revenue = monthly_gross_revenue * 12

    partner_share = (
        annual_gross_revenue * revenue_share / 100
    )

    annual_net_revenue = (
        annual_gross_revenue - partner_share
    )

    annual_contribution = (
        annual_net_revenue - annual_operating_cost
    )

    roi = calculate_roi(
        annual_contribution,
        investment_amount
    )

    break_even = calculate_break_even_months(
        investment_amount,
        monthly_gross_revenue,
        monthly_operating_cost
    )

    return {
        "chews": chews,
        "beneficiaries_per_chew": beneficiaries_per_chew,
        "beneficiaries": beneficiaries,
        "programme_months": programme_months,

        "total_budget": total_budget,

        "monthly_operating_cost":
            monthly_operating_cost,

        "annual_operating_cost":
            annual_operating_cost,

        "cost_per_chew":
            total_budget / chews if chews else 0,

        "cost_per_beneficiary":
            total_budget / beneficiaries
            if beneficiaries else 0,

        "monthly_gross_revenue":
            monthly_gross_revenue,

        "annual_gross_revenue":
            annual_gross_revenue,

        "partner_revenue_share":
            partner_share,

        "annual_net_revenue":
            annual_net_revenue,

        "annual_contribution":
            annual_contribution,

        "investment_amount":
            investment_amount,

        "roi":
            roi,

        "break_even_months":
            break_even,

        "payback_months":
            break_even,
    }


def run_default():

    budget = load_budget()
    assumptions = load_assumptions()

    result = calculate(
        chews=assumptions["CHEW_COUNT"],
        beneficiaries_per_chew=
            assumptions["BENEFICIARIES_PER_CHEW"],
        programme_months=
            assumptions["PILOT_DURATION"],
        total_budget=
            assumptions["TOTAL_BUDGET"],
        subscription_per_beneficiary=
            assumptions["SUBSCRIPTION_PER_BENEFICIARY"],
        investment_amount=
            assumptions["INVESTMENT_AMOUNT"],
        revenue_share=
            assumptions["REVENUE_SHARE"],
    )

    print("=" * 70)
    print("Yv-Me ROI & FINANCIAL ANALYTICS")
    print("=" * 70)

    print(f"CHEWs:                 {result['chews']:,.0f}")
    print(
        f"Beneficiaries/CHEW:   "
        f"{result['beneficiaries_per_chew']:,.0f}"
    )
    print(
        f"Beneficiaries:        "
        f"{result['beneficiaries']:,.0f}"
    )

    print(
        f"Programme Budget:     "
        f"NGN {result['total_budget']:,.2f}"
    )

    print(
        f"Monthly Cost:         "
        f"NGN {result['monthly_operating_cost']:,.2f}"
    )

    print(
        f"Annual Cost:          "
        f"NGN {result['annual_operating_cost']:,.2f}"
    )

    print(
        f"Cost/CHEW:            "
        f"NGN {result['cost_per_chew']:,.2f}"
    )

    print(
        f"Cost/Beneficiary:     "
        f"NGN {result['cost_per_beneficiary']:,.2f}"
    )

    print(
        f"Monthly Revenue:      "
        f"NGN {result['monthly_gross_revenue']:,.2f}"
    )

    print(
        f"Annual Revenue:       "
        f"NGN {result['annual_gross_revenue']:,.2f}"
    )

    print(
        f"Annual Contribution:  "
        f"NGN {result['annual_contribution']:,.2f}"
    )

    print(
        f"ROI:                  "
        f"{result['roi']:.2%}"
    )

    if math.isinf(result["break_even_months"]):
        print("Break-even:            NOT REACHED")
    else:
        print(
            f"Break-even:           "
            f"{result['break_even_months']:.2f} months"
        )

    print("=" * 70)


if __name__ == "__main__":
    run_default()
