import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st

from predictor.history_manager import (
    HistoryManager
)

from predictor.storage_forecaster import (
    StorageForecaster
)


st.title(
    "📈 Storage Forecast"
)

history_manager = (
    HistoryManager()
)

history = (
    history_manager.load_history()
)

if not history:

    st.warning(
        "No history found."
    )

    st.stop()

forecaster = (
    StorageForecaster()
)

forecast = (
    forecaster.forecast(
        history
    )
)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "30 Days",
        f"{forecast['30_days']/(1024**3):.2f} GB"
    )

with col2:

    st.metric(
        "60 Days",
        f"{forecast['60_days']/(1024**3):.2f} GB"
    )

with col3:

    st.metric(
        "90 Days",
        f"{forecast['90_days']/(1024**3):.2f} GB"
    )

storage_points = [
    item.total_storage /
    (1024 ** 3)
    for item in history
]

st.line_chart(
    storage_points
)