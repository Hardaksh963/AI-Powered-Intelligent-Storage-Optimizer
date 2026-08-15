import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from models.file_model import FileRecord


class LargeFileDetector:

    def find_large_files(
        self,
        files: list[FileRecord],
        min_size_mb: int = 100
    ):

        threshold = (
            min_size_mb
            * 1024
            * 1024
        )

        return [
            file
            for file in files
            if file.size >= threshold
        ]