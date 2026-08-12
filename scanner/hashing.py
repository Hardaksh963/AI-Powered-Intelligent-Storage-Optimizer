import hashlib
from pathlib import Path


DEFAULT_CHUNK_SIZE = 1024 * 1024  # 1 MB


def calculate_sha256(
    file_path: Path,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
) -> str:
    """
    Calculate SHA-256 hash of a file.

    The file is read in chunks so that large files
    do not need to be loaded entirely into memory.
    """

    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:

        while True:

            chunk = file.read(chunk_size)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()