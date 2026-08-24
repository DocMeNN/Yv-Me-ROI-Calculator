import streamlit as st
from calculator.v2.investment_case import build_v2_investment_case

def render_investment_case():
    st.markdown("### Investment Case")

    investment = st.number_input(
        "Investment Amount (NGN)",
        min_value=0.0,
        value=10000000.0,
        step=1000000.0,
        format="%.0f",
    )

    revenue_share = st.number_input(
        "Investor Revenue Share (%)",
        min_value=0.0,
        max_value=100.0,
        value=20.0,
        step=1.0,
    )

    years = st.number_input(
        "Projection Period (Years)",
        min_value=1,
        max_value=20,
        value=5,
        step=1,
    )

    if st.button("Calculate Investment Case", type="primary"):
        result = build_v2_investment_case(
            investment_amount=investment,
            revenue_share=revenue_share / 100,
            years=years,
        )

        st.session_state["v2_investment_case"] = result

    result = st.session_state.get("v2_investment_case")

    if result is not None:
        st.markdown("#### Investment Case Results")
        st.json(result)
