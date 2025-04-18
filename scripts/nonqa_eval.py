from autoevals.llm import *
import openai
import asyncio
from autoevals import init
import os
from braintrust import Eval
from autoevals import LevenshteinScorer

os.environ["OPENAI_API_KEY"] = "sk-or-v1-xxx"
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
os.environ["BRAINTRUST_API_KEY"] = "sk-xxxx"

client = init(openai.AsyncOpenAI(base_url=os.environ["OPENAI_API_BASE"], api_key=os.environ["OPENAI_API_KEY"], model="openai/gpt-4o-mini"))


Eval(
    "Autoevals",
    data=lambda: [
        dict(
            input="Which country has the highest population?",
            expected="China",
        ),
    ],
    task=lambda *args: "People's Republic of China",
    scores=[Factuality],
)


