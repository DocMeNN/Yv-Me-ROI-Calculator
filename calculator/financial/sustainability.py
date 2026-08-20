from dataclasses import dataclass
from math import ceil


@dataclass(frozen=True)
class SustainabilityAssumptions:
    monthly_fixed_cost: float
    monthly_variable_cost_per_beneficiary: float
    monthly_revenue_per_beneficiary: float
    beneficiaries: int

    def validate(self) -> None:
        if self.monthly_fixed_cost < 0:
            raise ValueError("Monthly fixed cost cannot be negative.")
        if self.monthly_variable_cost_per_beneficiary < 0:
            raise ValueError("Variable cost cannot be negative.")
        if self.monthly_revenue_per_beneficiary < 0:
            raise ValueError("Revenue per beneficiary cannot be negative.")
        if self.beneficiaries < 0:
            raise ValueError("Beneficiaries cannot be negative.")


def calculate_sustainability(
    assumptions: SustainabilityAssumptions,
) -> dict:
    assumptions.validate()

    contribution_per_beneficiary = (
        assumptions.monthly_revenue_per_beneficiary
        - assumptions.monthly_variable_cost_per_beneficiary
    )

    if contribution_per_beneficiary <= 0:
        break_even_beneficiaries = None
        break_even_reached = False
    else:
        break_even_beneficiaries = ceil(
            assumptions.monthly_fixed_cost
            / contribution_per_beneficiary
        )
        break_even_reached = (
            assumptions.beneficiaries >= break_even_beneficiaries
        )

    monthly_revenue = (
        assumptions.beneficiaries
        * assumptions.monthly_revenue_per_beneficiary
    )

    monthly_variable_cost = (
        assumptions.beneficiaries
        * assumptions.monthly_variable_cost_per_beneficiary
    )

    monthly_contribution = (
        monthly_revenue
        - monthly_variable_cost
        - assumptions.monthly_fixed_cost
    )

    if assumptions.beneficiaries > 0:
        required_subscription = (
            assumptions.monthly_fixed_cost
            / assumptions.beneficiaries
        ) + assumptions.monthly_variable_cost_per_beneficiary
    else:
        required_subscription = None

    return {
        "beneficiaries": assumptions.beneficiaries,
        "monthly_fixed_cost": assumptions.monthly_fixed_cost,
        "monthly_revenue": monthly_revenue,
        "monthly_variable_cost": monthly_variable_cost,
        "monthly_contribution": monthly_contribution,
        "contribution_per_beneficiary": contribution_per_beneficiary,
        "break_even_beneficiaries": break_even_beneficiaries,
        "break_even_reached": break_even_reached,
        "required_subscription": required_subscription,
    }
