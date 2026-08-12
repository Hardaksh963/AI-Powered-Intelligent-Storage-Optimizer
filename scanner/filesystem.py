from pathlib import Path
from typing import List

from models.file_model import FileRecord
from scanner.metadata import get_file_metadata
from scanner.hashing import calculate_sha256
from scanner.file_classifier import classify_file


class FileSystemScanner:

    def __init__(
        self,
        calculate_hash: bool = True,
    ):
        self.calculate_hash = calculate_hash

    def scan(
        self,
        root_path: str,
    ) -> List[FileRecord]:

        root = Path(root_path)

        if not root.exists():
            raise FileNotFoundError(
                f"Directory does not exist: {root_path}"
            )

        if not root.is_dir():
            raise NotADirectoryError(
                f"Path is not a directory: {root_path}"
            )

        records = []

        for file_path in self._walk_directory(root):

            try:

                metadata = get_file_metadata(
                    file_path
                )

                category = classify_file(
                    file_path
                )

                file_hash = None

                if self.calculate_hash:

                    try:
                        file_hash = calculate_sha256(
                            file_path
                        )

                    except (PermissionError, OSError) as error:

                        print(
                            f"Could not hash "
                            f"{file_path}: {error}"
                        )

                record = FileRecord(
                    path=metadata["path"],
                    name=metadata["name"],
                    extension=metadata["extension"],
                    size=metadata["size"],
                    created_at=metadata["created_at"],
                    modified_at=metadata["modified_at"],
                    accessed_at=metadata["accessed_at"],
                    category=category,
                    file_hash=file_hash,
                )

                records.append(record)

            except (PermissionError, OSError) as error:

                print(
                    f"Could not process "
                    f"{file_path}: {error}"
                )

        return records

    def _walk_directory(
        self,
        root: Path,
    ):

        for path in root.rglob("*"):

            if path.is_file():
                yield path