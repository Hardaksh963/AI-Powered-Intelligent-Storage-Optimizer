import streamlit as st
import json
from pathlib import Path
from ui.folder_picker import (
    pick_folder
)
def load_analysis():

    file = Path(
        "data/latest_analysis.json"
    )

    if not file.exists():
        return None

    with open(
        file,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


analysis = load_analysis()
if "selected_folder" not in st.session_state:

    st.session_state.selected_folder = ""


st.title(
    "💾 AI Storage Optimizer"
)

col1, col2 = st.columns([1, 3])

with col1:

    if st.button(
        "📂 Browse Folder"
    ):

        folder = pick_folder()

        if folder:

            st.session_state.selected_folder = folder

with col2:

    st.text_input(
        "Selected Folder",
        value=st.session_state.selected_folder,
        disabled=True
    )


import subprocess


if st.button(
    "🔍 Scan Folder"
):

    folder = (
        st.session_state.selected_folder
    )

    if not folder:

        st.warning(
            "Select a folder first."
        )

    else:

        with st.spinner(
            "Scanning..."
        ):

            subprocess.run(
                [
                    "python",
                    "scripts/export_analysis.py",
                    folder
                ]
            )

        st.success(
            "Scan completed."
        )

if st.button(
    "📄 Generate AI Report"
):

    with st.spinner(
        "Generating report..."
    ):

        subprocess.run(
            [
                "python",
                "scripts/generate_ai_report.py"
            ]
        )

    st.success(
        "Report generated."
    )
analysis = load_analysis()
if analysis:

    stats = analysis["statistics"]

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Files",
            stats["total_files"]
        )

    with c2:

        st.metric(
            "Storage",
            f"{stats['total_size']/(1024**3):.2f} GB"
        )

    with c3:

        st.metric(
            "Duplicates",
            len(
                analysis["duplicates"]
            )
        )

    with c4:

        st.metric(
            "Unused",
            len(
                analysis["unused_files"]
            )
        )