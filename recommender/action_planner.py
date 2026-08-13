class ActionPlanner:

    def summarize(
        self,
        recommendations
    ):

        summary = {
            "KEEP": 0,
            "REVIEW": 0,
            "ARCHIVE": 0,
            "CLEAN": 0,
        }

        for rec in recommendations:

            summary[
                rec.action
            ] += 1

        return summary