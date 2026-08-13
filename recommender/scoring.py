import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from datetime import datetime

from models.file_model import FileRecord


class FileScorer:

    def calculate_score(
        self,
        file: FileRecord
    ) -> float:

        score = 0

        now = datetime.now()

        # Large files matter more
        size_mb = file.size / (1024 * 1024)

        if size_mb > 1000:
            score += 40

        elif size_mb > 500:
            score += 25

        elif size_mb > 100:
            score += 10

        # Old files

        if file.accessed_at:

            age = (
                now - file.accessed_at
            ).days

            if age > 365:
                score += 30

            elif age > 180:
                score += 20

            elif age > 90:
                score += 10

        # Duplicate files

        if file.is_duplicate:
            score += 35

        return min(score, 100)