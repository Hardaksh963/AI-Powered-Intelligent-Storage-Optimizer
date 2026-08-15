import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from pathlib import Path

from models.file_model import FileRecord


class RiskAssessor:

    IMPORTANT_NAMES = {
        "resume",
        "cv",
        "thesis",
        "project",
        "report",
        "assignment",
    }

    def assess(
        self,
        file: FileRecord,
        importance_score: float
    ):

        name = file.name.lower()

        if any(
            keyword in name
            for keyword in self.IMPORTANT_NAMES
        ):
            return "HIGH"

        if file.category in {
            "documents",
            "images"
        }:
            if importance_score > 60:
                return "HIGH"

        if file.is_duplicate:
            return "LOW"

        if importance_score > 70:
            return "HIGH"

        if importance_score > 40:
            return "MEDIUM"

        return "LOW"