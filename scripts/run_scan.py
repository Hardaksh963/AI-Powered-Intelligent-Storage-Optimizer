import json
import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scanner import FileSystemScanner


def main():

    if len(sys.argv) < 2:

        print(
            "Usage:"
        )

        print(
            "python scripts/run_scan.py <directory>"
        )

        return

    directory = sys.argv[1]

    print("=" * 60)
    print("AI STORAGE COPILOT")
    print("Filesystem Scanner")
    print("=" * 60)

    print(f"\nScanning: {directory}")
    print("Please wait...\n")

    scanner = FileSystemScanner(
        calculate_hash=True
    )

    records = scanner.scan(directory)

    print("=" * 60)
    print(f"Files discovered: {len(records)}")
    print("=" * 60)

    for record in records[:20]:

        size_mb = record.size / (
            1024 * 1024
        )

        print(
            f"\n{record.name}"
        )

        print(
            f"  Path: {record.path}"
        )

        print(
            f"  Size: {size_mb:.2f} MB"
        )

        print(
            f"  Category: {record.category}"
        )

        print(
            f"  Hash: {record.file_hash}"
        )

    if len(records) > 20:

        print(
            f"\n... and "
            f"{len(records) - 20} more files."
        )

    # Save scan results
    output_directory = (
        PROJECT_ROOT
        / "data"
        / "scans"
    )

    output_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = (
        output_directory
        / "latest_scan.json"
    )

    with output_file.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            [
                record.to_dict()
                for record in records
            ],
            file,
            indent=2,
            ensure_ascii=False,
        )

    print(
        f"\nScan saved to: {output_file}"
    )


if __name__ == "__main__":
    main()