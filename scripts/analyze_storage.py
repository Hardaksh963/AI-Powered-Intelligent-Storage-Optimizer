import sys
from pathlib import Path

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scanner import FileSystemScanner
from analyzer import StorageAnalyzer


def bytes_to_gb(size):

    return size / (1024 ** 3)


def main():

    if len(sys.argv) < 2:

        print(
            "Usage: python scripts/analyze_storage.py <directory>"
        )
        return

    directory = sys.argv[1]

    print("\nScanning storage...\n")

    scanner = FileSystemScanner()

    files = scanner.scan(directory)

    analyzer = StorageAnalyzer()

    results = analyzer.analyze(files)

    stats = results["statistics"]

    print("=" * 60)
    print("STORAGE ANALYSIS")
    print("=" * 60)

    print(
        f"Files: {stats['total_files']}"
    )

    print(
        f"Storage: {bytes_to_gb(stats['total_size']):.2f} GB"
    )

    print(
        f"Duplicate Groups: "
        f"{len(results['duplicates'])}"
    )

    print(
        f"Unused Files: "
        f"{len(results['unused_files'])}"
    )

    print(
        f"Large Files: "
        f"{len(results['large_files'])}"
    )

    print("\nCategory Breakdown")

    for category, size in sorted(
        stats["categories"].items(),
        key=lambda x: x[1],
        reverse=True
    ):

        print(
            f"{category:<15}"
            f"{bytes_to_gb(size):.2f} GB"
        )


if __name__ == "__main__":
    main()