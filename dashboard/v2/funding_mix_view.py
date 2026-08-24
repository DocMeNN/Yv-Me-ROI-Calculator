import streamlit as st

from calculator.v2.funding_mix import FundingSource, evaluate_funding_mix


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


def render_funding_mix():
    st.markdown(
        '<div class="v2-section">Funding Mix</div>',
        unsafe_allow_html=True,
    )

    st.caption(
        "Evaluate the proposed capital structure across investor, partner, "
        "grant and other funding sources."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        total_investment = st.number_input(
            "Total Investment Requirement (NGN)",
            min_value=0.0,
            value=10000000.0,
            step=500000.0,
            key="v2_funding_total",
        )

    with col2:
        investor_pct = st.number_input(
            "Investor Share (%)",
            min_value=0.0,
            max_value=100.0,
            value=40.0,
            step=5.0,
            key="v2_investor_pct",
        )

    with col3:
        partner_pct = st.number_input(
            "Partner Share (%)",
            min_value=0.0,
            max_value=100.0,
            value=30.0,
            step=5.0,
            key="v2_partner_pct",
        )

    grant_pct = max(0.0, 100.0 - investor_pct - partner_pct)

    st.info(
        f"Calculated Grant / Other Share: **{grant_pct:.1f}%**"
    )

    try:
        sources = [
            FundingSource(
                name="Investor",
                amount=total_investment * investor_pct / 100,
            ),
            FundingSource(
                name="Partner",
                amount=total_investment * partner_pct / 100,
            ),
            FundingSource(
                name="Grant / Other",
                amount=total_investment * grant_pct / 100,
            ),
        ]

        result = evaluate_funding_mix(
            sources=sources,
            total_required=total_investment,
        )

    except TypeError:
        try:
            result = evaluate_funding_mix(
                sources,
                total_investment,
            )
        except Exception as exc:
            st.error(f"Funding Mix engine adapter error: {exc}")
            return

    except Exception as exc:
        st.error(f"Funding Mix engine error: {exc}")
        return

    total_funded = _value(
        result,
        "total_funding",
        "total_funded",
        "funded_amount",
        default=sum(source.amount for source in sources),
    )

    funding_gap = _value(
        result,
        "funding_gap",
        "gap",
        "shortfall",
        default=max(0, total_investment - total_funded),
    )

    coverage = _value(
        result,
        "coverage_ratio",
        "funding_coverage",
        "coverage",
        default=(
            total_funded / total_investment
            if total_investment
            else 0
        ),
    )

    cols = st.columns(3)

    with cols[0]:
        st.metric(
            "Total Funded",
            f"₦{float(total_funded):,.0f}",
        )

    with cols[1]:
        st.metric(
            "Funding Gap",
            f"₦{float(funding_gap):,.0f}",
        )

    with cols[2]:
        st.metric(
            "Funding Coverage",
            f"{float(coverage):.1%}",
        )

    st.markdown(
        '<div class="v2-section">Funding Sources</div>',
        unsafe_allow_html=True,
    )

    table = [
        {
            "Source": source.name,
            "Amount (NGN)": source.amount,
            "Share": (
                source.amount / total_investment
                if total_investment
                else 0
            ),
        }
        for source in sources
    ]

    st.dataframe(
        table,
        column_config={
            "Amount (NGN)": st.column_config.NumberColumn(
                format="₦%,.0f"
            ),
            "Share": st.column_config.NumberColumn(
                format="%.1f%%"
            ),
        },
        width="stretch",
        hide_index=True,
    )

    with st.expander("Funding Mix Engine Output"):
        if isinstance(result, dict):
            st.json(result)
        else:
            st.write(vars(result))
