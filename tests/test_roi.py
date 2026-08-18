from data.model import PROGRAMME
from calculator.roi import (
    cost_per_chew,
    cost_per_beneficiary,
    monthly_programme_cost,
)

def test_programme():
    assert PROGRAMME["chews"] == 100
    assert PROGRAMME["beneficiaries"] == 1000
    assert PROGRAMME["beneficiaries_per_chew"] == 10

def test_cost_per_chew():
    assert cost_per_chew() == 4269060.31

def test_cost_per_beneficiary():
    assert cost_per_beneficiary() == 426906.031

def test_monthly_cost():
    assert monthly_programme_cost() == 35575502.583333336
