from calculator.v2.cash_flow import AnnualOperatingPeriod, build_investor_cash_flows


def investor_roi(cash_flows):
    investment = sum(cf.investment for cf in cash_flows)
    returns = sum(cf.revenue_share for cf in cash_flows)
    if investment == 0:
        return 0.0
    return (returns - investment) / investment


def payback_year(cash_flows):
    for cf in cash_flows:
        if cf.year > 0 and cf.cumulative_cash_flow >= 0:
            return cf.year
    return None


def net_investor_return(cash_flows):
    return sum(cf.net_cash_flow for cf in cash_flows)


def investor_summary(cash_flows):
    return {
        "total_investment": sum(cf.investment for cf in cash_flows),
        "total_returns": sum(cf.revenue_share for cf in cash_flows),
        "net_return": net_investor_return(cash_flows),
        "roi": investor_roi(cash_flows),
        "payback_year": payback_year(cash_flows),
    }
