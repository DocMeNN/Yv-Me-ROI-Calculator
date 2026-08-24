import streamlit as st

from calculator.v2.investment_case import build_v2_investment_case


def render_investment_case():
    st.markdown(
        '<div class="v2-section">Investment Case</div>',
        unsafe_allow_html=True,
    )

    st.caption(
        "V2 investment-case engine — executive view of the underlying financial case."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        chews = st.number_input(
            "CHEWs",
            min_value=1,
            value=10,
            step=10,
            key="v2_chews",
        )

    with col2:
        patients_per_chew = st.number_input(
            "Patients per CHEW",
            min_value=1,
            value=10,
            step=1,
            key="v2_patients_per_chew",
        )

    with col3:
        subscription = st.number_input(
            "Subscription / Patient / Month (NGN)",
            min_value=0.0,
            value=15000.0,
            step=500.0,
            key="v2_subscription",
        )

    try:
        result = build_v2_investment_case(
            chews=chews,
            patients_per_chew=patients_per_chew,
            subscription_per_patient=subscription,
        )
    except TypeError:
        try:
            result = build_v2_investment_case(
                chews,
                patients_per_chew,
                subscription,
            )
        except TypeError:
            st.error(
                "Investment Case engine signature does not match the current dashboard adapter."
            )
            return

    if not isinstance(result, dict):
        result = vars(result)

    def first_value(*names, default=0):
        for name in names:
            if name in result:
                return result[name]
        return default

    patients = first_value(
        "patients",
        "total_patients",
        "patient_count",
    )

    monthly_revenue = first_value(
        "monthly_revenue",
        "monthly_subscription_revenue",
        "revenue_monthly",
    )

    annual_revenue = first_value(
        "annual_revenue",
        "annual_subscription_revenue",
        "revenue_annual",
    )

    investment = first_value(
        "investment",
        "initial_investment",
        "setup_cost",
        "total_investment",
    )

    cols = st.columns(4)

    metrics = [
        ("Patients", patients, "{:,.0f}"),
        ("Monthly Revenue", monthly_revenue, "₦{:,.0f}"),
        ("Annual Revenue", annual_revenue, "₦{:,.0f}"),
        ("Initial Investment", investment, "₦{:,.0f}"),
    ]

    for col, (label, value, fmt) in zip(cols, metrics):
        with col:
            try:
                display_value = fmt.format(float(value))
            except (TypeError, ValueError):
                display_value = str(value)

            st.metric(label, display_value)

    with st.expander("Investment Case Engine Output"):
        st.json(result)
