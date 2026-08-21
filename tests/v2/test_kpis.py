from calculator.v2.kpis import calculate_kpis


def test_kpi_calculations():
    result = calculate_kpis(
        beneficiaries=1000,
        paying_beneficiaries=900,
        annual_revenue=180000000,
        annual_operating_cost=120000000,
        investment=100000000,
    )

    assert len(result) == 8

    values = {kpi.name: kpi.value for kpi in result}

    assert values["Beneficiaries"] == 1000
    assert values["Collection Rate"] == 0.9
    assert values["Annual Revenue"] == 180000000
    assert values["Annual Operating Cost"] == 120000000
    assert values["Operating Margin"] == 1 / 3
    assert values["ROI"] == 0.6
    assert values["Revenue per Beneficiary"] == 180000
    assert values["Cost per Beneficiary"] == 120000


def test_kpi_zero_safety():
    result = calculate_kpis(
        beneficiaries=0,
        paying_beneficiaries=0,
        annual_revenue=0,
        annual_operating_cost=0,
        investment=0,
    )

    values = {kpi.name: kpi.value for kpi in result}

    assert values["Collection Rate"] == 0
    assert values["Operating Margin"] == 0
    assert values["ROI"] == 0
    assert values["Revenue per Beneficiary"] == 0
    assert values["Cost per Beneficiary"] == 0
