from calculator.v2.partnership import (
    STRUCTURES,
    calculate_partner_share,
    compare_partnership_structures,
    evaluate_structure,
)


def test_partnership_catalog():
    assert set(STRUCTURES.keys()) == {
        "revenue_share",
        "grant",
        "equity",
        "blended",
        "sponsorship",
        "working_capital",
    }


def test_revenue_share():
    result = evaluate_structure(
        STRUCTURES["revenue_share"],
        annual_revenue=180000000,
        annual_operating_cost=120000000,
        setup_cost=100000000,
    )

    assert result["partner_investment"] == 100000000
    assert result["partner_revenue_share"] == 18000000
    assert result["programme_contribution"] == 60000000


def test_partner_share():
    assert calculate_partner_share(200000000, STRUCTURES["revenue_share"]) == 20000000


def test_compare_structures():
    result = compare_partnership_structures(
        annual_revenue=180000000,
        annual_operating_cost=120000000,
        setup_cost=100000000,
    )

    assert len(result) == 6
    assert result["revenue_share"]["partner_revenue_share"] == 18000000
    assert result["blended"]["partner_revenue_share"] == 9000000
    assert result["equity"]["equity_percentage"] == 0.20
