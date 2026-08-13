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
from recommender import RecommendationEngine
from recommender.action_planner import (
    ActionPlanner
)


def main():

    if len(sys.argv) < 2:

        print(
            "Usage: "
            "python recommend_storage.py "
            "<directory>"
        )

        return

    directory = sys.argv[1]

    print(
        "\nAnalyzing storage...\n"
    )

    scanner = FileSystemScanner()

    files = scanner.scan(directory)

    analyzer = StorageAnalyzer()

    analyzer.analyze(files)

    engine = RecommendationEngine()

    recommendations = engine.generate(
        files
    )

    planner = ActionPlanner()

    summary = planner.summarize(
        recommendations
    )

    print("=" * 60)
    print("STORAGE RECOMMENDATIONS")
    print("=" * 60)

    print("\nSummary")

    for action, count in summary.items():

        print(
            f"{action:<10} {count}"
        )

    print(
        "\nTop Recommendations\n"
    )

    for rec in recommendations[:10]:

        print(
            f"[{rec.action}] "
            f"{rec.file.name}"
        )

        print(
            f"Confidence: "
            f"{rec.confidence:.0f}%"
        )

        print(
            f"Reason: "
            f"{rec.reason}"
        )

        print("-" * 50)


if __name__ == "__main__":
    main()