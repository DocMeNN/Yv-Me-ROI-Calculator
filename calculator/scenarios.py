from calculator.analytics import calculate


SCENARIOS = {

    "BASE": {
        "chews": 100,
        "beneficiaries_per_chew": 10,
        "programme_months": 12,
        "subscription": 0,
        "investment": 426906031,
        "revenue_share": 0,
    },

    "CONSERVATIVE": {
        "chews": 100,
        "beneficiaries_per_chew": 10,
        "programme_months": 12,
        "subscription": 10000,
        "investment": 426906031,
        "revenue_share": 20,
    },

    "MODERATE": {
        "chews": 100,
        "beneficiaries_per_chew": 10,
        "programme_months": 12,
        "subscription": 15000,
        "investment": 426906031,
        "revenue_share": 15,
    },

    "GROWTH": {
        "chews": 200,
        "beneficiaries_per_chew": 10,
        "programme_months": 12,
        "subscription": 15000,
        "investment": 426906031,
        "revenue_share": 10,
    },

    "SCALE": {
        "chews": 500,
        "beneficiaries_per_chew": 10,
        "programme_months": 12,
        "subscription": 15000,
        "investment": 426906031,
        "revenue_share": 10,
    },
}


def run_scenarios():

    budget = 426906031

    print("=" * 90)
    print("Yv-Me SCENARIO ANALYSIS")
    print("=" * 90)

    for name, s in SCENARIOS.items():

        result = calculate(
            chews=s["chews"],
            beneficiaries_per_chew=s["beneficiaries_per_chew"],
            programme_months=s["programme_months"],
            total_budget=budget,
            subscription_per_beneficiary=s["subscription"],
            investment_amount=s["investment"],
            revenue_share=s["revenue_share"],
        )

        print("")
        print(f"SCENARIO: {name}")
        print(f"CHEWs: {result['chews']:,}")
        print(f"Beneficiaries: {result['beneficiaries']:,}")
        print(
            f"Annual Revenue: "
            f"NGN {result['annual_gross_revenue']:,.0f}"
        )
        print(
            f"Annual Contribution: "
            f"NGN {result['annual_contribution']:,.0f}"
        )
        print(
            f"ROI: "
            f"{result['roi']:.2%}"
        )

    print("")
    print("=" * 90)


if __name__ == "__main__":
    run_scenarios()
