import streamlit as st

from calculator.v2.partnership import (
    PartnershipStructure,
    STRUCTURES,
    calculate_partner_share,
    calculate_partner_investment,
    evaluate_structure,
)


def render_partnership():
    st.markdown(
        '<div class="v2-section">Partnership Structure</div>',
        unsafe_allow_html=True,
    )

    st.caption(
        "Evaluate the proposed private-partnership structure and commercial allocation."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        investment = st.number_input(
            "Investment Amount (NGN)",
            min_value=0.0,
            value=10000000.0,
            step=500000.0,
            key="v2_partnership_investment",
        )

    with col2:
        investor_share = st.number_input(
            "Investor Equity (%)",
            min_value=0.0,
            max_value=100.0,
            value=40.0,
            step=5.0,
            key="v2_partnership_investor_share",
        )

    with col3:
        revenue_share = st.number_input(
            "Revenue Share (%)",
            min_value=0.0,
            max_value=100.0,
            value=20.0,
            step=5.0,
            key="v2_partnership_revenue_share",
        )

    annual_revenue = st.number_input(
        "Annual Revenue (NGN)",
        min_value=0.0,
        value=18000000.0,
        step=500000.0,
        format="%.0f",
        key="v2_partnership_annual_revenue",
    )

    annual_operating_cost = st.number_input(
        "Annual Operating Cost (NGN)",
        min_value=0.0,
        value=13200000.0,
        step=500000.0,
        format="%.0f",
        key="v2_partnership_operating_cost",
    )

    setup_cost = st.number_input(
        "Setup Cost (NGN)",
        min_value=0.0,
        value=investment,
        step=500000.0,
        format="%.0f",
        key="v2_partnership_setup_cost",
    )

    structure = PartnershipStructure(
        name="Custom Partnership",
        funding_type="revenue_share",
        initial_investment=float(investment),
        revenue_share=revenue_share / 100,
        equity_percentage=investor_share / 100,
    )

    try:
        result = evaluate_structure(
            structure=structure,
            annual_revenue=float(annual_revenue),
            annual_operating_cost=float(annual_operating_cost),
            setup_cost=float(setup_cost),
        )
    except Exception as exc:
        st.error(f"Partnership engine error: {exc}")
        return

    partner_investment = result.get(
        "partner_investment",
        calculate_partner_investment(structure, setup_cost),
    )

    partner_revenue_share = result.get(
        "partner_revenue_share",
        calculate_partner_share(annual_revenue, structure),
    )

    cols = st.columns(4)

    with cols[0]:
        st.metric(
            "Partner Investment",
            f"₦{float(partner_investment):,.0f}",
        )

    with cols[1]:
        st.metric(
            "Investor Equity",
            f"{investor_share:.1f}%",
        )

    with cols[2]:
        st.metric(
            "Revenue Share",
            f"{revenue_share:.1f}%",
        )

    with cols[3]:
        st.metric(
            "Annual Partner Revenue",
            f"₦{float(partner_revenue_share):,.0f}",
        )

    st.markdown(
        '<div class="v2-section">Available Structures</div>',
        unsafe_allow_html=True,
    )

    structure_rows = [
        {
            "Structure": key,
            "Funding Type": item.funding_type,
            "Initial Investment": item.initial_investment,
            "Revenue Share": item.revenue_share,
            "Equity": item.equity_percentage,
            "Grant": item.grant_amount,
            "Working Capital": item.working_capital,
        }
        for key, item in STRUCTURES.items()
    ]

    st.dataframe(
        structure_rows,
        width="stretch",
        hide_index=True,
    )

    with st.expander("Partnership Engine Output"):
        st.json(result)
