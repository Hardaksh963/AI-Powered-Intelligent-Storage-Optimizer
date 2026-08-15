import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

    NVIDIA_BASE_URL = os.getenv(
        "NVIDIA_BASE_URL",
        "https://integrate.api.nvidia.com/v1"
    )

    NVIDIA_MODEL = os.getenv(
        "NVIDIA_MODEL",
        "nvidia/llama-3.3-nemotron-super-49b-v1"
    )


settings = Settings()