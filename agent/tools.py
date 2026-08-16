class StorageTools:

    @staticmethod
    def get_storage_summary(
        analysis_results
    ):

        return analysis_results

    @staticmethod
    def get_forecast(
        forecast_results
    ):

        return forecast_results

    @staticmethod
    def get_duplicate_count(
        analysis_results
    ):

        return len(
            analysis_results.get(
                "duplicates",
                []
            )
        )

    @staticmethod
    def get_unused_count(
        analysis_results
    ):

        return len(
            analysis_results.get(
                "unused_files",
                []
            )
        )

    @staticmethod
    def get_large_file_count(
        analysis_results
    ):

        return len(
            analysis_results.get(
                "large_files",
                []
            )
        )