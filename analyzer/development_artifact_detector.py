import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from pathlib import Path

from models.file_model import FileRecord


ARTIFACT_PATTERNS = {
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".next",
    "dist",
    "build",
    "target",
    ".gradle",
    ".cache",
    "coverage",
    "bin",
    "obj",
}


class DevelopmentArtifactDetector:

    def find_artifacts(
        self,
        files: list[FileRecord]
    ):

        artifacts = []

        for file in files:

            path_parts = {
                part.lower()
                for part in Path(file.path).parts
            }

            if path_parts.intersection(
                ARTIFACT_PATTERNS
            ):
                artifacts.append(file)

        return artifacts