import pytest

from calculator.financial.revenue_model import (
    RevenueAssumptions,
    calculate_revenue,
)


def test_revenue_model_baseline():
    result = calculate_revenue(
        RevenueAssumptions(
            beneficiaries=1000,
            monthly_subscription=15000,
        )
    )

    assert result["paying_beneficiaries"] == 1000
    assert result["monthly_revenue"] == 15000000
    assert result["annual_revenue"] == 180000000


def test_revenue_model_collection_rate():
    result = calculate_revenue(
        RevenueAssumptions(
            beneficiaries=1000,
            monthly_subscription=15000,
            collection_rate=0.8,
        )
    )

    assert result["monthly_revenue"] == 12000000


def test_revenue_model_free_beneficiaries():
    result = calculate_revenue(
        RevenueAssumptions(
            beneficiaries=1000,
            monthly_subscription=15000,
            free_beneficiaries=100,
        )
    )

    assert result["paying_beneficiaries"] == 900
    assert result["monthly_revenue"] == 13500000


@pytest.mark.parametrize(
    "assumptions",
    [
        RevenueAssumptions(1000, 15000, collection_rate=1.1),
        RevenueAssumptions(1000, 15000, free_beneficiaries=1001),
        RevenueAssumptions(-1, 15000),
        RevenueAssumptions(1000, -1),
    ],
)
def test_revenue_model_validation(assumptions):
    with pytest.raises(ValueError):
        calculate_revenue(assumptions)
