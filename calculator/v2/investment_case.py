from calculator.v2.cash_flow import (
    AnnualOperatingPeriod,
    build_investor_cash_flows,
    build_programme_cash_flows,
)
from calculator.v2.funding_mix import FundingSource, evaluate_funding_mix
from calculator.v2.investor_returns import investor_summary
from calculator.v2.partnership import compare_partnership_structures
from calculator.v2.returns import irr, npv
from calculator.v2.scenarios import compare_scenarios
from calculator.v2.sensitivity import calculate_sensitivity


def build_v2_investment_case(
    starting_beneficiaries: int,
    monthly_subscription: float,
    annual_operating_cost: float,
    setup_cost: float,
    initial_investment: float,
    revenue_share: float = 0.10,
    years: int = 5,
    discount_rate: float = 0.10,
) -> dict:
    scenario_results = compare_scenarios(
        starting_beneficiaries=starting_beneficiaries,
        monthly_subscription=monthly_subscription,
        annual_operating_cost=annual_operating_cost,
        years=years,
    )

    base = scenario_results["base"]

    periods = [
        AnnualOperatingPeriod(
            year=row["year"],
            beneficiaries=row["beneficiaries"],
            paying_beneficiaries=round(
                row["beneficiaries"] * row["collection_rate"]
            ),
            revenue=row["revenue"],
            operating_cost=row["operating_cost"],
        )
        for row in base
    ]

    programme_cash_flows = build_programme_cash_flows(
        periods,
        initial_investment=initial_investment,
    )

    investor_cash_flows = build_investor_cash_flows(
        periods,
        initial_investment=initial_investment,
        revenue_share=revenue_share,
    )

    investor_metrics = investor_summary(investor_cash_flows)

    investor_npv = npv(
        [cf.net_cash_flow for cf in investor_cash_flows],
        discount_rate,
    )

    investor_irr = irr(
        [cf.net_cash_flow for cf in investor_cash_flows]
    )

    partnership_structures = compare_partnership_structures(
        annual_revenue=base[-1]["revenue"],
        annual_operating_cost=base[-1]["operating_cost"],
        setup_cost=setup_cost,
    )

    funding_mix = evaluate_funding_mix(
        [
            FundingSource(
                name="Initial Investor",
                funding_type="investment",
                amount=initial_investment,
                revenue_share=revenue_share,
            )
        ],
        setup_cost=setup_cost,
    )

    sensitivity = {
        "subscription": calculate_sensitivity(
            "subscription",
            [
                monthly_subscription * 0.80,
                monthly_subscription,
                monthly_subscription * 1.20,
            ],
            starting_beneficiaries,
            monthly_subscription,
            annual_operating_cost,
            initial_investment,
        ),
        "beneficiaries": calculate_sensitivity(
            "beneficiaries",
            [
                starting_beneficiaries * 0.80,
                starting_beneficiaries,
                starting_beneficiaries * 1.20,
            ],
            starting_beneficiaries,
            monthly_subscription,
            annual_operating_cost,
            initial_investment,
        ),
    }

    return {
        "scenarios": scenario_results,
        "base_periods": periods,
        "programme_cash_flows": programme_cash_flows,
        "investor_cash_flows": investor_cash_flows,
        "investor_metrics": investor_metrics,
        "investor_npv": investor_npv,
        "investor_irr": investor_irr,
        "partnership_structures": partnership_structures,
        "funding_mix": funding_mix,
        "sensitivity": sensitivity,
    }
