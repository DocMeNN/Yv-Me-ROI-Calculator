from dataclasses import dataclass


@dataclass(frozen=True)
class GrantAssumptions:
    programme_cost: float
    grant_amount: float
    programme_duration_months: int
    beneficiaries: int

    def validate(self) -> None:
        if self.programme_cost <= 0:
            raise ValueError("Programme cost must be positive.")
        if self.grant_amount < 0:
            raise ValueError("Grant amount cannot be negative.")
        if self.programme_duration_months <= 0:
            raise ValueError("Programme duration must be positive.")
        if self.beneficiaries <= 0:
            raise ValueError("Beneficiaries must be positive.")


def calculate_grant_metrics(assumptions: GrantAssumptions) -> dict:
    assumptions.validate()

    gap = max(
        assumptions.programme_cost - assumptions.grant_amount,
        0.0,
    )

    coverage = min(
        assumptions.grant_amount / assumptions.programme_cost,
        1.0,
    )

    cost_per_beneficiary = (
        assumptions.programme_cost / assumptions.beneficiaries
    )

    grant_per_beneficiary = (
        assumptions.grant_amount / assumptions.beneficiaries
    )

    monthly_programme_cost = (
        assumptions.programme_cost
        / assumptions.programme_duration_months
    )

    return {
        "programme_cost": assumptions.programme_cost,
        "grant_amount": assumptions.grant_amount,
        "funding_gap": gap,
        "funding_coverage": coverage,
        "beneficiaries": assumptions.beneficiaries,
        "cost_per_beneficiary": cost_per_beneficiary,
        "grant_per_beneficiary": grant_per_beneficiary,
        "programme_duration_months": assumptions.programme_duration_months,
        "monthly_programme_cost": monthly_programme_cost,
    }
