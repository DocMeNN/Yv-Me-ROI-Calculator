def break_even_beneficiaries(
    monthly_fixed_cost: float,
    monthly_variable_cost_per_beneficiary: float,
    monthly_revenue_per_beneficiary: float,
) -> int:
    contribution_per_beneficiary = (
        monthly_revenue_per_beneficiary - monthly_variable_cost_per_beneficiary
    )
    if contribution_per_beneficiary <= 0:
        raise ValueError("Revenue per beneficiary must exceed variable cost.")
    return int(-(-monthly_fixed_cost // contribution_per_beneficiary))


def break_even_subscription(
    monthly_cost: float,
    paying_beneficiaries: int,
    collection_rate: float = 1.0,
) -> float:
    if paying_beneficiaries <= 0 or collection_rate <= 0:
        raise ValueError("Paying beneficiaries and collection rate must be positive.")
    return monthly_cost / (paying_beneficiaries * collection_rate)
