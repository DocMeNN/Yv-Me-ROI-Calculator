from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class PartnershipStructure:
    name: str
    funding_type: str
    initial_investment: float
    revenue_share: float = 0.0
    grant_amount: float = 0.0
    equity_percentage: float = 0.0
    working_capital: float = 0.0


STRUCTURES = {
    "revenue_share": PartnershipStructure(
        name="Revenue Share",
        funding_type="revenue_share",
        initial_investment=0.0,
        revenue_share=0.10,
    ),
    "grant": PartnershipStructure(
        name="Grant",
        funding_type="grant",
        initial_investment=0.0,
        grant_amount=0.0,
    ),
    "equity": PartnershipStructure(
        name="Equity",
        funding_type="equity",
        initial_investment=0.0,
        equity_percentage=0.20,
    ),
    "blended": PartnershipStructure(
        name="Blended Finance",
        funding_type="blended",
        initial_investment=0.0,
        revenue_share=0.05,
        grant_amount=0.0,
    ),
    "sponsorship": PartnershipStructure(
        name="Programme Sponsorship",
        funding_type="sponsorship",
        initial_investment=0.0,
        grant_amount=0.0,
    ),
    "working_capital": PartnershipStructure(
        name="Working Capital",
        funding_type="working_capital",
        initial_investment=0.0,
        working_capital=0.0,
    ),
}


def calculate_partner_share(revenue: float, structure: PartnershipStructure) -> float:
    return revenue * structure.revenue_share


def calculate_partner_investment(
    structure: PartnershipStructure,
    setup_cost: float,
) -> float:
    if structure.initial_investment > 0:
        return structure.initial_investment

    if structure.working_capital > 0:
        return structure.working_capital

    if structure.grant_amount > 0:
        return structure.grant_amount

    return setup_cost if structure.funding_type in {"revenue_share", "equity"} else 0.0


def evaluate_structure(
    structure: PartnershipStructure,
    annual_revenue: float,
    annual_operating_cost: float,
    setup_cost: float,
) -> dict:
    partner_investment = calculate_partner_investment(structure, setup_cost)
    partner_share = calculate_partner_share(annual_revenue, structure)
    programme_contribution = annual_revenue - annual_operating_cost

    return {
        "name": structure.name,
        "funding_type": structure.funding_type,
        "partner_investment": partner_investment,
        "partner_revenue_share": partner_share,
        "programme_contribution": programme_contribution,
        "equity_percentage": structure.equity_percentage,
        "grant_amount": structure.grant_amount,
        "working_capital": structure.working_capital,
    }


def compare_partnership_structures(
    annual_revenue: float,
    annual_operating_cost: float,
    setup_cost: float,
) -> dict:
    return {
        key: evaluate_structure(
            structure,
            annual_revenue,
            annual_operating_cost,
            setup_cost,
        )
        for key, structure in STRUCTURES.items()
    }
