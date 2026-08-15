from datetime import datetime
from statistics import mean


class StorageForecaster:

    def forecast(
        self,
        history
    ):

        if len(history) < 2:

            return {
                "daily_growth": 0,
                "30_days": None,
                "60_days": None,
                "90_days": None,
            }

        growth_rates = []

        for i in range(
            1,
            len(history)
        ):

            previous = history[i - 1]
            current = history[i]

            delta_storage = (
                current["storage"]
                - previous["storage"]
            )

            delta_days = (
                current["date"]
                - previous["date"]
            ).days

            if delta_days > 0:

                growth_rates.append(
                    delta_storage /
                    delta_days
                )

        daily_growth = mean(
            growth_rates
        )

        current_storage = (
            history[-1]["storage"]
        )

        return {
            "daily_growth":
                daily_growth,

            "30_days":
                current_storage +
                daily_growth * 30,

            "60_days":
                current_storage +
                daily_growth * 60,

            "90_days":
                current_storage +
                daily_growth * 90,
        }