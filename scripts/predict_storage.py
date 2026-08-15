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

from predictor import (
    SnapshotManager,
    HistoryManager,
    GrowthAnalyzer,
    StorageForecaster
)


def bytes_to_gb(size):

    return round(
        size / (1024 ** 3),
        2
    )


def main():

    if len(sys.argv) < 2:

        print(
            "Usage: python predict_storage.py <directory>"
        )

        return

    directory = sys.argv[1]

    scanner = FileSystemScanner()

    files = scanner.scan(directory)

    snapshot_manager = SnapshotManager()

    snapshot = (
        snapshot_manager.create_snapshot(
            files
        )
    )

    history_manager = HistoryManager()

    # history_manager.save_snapshot(
    #     snapshot
    # )

    history = (
        history_manager.load_history()
    )
    print(f"\nHistory Records: {len(history)}")

    if history:
        print(
            f"First Snapshot: "
            f"{history[0].total_storage / (1024**3):.2f} GB"
        )

        print(
            f"Last Snapshot: "
            f"{history[-1].total_storage / (1024**3):.2f} GB"
        )
    analyzer = GrowthAnalyzer()

    daily_growth = (
        analyzer.calculate_daily_growth(
            history
        )
    )

    forecaster = StorageForecaster()

    predictions = forecaster.forecast(
            history
        )
    
    days_until_full = (
        forecaster.estimate_disk_full(
            history,
            disk_capacity=500 * 1024**3
        )
    )
    
    print("\nSTORAGE FORECAST\n")

    if not history:
        print(
            "\nNo historical data found."
        )
        print(
            "Run generate_demo_history.py first."
        )
        return

    current_storage = (
        history[-1].total_storage
    )

    print(
        f"Current Storage: "
        f"{bytes_to_gb(current_storage)} GB"
    )

    print(
        f"Daily Growth: "
        f"{bytes_to_gb(daily_growth)} GB/day"
    )

    print("\nPredictions")

    print(
        f"30 Days: "
        f"{bytes_to_gb(predictions['30_days'])} GB"
    )

    print(
        f"60 Days: "
        f"{bytes_to_gb(predictions['60_days'])} GB"
    )

    print(
        f"90 Days: "
        f"{bytes_to_gb(predictions['90_days'])} GB"
    )

    print(
        f"Disk Full Estimate: "
        f"{days_until_full} days"
    )

if __name__ == "__main__":
    main()