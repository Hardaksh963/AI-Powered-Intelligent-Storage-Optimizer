import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import json
from pathlib import Path

from models.storage_snapshot import (
    StorageSnapshot
)


class HistoryManager:

    def __init__(self):

        self.history_file = (
            Path("data/history/storage_history.json")
        )

        self.history_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    def load_history(self):

        if not self.history_file.exists():
            return []

        with open(
            self.history_file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        return [
            StorageSnapshot.from_dict(item)
            for item in data
        ]

    def save_snapshot(
        self,
        snapshot: StorageSnapshot
    ):

        history = self.load_history()

        history.append(snapshot)

        with open(
            self.history_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                [
                    item.to_dict()
                    for item in history
                ],
                f,
                indent=2
            )