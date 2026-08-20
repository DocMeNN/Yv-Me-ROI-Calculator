from dataclasses import dataclass

from calculator.financial.revenue import (
    annual_subscription_revenue,
    subscription_revenue,
)


@dataclass(frozen=True)
class RevenueAssumptions:
    beneficiaries: int
    monthly_subscription: float
    collection_rate: float = 1.0
    free_beneficiaries: int = 0
    months: int = 12

    def validate(self) -> None:
        if self.beneficiaries < 0:
            raise ValueError("Beneficiaries cannot be negative.")
        if self.monthly_subscription < 0:
            raise ValueError("Monthly subscription cannot be negative.")
        if not 0 <= self.collection_rate <= 1:
            raise ValueError("Collection rate must be between 0 and 1.")
        if self.free_beneficiaries < 0:
            raise ValueError("Free beneficiaries cannot be negative.")
        if self.free_beneficiaries > self.beneficiaries:
            raise ValueError("Free beneficiaries cannot exceed beneficiaries.")
        if self.months <= 0:
            raise ValueError("Months must be positive.")


def calculate_revenue(assumptions: RevenueAssumptions) -> dict:
    assumptions.validate()

    monthly = subscription_revenue(
        beneficiaries=assumptions.beneficiaries,
        monthly_subscription=assumptions.monthly_subscription,
        collection_rate=assumptions.collection_rate,
        free_beneficiaries=assumptions.free_beneficiaries,
    )

    annual = annual_subscription_revenue(
        beneficiaries=assumptions.beneficiaries,
        monthly_subscription=assumptions.monthly_subscription,
        collection_rate=assumptions.collection_rate,
        free_beneficiaries=assumptions.free_beneficiaries,
        months=assumptions.months,
    )

    paying = assumptions.beneficiaries - assumptions.free_beneficiaries

    return {
        "beneficiaries": assumptions.beneficiaries,
        "paying_beneficiaries": paying,
        "free_beneficiaries": assumptions.free_beneficiaries,
        "monthly_subscription": assumptions.monthly_subscription,
        "collection_rate": assumptions.collection_rate,
        "monthly_revenue": monthly,
        "annual_revenue": annual,
    }
