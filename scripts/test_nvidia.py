import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from llm.nvidia_client import NvidiaLLM


llm = NvidiaLLM()

response = llm.generate(
    "In one sentence, explain what storage optimization means."
)

print(response)