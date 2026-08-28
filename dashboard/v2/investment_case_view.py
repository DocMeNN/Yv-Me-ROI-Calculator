import streamlit as st
from calculator.v2.investment_case import build_v2_investment_case


def render_investment_case():
    st.markdown("### Investment Case")

    col1, col2, col3 = st.columns(3)

    with col1:
        investment = st.number_input(
            "Initial Investment (NGN)",
            min_value=0.0,
            value=10000000.0,
            step=1000000.0,
            format="%.0f",
            key="v2_investment_amount",
        )

    with col2:
        beneficiaries = st.number_input(
            "Starting Beneficiaries",
            min_value=1,
            value=100,
            step=10,
            key="v2_starting_beneficiaries",
        )

    with col3:
        subscription = st.number_input(
            "Monthly Subscription (NGN)",
            min_value=0.0,
            value=15000.0,
            step=1000.0,
            format="%.0f",
            key="v2_monthly_subscription",
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        operating_cost = st.number_input(
            "Annual Operating Cost (NGN)",
            min_value=0.0,
            value=13200000.0,
            step=500000.0,
            format="%.0f",
            key="v2_annual_operating_cost",
        )

    with col5:
        setup_cost = st.number_input(
            "Setup Cost (NGN)",
            min_value=0.0,
            value=investment,
            step=500000.0,
            format="%.0f",
            key="v2_setup_cost",
        )

    with col6:
        revenue_share = st.number_input(
            "Investor Revenue Share (%)",
            min_value=0.0,
            max_value=100.0,
            value=20.0,
            step=1.0,
            key="v2_investor_revenue_share",
        )

    years = st.number_input(
        "Projection Period (Years)",
        min_value=1,
        max_value=20,
        value=5,
        step=1,
        key="v2_projection_years",
    )

    if st.button("Calculate Investment Case", type="primary"):
        result = build_v2_investment_case(
            starting_beneficiaries=int(beneficiaries),
            monthly_subscription=float(subscription),
            annual_operating_cost=float(operating_cost),
            setup_cost=float(setup_cost),
            initial_investment=float(investment),
            revenue_share=revenue_share / 100,
            years=int(years),
        )

        st.session_state["v2_investment_case"] = result
        st.session_state["v2_periods"] = result["base_periods"]

    result = st.session_state.get("v2_investment_case")

    if result is not None:
        st.markdown("#### Investment Case Results")
        st.json(result)

