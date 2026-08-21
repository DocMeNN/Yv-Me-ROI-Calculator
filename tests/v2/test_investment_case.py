from calculator.v2.investment_case import build_v2_investment_case


def test_build_v2_investment_case():
    result = build_v2_investment_case(
        starting_beneficiaries=1000,
        monthly_subscription=15000,
        annual_operating_cost=120000000,
        setup_cost=100000000,
        initial_investment=100000000,
        revenue_share=0.10,
        years=5,
        discount_rate=0.10,
    )

    assert len(result["scenarios"]) == 4
    assert len(result["base_periods"]) == 5
    assert len(result["programme_cash_flows"]) == 6
    assert len(result["investor_cash_flows"]) == 6

    assert "roi" in result["investor_metrics"]
    assert "payback_year" in result["investor_metrics"]

    assert result["investor_npv"] is not None
    assert result["investor_irr"] is not None

    assert len(result["partnership_structures"]) == 6
    assert result["funding_mix"]["total_funding"] == 100000000

    assert len(result["sensitivity"]["subscription"]) == 3
    assert len(result["sensitivity"]["beneficiaries"]) == 3


def test_base_case_growth():
    result = build_v2_investment_case(
        starting_beneficiaries=1000,
        monthly_subscription=15000,
        annual_operating_cost=120000000,
        setup_cost=100000000,
        initial_investment=100000000,
    )

    assert (
        result["base_periods"][-1].beneficiaries
        > result["base_periods"][0].beneficiaries
    )

    assert (
        result["base_periods"][-1].revenue
        > result["base_periods"][0].revenue
    )
