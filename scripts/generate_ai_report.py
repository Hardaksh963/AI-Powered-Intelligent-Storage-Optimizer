import os
import sys
from pathlib import Path

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from llm.nvidia_client import NvidiaLLM
from predictor.history_manager import HistoryManager
from predictor.storage_forecaster import StorageForecaster


def bytes_to_gb(size):

    return round(
        size / (1024 ** 3),
        2
    )


def build_report_data():

    history_manager = HistoryManager()

    history = history_manager.load_history()

    if not history:
        return None

    latest = history[-1]

    forecaster = StorageForecaster()

    forecast = forecaster.forecast(
        history
    )

    days_until_full = (
        forecaster.estimate_disk_full(
            history,
            disk_capacity=500 * 1024**3
        )
    )

    return {
        "current_storage":
            bytes_to_gb(
                latest.total_storage
            ),

        "total_files":
            latest.total_files,

        "daily_growth":
            bytes_to_gb(
                forecast["daily_growth"]
            ),

        "30_days":
            bytes_to_gb(
                forecast["30_days"]
            ),

        "60_days":
            bytes_to_gb(
                forecast["60_days"]
            ),

        "90_days":
            bytes_to_gb(
                forecast["90_days"]
            ),

        "days_until_full":
            days_until_full
    }


def generate_report():

    data = build_report_data()

    if not data:

        print(
            "No history data found."
        )

        return

    prompt = f"""
You are an expert storage optimization consultant.

Analyze the following storage report.

Current Storage:
{data['current_storage']} GB

Total Files:
{data['total_files']}

Daily Growth:
{data['daily_growth']} GB/day

30 Day Forecast:
{data['30_days']} GB

60 Day Forecast:
{data['60_days']} GB

90 Day Forecast:
{data['90_days']} GB

Disk Full Estimate:
{data['days_until_full']} days

Generate:

1. Executive Summary
2. Storage Health Score (0-100)
3. Growth Analysis
4. Risks
5. Cleanup Recommendations
6. Archiving Recommendations
7. Action Plan

Be specific and practical.
"""

    llm = NvidiaLLM()

    report = llm.generate(prompt)

    print("\n")
    print("=" * 60)
    print("AI STORAGE REPORT")
    print("=" * 60)
    print("\n")

    print(report)

    save_report(report)


def save_report(report):

    reports_dir = Path(
        "data/reports"
    )

    reports_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    report_file = (
        reports_dir /
        "latest_report.md"
    )

    with open(
        report_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(report)

    print(
        f"\nReport saved to:"
    )

    print(
        report_file.resolve()
    )


if __name__ == "__main__":
    generate_report()