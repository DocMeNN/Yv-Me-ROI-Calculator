import pytest

from calculator.financial.investor_model import (
    InvestorAssumptions,
    calculate_investor_metrics,
)


def test_investor_baseline():
    result = calculate_investor_metrics(
        InvestorAssumptions(
            investment_amount=10000000,
            investor_revenue=15000000,
            monthly_investor_cashflow=1250000,
            revenue_share=0.20,
        )
    )

    assert result["net_return"] == 5000000
    assert result["roi"] == 0.5
    assert result["payback_months"] == 8
    assert result["revenue_share"] == 0.20


def test_investor_zero_cashflow():
    result = calculate_investor_metrics(
        InvestorAssumptions(
            investment_amount=10000000,
            investor_revenue=12000000,
            monthly_investor_cashflow=0,
        )
    )

    assert result["payback_months"] is None


@pytest.mark.parametrize(
    "assumptions",
    [
        InvestorAssumptions(0, 1000000, 100000),
        InvestorAssumptions(-1, 1000000, 100000),
        InvestorAssumptions(1000000, -1, 100000),
        InvestorAssumptions(1000000, 1000000, -1),
        InvestorAssumptions(1000000, 1000000, 100000, 1.1),
    ],
)
def test_investor_validation(assumptions):
    with pytest.raises(ValueError):
        calculate_investor_metrics(assumptions)
