import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from pathlib import Path
from datetime import datetime
from typing import Optional


def get_file_metadata(file_path: Path) -> dict:
    """
    Extract metadata from a single file.
    """

    stat = file_path.stat()

    return {
        "path": str(file_path.resolve()),
        "name": file_path.name,
        "extension": file_path.suffix.lower(),

        "size": stat.st_size,

        "created_at": _timestamp_to_datetime(
            stat.st_ctime
        ),

        "modified_at": _timestamp_to_datetime(
            stat.st_mtime
        ),

        "accessed_at": _timestamp_to_datetime(
            stat.st_atime
        ),
    }


def _timestamp_to_datetime(
    timestamp: float,
) -> Optional[datetime]:

    try:
        return datetime.fromtimestamp(timestamp)
    except (OSError, ValueError):
        return None