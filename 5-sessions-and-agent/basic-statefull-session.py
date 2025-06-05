import uuid

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_answering_agent import question_answering_agent

load_dotenv()


# Create a new session service to store state
session_service_stateful = InMemorySessionService() # in memory i.e. session lost data lost

initial_state = {
    "user_name": "Aditya Raj",
    "user_preferences": """
        I like to play Football, Cricket.
        My favorite food is North Indian.
        My favorite TV show is Chakravarti Ashoka Samrat.
    """,
}

# Create a NEW session
APP_NAME = "Raj Bot"
USER_ID = "Aditya_Raj"
SESSION_ID = str(uuid.uuid4())
stateful_session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)
print("CREATED NEW SESSION:")
print(f"\tSession ID: {SESSION_ID}")

# just like explained in a diagram
runner = Runner(
    agent=question_answering_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful,
)
# taking input from "user"
new_message = types.Content(
    role="user", parts=[types.Part(text="What is Aditya's favorite TV show?")]
)
# giving new input from the user to agent and running a loop of events because each event produce some result and in final will combine results of all event
for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final Response: {event.content.parts[0].text}")

print("==== Session Event Exploration ====")
session = session_service_stateful.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
)

# Log final Session state
print("=== Final Session State ===")
for key, value in session.state.items():
    print(f"{key}: {value}")