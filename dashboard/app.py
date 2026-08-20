import streamlit as st
import pandas as pd
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calculator.analytics import calculate
from dashboard.financial_intelligence_panel import financial_intelligence_panel

st.set_page_config(
    page_title="Yv-Me ROI Calculator",
    page_icon="📊",
    layout="wide"
)

st.title("Yv-Me ROI Calculator")
st.caption(
    "EasePal Care — Yobe State Programme Economics & Partnership ROI"
)

st.markdown("---")

# ============================================================
# ASSUMPTIONS
# ============================================================

st.header("1. Adjustable Programme Assumptions")

col1, col2, col3, col4 = st.columns(4)

with col1:
    chews = st.number_input(
        "CHEWs",
        min_value=1,
        value=100,
        step=1
    )

with col2:
    beneficiaries_per_chew = st.number_input(
        "Beneficiaries per CHEW",
        min_value=1,
        value=10,
        step=1
    )

with col3:
    programme_months = st.number_input(
        "Programme Duration (Months)",
        min_value=1,
        value=12,
        step=1
    )

with col4:
    total_budget = st.number_input(
        "Programme Budget (NGN)",
        min_value=0.0,
        value=426906031.0,
        step=1000000.0
    )

col5, col6, col7 = st.columns(3)

with col5:
    subscription = st.number_input(
        "Subscription / Beneficiary / Month (NGN)",
        min_value=0.0,
        value=15000.0,
        step=1000.0
    )

with col6:
    investment = st.number_input(
        "Investor / Partner Investment (NGN)",
        min_value=0.0,
        value=426906031.0,
        step=1000000.0
    )

with col7:
    revenue_share = st.number_input(
        "Partner Revenue Share (%)",
        min_value=0.0,
        max_value=100.0,
        value=10.0,
        step=1.0
    )

# ============================================================
# CALCULATE
# ============================================================

result = calculate(
    chews=chews,
    beneficiaries_per_chew=beneficiaries_per_chew,
    programme_months=programme_months,
    total_budget=total_budget,
    subscription_per_beneficiary=subscription,
    investment_amount=investment,
    revenue_share=revenue_share,
)

# ============================================================
# VALIDATION
# ============================================================

expected_beneficiaries = chews * beneficiaries_per_chew

st.success(
    f"Care Delivery Model: 1 CHEW : {beneficiaries_per_chew} "
    f"Beneficiaries | Total Beneficiaries: "
    f"{expected_beneficiaries:,}"
)

# ============================================================
# KPI DASHBOARD
# ============================================================

st.markdown("---")
st.header("2. Financial Dashboard")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Beneficiaries",
    f"{result['beneficiaries']:,}"
)

c2.metric(
    "Programme Budget",
    f"₦{result['total_budget']:,.0f}"
)

c3.metric(
    "Annual Revenue",
    f"₦{result['annual_gross_revenue']:,.0f}"
)

c4.metric(
    "ROI",
    f"{result['roi']:.2%}"
)

c5, c6, c7, c8 = st.columns(4)

c5.metric(
    "Monthly Cost",
    f"₦{result['monthly_operating_cost']:,.0f}"
)

c6.metric(
    "Cost / CHEW",
    f"₦{result['cost_per_chew']:,.0f}"
)

c7.metric(
    "Cost / Beneficiary",
    f"₦{result['cost_per_beneficiary']:,.0f}"
)

if result["break_even_months"] == float("inf"):
    break_even_display = "Not reached"
else:
    break_even_display = f"{result['break_even_months']:.1f} months"

c8.metric(
    "Break-even",
    break_even_display
)

# ============================================================
# REVENUE / COST ANALYSIS
# ============================================================

st.markdown("---")
st.header("3. Revenue & Cost Analysis")

financial_data = pd.DataFrame({
    "Metric": [
        "Programme Budget",
        "Annual Operating Cost",
        "Annual Gross Revenue",
        "Partner Revenue Share",
        "Annual Net Revenue",
        "Annual Contribution",
    ],
    "Amount (NGN)": [
        result["total_budget"],
        result["annual_operating_cost"],
        result["annual_gross_revenue"],
        result["partner_revenue_share"],
        result["annual_net_revenue"],
        result["annual_contribution"],
    ]
})

st.dataframe(
    financial_data.style.format(
        {"Amount (NGN)": "₦{:,.2f}"}
    ),
    use_container_width=True,
    hide_index=True
)

# ============================================================
# SCALING ANALYSIS
# ============================================================

st.markdown("---")
st.header("4. Scaling Analysis")

scale_levels = [10, 50, 100, 200, 500, 1000, 2000, 5000]

scale_rows = []

for scale_chews in scale_levels:

    scale_result = calculate(
        chews=scale_chews,
        beneficiaries_per_chew=beneficiaries_per_chew,
        programme_months=programme_months,
        total_budget=total_budget,
        subscription_per_beneficiary=subscription,
        investment_amount=investment,
        revenue_share=revenue_share,
    )

    scale_rows.append({
        "CHEWs": scale_chews,
        "Beneficiaries":
            scale_result["beneficiaries"],
        "Monthly Revenue":
            scale_result["monthly_gross_revenue"],
        "Annual Revenue":
            scale_result["annual_gross_revenue"],
        "Annual Contribution":
            scale_result["annual_contribution"],
        "ROI":
            scale_result["roi"],
    })

scale_df = pd.DataFrame(scale_rows)

st.dataframe(
    scale_df.style.format({
        "Monthly Revenue": "₦{:,.0f}",
        "Annual Revenue": "₦{:,.0f}",
        "Annual Contribution": "₦{:,.0f}",
        "ROI": "{:.2%}",
    }),
    use_container_width=True,
    hide_index=True
)

# ============================================================
# CHARTS
# ============================================================

st.subheader("Annual Revenue by Scale")

chart_revenue = scale_df.set_index("CHEWs")[
    ["Annual Revenue"]
]

st.bar_chart(chart_revenue)

st.subheader("Annual Contribution by Scale")

chart_contribution = scale_df.set_index("CHEWs")[
    ["Annual Contribution"]
]

st.bar_chart(chart_contribution)

# ============================================================
# INVESTOR VIEW
# ============================================================

st.markdown("---")
st.header("5. Investor / Partner View")

investor_col1, investor_col2 = st.columns(2)

with investor_col1:

    st.metric(
        "Partner Investment",
        f"₦{result['investment_amount']:,.0f}"
    )

    st.metric(
        "Partner Revenue Share",
        f"{revenue_share:.1f}%"
    )

with investor_col2:

    st.metric(
        "Annual Net Revenue",
        f"₦{result['annual_net_revenue']:,.0f}"
    )

    st.metric(
        "Annual Contribution",
        f"₦{result['annual_contribution']:,.0f}"
    )

# ============================================================
# ============================================================
# EXPORT & PRESENTATION
# ============================================================

st.header("6. Export & Presentation")

st.markdown(
    "Generate presentation-ready financial outputs from the "
    "current adjustable assumptions and ROI model."
)

from dashboard.export_panel import export_panel

export_panel()


# ============================================================
# FINANCIAL INTELLIGENCE
# ============================================================

financial_intelligence_panel(
    beneficiaries=result["beneficiaries"],
    programme_cost=result["total_budget"],
    monthly_subscription=subscription,
    programme_duration_months=programme_months,
    investment_amount=investment,
    revenue_share=revenue_share,
)
