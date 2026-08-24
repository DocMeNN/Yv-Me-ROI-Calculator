import streamlit as st

from calculator.v2.investor_returns import (
    calculate_investor_returns,
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


def render_returns():
    st.markdown(
        '<div class="v2-section">Investor Returns</div>',
        unsafe_allow_html=True,
    )

    st.caption(
        "Evaluate investor cash returns, payback and return performance."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        investment = st.number_input(
            "Investment Amount (NGN)",
            min_value=0.0,
            value=10000000.0,
            step=500000.0,
            key="v2_returns_investment",
        )

    with col2:
        annual_cash_return = st.number_input(
            "Annual Cash Return (NGN)",
            min_value=0.0,
            value=3000000.0,
            step=100000.0,
            key="v2_returns_annual_cash",
        )

    with col3:
        years = st.number_input(
            "Investment Period (Years)",
            min_value=1,
            value=5,
            step=1,
            key="v2_returns_years",
        )

    try:
        result = calculate_investor_returns(
            investment_amount=investment,
            annual_cash_return=annual_cash_return,
            years=years,
        )

    except TypeError:
        try:
            result = calculate_investor_returns(
                investment,
                annual_cash_return,
                years,
            )
        except Exception as exc:
            st.error(f"Investor Returns engine adapter error: {exc}")
            return

    except Exception as exc:
        st.error(f"Investor Returns engine error: {exc}")
        return

    total_return = _value(
        result,
        "total_return",
        "cumulative_return",
        "total_cash_return",
        default=annual_cash_return * years,
    )

    roi = _value(
        result,
        "roi",
        "return_on_investment",
        default=(
            total_return / investment
            if investment
            else 0
        ),
    )

    payback = _value(
        result,
        "payback_period",
        "payback_years",
        "simple_payback",
        default=(
            investment / annual_cash_return
            if annual_cash_return
            else 0
        ),
    )

    cols = st.columns(4)

    metrics = [
        ("Initial Investment", investment, "₦{:,.0f}"),
        ("Total Cash Return", total_return, "₦{:,.0f}"),
        ("ROI", roi, "{:.1%}"),
        ("Payback Period", payback, "{:.2f} yrs"),
    ]

    for col, (label, value, fmt) in zip(cols, metrics):
        with col:
            try:
                st.metric(label, fmt.format(float(value)))
            except (TypeError, ValueError):
                st.metric(label, str(value))

    with st.expander("Investor Returns Engine Output"):
        if isinstance(result, dict):
            st.json(result)
        else:
            st.write(vars(result))
