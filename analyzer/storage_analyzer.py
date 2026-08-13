from analyzer.duplicate_detector import DuplicateDetector
from analyzer.unused_detector import UnusedFileDetector
from analyzer.large_file_detector import LargeFileDetector
from analyzer.storage_statistics import StorageStatistics


class StorageAnalyzer:

    def __init__(self):

        self.duplicate_detector = DuplicateDetector()
        self.unused_detector = UnusedFileDetector()
        self.large_file_detector = LargeFileDetector()
        self.statistics = StorageStatistics()

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

        return {
            "duplicates": duplicates,
            "unused_files": unused_files,
            "large_files": large_files,
            "statistics": stats,
        }