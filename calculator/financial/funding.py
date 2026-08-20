def funding_gap(
    programme_cost: float,
    confirmed_funding: float,
) -> float:
    return max(programme_cost - confirmed_funding, 0.0)


def funding_coverage(
    programme_cost: float,
    confirmed_funding: float,
) -> float:
    if programme_cost <= 0:
        raise ValueError("Programme cost must be positive.")
    return confirmed_funding / programme_cost
