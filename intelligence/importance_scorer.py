import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from datetime import datetime

from models.file_model import FileRecord


class ImportanceScorer:

    IMPORTANT_CATEGORIES = {
        "documents",
        "images",
    }

    def calculate(
        self,
        file: FileRecord
    ) -> float:

        score = 50

        if file.category in self.IMPORTANT_CATEGORIES:
            score += 20

        if file.is_duplicate:
            score -= 25

        if file.accessed_at:

            age = (
                datetime.now()
                - file.accessed_at
            ).days

            if age < 30:
                score += 20

            elif age > 365:
                score -= 15

        return max(
            0,
            min(score, 100)
        )