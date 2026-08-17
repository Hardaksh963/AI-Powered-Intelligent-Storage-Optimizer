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
        forecast,
        analysis
    ):

        route = self.router.route(
            query
        )

        prompt = f"""
    Storage Summary

    {storage_summary}

    Forecast

    {forecast}

    Analysis Results

    Duplicates:
    {analysis.get('duplicates', [])}

    Unused Files:
    {analysis.get('unused_files', [])}

    Large Files:
    {analysis.get('large_files', [])}

    Recommendations:
    {analysis.get('recommendations', [])}

    User Question:
    {query}

    Answer using the actual storage data.

    If recommending deletion,
    mention exact files.

    If recommending archiving,
    mention exact files.

    Be concise and practical.
    """

        return self.llm.generate(prompt)