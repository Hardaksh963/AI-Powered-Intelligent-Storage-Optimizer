import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from models.file_model import FileRecord


class RiskAssessor:

    def assess(
        self,
        file: FileRecord,
        importance_score: float
    ):

        if importance_score > 80:
            return "HIGH"

        if importance_score > 50:
            return "MEDIUM"

        return "LOW"