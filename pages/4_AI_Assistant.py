import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import json

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
    "🤖 AI Assistant"
)

with open(
    "data/latest_analysis.json",
    "r",
    encoding="utf-8"
) as f:

    analysis = json.load(f)

history = (
    HistoryManager()
    .load_history()
)

forecast = (
    StorageForecaster()
    .forecast(history)
)

agent = StorageAgent()

query = st.text_area(
    "Ask a question"
)

if st.button(
    "Analyze"
):

    with st.spinner(
        "Thinking..."
    ):

        response = (
            agent.answer_query(
                query=query,
                storage_summary=analysis[
                    "statistics"
                ],
                forecast=forecast,
                analysis=analysis
            )
        )

        st.markdown(
            response
        )