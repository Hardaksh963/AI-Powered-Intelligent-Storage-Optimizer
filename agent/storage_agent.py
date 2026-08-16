from llm.nvidia_client import NvidiaLLM

from agent.prompts import (
    SYSTEM_PROMPT,
    SUMMARY_PROMPT
)

from agent.query_router import (
    QueryRouter
)


class StorageAgent:

    def __init__(self):

        self.llm = NvidiaLLM()

        self.router = QueryRouter()

    def explain_recommendation(
        self,
        file_name,
        action,
        reason
    ):

        prompt = f"""
File Name:
{file_name}

Recommended Action:
{action}

Reason:
{reason}

Explain:
1. Why this recommendation was made
2. Potential storage savings
3. Risks
4. Final recommendation
"""

        return self.llm.generate(prompt)

    def answer_query(
        self,
        query,
        storage_summary,
        forecast
    ):

        route = self.router.route(
            query
        )

        prompt = SUMMARY_PROMPT.format(
            summary=storage_summary,
            forecast=forecast,
            query=query
        )

        return self.llm.generate(
            f"{SYSTEM_PROMPT}\n\n"
            f"Query Type: {route}\n\n"
            f"{prompt}"
        )