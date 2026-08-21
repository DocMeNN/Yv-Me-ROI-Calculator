from dataclasses import dataclass


@dataclass(frozen=True)
class SensitivityPoint:
    parameter: str
    value: float
    annual_revenue: float
    annual_operating_cost: float
    net_cash_flow: float
    roi: float


def calculate_sensitivity(
    parameter: str,
    values: list[float],
    beneficiaries: int,
    monthly_subscription: float,
    annual_operating_cost: float,
    investment: float,
    collection_rate: float = 1.0,
) -> list[SensitivityPoint]:
    results = []

    for value in values:
        if parameter == "subscription":
            subscription = value
            revenue = (
                beneficiaries
                * subscription
                * 12
                * collection_rate
            )
            cost = annual_operating_cost

        elif parameter == "beneficiaries":
            revenue = (
                int(value)
                * monthly_subscription
                * 12
                * collection_rate
            )
            cost = annual_operating_cost

        elif parameter == "operating_cost":
            revenue = (
                beneficiaries
                * monthly_subscription
                * 12
                * collection_rate
            )
            cost = value

        elif parameter == "collection_rate":
            revenue = (
                beneficiaries
                * monthly_subscription
                * 12
                * value
            )
            cost = annual_operating_cost

        else:
            raise ValueError(f"Unsupported sensitivity parameter: {parameter}")

        net_cash_flow = revenue - cost
        roi = (
            net_cash_flow / investment
            if investment
            else 0.0
        )

        results.append(
            SensitivityPoint(
                parameter=parameter,
                value=value,
                annual_revenue=revenue,
                annual_operating_cost=cost,
                net_cash_flow=net_cash_flow,
                roi=roi,
            )
        )

    return results
