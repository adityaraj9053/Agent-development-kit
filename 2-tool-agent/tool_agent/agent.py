from datetime import datetime
from google.adk.agents import Agent
from google.adk.tools import google_search
# from litellm.proxy.mcp_tools import get_current_time

def get_current_time() -> dict:
    """
    Get the current time in format6 YYYY-MM-DD HH:MM:SS
    """

    #return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "currentTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


root_agent = Agent(
    name = "tool_agent",
    model = "gemini-1.5-flash",
    description = "ToolAgent",
    instruction = """
    You are a helpful assistant that can use the following tools -  get_current_time.
    """,

tools = [ get_current_time],
    # tools = [ get_current_time, google_search], # <- NOT ALLOWED

)
