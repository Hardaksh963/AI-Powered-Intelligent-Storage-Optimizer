from datetime import datetime


class ArchiveRecommender:

    def recommend(
        self,
        files
    ):

        recommendations = []

        now = datetime.now()

        for file in files:

            if not file.accessed_at:
                continue

            age = (
                now - file.accessed_at
            ).days

            size_mb = (
                file.size /
                (1024 * 1024)
            )

            if (
                age > 180
                and size_mb > 50
                and not file.is_duplicate
            ):

                recommendations.append({
                    "file": file,
                    "reason":
                        "Old large file suitable for archival storage"
                })

        return recommendations