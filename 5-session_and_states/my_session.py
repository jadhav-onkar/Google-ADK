
from google.adk.sessions import InMemorySessionService, Session

s_service = InMemorySessionService()

eg_session = s_service.create_session(
    app_name="my_app",
    user_id="my_user_id",
    state={"key":"values"}
)

print(f"--- Examining Session Properties ---")
print(f"ID (`id`):                {eg_session.id}")
print(f"Application Name (`app_name`): {eg_session.app_name}")
print(f"User ID (`user_id`):         {eg_session.user_id}")
print(f"State (`state`):           {eg_session.state}") # Note: Only shows initial state here
print(f"Events (`events`):         {eg_session.events}") # Initially empty
print(f"Last Update (`last_update_time`): {eg_session.last_update_time:.2f}")
print(f"---------------------------------")

temp_service =  s_service.delete_session(app_name=eg_session.app_name,
                             user_id=eg_session.user_id, session_id=eg_session.id)
print("The final status of temp_service - ", temp_service)