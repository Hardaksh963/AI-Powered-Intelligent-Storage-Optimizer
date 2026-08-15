from llm.nvidia_client import NvidiaLLM


class StorageAgent:

    def __init__(self):

        self.llm = NvidiaLLM()

    def explain_recommendation(
        self,
        file_name,
        action,
        reason
    ):

        prompt = f"""
You are an expert storage optimization assistant.

File Name:
{file_name}

Recommended Action:
{action}

Reason:
{reason}

Explain:
1. Why this recommendation was made
2. Potential storage savings
3. Any risks involved
4. Whether the user should keep, archive or remove it

Keep the response concise.
"""

        return self.llm.generate(prompt)