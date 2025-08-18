import uuid
from google.adk.sessions import InMemorySessionService, session
from google.adk.runners import Runner
from dotenv import load_dotenv
from google.genai import types
from qa_agent.agent import root_agent

load_dotenv()
s_service = InMemorySessionService()

user_state = {
    "user_name": "Ganesh",
    "user_preferences": """
        I like to play Pickleball, Disc Golf, and Tennis.
        My favorite food is Mexican.
        My favorite TV show is Game of Thrones.
        Loves it when people like and subscribe to his YouTube channel.
    """,
}

SESSION_ID=str(uuid.uuid4())
APP_NAME="qa bot"
USER_ID="user1"
new_session = s_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    state=user_state,
    session_id=SESSION_ID
) 

print("CREATED NEW SESSION:")
print(f"\tSession ID: {SESSION_ID}")

runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=s_service,
)

new_msg = types.Content(
    role="user",
    parts=[types.Part(text="What is ganesh favorite TV show?")]
)

for envents in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_msg
):
    if envents.is_final_response():
        if envents.content and envents.content.parts:
            print(f"final responce :: {envents.content.parts[0].text}")

print("==== Session Event Exploration ====")
session = s_service.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
)

print("=== Final Session State ===")
for key, value in session.state.items():
    print(f"{key}: {value}")