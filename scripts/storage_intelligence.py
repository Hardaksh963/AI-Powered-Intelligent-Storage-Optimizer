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
from intelligence import ReportGenerator


def main():

    if len(sys.argv) < 2:
        print(
            "Usage: python storage_intelligence.py <directory>"
        )
        return

    directory = sys.argv[1]

    scanner = FileSystemScanner()

    files = scanner.scan(directory)

    analyzer = StorageAnalyzer()

    analyzer.analyze(files)

    engine = RecommendationEngine()

    recommendations = engine.generate(
        files
    )

    generator = ReportGenerator()

    report = generator.generate_report(
        recommendations
    )

    print("\nSTORAGE INTELLIGENCE REPORT\n")

    for item in report:

        print(
            f"\nFile: {item['file']}"
        )

        print(
            f"Action: {item['action']}"
        )

        print(
            f"Importance: "
            f"{item['importance']:.0f}"
        )

        print(
            f"Risk: "
            f"{item['risk']}"
        )

        print(
            f"Reason: "
            f"{item['reason']}"
        )

        print("-" * 50)


if __name__ == "__main__":
    main()