import pytest
from calculator.financial.investment import investor_return, investor_roi, payback_months


def test_investor_return():
    assert investor_return(1000000, 1500000) == 500000


def test_investor_roi():
    assert investor_roi(1000000, 1500000) == 0.5


def test_payback_months():
    assert payback_months(1200000, 200000) == 6


def test_invalid_investment():
    with pytest.raises(ValueError):
        investor_roi(0, 1000000)
