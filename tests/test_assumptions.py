from calculator.assumptions import calculate

def test_one_to_ten_model():

    values = {
        "CHEW_COUNT": 100,
        "BENEFICIARIES_PER_CHEW": 10,
        "PILOT_DURATION": 12,
        "TOTAL_BUDGET": 426906031,
        "SUBSCRIPTION_PER_BENEFICIARY": 0,
        "REVENUE_SHARE": 0,
        "INVESTMENT_AMOUNT": 0,
    }

    result = calculate(values)

    assert result["chews"] == 100
    assert result["beneficiaries"] == 1000
    assert result["beneficiaries_per_chew"] == 10
    assert result["total_budget"] == 426906031

def test_adjustable_chews():

    values = {
        "CHEW_COUNT": 200,
        "BENEFICIARIES_PER_CHEW": 10,
        "PILOT_DURATION": 12,
        "TOTAL_BUDGET": 426906031,
        "SUBSCRIPTION_PER_BENEFICIARY": 0,
        "REVENUE_SHARE": 0,
        "INVESTMENT_AMOUNT": 0,
    }

    result = calculate(values)

    assert result["beneficiaries"] == 2000

def test_subscription_revenue():

    values = {
        "CHEW_COUNT": 100,
        "BENEFICIARIES_PER_CHEW": 10,
        "PILOT_DURATION": 12,
        "TOTAL_BUDGET": 426906031,
        "SUBSCRIPTION_PER_BENEFICIARY": 15000,
        "REVENUE_SHARE": 0,
        "INVESTMENT_AMOUNT": 100000000,
    }

    result = calculate(values)

    assert result["monthly_revenue"] == 15000000
    assert result["annual_revenue"] == 180000000
