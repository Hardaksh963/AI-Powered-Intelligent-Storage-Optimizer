from statistics import mean


class StorageForecaster:

    def calculate_daily_growth(
        self,
        history
    ):

        if len(history) < 2:
            return 0

        growth_rates = []

        for i in range(1, len(history)):

            previous = history[i - 1]
            current = history[i]

            delta_storage = (
                current.total_storage
                - previous.total_storage
            )

            delta_days = (
                current.timestamp
                - previous.timestamp
            ).days

            if delta_days > 0:

                growth_rates.append(
                    delta_storage / delta_days
                )

        if not growth_rates:
            return 0

        return mean(growth_rates)

    def forecast(
        self,
        history
    ):

        if len(history) < 2:

            current_storage = (
                history[-1].total_storage
                if history
                else 0
            )

            return {
                "daily_growth": 0,
                "30_days": current_storage,
                "60_days": current_storage,
                "90_days": current_storage,
            }

        daily_growth = (
            self.calculate_daily_growth(
                history
            )
        )

        current_storage = (
            history[-1].total_storage
        )

        return {
            "daily_growth":
                daily_growth,

            "30_days":
                current_storage +
                (daily_growth * 30),

            "60_days":
                current_storage +
                (daily_growth * 60),

            "90_days":
                current_storage +
                (daily_growth * 90),
        }

    def estimate_disk_full(
        self,
        history,
        disk_capacity
    ):

        daily_growth = (
            self.calculate_daily_growth(
                history
            )
        )

        if daily_growth <= 0:
            return None

        current_storage = (
            history[-1].total_storage
        )

        remaining_space = (
            disk_capacity -
            current_storage
        )

        if remaining_space <= 0:
            return 0

        return round(
            remaining_space /
            daily_growth,
            1
        )