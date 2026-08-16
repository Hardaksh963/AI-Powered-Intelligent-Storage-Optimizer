import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from openai import OpenAI

from config.settings import settings


class NvidiaLLM:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.NVIDIA_API_KEY,
            base_url=settings.NVIDIA_BASE_URL
        )

        self.model = settings.NVIDIA_MODEL

    def generate(
        self,
        prompt: str,
        temperature: float = 0.2
    ):

        try:

            response = self.client.chat.completions.create(
                model=self.model,
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

        except Exception as e:

            print("\n========== NVIDIA ERROR ==========")
            print(f"Model: {self.model}")
            print(f"Base URL: {settings.NVIDIA_BASE_URL}")
            print(f"Error: {e}")
            print("==================================\n")

            raise