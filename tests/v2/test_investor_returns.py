from calculator.v2.cash_flow import AnnualOperatingPeriod, build_investor_cash_flows
from calculator.v2.investor_returns import (
    investor_roi,
    investor_summary,
    net_investor_return,
    payback_year,
)


def test_investor_roi():
    periods = [
        AnnualOperatingPeriod(1, 1000, 1000, 200000000, 120000000),
        AnnualOperatingPeriod(2, 1500, 1500, 300000000, 160000000),
        AnnualOperatingPeriod(3, 2000, 2000, 400000000, 200000000),
    ]

    cash_flows = build_investor_cash_flows(
        periods,
        initial_investment=100000000,
        revenue_share=0.10,
    )

    assert investor_roi(cash_flows) == -0.1
    assert net_investor_return(cash_flows) == -10000000


def test_payback_year():
    periods = [
        AnnualOperatingPeriod(1, 1000, 1000, 600000000, 120000000),
        AnnualOperatingPeriod(2, 1500, 1500, 700000000, 160000000),
    ]

    cash_flows = build_investor_cash_flows(
        periods,
        initial_investment=100000000,
        revenue_share=0.10,
    )

    assert payback_year(cash_flows) == 2


def test_investor_summary():
    periods = [
        AnnualOperatingPeriod(1, 1000, 1000, 200000000, 120000000),
        AnnualOperatingPeriod(2, 1500, 1500, 300000000, 160000000),
    ]

    cash_flows = build_investor_cash_flows(
        periods,
        initial_investment=100000000,
        revenue_share=0.10,
    )

    summary = investor_summary(cash_flows)

    assert summary["total_investment"] == 100000000
    assert summary["total_returns"] == 50000000
    assert summary["net_return"] == -50000000
    assert summary["roi"] == -0.5
    assert summary["payback_year"] is None
