from calculator.financial.intelligence import calculate_financial_intelligence


def test_unified_financial_intelligence():
    result = calculate_financial_intelligence(
        beneficiaries=1000,
        programme_cost=426906031,
        monthly_subscription=15000,
        collection_rate=0.8,
        free_beneficiaries=100,
        grant_amount=300000000,
        investment_amount=10000000,
        investor_revenue=15000000,
        monthly_investor_cashflow=1250000,
        revenue_share=0.20,
        monthly_fixed_cost=1000000,
        monthly_variable_cost_per_beneficiary=5000,
        programme_duration_months=12,
    )

    assert result["revenue"]["paying_beneficiaries"] == 900
    assert result["revenue"]["monthly_revenue"] == 10800000
    assert result["grant"]["funding_gap"] == 126906031
    assert result["investor"]["roi"] == 0.5
    assert result["investor"]["payback_months"] == 8
    assert result["funding_gap"] == 126906031
    assert result["funding_coverage"] < 1
    assert result["sustainability"]["break_even_reached"] is True
