from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dashboard.exports import generate_xlsx, generate_pptx


def export_panel():

    try:
        import streamlit as st
    except ImportError:
        return

    st.subheader("Export & Presentation")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "Generate Excel Workbook",
            use_container_width=True
        ):
            if generate_xlsx():
                file_path = (
                    ROOT /
                    "exports" /
                    "xlsx" /
                    "Yv-Me_ROI_Calculator.xlsx"
                )

                with open(file_path, "rb") as f:
                    st.download_button(
                        "Download Excel",
                        f,
                        file_name="Yv-Me_ROI_Calculator.xlsx",
                        mime=(
                            "application/vnd.openxmlformats-"
                            "officedocument.spreadsheetml.sheet"
                        ),
                        use_container_width=True
                    )

    with col2:
        if st.button(
            "Generate Investor / Donor PPT",
            use_container_width=True
        ):
            if generate_pptx():
                file_path = (
                    ROOT /
                    "exports" /
                    "pptx" /
                    "Yv-Me_Investor_Donor_Grant_Presentation.pptx"
                )

                with open(file_path, "rb") as f:
                    st.download_button(
                        "Download PowerPoint",
                        f,
                        file_name=(
                            "Yv-Me_Investor_Donor_Grant_Presentation.pptx"
                        ),
                        mime=(
                            "application/vnd.openxmlformats-"
                            "officedocument.presentationml.presentation"
                        ),
                        use_container_width=True
                    )
