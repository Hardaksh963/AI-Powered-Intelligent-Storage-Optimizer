class StorageInsights:

    def generate(
        self,
        files,
        recommendations
    ):

        duplicate_files = sum(
            1
            for f in files
            if f.is_duplicate
        )

        duplicate_size = sum(
            f.size
            for f in files
            if f.is_duplicate
        )

        archive_count = sum(
            1
            for r in recommendations
            if r.action == "ARCHIVE"
        )

        clean_count = sum(
            1
            for r in recommendations
            if r.action == "CLEAN"
        )

        return {
            "duplicate_files":
                duplicate_files,

            "duplicate_size":
                duplicate_size,

            "archive_count":
                archive_count,

            "clean_count":
                clean_count,
        }