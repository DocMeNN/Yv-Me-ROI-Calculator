import pytest

from calculator.financial.sustainability import (
    SustainabilityAssumptions,
    calculate_sustainability,
)


def test_sustainability_baseline():
    result = calculate_sustainability(
        SustainabilityAssumptions(
            monthly_fixed_cost=1000000,
            monthly_variable_cost_per_beneficiary=5000,
            monthly_revenue_per_beneficiary=15000,
            beneficiaries=100,
        )
    )

    assert result["monthly_revenue"] == 1500000
    assert result["monthly_variable_cost"] == 500000
    assert result["monthly_contribution"] == 0
    assert result["break_even_beneficiaries"] == 100
    assert result["break_even_reached"] is True
    assert result["required_subscription"] == 15000


def test_sustainability_above_break_even():
    result = calculate_sustainability(
        SustainabilityAssumptions(
            monthly_fixed_cost=1000000,
            monthly_variable_cost_per_beneficiary=5000,
            monthly_revenue_per_beneficiary=15000,
            beneficiaries=200,
        )
    )

    assert result["monthly_contribution"] == 1000000
    assert result["break_even_reached"] is True


def test_sustainability_below_break_even():
    result = calculate_sustainability(
        SustainabilityAssumptions(
            monthly_fixed_cost=1000000,
            monthly_variable_cost_per_beneficiary=5000,
            monthly_revenue_per_beneficiary=15000,
            beneficiaries=50,
        )
    )

    assert result["monthly_contribution"] == -500000
    assert result["break_even_reached"] is False


def test_no_positive_contribution():
    result = calculate_sustainability(
        SustainabilityAssumptions(
            monthly_fixed_cost=1000000,
            monthly_variable_cost_per_beneficiary=15000,
            monthly_revenue_per_beneficiary=15000,
            beneficiaries=100,
        )
    )

    assert result["break_even_beneficiaries"] is None
    assert result["break_even_reached"] is False


@pytest.mark.parametrize(
    "assumptions",
    [
        SustainabilityAssumptions(-1, 5000, 15000, 100),
        SustainabilityAssumptions(1000000, -1, 15000, 100),
        SustainabilityAssumptions(1000000, 5000, -1, 100),
        SustainabilityAssumptions(1000000, 5000, 15000, -1),
    ],
)
def test_sustainability_validation(assumptions):
    with pytest.raises(ValueError):
        calculate_sustainability(assumptions)
