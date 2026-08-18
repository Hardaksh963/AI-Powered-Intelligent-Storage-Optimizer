import json
from pathlib import Path


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


def load_report():

    file = Path(
        "data/reports/latest_report.md"
    )

    if not file.exists():
        return None

    return file.read_text(
        encoding="utf-8"
    )