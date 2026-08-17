import os
import sys
import json
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
from recommender.recommendation_engine import RecommendationEngine


def bytes_to_gb(size):

    return round(
        size / (1024 ** 3),
        2
    )


def serialize_duplicates(
    duplicate_groups
):

    output = []

    for group in duplicate_groups:

        files = []

        for file in group:

            files.append({
                "name": file.name,
                "path": file.path,
                "size_gb": bytes_to_gb(file.size)
            })

        output.append(files)

    return output


def serialize_files(files):

    result = []

    for file in files[:50]:

        result.append({
            "name": file.name,
            "path": file.path,
            "size_gb": bytes_to_gb(file.size)
        })

    return result


def serialize_recommendations(
    recommendations
):

    result = []

    for rec in recommendations[:50]:

        result.append({
            "file": rec.file.name,
            "path": rec.file.path,
            "action": rec.action,
            "confidence": rec.confidence,
            "reason": rec.reason
        })

    return result


def main():

    if len(sys.argv) < 2:

        print(
            "Usage: python export_analysis.py <directory>"
        )

        return

    directory = sys.argv[1]

    scanner = FileSystemScanner()

    files = scanner.scan(directory)

    analyzer = StorageAnalyzer()

    results = analyzer.analyze(files)

    engine = RecommendationEngine()

    recommendations = (
        engine.generate(files)
    )

    export_data = {

        "statistics":
            results["statistics"],

        "duplicates":
            serialize_duplicates(
                results["duplicates"]
            ),

        "unused_files":
            serialize_files(
                results["unused_files"]
            ),

        "large_files":
            serialize_files(
                results["large_files"]
            ),

        "recommendations":
            serialize_recommendations(
                recommendations
            )
    }

    output_file = Path(
        "data/latest_analysis.json"
    )

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            export_data,
            f,
            indent=2
        )

    print(
        f"\nAnalysis exported to:\n"
        f"{output_file.resolve()}"
    )


if __name__ == "__main__":
    main()