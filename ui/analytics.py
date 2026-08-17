import json
from pathlib import Path

import pandas as pd
import streamlit as st


st.title(
    "📊 Storage Analytics"
)


@st.cache_data
def load_analysis():

    with open(
        "data/latest_analysis.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


analysis = load_analysis()

st.subheader(
    "Duplicate Files"
)

duplicates = []

for group in analysis["duplicates"]:

    for file in group:

        duplicates.append(file)

if duplicates:

    st.dataframe(
        pd.DataFrame(
            duplicates
        ),
        use_container_width=True
    )

else:

    st.info(
        "No duplicates found."
    )

st.divider()

st.subheader(
    "Unused Files"
)

unused = analysis["unused_files"]

if unused:

    st.dataframe(
        pd.DataFrame(unused),
        use_container_width=True
    )

else:

    st.info(
        "No unused files found."
    )

st.divider()

st.subheader(
    "Large Files"
)

large_files = analysis["large_files"]

if large_files:

    st.dataframe(
        pd.DataFrame(
            large_files
        ),
        use_container_width=True
    )

else:

    st.info(
        "No large files found."
    )