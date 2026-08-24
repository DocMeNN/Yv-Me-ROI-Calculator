import streamlit as st

from .funding_mix_view import render_funding_mix
from .investment_case_view import render_investment_case
from .navigation import dashboard_modules
from .npv_irr_view import render_npv_irr
from .partnership_view import render_partnership
from .returns_view import render_returns
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
        ("Returns", "Connected"),
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


def render_dashboard():
    render_header()
    render_status()

    st.divider()

    module = render_navigation()

    st.divider()

    if module == "Investment Case":
        render_investment_case()

    elif module == "Funding Mix":
        render_funding_mix()

    elif module == "Partnership Structure":
        render_partnership()

    elif module == "Investor Returns":
        render_returns()

    elif module == "NPV / IRR":
        render_npv_irr()

    else:
        st.markdown(
            f'<div class="v2-section">{module}</div>',
            unsafe_allow_html=True,
        )

        st.info(
            f"{module} module is connected to the V2 dashboard architecture. "
            "The validated financial engine will be surfaced here in the next integration step."
        )
