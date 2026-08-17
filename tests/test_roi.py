from data.model import PROGRAMME
from calculator.roi import (
    cost_per_chew,
    cost_per_beneficiary,
    monthly_programme_cost,
)


def test_programme():
    assert PROGRAMME["chews"] == 100
    assert PROGRAMME["beneficiaries"] == 500
    assert PROGRAMME["beneficiaries_per_chew"] == 5


def test_cost_per_chew():
    assert cost_per_chew() == 4_073_435.31


def test_cost_per_beneficiary():
    assert cost_per_beneficiary() == 814_687.062


def test_monthly_cost():
    assert monthly_programme_cost() == 33_945_294.25
