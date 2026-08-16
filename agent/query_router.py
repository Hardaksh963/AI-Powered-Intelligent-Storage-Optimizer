class QueryRouter:

    def route(
        self,
        query: str
    ):

        query = query.lower()

        if any(
            word in query
            for word in [
                "forecast",
                "future",
                "growth",
                "prediction"
            ]
        ):
            return "forecast"

        if any(
            word in query
            for word in [
                "duplicate",
                "duplicates"
            ]
        ):
            return "duplicates"

        if any(
            word in query
            for word in [
                "unused",
                "old",
                "archive"
            ]
        ):
            return "archive"

        if any(
            word in query
            for word in [
                "free",
                "cleanup",
                "delete"
            ]
        ):
            return "cleanup"

        return "general"