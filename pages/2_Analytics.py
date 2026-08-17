import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import json

import pandas as pd
import streamlit as st


st.title(
    "📁 Analytics"
)

with open(
    "data/latest_analysis.json",
    "r",
    encoding="utf-8"
) as f:

    analysis = json.load(f)

tabs = st.tabs(
    [
        "Duplicates",
        "Unused",
        "Large Files",
        "Recommendations"
    ]
)

with tabs[0]:

    rows = []

    for group in analysis["duplicates"]:

        for file in group:

            rows.append(file)

    if rows:

        st.dataframe(
            pd.DataFrame(rows),
            use_container_width=True
        )

with tabs[1]:

    st.dataframe(
        pd.DataFrame(
            analysis["unused_files"]
        ),
        use_container_width=True
    )

with tabs[2]:

    st.dataframe(
        pd.DataFrame(
            analysis["large_files"]
        ),
        use_container_width=True
    )

with tabs[3]:

    st.dataframe(
        pd.DataFrame(
            analysis["recommendations"]
        ),
        use_container_width=True
    )