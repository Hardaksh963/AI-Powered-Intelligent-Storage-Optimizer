from openai import OpenAI

from config.settings import settings


class NvidiaLLM:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.NVIDIA_API_KEY,
            base_url=settings.NVIDIA_BASE_URL
        )

    def generate(
        self,
        prompt: str,
        temperature: float = 0.2
    ):

        response = self.client.chat.completions.create(
            model=settings.NVIDIA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=temperature,
            max_tokens=1000
        )

        return response.choices[0].message.content