from __future__ import annotations

import streamlit as st

from calculator.v2.cash_flow import (
    AnnualOperatingPeriod,
    build_investor_cash_flows,
)
from calculator.v2.investor_returns import investor_summary
from calculator.v2.returns import irr, npv


def render_returns():
    st.markdown(
        '<div class="v2-section">Investor Returns</div>',
        unsafe_allow_html=True,
    )

    st.caption(
        "Evaluate investor cash returns, ROI, payback, NPV and IRR."
    )

    investment_amount = st.number_input(
        "Investment Amount (NGN)",
        min_value=0.0,
        value=10000000.0,
        step=500000.0,
        key="v2_returns_investment",
    )

    periods = st.session_state.get("v2_periods")

    if not periods:
        periods = [
            AnnualOperatingPeriod(
                year=year,
                revenue=0.0,
                operating_cost=0.0,
                investor_share=0.0,
            )
            for year in range(1, 6)
        ]

    try:
        cash_flows = build_investor_cash_flows(
            periods=periods,
            investment_amount=investment_amount,
        )

        summary = investor_summary(cash_flows)

        values = [cf.net_cash_flow for cf in cash_flows]

        try:
            calculated_npv = npv(values)
        except TypeError:
            calculated_npv = npv(0.10, values)

        try:
            calculated_irr = irr(values)
        except TypeError:
            calculated_irr = irr(values)

    except Exception as exc:
        st.error(f"Investor Returns engine error: {exc}")
        return

    cols = st.columns(4)

    with cols[0]:
        st.metric(
            "Total Investment",
            f"₦{float(summary['total_investment']):,.0f}",
        )

    with cols[1]:
        st.metric(
            "Total Returns",
            f"₦{float(summary['total_returns']):,.0f}",
        )

    with cols[2]:
        st.metric(
            "ROI",
            f"{float(summary['roi']):.1%}",
        )

    with cols[3]:
        payback = summary["payback_year"]
        st.metric(
            "Payback",
            f"Year {payback}" if payback is not None else "Not reached",
        )

    st.markdown(
        '<div class="v2-section">NPV / IRR</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "NPV",
            f"₦{float(calculated_npv):,.0f}",
        )

    with col2:
        st.metric(
            "IRR",
            f"{float(calculated_irr):.2%}",
        )

    st.markdown(
        '<div class="v2-section">Investor Cash Flow</div>',
        unsafe_allow_html=True,
    )

    table = [
        {
            "Year": cf.year,
            "Investment (NGN)": cf.investment,
            "Revenue Share (NGN)": cf.revenue_share,
            "Net Cash Flow (NGN)": cf.net_cash_flow,
            "Cumulative Cash Flow (NGN)": cf.cumulative_cash_flow,
        }
        for cf in cash_flows
    ]

    st.dataframe(
        table,
        width="stretch",
        hide_index=True,
    )

    with st.expander("Investor Returns Engine Output"):
        st.json(summary)
