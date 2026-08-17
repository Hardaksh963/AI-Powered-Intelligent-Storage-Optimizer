import json
from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Storage Optimizer",
    page_icon="💾",
    layout="wide"
)


@st.cache_data
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

st.title("💾 AI Storage Optimizer")

if not analysis:

    st.error(
        "Run export_analysis.py first."
    )

    st.stop()

stats = analysis["statistics"]

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Files",
        stats["total_files"]
    )

with col2:

    st.metric(
        "Storage (MB)",
        round(
            stats["total_size"] /
            (1024 * 1024),
            2
        )
    )

with col3:

    st.metric(
        "Duplicate Groups",
        len(
            analysis["duplicates"]
        )
    )

with col4:

    st.metric(
        "Unused Files",
        len(
            analysis["unused_files"]
        )
    )

st.divider()

st.subheader(
    "Category Breakdown"
)

st.json(
    stats["categories"]
)   