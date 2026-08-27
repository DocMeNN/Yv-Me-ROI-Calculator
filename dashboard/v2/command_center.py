from __future__ import annotations

import streamlit as st

from .cash_flow_view import render_cash_flow_view
from .funding_mix_view import render_funding_mix
from .investment_case_view import render_investment_case
from .kpis_view import render_kpis_view
from .navigation import dashboard_modules
from .partnership_view import render_partnership
from .returns_view import render_returns
from .scenarios_view import render_scenarios_view
from .sensitivity_view import render_sensitivity_view
from .npv_irr_view import render_npv_irr
from .shell import render_header


def render_navigation():
    modules = list(dashboard_modules().keys())

    if "v2_module" not in st.session_state:
        st.session_state.v2_module = modules[0]

    selected = st.radio(
        "V2 Intelligence Modules",
        modules,
        horizontal=True,
        key="v2_module_selector",
        label_visibility="collapsed",
    )

    st.session_state.v2_module = selected
    return selected


def render_status():
    st.markdown(
        '<div class="v2-section">Executive Status</div>',
        unsafe_allow_html=True,
    )

    cols = st.columns(4)

    cards = [
        ("Investment Case", "Connected"),
        ("Funding Mix", "Connected"),
        ("Partnership", "Connected"),
        ("Investor Returns", "Connected"),
    ]

    for col, (label, value) in zip(cols, cards):
        with col:
            st.markdown(
                f"""
                <div class="v2-card">
                    <div style="font-size:0.82rem;color:#64748b;">{label}</div>
                    <div style="font-size:1.35rem;font-weight:700;margin-top:0.3rem;">
                        {value}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def _default_periods():
    from calculator.v2.cash_flow import AnnualOperatingPeriod

    return [
        AnnualOperatingPeriod(
            year=year,
            revenue=0.0,
            operating_cost=0.0,
            investor_share=0.0,
        )
        for year in range(1, 6)
    ]


def render_dashboard():
    render_header()
    render_status()

    st.divider()

    module = render_navigation()

    st.divider()

    if module == "Investment Case":
        render_investment_case()

    elif module == "Scenarios":
        render_scenarios_view()

    elif module == "Partnership":
        render_partnership()

    elif module == "Cash Flow":
        periods = st.session_state.get("v2_periods") or _default_periods()
        investment_amount = st.session_state.get(
            "v2_investment_amount",
            10000000.0,
        )
        render_cash_flow_view(
            periods=periods,
            investment_amount=investment_amount,
        )

    elif module == "Sensitivity":
        render_sensitivity_view()

    elif module == "Funding Mix":
        render_funding_mix()

    elif module == "Assumptions":
        st.markdown(
            '<div class="v2-section">Assumptions</div>',
            unsafe_allow_html=True,
        )
        st.info(
            "Assumptions module is reserved for the V2 editable assumptions integration."
        )

    elif module == "Exports":
        st.markdown(
            '<div class="v2-section">Exports</div>',
            unsafe_allow_html=True,
        )
        st.info(
            "Exports module is reserved for the V2 export integration."
        )

    elif module == "Executive":
        render_status()

    elif module == "Investor Returns":
        render_returns()

    elif module == "NPV / IRR":
        render_npv_irr()

    elif module == "KPIs":
        render_kpis_view()

    else:
        st.markdown(
            f'<div class="v2-section">{module}</div>',
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    render_dashboard()
