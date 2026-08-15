import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from analyzer.duplicate_detector import DuplicateDetector
from analyzer.unused_detector import UnusedFileDetector
from analyzer.large_file_detector import LargeFileDetector
from analyzer.storage_statistics import StorageStatistics
from analyzer.development_artifact_detector import (
    DevelopmentArtifactDetector
)

class StorageAnalyzer:

    def __init__(self):

        self.duplicate_detector = DuplicateDetector()
        self.unused_detector = UnusedFileDetector()
        self.large_file_detector = LargeFileDetector()
        self.statistics = StorageStatistics()
        self.artifact_detector = (
            DevelopmentArtifactDetector()
        )
    def analyze(self, files):

        duplicates = self.duplicate_detector.find_duplicates(
            files
        )

        unused_files = self.unused_detector.find_unused_files(
            files
        )

        large_files = self.large_file_detector.find_large_files(
            files
        )

        stats = self.statistics.generate(
            files
        )
        artifacts = (
            self.artifact_detector.find_artifacts(
                files
            )
        )
        return {
            "duplicates": duplicates,
            "unused_files": unused_files,
            "large_files": large_files,
            "statistics": stats,
            "artifacts": artifacts,
        }