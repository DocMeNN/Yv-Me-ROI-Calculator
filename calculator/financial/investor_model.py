from dataclasses import dataclass


@dataclass(frozen=True)
class InvestorAssumptions:
    investment_amount: float
    investor_revenue: float
    monthly_investor_cashflow: float
    revenue_share: float = 0.0

    def validate(self) -> None:
        if self.investment_amount <= 0:
            raise ValueError("Investment amount must be positive.")
        if self.investor_revenue < 0:
            raise ValueError("Investor revenue cannot be negative.")
        if self.monthly_investor_cashflow < 0:
            raise ValueError("Monthly investor cashflow cannot be negative.")
        if not 0 <= self.revenue_share <= 1:
            raise ValueError("Revenue share must be between 0 and 1.")


def calculate_investor_metrics(assumptions: InvestorAssumptions) -> dict:
    assumptions.validate()

    investment = assumptions.investment_amount
    revenue = assumptions.investor_revenue
    net_return = revenue - investment
    roi = net_return / investment

    if assumptions.monthly_investor_cashflow > 0:
        payback_months = investment / assumptions.monthly_investor_cashflow
    else:
        payback_months = None

    return {
        "investment_amount": investment,
        "investor_revenue": revenue,
        "net_return": net_return,
        "roi": roi,
        "revenue_share": assumptions.revenue_share,
        "monthly_investor_cashflow": assumptions.monthly_investor_cashflow,
        "payback_months": payback_months,
    }
