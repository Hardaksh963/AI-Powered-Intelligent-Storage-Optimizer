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