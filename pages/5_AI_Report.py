import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from pathlib import Path
import subprocess
import streamlit as st


st.title(
    "📄 AI Report"
)
if st.button(
    "📄 Generate Report"
):

    with st.spinner(
        "Generating..."
    ):

        subprocess.run(
            [
                "python",
                "scripts/generate_ai_report.py"
            ]
        )

    st.success(
        "Report Generated"
    )

report_file = Path(
    "data/reports/latest_report.md"
)

if not report_file.exists():

    st.warning(
        "Generate report first."
    )

    st.stop()

with open(
    report_file,
    "r",
    encoding="utf-8"
) as f:

    report = f.read()

st.markdown(
    report
)