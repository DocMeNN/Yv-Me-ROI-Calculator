def investor_return(
    investment_amount: float,
    investor_revenue: float,
) -> float:
    if investment_amount <= 0:
        raise ValueError("Investment amount must be positive.")
    return investor_revenue - investment_amount


def investor_roi(
    investment_amount: float,
    investor_revenue: float,
) -> float:
    if investment_amount <= 0:
        raise ValueError("Investment amount must be positive.")
    return (investor_revenue - investment_amount) / investment_amount


def payback_months(
    investment_amount: float,
    monthly_investor_cashflow: float,
) -> float:
    if investment_amount < 0:
        raise ValueError("Investment amount cannot be negative.")
    if monthly_investor_cashflow <= 0:
        raise ValueError("Monthly investor cashflow must be positive.")
    return investment_amount / monthly_investor_cashflow
