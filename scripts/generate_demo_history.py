import sys
from pathlib import Path
from datetime import datetime, timedelta
import random

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from predictor.history_manager import HistoryManager
from models.storage_snapshot import StorageSnapshot


def generate_demo_history():

    history_manager = HistoryManager()

    # Clear old history file
    if history_manager.history_file.exists():
        history_manager.history_file.unlink()

    start_date = datetime.now() - timedelta(days=30)

    # Start at 100 GB
    current_storage = 100 * 1024**3

    print("Generating demo history...\n")

    for day in range(30):

        growth_gb = random.uniform(
            0.5,
            2.0
        )

        current_storage += (
            growth_gb * 1024**3
        )

        snapshot = StorageSnapshot(
            timestamp=start_date + timedelta(days=day),
            total_files=10000 + (day * 50),
            total_storage=int(current_storage)
        )

        history_manager.save_snapshot(
            snapshot
        )

        print(
            f"Day {day + 1:02d} | "
            f"Storage: "
            f"{current_storage / (1024**3):.2f} GB"
        )

    print(
        "\nDemo history created successfully."
    )


if __name__ == "__main__":
    generate_demo_history()