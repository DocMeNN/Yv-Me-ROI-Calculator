from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class InvestmentTimeline:
    years: int = 5
    initial_investment: float = 0.0


@dataclass(frozen=True)
class AnnualOperatingPeriod:
    year: int
    beneficiaries: int
    paying_beneficiaries: int
    revenue: float
    operating_cost: float
    grant_funding: float = 0.0
    capital_expenditure: float = 0.0


@dataclass(frozen=True)
class ProgrammeCashFlow:
    year: int
    revenue: float
    operating_cost: float
    grant_funding: float
    capital_expenditure: float
    net_operating_cash_flow: float
    net_cash_flow: float
    cumulative_cash_flow: float


@dataclass(frozen=True)
class InvestorCashFlow:
    year: int
    investment: float
    revenue_share: float
    net_cash_flow: float
    cumulative_cash_flow: float


def build_programme_cash_flows(
    periods: List[AnnualOperatingPeriod],
    initial_investment: float = 0.0,
) -> List[ProgrammeCashFlow]:
    results = []
    cumulative = -initial_investment

    if initial_investment:
        results.append(
            ProgrammeCashFlow(
                year=0,
                revenue=0.0,
                operating_cost=0.0,
                grant_funding=0.0,
                capital_expenditure=initial_investment,
                net_operating_cash_flow=0.0,
                net_cash_flow=-initial_investment,
                cumulative_cash_flow=cumulative,
            )
        )

    for period in periods:
        net_operating = period.revenue + period.grant_funding - period.operating_cost
        net_cash = net_operating - period.capital_expenditure
        cumulative += net_cash

        results.append(
            ProgrammeCashFlow(
                year=period.year,
                revenue=period.revenue,
                operating_cost=period.operating_cost,
                grant_funding=period.grant_funding,
                capital_expenditure=period.capital_expenditure,
                net_operating_cash_flow=net_operating,
                net_cash_flow=net_cash,
                cumulative_cash_flow=cumulative,
            )
        )

    return results


def build_investor_cash_flows(
    periods: List[AnnualOperatingPeriod],
    initial_investment: float,
    revenue_share: float,
) -> List[InvestorCashFlow]:
    results = []
    cumulative = -initial_investment

    results.append(
        InvestorCashFlow(
            year=0,
            investment=initial_investment,
            revenue_share=0.0,
            net_cash_flow=-initial_investment,
            cumulative_cash_flow=cumulative,
        )
    )

    for period in periods:
        investor_revenue = period.revenue * revenue_share
        cumulative += investor_revenue

        results.append(
            InvestorCashFlow(
                year=period.year,
                investment=0.0,
                revenue_share=investor_revenue,
                net_cash_flow=investor_revenue,
                cumulative_cash_flow=cumulative,
            )
        )

    return results
