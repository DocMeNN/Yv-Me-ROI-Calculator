from calculator.v2.scenarios import (
    SCENARIOS,
    compare_scenarios,
    project_scenario,
)


def test_scenario_catalog():
    assert set(SCENARIOS.keys()) == {
        "conservative",
        "base",
        "growth",
        "scale",
    }


def test_scenario_projection():
    result = project_scenario(
        SCENARIOS["base"],
        starting_beneficiaries=1000,
        monthly_subscription=15000,
        annual_operating_cost=120000000,
        years=5,
    )

    assert len(result) == 5
    assert result[0]["year"] == 1
    assert result[0]["beneficiaries"] == 1100
    assert result[0]["subscription"] == 15000
    assert result[0]["revenue"] == 178200000


def test_scenario_comparison():
    result = compare_scenarios(
        starting_beneficiaries=1000,
        monthly_subscription=15000,
        annual_operating_cost=120000000,
        years=5,
    )

    assert len(result) == 4
    assert len(result["conservative"]) == 5
    assert len(result["base"]) == 5
    assert len(result["growth"]) == 5
    assert len(result["scale"]) == 5

    assert (
        result["scale"][-1]["beneficiaries"]
        > result["base"][-1]["beneficiaries"]
        > result["conservative"][-1]["beneficiaries"]
    )
