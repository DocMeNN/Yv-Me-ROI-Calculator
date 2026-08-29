from __future__ import annotations

import streamlit as st

from calculator.v2.cash_flow import (
    AnnualOperatingPeriod,
    build_investor_cash_flows,
)


def render_cash_flow_view(
    *,
    periods: list[AnnualOperatingPeriod],
    investment_amount: float,
) -> None:
    st.markdown("### Cash Flow")

    revenue_share = float(
        st.session_state.get("v2_revenue_share", 0.20)
    )

    cash_flows = build_investor_cash_flows(
        periods=periods,
        initial_investment=investment_amount,
        revenue_share=revenue_share,
    )

    st.dataframe(
        [
            {
                "Year": cf.year,
                "Cash Flow (NGN)": cf.net_cash_flow,
            }
            for cf in cash_flows
        ],
        width="stretch",
        hide_index=True,
    )

    total_cash_flow = sum(cf.net_cash_flow for cf in cash_flows)

    col1, col2 = st.columns(2)

    col1.metric(
        "Total Cash Flow",
        f"₦{total_cash_flow:,.0f}",
    )

    col2.metric(
        "Initial Investment",
        f"₦{investment_amount:,.0f}",
    )
