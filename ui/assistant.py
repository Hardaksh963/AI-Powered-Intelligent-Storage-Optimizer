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

from agent.storage_agent import (
    StorageAgent
)

from predictor.history_manager import (
    HistoryManager
)

from predictor.storage_forecaster import (
    StorageForecaster
)


st.title(
    "🤖 AI Storage Assistant"
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

history = (
    HistoryManager()
    .load_history()
)

forecast = (
    StorageForecaster()
    .forecast(history)
)

storage_summary = (
    analysis["statistics"]
)

agent = StorageAgent()

question = st.text_input(
    "Ask a question"
)

if st.button("Ask"):

    with st.spinner(
        "Thinking..."
    ):

        response = (
            agent.answer_query(
                query=question,
                storage_summary=storage_summary,
                forecast=forecast,
                analysis=analysis
            )
        )

        st.markdown(response)