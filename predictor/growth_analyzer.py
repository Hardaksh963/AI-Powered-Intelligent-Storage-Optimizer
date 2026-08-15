class GrowthAnalyzer:

    def calculate_daily_growth(
        self,
        history
    ):

        if len(history) < 2:
            return 0

        first = history[0]
        last = history[-1]

        days = (
            last.timestamp -
            first.timestamp
        ).days

        if days <= 0:
            return 0

        growth = (
            last.total_storage -
            first.total_storage
        )

        return growth / days