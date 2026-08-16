import json
from pathlib import Path


class UserMemory:

    def __init__(self):

        self.memory_file = Path(
            "data/preferences.json"
        )

        self.memory_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    def load(self):

        if not self.memory_file.exists():

            return {
                "never_delete": [],
                "preferred_action": "archive",
                "cleanup_threshold_days": 180
            }

        with open(
            self.memory_file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    def save(
        self,
        preferences
    ):

        with open(
            self.memory_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                preferences,
                f,
                indent=4
            )

    def update(
        self,
        key,
        value
    ):

        memory = self.load()

        memory[key] = value

        self.save(memory)

        return memory