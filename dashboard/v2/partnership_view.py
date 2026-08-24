import streamlit as st

from calculator.v2.partnership import (
    PartnershipStructure,
    evaluate_partnership_structure,
)


def _value(result, *names, default=0):
    if isinstance(result, dict):
        for name in names:
            if name in result:
                return result[name]
    else:
        for name in names:
            if hasattr(result, name):
                return getattr(result, name)
    return default


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

    try:
        structure = PartnershipStructure(
            investment_amount=investment,
            investor_share=investor_share / 100,
            revenue_share=revenue_share / 100,
        )

        result = evaluate_partnership_structure(structure)

    except TypeError:
        try:
            structure = PartnershipStructure(
                investment=investment,
                investor_share=investor_share / 100,
                revenue_share=revenue_share / 100,
            )

            result = evaluate_partnership_structure(structure)

        except Exception as exc:
            st.error(f"Partnership engine adapter error: {exc}")
            return

    except Exception as exc:
        st.error(f"Partnership engine error: {exc}")
        return

    partner_return = _value(
        result,
        "investor_return",
        "partner_return",
        "expected_return",
        "return_amount",
        default=investment * investor_share / 100,
    )

    revenue_allocation = _value(
        result,
        "revenue_allocation",
        "investor_revenue",
        "revenue_share_amount",
        default=0,
    )

    remaining_share = max(0.0, 1 - (revenue_share / 100))

    cols = st.columns(4)

    metrics = [
        ("Investment", investment, "₦{:,.0f}"),
        ("Investor Equity", investor_share / 100, "{:.1%}"),
        ("Revenue Share", revenue_share / 100, "{:.1%}"),
        ("Partner Return", partner_return, "₦{:,.0f}"),
    ]

    for col, (label, value, fmt) in zip(cols, metrics):
        with col:
            try:
                st.metric(label, fmt.format(float(value)))
            except (TypeError, ValueError):
                st.metric(label, str(value))

    st.markdown(
        '<div class="v2-section">Commercial Structure</div>',
        unsafe_allow_html=True,
    )

    structure_data = [
        {
            "Component": "Investor Equity",
            "Share": investor_share / 100,
        },
        {
            "Component": "Revenue Share",
            "Share": revenue_share / 100,
        },
        {
            "Component": "Remaining Revenue",
            "Share": remaining_share,
        },
    ]

    st.dataframe(
        structure_data,
        column_config={
            "Share": st.column_config.NumberColumn(
                format="%.1f%%"
            )
        },
        width="stretch",
        hide_index=True,
    )

    if revenue_allocation:
        st.metric(
            "Investor Revenue Allocation",
            f"₦{float(revenue_allocation):,.0f}",
        )

    with st.expander("Partnership Engine Output"):
        if isinstance(result, dict):
            st.json(result)
        else:
            st.write(vars(result))
