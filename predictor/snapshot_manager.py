from datetime import datetime

from models.storage_snapshot import (
    StorageSnapshot
)


class SnapshotManager:

    def create_snapshot(
        self,
        files
    ):

        total_storage = sum(
            file.size
            for file in files
        )

        return StorageSnapshot(
            timestamp=datetime.now(),
            total_files=len(files),
            total_storage=total_storage
        )