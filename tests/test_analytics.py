from calculator.analytics import calculate


def test_core_model():

    result = calculate(
        chews=100,
        beneficiaries_per_chew=10,
        programme_months=12,
        total_budget=426906031,
        subscription_per_beneficiary=0,
        investment_amount=426906031,
        revenue_share=0,
    )

    assert result["beneficiaries"] == 1000
    assert result["total_budget"] == 426906031


def test_revenue():

    result = calculate(
        chews=100,
        beneficiaries_per_chew=10,
        programme_months=12,
        total_budget=426906031,
        subscription_per_beneficiary=15000,
        investment_amount=426906031,
        revenue_share=0,
    )

    assert result["monthly_gross_revenue"] == 15000000
    assert result["annual_gross_revenue"] == 180000000


def test_scaling():

    result = calculate(
        chews=500,
        beneficiaries_per_chew=10,
        programme_months=12,
        total_budget=426906031,
        subscription_per_beneficiary=15000,
        investment_amount=426906031,
        revenue_share=0,
    )

    assert result["beneficiaries"] == 5000
    assert result["monthly_gross_revenue"] == 75000000
