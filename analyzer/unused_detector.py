import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from datetime import datetime

from models.file_model import FileRecord


class UnusedFileDetector:

    def find_unused_files(
        self,
        files: list[FileRecord],
        days_threshold: int = 180
    ):

        now = datetime.now()

        unused_files = []

        for file in files:

            if not file.accessed_at:
                continue

            age = (
                now - file.accessed_at
            ).days

            if age >= days_threshold:

                unused_files.append(file)

        return unused_files