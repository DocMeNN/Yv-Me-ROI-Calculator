from __future__ import annotations

import streamlit as st

from calculator.v2.kpis import calculate_kpis


def render_kpis_view(
    *,
    investment_amount: float,
    revenue: float,
    operating_cost: float,
) -> None:
    st.markdown("### KPI Intelligence")

    try:
        result = calculate_kpis(
            investment_amount=investment_amount,
            revenue=revenue,
            operating_cost=operating_cost,
        )
    except TypeError:
        st.info("KPI engine requires its configured V2 inputs.")
        return

    values = (
        result if isinstance(result, dict)
        else vars(result)
    )

    cols = st.columns(min(len(values), 4))

    for index, (name, value) in enumerate(values.items()):
        if index >= len(cols):
            break

        label = name.replace("_", " ").title()

        if isinstance(value, (int, float)):
            cols[index].metric(label, f"{value:,.2f}")
        else:
            cols[index].metric(label, str(value))
