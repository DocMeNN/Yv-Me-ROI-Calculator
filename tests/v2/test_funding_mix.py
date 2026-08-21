from calculator.v2.funding_mix import FundingSource, evaluate_funding_mix


def test_funding_mix_balances_setup_cost():
    sources = [
        FundingSource("Grant", "grant", 50000000),
        FundingSource("Investor", "revenue_share", 50000000, revenue_share=0.10),
    ]

    result = evaluate_funding_mix(sources, setup_cost=100000000)

    assert result["total_funding"] == 100000000
    assert result["funding_gap"] == 0
    assert result["surplus"] == 0
    assert result["revenue_share"] == 0.10


def test_funding_mix_detects_gap():
    sources = [
        FundingSource("Grant", "grant", 40000000),
        FundingSource("Investor", "equity", 30000000, equity_percentage=0.20),
    ]

    result = evaluate_funding_mix(sources, setup_cost=100000000)

    assert result["total_funding"] == 70000000
    assert result["funding_gap"] == 30000000
    assert result["equity_percentage"] == 0.20


def test_funding_mix_detects_surplus():
    sources = [
        FundingSource("Grant", "grant", 120000000),
    ]

    result = evaluate_funding_mix(sources, setup_cost=100000000)

    assert result["funding_gap"] == 0
    assert result["surplus"] == 20000000
