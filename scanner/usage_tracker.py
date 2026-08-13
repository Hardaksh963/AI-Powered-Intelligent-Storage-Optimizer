import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from datetime import datetime
from models.file_model import FileRecord


def calculate_file_age(
    file_record: FileRecord,
) -> int:

    if not file_record.modified_at:
        return 0

    now = datetime.now()

    delta = now - file_record.modified_at

    return max(0, delta.days)


def calculate_days_since_access(
    file_record: FileRecord,
) -> int:

    if not file_record.accessed_at:
        return 0

    now = datetime.now()

    delta = now - file_record.accessed_at

    return max(0, delta.days)