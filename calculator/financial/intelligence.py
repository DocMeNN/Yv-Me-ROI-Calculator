from calculator.financial.funding import funding_coverage, funding_gap
from calculator.financial.grant_model import GrantAssumptions, calculate_grant_metrics
from calculator.financial.investor_model import InvestorAssumptions, calculate_investor_metrics
from calculator.financial.revenue_model import RevenueAssumptions, calculate_revenue
from calculator.financial.sustainability import (
    SustainabilityAssumptions,
    calculate_sustainability,
)


def calculate_financial_intelligence(
    beneficiaries: int,
    programme_cost: float,
    monthly_subscription: float,
    collection_rate: float = 1.0,
    free_beneficiaries: int = 0,
    grant_amount: float = 0.0,
    investment_amount: float = 0.0,
    investor_revenue: float = 0.0,
    monthly_investor_cashflow: float = 0.0,
    revenue_share: float = 0.0,
    monthly_fixed_cost: float = 0.0,
    monthly_variable_cost_per_beneficiary: float = 0.0,
    programme_duration_months: int = 12,
) -> dict:
    revenue = calculate_revenue(
        RevenueAssumptions(
            beneficiaries=beneficiaries,
            monthly_subscription=monthly_subscription,
            collection_rate=collection_rate,
            free_beneficiaries=free_beneficiaries,
            months=programme_duration_months,
        )
    )

    grant = calculate_grant_metrics(
        GrantAssumptions(
            programme_cost=programme_cost,
            grant_amount=grant_amount,
            programme_duration_months=programme_duration_months,
            beneficiaries=beneficiaries,
        )
    )

    sustainability = calculate_sustainability(
        SustainabilityAssumptions(
            monthly_fixed_cost=monthly_fixed_cost,
            monthly_variable_cost_per_beneficiary=monthly_variable_cost_per_beneficiary,
            monthly_revenue_per_beneficiary=monthly_subscription * collection_rate,
            beneficiaries=beneficiaries - free_beneficiaries,
        )
    )

    investor = None
    if investment_amount > 0:
        investor = calculate_investor_metrics(
            InvestorAssumptions(
                investment_amount=investment_amount,
                investor_revenue=investor_revenue,
                monthly_investor_cashflow=monthly_investor_cashflow,
                revenue_share=revenue_share,
            )
        )

    return {
        "revenue": revenue,
        "grant": grant,
        "sustainability": sustainability,
        "investor": investor,
        "funding_gap": funding_gap(programme_cost, grant_amount),
        "funding_coverage": funding_coverage(programme_cost, grant_amount),
    }
