from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Scenario:
    name: str
    beneficiaries_growth: float
    collection_rate: float
    cost_multiplier: float
    subscription_multiplier: float


SCENARIOS = {
    "conservative": Scenario(
        name="Conservative",
        beneficiaries_growth=0.05,
        collection_rate=0.80,
        cost_multiplier=1.15,
        subscription_multiplier=0.90,
    ),
    "base": Scenario(
        name="Base",
        beneficiaries_growth=0.10,
        collection_rate=0.90,
        cost_multiplier=1.00,
        subscription_multiplier=1.00,
    ),
    "growth": Scenario(
        name="Growth",
        beneficiaries_growth=0.20,
        collection_rate=0.95,
        cost_multiplier=0.95,
        subscription_multiplier=1.05,
    ),
    "scale": Scenario(
        name="Scale",
        beneficiaries_growth=0.35,
        collection_rate=0.97,
        cost_multiplier=0.90,
        subscription_multiplier=1.10,
    ),
}


def project_scenario(
    scenario: Scenario,
    starting_beneficiaries: int,
    monthly_subscription: float,
    annual_operating_cost: float,
    years: int = 5,
) -> List[dict]:
    results = []
    beneficiaries = starting_beneficiaries

    for year in range(1, years + 1):
        beneficiaries = round(
            beneficiaries * (1 + scenario.beneficiaries_growth)
        )

        subscription = monthly_subscription * scenario.subscription_multiplier
        annual_revenue = (
            beneficiaries
            * subscription
            * 12
            * scenario.collection_rate
        )

        annual_cost = annual_operating_cost * scenario.cost_multiplier

        results.append(
            {
                "year": year,
                "beneficiaries": beneficiaries,
                "subscription": subscription,
                "collection_rate": scenario.collection_rate,
                "revenue": annual_revenue,
                "operating_cost": annual_cost,
                "net_cash_flow": annual_revenue - annual_cost,
            }
        )

    return results


def compare_scenarios(
    starting_beneficiaries: int,
    monthly_subscription: float,
    annual_operating_cost: float,
    years: int = 5,
) -> dict:
    return {
        key: project_scenario(
            scenario,
            starting_beneficiaries,
            monthly_subscription,
            annual_operating_cost,
            years,
        )
        for key, scenario in SCENARIOS.items()
    }
