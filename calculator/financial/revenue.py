def subscription_revenue(
    beneficiaries: int,
    monthly_subscription: float,
    collection_rate: float = 1.0,
    free_beneficiaries: int = 0,
) -> float:
    paying_beneficiaries = max(beneficiaries - free_beneficiaries, 0)
    return paying_beneficiaries * monthly_subscription * collection_rate


def annual_subscription_revenue(
    beneficiaries: int,
    monthly_subscription: float,
    collection_rate: float = 1.0,
    free_beneficiaries: int = 0,
    months: int = 12,
) -> float:
    return subscription_revenue(
        beneficiaries,
        monthly_subscription,
        collection_rate,
        free_beneficiaries,
    ) * months
