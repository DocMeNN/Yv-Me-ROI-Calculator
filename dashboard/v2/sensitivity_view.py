from __future__ import annotations

import streamlit as st

from calculator.v2.sensitivity import SensitivityPoint, calculate_sensitivity


def render_sensitivity_view() -> None:
    st.markdown("### Sensitivity Analysis")

    st.caption(
        "Evaluate how changes in key assumptions affect the investment case."
    )

    st.info(
        "Sensitivity engine is available. Configure scenario inputs to generate the analysis."
    )
