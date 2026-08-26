from __future__ import annotations

import streamlit as st

from calculator.v2.scenarios import *


def render_scenarios_view() -> None:
    st.markdown("### Scenario Analysis")
    st.caption(
        "Compare the configured V2 conservative, base, growth and scale cases."
    )

    try:
        scenario_names = [
            "conservative",
            "base",
            "growth",
            "scale",
        ]

        st.dataframe(
            [{"Scenario": name.title()} for name in scenario_names],
            width="stretch",
            hide_index=True,
        )
    except Exception as exc:
        st.error(f"Scenario engine error: {exc}")
