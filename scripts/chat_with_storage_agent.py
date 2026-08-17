import os
import sys
from pathlib import Path
import json

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from agent.storage_agent import StorageAgent
from predictor.history_manager import HistoryManager
from predictor.storage_forecaster import StorageForecaster


def load_forecast():

    history_manager = HistoryManager()

    history = history_manager.load_history()

    if not history:
        return {
            "error": "No storage history found."
        }

    forecaster = StorageForecaster()

    return forecaster.forecast(history)


def build_storage_summary():

    history_manager = HistoryManager()

    history = history_manager.load_history()

    if not history:
        return {
            "total_storage": 0,
            "total_files": 0
        }

    latest = history[-1]

    return {
        "total_storage_gb": round(
            latest.total_storage /
            (1024 ** 3),
            2
        ),
        "total_files":
            latest.total_files
    }

def load_analysis():

    analysis_file = Path(
        "data/latest_analysis.json"
    )

    if not analysis_file.exists():

        return {}

    with open(
        analysis_file,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)

def main():

    print("=" * 60)
    print("AI STORAGE ASSISTANT")
    print("=" * 60)

    print(
        "\nType 'exit' to quit.\n"
    )

    agent = StorageAgent()

    storage_summary = (
        build_storage_summary()
    )

    forecast = (
        load_forecast()
    )
    analysis = load_analysis()
    while True:

        query = input(
            "\nYou: "
        ).strip()

        if query.lower() in [
            "exit",
            "quit"
        ]:
            print(
                "\nGoodbye!"
            )
            break

        try:

            response = agent.answer_query(
                query=query,
                storage_summary=storage_summary,
                forecast=forecast,
                analysis=analysis
            )

            print(
                "\nAssistant:\n"
            )

            print(response)

        except Exception as e:

            print(
                f"\nError: {e}"
            )


if __name__ == "__main__":
    main()