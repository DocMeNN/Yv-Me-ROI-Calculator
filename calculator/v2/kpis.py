from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class KPI:
    name: str
    value: float
    unit: str
    interpretation: str


def calculate_kpis(
    beneficiaries: int,
    paying_beneficiaries: int,
    annual_revenue: float,
    annual_operating_cost: float,
    investment: float,
) -> List[KPI]:
    collection_rate = (
        paying_beneficiaries / beneficiaries
        if beneficiaries
        else 0.0
    )

    operating_margin = (
        (annual_revenue - annual_operating_cost) / annual_revenue
        if annual_revenue
        else 0.0
    )

    roi = (
        (annual_revenue - annual_operating_cost) / investment
        if investment
        else 0.0
    )

    revenue_per_beneficiary = (
        annual_revenue / beneficiaries
        if beneficiaries
        else 0.0
    )

    cost_per_beneficiary = (
        annual_operating_cost / beneficiaries
        if beneficiaries
        else 0.0
    )

    return [
        KPI(
            "Beneficiaries",
            beneficiaries,
            "people",
            "Total programme beneficiaries",
        ),
        KPI(
            "Collection Rate",
            collection_rate,
            "%",
            "Share of beneficiaries generating collected subscription revenue",
        ),
        KPI(
            "Annual Revenue",
            annual_revenue,
            "NGN",
            "Total annual programme revenue",
        ),
        KPI(
            "Annual Operating Cost",
            annual_operating_cost,
            "NGN",
            "Total annual operating expenditure",
        ),
        KPI(
            "Operating Margin",
            operating_margin,
            "%",
            "Revenue remaining after operating costs",
        ),
        KPI(
            "ROI",
            roi,
            "%",
            "Annual net return relative to investment",
        ),
        KPI(
            "Revenue per Beneficiary",
            revenue_per_beneficiary,
            "NGN",
            "Average annual revenue generated per beneficiary",
        ),
        KPI(
            "Cost per Beneficiary",
            cost_per_beneficiary,
            "NGN",
            "Average annual operating cost per beneficiary",
        ),
    ]
