import streamlit as st


def render_header():
    st.set_page_config(
        page_title="Yv-Me | Investor & Partnership Intelligence",
        page_icon="Y",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 1.2rem;
            padding-bottom: 1rem;
            max-width: 1500px;
        }

        .v2-title {
            font-size: 2rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            margin-bottom: 0.15rem;
        }

        .v2-subtitle {
            color: #64748b;
            font-size: 0.95rem;
            margin-bottom: 1rem;
        }

        .v2-card {
            padding: 1rem;
            border: 1px solid rgba(100,116,139,0.18);
            border-radius: 14px;
            background: rgba(255,255,255,0.72);
            min-height: 100px;
        }

        .v2-section {
            font-size: 1rem;
            font-weight: 650;
            margin: 0.8rem 0 0.5rem 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="v2-title">Yv-Me Investor & Partnership Intelligence</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="v2-subtitle">Financial decision support for investment, sustainability, partnership and scale.</div>',
        unsafe_allow_html=True,
    )
