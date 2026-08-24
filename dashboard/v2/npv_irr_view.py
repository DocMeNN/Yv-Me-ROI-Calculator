import streamlit as st

from calculator.v2.returns import irr, npv


def render_npv_irr():
    st.markdown(
        '<div class="v2-section">NPV & IRR</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        discount_rate = st.number_input(
            "Discount Rate (%)",
            min_value=0.0,
            value=10.0,
            step=1.0,
            key="v2_discount_rate",
        ) / 100

    with col2:
        investment = st.number_input(
            "Initial Investment (NGN)",
            min_value=0.0,
            value=10000000.0,
            step=500000.0,
            key="v2_npv_investment",
        )

    annual_return = st.number_input(
        "Annual Cash Flow (NGN)",
        min_value=0.0,
        value=3000000.0,
        step=100000.0,
        key="v2_npv_cashflow",
    )

    years = st.number_input(
        "Projection Years",
        min_value=1,
        value=5,
        step=1,
        key="v2_npv_years",
    )

    cash_flows = [-investment] + [annual_return] * years

    try:
        npv_value = npv(
            discount_rate,
            cash_flows,
        )

        irr_value = irr(cash_flows)

    except Exception as exc:
        st.error(f"Returns engine error: {exc}")
        return

    cols = st.columns(2)

    with cols[0]:
        st.metric(
            "NPV",
            f"₦{float(npv_value):,.0f}",
        )

    with cols[1]:
        if irr_value is None:
            st.metric("IRR", "N/A")
        else:
            st.metric(
                "IRR",
                f"{float(irr_value):.1%}",
            )

    with st.expander("Cash Flow Series"):
        st.write(cash_flows)
