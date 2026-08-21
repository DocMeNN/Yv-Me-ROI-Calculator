from typing import Iterable, Optional


def npv(cash_flows: Iterable[float], discount_rate: float) -> float:
    if discount_rate <= -1:
        raise ValueError("discount_rate must be greater than -1")

    return sum(
        cash_flow / ((1 + discount_rate) ** period)
        for period, cash_flow in enumerate(cash_flows)
    )


def irr(
    cash_flows: Iterable[float],
    lower: float = -0.9999,
    upper: float = 10.0,
    tolerance: float = 1e-10,
    max_iterations: int = 200,
) -> Optional[float]:
    flows = list(cash_flows)

    if not flows or not any(cf < 0 for cf in flows) or not any(cf > 0 for cf in flows):
        return None

    low = lower
    high = upper
    low_value = npv(flows, low)
    high_value = npv(flows, high)

    if low_value * high_value > 0:
        return None

    for _ in range(max_iterations):
        mid = (low + high) / 2
        mid_value = npv(flows, mid)

        if abs(mid_value) <= tolerance:
            return mid

        if low_value * mid_value <= 0:
            high = mid
            high_value = mid_value
        else:
            low = mid
            low_value = mid_value

    return (low + high) / 2
