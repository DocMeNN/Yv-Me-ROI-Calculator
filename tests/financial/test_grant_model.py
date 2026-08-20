import pytest

from calculator.financial.grant_model import (
    GrantAssumptions,
    calculate_grant_metrics,
)


def test_grant_baseline():
    result = calculate_grant_metrics(
        GrantAssumptions(
            programme_cost=426906031,
            grant_amount=300000000,
            programme_duration_months=12,
            beneficiaries=1000,
        )
    )

    assert result["funding_gap"] == 126906031
    assert result["funding_coverage"] < 1
    assert result["cost_per_beneficiary"] == 426906.031
    assert result["grant_per_beneficiary"] == 300000


def test_full_grant_coverage():
    result = calculate_grant_metrics(
        GrantAssumptions(
            programme_cost=1000000,
            grant_amount=1500000,
            programme_duration_months=12,
            beneficiaries=100,
        )
    )

    assert result["funding_gap"] == 0
    assert result["funding_coverage"] == 1.0


@pytest.mark.parametrize(
    "assumptions",
    [
        GrantAssumptions(0, 1000000, 12, 100),
        GrantAssumptions(1000000, -1, 12, 100),
        GrantAssumptions(1000000, 500000, 0, 100),
        GrantAssumptions(1000000, 500000, 12, 0),
    ],
)
def test_grant_validation(assumptions):
    with pytest.raises(ValueError):
        calculate_grant_metrics(assumptions)
