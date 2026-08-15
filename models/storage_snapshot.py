from dataclasses import dataclass
from datetime import datetime


@dataclass
class StorageSnapshot:
    timestamp: datetime
    total_files: int
    total_storage: int

    def to_dict(self):
        return {
            "timestamp": self.timestamp.isoformat(),
            "total_files": self.total_files,
            "total_storage": self.total_storage
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            timestamp=datetime.fromisoformat(
                data["timestamp"]
            ),
            total_files=data["total_files"],
            total_storage=data["total_storage"]
        )