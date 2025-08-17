
import os
import random
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(
    model="openai/o3",
    api_key=os.getenv("OPEN_AI_API_KEY")
)

def funny_jokes():
    jokes = [
        "I told my computer a joke… it froze.",
        "Parallel lines have so much in common… it’s a shame they’ll never meet.",
        "I would tell you a construction joke… but I’m still working on it.",
        "My math teacher called me average… how mean!"
    ]
    return random.choice(jokes)

root_agent = Agent(
    name="funny_jokes",
    model=model,
    instruction="""
    you are an joke model that uses following tool "funny_jokes"
    """,
    description="joke model",
    tools=[funny_jokes]
)

