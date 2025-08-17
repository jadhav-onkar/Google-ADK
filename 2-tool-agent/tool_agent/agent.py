
from google.adk.agents import Agent
from google.adk.tools import google_search
import datetime

def get_current_time() -> dict:
    """
    get current time in format YYYY:MM:DD HH:MM:SS
    """
    return {
        "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="tool agent",
    instruction="you are an agent that use following tool - get_current_time",
    # tools=[google_search]
    tools=[get_current_time]
)
