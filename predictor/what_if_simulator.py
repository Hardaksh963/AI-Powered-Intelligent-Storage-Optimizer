class WhatIfSimulator:

    def simulate_cleanup(
        self,
        current_storage,
        storage_saved
    ):

        return max(
            0,
            current_storage -
            storage_saved
        )

    def simulate_growth_change(
        self,
        current_storage,
        daily_growth,
        percentage_change
    ):

        new_growth = (
            daily_growth *
            (
                1 +
                percentage_change / 100
            )
        )

        return {
            "new_daily_growth":
                new_growth,

            "30_days":
                current_storage +
                new_growth * 30,

            "90_days":
                current_storage +
                new_growth * 90
        }