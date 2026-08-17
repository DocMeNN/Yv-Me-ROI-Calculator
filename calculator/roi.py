from data.model import PROGRAMME


def cost_per_chew(total_cost=None):
    total = total_cost or PROGRAMME["total_budget"]
    return total / PROGRAMME["chews"]


def cost_per_beneficiary(total_cost=None):
    total = total_cost or PROGRAMME["total_budget"]
    return total / PROGRAMME["beneficiaries"]


def monthly_programme_cost(total_cost=None):
    total = total_cost or PROGRAMME["total_budget"]
    return total / PROGRAMME["pilot_months"]


def annual_roi(revenue, cost=None):
    total_cost = cost or PROGRAMME["total_budget"]

    if total_cost == 0:
        return 0

    return (revenue - total_cost) / total_cost


def break_even_revenue(cost=None):
    return cost or PROGRAMME["total_budget"]
