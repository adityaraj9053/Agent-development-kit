# Callbacks
It is a function which executes at specific pointin the agent execution's point

## CallbackContext
The CallbackContext allows the agent to access all information it needs to properly handle what's going on. It provides  to all callback types and contains:

- **`agent_name:`**  The name of the agent being executed
- **`invocation_id:`**  A unique identifier for the current agent invocation
- **`state:`**  Access to the session state, allowing you to read/write persistent data
- **`app_name:`**  The name of the application
- **`user_id:`**  The ID of the current user
- **`session_id:`**  The ID of the current session


## Purpose of Before-agent-callback
beforr calling function set state like before running this agent, extract required information such as username, id, subacription, etc..

## Purpose of After-agent-callback
modifying final state, add logging

## Purpose of Before-model-callback
adding dynamic instruction, injecting examples, modifying model config, implementing guardrails.\
ex - Here, before sending to model it is checking thge input. 
````python
def before_model_callback(callback_context, llm_request):
    for content in reversed(llm_request.contents):
        if content.role == "user" and "sucks" in content.parts[0].text.lower():
            return LlmResponse(
                content=types.Content(
                    role="model",
                    parts=[types.Part(text="Please avoid inappropriate language.")]
                )
            )
    return None  # Continue as normal

Output:

if input is: "This product sucks!" → It will Block .
`````

## Purpose of After-model-callback
Allows inspection and modification of tool's result 