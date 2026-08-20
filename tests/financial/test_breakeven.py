import pytest
from calculator.financial.breakeven import break_even_beneficiaries, break_even_subscription


def test_break_even_beneficiaries():
    assert break_even_beneficiaries(1000000, 0, 15000) == 67


def test_break_even_subscription():
    assert break_even_subscription(1000000, 100) == 10000


def test_invalid_break_even_margin():
    with pytest.raises(ValueError):
        break_even_beneficiaries(1000000, 15000, 15000)
