import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import json

from pathlib import Path

import streamlit as st


st.title(
    "📊 Executive Dashboard"
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

if not analysis:

    st.error(
        "Run export_analysis.py first."
    )

    st.stop()

stats = analysis["statistics"]
health_score = 82
duplicates = len(
    analysis["duplicates"]
)

unused = len(
    analysis["unused_files"]
)

large = len(
    analysis["large_files"]
)

col1, col2, col3, col4, col5= st.columns(5)

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
        "Duplicates",
        duplicates
    )

with col4:

    st.metric(
        "Unused Files",
        unused
    )
with col5:
    st.metric(
    "Health Score",
    f"{health_score}/100"
)
st.divider()

st.subheader(
    "Storage Categories"
)

st.json(
    stats["categories"]
)