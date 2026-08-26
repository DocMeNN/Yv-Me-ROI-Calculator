import streamlit as st

from calculator.v2.partnership import (
    PartnershipStructure,
    STRUCTURES,
    calculate_partner_share,
    calculate_partner_investment,
    evaluate_structure,
    compare_partnership_structures,
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
            "Investor Share (%)",
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

    structure = PartnershipStructure(
        name="Custom Partnership",
        investment_amount=investment,
        investor_share=investor_share / 100,
        revenue_share=revenue_share / 100,
    )

    try:
        result = evaluate_structure(structure)
    except TypeError:
        try:
            result = evaluate_structure(
                investment=investment,
                investor_share=investor_share / 100,
                revenue_share=revenue_share / 100,
            )
        except Exception as exc:
            st.error(f"Partnership engine adapter error: {exc}")
            return
    except Exception as exc:
        st.error(f"Partnership engine error: {exc}")
        return

    def value(result, *names, default=0):
        if isinstance(result, dict):
            for name in names:
                if name in result:
                    return result[name]
        else:
            for name in names:
                if hasattr(result, name):
                    return getattr(result, name)
        return default

    partner_investment = value(
        result,
        "partner_investment",
        "investment",
        default=calculate_partner_investment(investment, structure),
    )

    partner_share = value(
        result,
        "partner_share",
        "revenue_share",
        default=calculate_partner_share(revenue_share, structure),
    )

    cols = st.columns(3)

    with cols[0]:
        st.metric(
            "Partner Investment",
            f"₦{float(partner_investment):,.0f}",
        )

    with cols[1]:
        st.metric(
            "Investor Share",
            f"{investor_share:.1f}%",
        )

    with cols[2]:
        st.metric(
            "Revenue Share",
            f"{float(partner_share):,.1f}%",
        )

    st.markdown(
        '<div class="v2-section">Available Structures</div>',
        unsafe_allow_html=True,
    )

    structure_rows = []

    for key, item in STRUCTURES.items():
        structure_rows.append(
            {
                "Structure": key,
                "Description": getattr(item, "description", ""),
            }
        )

    st.dataframe(
        structure_rows,
        width="stretch",
        hide_index=True,
    )

    with st.expander("Partnership Engine Output"):
        if isinstance(result, dict):
            st.json(result)
        else:
            st.write(vars(result))
