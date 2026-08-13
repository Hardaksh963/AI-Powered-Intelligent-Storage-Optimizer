import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class FileRecord:
    path: str
    name: str
    extension: str

    size: int

    created_at: Optional[datetime]
    modified_at: Optional[datetime]
    accessed_at: Optional[datetime]

    category: str

    file_hash: Optional[str] = None

    is_duplicate: bool = False
    duplicate_group: Optional[str] = None

    def to_dict(self):
        return {
            "path": self.path,
            "name": self.name,
            "extension": self.extension,
            "size": self.size,
            "created_at": (
                self.created_at.isoformat()
                if self.created_at
                else None
            ),
            "modified_at": (
                self.modified_at.isoformat()
                if self.modified_at
                else None
            ),
            "accessed_at": (
                self.accessed_at.isoformat()
                if self.accessed_at
                else None
            ),
            "category": self.category,
            "file_hash": self.file_hash,
            "is_duplicate": self.is_duplicate,
            "duplicate_group": self.duplicate_group,
        }