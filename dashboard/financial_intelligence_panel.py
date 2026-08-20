from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from calculator.financial.intelligence import calculate_financial_intelligence


def financial_intelligence_panel(
    beneficiaries,
    programme_cost,
    monthly_subscription,
    programme_duration_months,
    investment_amount,
    revenue_share,
):
    import streamlit as st

    st.markdown("---")
    st.header("7. Financial Intelligence")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        collection_rate = st.number_input(
            "Collection Rate (%)",
            min_value=0.0,
            max_value=100.0,
            value=100.0,
            step=1.0,
            key="fi_collection_rate",
        )

    with col2:
        free_beneficiaries = st.number_input(
            "Free Beneficiaries",
            min_value=0,
            max_value=int(beneficiaries),
            value=0,
            step=1,
            key="fi_free_beneficiaries",
        )

    with col3:
        grant_amount = st.number_input(
            "Grant / Donor Funding (NGN)",
            min_value=0.0,
            value=0.0,
            step=1000000.0,
            key="fi_grant_amount",
        )

    with col4:
        variable_cost = st.number_input(
            "Variable Cost / Beneficiary / Month (NGN)",
            min_value=0.0,
            value=0.0,
            step=1000.0,
            key="fi_variable_cost",
        )

    intelligence = calculate_financial_intelligence(
        beneficiaries=int(beneficiaries),
        programme_cost=float(programme_cost),
        monthly_subscription=float(monthly_subscription),
        collection_rate=collection_rate / 100,
        free_beneficiaries=int(free_beneficiaries),
        grant_amount=float(grant_amount),
        investment_amount=float(investment_amount),
        investor_revenue=float(
            max(
                0,
                beneficiaries
                * monthly_subscription
                * (collection_rate / 100)
                * 12
                * (revenue_share / 100),
            )
        ),
        monthly_investor_cashflow=float(
            max(
                0,
                beneficiaries
                * monthly_subscription
                * (collection_rate / 100)
                * (revenue_share / 100),
            )
        ),
        revenue_share=revenue_share / 100,
        monthly_fixed_cost=float(
            programme_cost / programme_duration_months
        ),
        monthly_variable_cost_per_beneficiary=float(variable_cost),
        programme_duration_months=int(programme_duration_months),
    )

    revenue = intelligence["revenue"]
    grant = intelligence["grant"]
    sustainability = intelligence["sustainability"]
    investor = intelligence["investor"]

    st.subheader("Revenue Intelligence")

    r1, r2, r3, r4 = st.columns(4)

    r1.metric(
        "Paying Beneficiaries",
        f"{revenue['paying_beneficiaries']:,}",
    )

    r2.metric(
        "Monthly Revenue",
        f"?{revenue['monthly_revenue']:,.0f}",
    )

    r3.metric(
        "Annual Revenue",
        f"?{revenue['annual_revenue']:,.0f}",
    )

    r4.metric(
        "Collection Rate",
        f"{revenue['collection_rate']:.1%}",
    )

    st.subheader("Grant / Donor Intelligence")

    g1, g2, g3, g4 = st.columns(4)

    g1.metric(
        "Grant Amount",
        f"?{grant['grant_amount']:,.0f}",
    )

    g2.metric(
        "Funding Gap",
        f"?{grant['funding_gap']:,.0f}",
    )

    g3.metric(
        "Funding Coverage",
        f"{grant['funding_coverage']:.1%}",
    )

    g4.metric(
        "Cost / Beneficiary",
        f"?{grant['cost_per_beneficiary']:,.0f}",
    )

    st.subheader("Sustainability Intelligence")

    s1, s2, s3, s4 = st.columns(4)

    s1.metric(
        "Contribution / Beneficiary",
        f"?{sustainability['contribution_per_beneficiary']:,.0f}",
    )

    s2.metric(
        "Break-even Beneficiaries",
        (
            "N/A"
            if sustainability["break_even_beneficiaries"] is None
            else f"{sustainability['break_even_beneficiaries']:,}"
        ),
    )

    s3.metric(
        "Break-even Status",
        "REACHED" if sustainability["break_even_reached"] else "NOT REACHED",
    )

    s4.metric(
        "Required Subscription",
        (
            "N/A"
            if sustainability["required_subscription"] is None
            else f"?{sustainability['required_subscription']:,.0f}"
        ),
    )

    st.subheader("Investor / Partner Intelligence")

    if investor is None:
        st.info("Enter an investment amount above to activate investor metrics.")
    else:
        i1, i2, i3, i4 = st.columns(4)

        i1.metric(
            "Net Return",
            f"?{investor['net_return']:,.0f}",
        )

        i2.metric(
            "Investor ROI",
            f"{investor['roi']:.1%}",
        )

        i3.metric(
            "Revenue Share",
            f"{investor['revenue_share']:.1%}",
        )

        i4.metric(
            "Payback",
            (
                "N/A"
                if investor["payback_months"] is None
                else f"{investor['payback_months']:.1f} months"
            ),
        )
