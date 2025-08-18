
from google.adk.agents import Agent
from dotenv import load_dotenv

load_dotenv()

root_agent = Agent(
    name="qa_agent",
    model="gemini-2.0-flash",
    description="Question answer agent",
    instruction="""
    You are a helpful assistant that answers questions about the user's preferences.

    Here is some information about the user:
    Name: 
    {user_name}
    Preferences: 
    {user_preferences}
    """
)