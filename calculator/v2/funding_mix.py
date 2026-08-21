from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class FundingSource:
    name: str
    funding_type: str
    amount: float
    cost_of_capital: float = 0.0
    revenue_share: float = 0.0
    equity_percentage: float = 0.0


@dataclass(frozen=True)
class FundingMix:
    sources: List[FundingSource]

    @property
    def total_funding(self) -> float:
        return sum(source.amount for source in self.sources)

    @property
    def total_revenue_share(self) -> float:
        return sum(source.revenue_share for source in self.sources)

    @property
    def total_equity_percentage(self) -> float:
        return sum(source.equity_percentage for source in self.sources)


def evaluate_funding_mix(
    sources: List[FundingSource],
    setup_cost: float,
) -> dict:
    mix = FundingMix(sources)

    funding_gap = max(setup_cost - mix.total_funding, 0.0)
    surplus = max(mix.total_funding - setup_cost, 0.0)

    return {
        "total_funding": mix.total_funding,
        "setup_cost": setup_cost,
        "funding_gap": funding_gap,
        "surplus": surplus,
        "revenue_share": mix.total_revenue_share,
        "equity_percentage": mix.total_equity_percentage,
    }
