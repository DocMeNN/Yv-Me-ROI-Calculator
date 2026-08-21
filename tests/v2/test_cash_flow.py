from calculator.v2.cash_flow import (
    AnnualOperatingPeriod,
    build_investor_cash_flows,
    build_programme_cash_flows,
)


def test_programme_cash_flow_timeline():
    periods = [
        AnnualOperatingPeriod(
            year=1,
            beneficiaries=1000,
            paying_beneficiaries=1000,
            revenue=180000000,
            operating_cost=120000000,
        ),
        AnnualOperatingPeriod(
            year=2,
            beneficiaries=1500,
            paying_beneficiaries=1500,
            revenue=270000000,
            operating_cost=150000000,
        ),
    ]

    result = build_programme_cash_flows(periods, initial_investment=100000000)

    assert result[0].year == 0
    assert result[0].net_cash_flow == -100000000
    assert result[1].net_cash_flow == 60000000
    assert result[2].net_cash_flow == 120000000
    assert result[2].cumulative_cash_flow == 80000000


def test_investor_cash_flow_timeline():
    periods = [
        AnnualOperatingPeriod(
            year=1,
            beneficiaries=1000,
            paying_beneficiaries=1000,
            revenue=180000000,
            operating_cost=120000000,
        ),
        AnnualOperatingPeriod(
            year=2,
            beneficiaries=1500,
            paying_beneficiaries=1500,
            revenue=270000000,
            operating_cost=150000000,
        ),
    ]

    result = build_investor_cash_flows(
        periods,
        initial_investment=100000000,
        revenue_share=0.10,
    )

    assert result[0].net_cash_flow == -100000000
    assert result[1].revenue_share == 18000000
    assert result[2].revenue_share == 27000000
    assert result[2].cumulative_cash_flow == -55000000
