import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from collections import defaultdict

from models.file_model import FileRecord


class StorageStatistics:

    def generate(
        self,
        files: list[FileRecord]
    ):

        stats = defaultdict(int)

        total_size = 0

        for file in files:

            stats[file.category] += file.size
            total_size += file.size

        return {
            "total_files": len(files),
            "total_size": total_size,
            "categories": dict(stats),
        }