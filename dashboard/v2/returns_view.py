from __future__ import annotations

import streamlit as st

from calculator.v2.cash_flow import (
    AnnualOperatingPeriod,
    build_investor_cash_flows,
)
from calculator.v2.investor_returns import (
    calculate_investor_returns,
)


def render_returns_view(
    *,
    periods: list[AnnualOperatingPeriod],
    investment_amount: float,
) -> None:
    st.markdown("### Investor Returns")

    cash_flows = build_investor_cash_flows(
        periods=periods,
        investment_amount=investment_amount,
    )

    returns = calculate_investor_returns(cash_flows)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "NPV",
        f"₦{returns.npv:,.0f}",
    )

    col2.metric(
        "IRR",
        f"{returns.irr:.2%}",
    )

    col3.metric(
        "Investment",
        f"₦{investment_amount:,.0f}",
    )

    st.markdown("#### Investor Cash Flow")

    st.dataframe(
        [
            {
                "Year": cf.year,
                "Cash Flow (NGN)": cf.cash_flow,
            }
            for cf in cash_flows
        ],
        width="stretch",
        hide_index=True,
    )

    st.markdown("#### Return Interpretation")

    if returns.irr > 0:
        st.success("The investment case generates a positive investor return.")
    else:
        st.warning("The investment case does not currently generate a positive IRR.")
