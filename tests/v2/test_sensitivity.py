from calculator.v2.sensitivity import SensitivityPoint, calculate_sensitivity


def test_subscription_sensitivity():
    result = calculate_sensitivity(
        "subscription",
        [10000, 15000, 20000],
        beneficiaries=1000,
        monthly_subscription=15000,
        annual_operating_cost=120000000,
        investment=100000000,
    )

    assert len(result) == 3
    assert result[0].annual_revenue == 120000000
    assert result[1].annual_revenue == 180000000
    assert result[2].annual_revenue == 240000000


def test_beneficiary_sensitivity():
    result = calculate_sensitivity(
        "beneficiaries",
        [1000, 1500, 2000],
        beneficiaries=1000,
        monthly_subscription=15000,
        annual_operating_cost=120000000,
        investment=100000000,
    )

    assert result[0].annual_revenue == 180000000
    assert result[1].annual_revenue == 270000000
    assert result[2].annual_revenue == 360000000


def test_collection_rate_sensitivity():
    result = calculate_sensitivity(
        "collection_rate",
        [0.80, 0.90, 1.00],
        beneficiaries=1000,
        monthly_subscription=15000,
        annual_operating_cost=120000000,
        investment=100000000,
    )

    assert result[0].annual_revenue == 144000000
    assert result[1].annual_revenue == 162000000
    assert result[2].annual_revenue == 180000000


def test_operating_cost_sensitivity():
    result = calculate_sensitivity(
        "operating_cost",
        [100000000, 120000000, 150000000],
        beneficiaries=1000,
        monthly_subscription=15000,
        annual_operating_cost=120000000,
        investment=100000000,
    )

    assert result[0].net_cash_flow == 80000000
    assert result[1].net_cash_flow == 60000000
    assert result[2].net_cash_flow == 30000000


def test_invalid_parameter():
    try:
        calculate_sensitivity(
            "invalid",
            [1, 2, 3],
            beneficiaries=1000,
            monthly_subscription=15000,
            annual_operating_cost=120000000,
            investment=100000000,
        )
        assert False
    except ValueError:
        assert True
