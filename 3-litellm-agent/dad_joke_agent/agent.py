# Our aim is to connect our adk to other AI models other than Gemini.

# LiteLLM is an open-source tool developed by BerriAI that provides a unified interface to interact with over 100 large
# language model (LLM) APIs. It allows developers to seamlessly switch between different LLM providers—such as OpenAI,
# Azure, Google Vertex AI, Cohere, Anthropic, Hugging Face, and more—using a consistent OpenAI-compatible API format

import os
import random

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(
    model = "openrouter/openai/gpt-3.5-turbo",
    api_key = os.getenv("OPENROUTER_API_KEY"),
)
def get_dad_joke() :
    jokes = [
        "Why did the chicken cross the road? To get to the other side.",
        "What will you call a belt made up of watches? A waist of time.",
        "What will you call a fake spaghetti? An Impasta.",
        "Ram keh gye the siya se aisa kalyug aaega, Santa padh ke aaega aur Banta top kr jaega",
    ]
    return random.choice(jokes)


root_agent = Agent(
    name = "dad_joke_agent",
    model = model,
    description = "dad joke Agent",
    instruction = """
    You are a helpful assistant that tells dad jokes.
    When asked for a joke, **call the 'get_dad_joke' tool exactly once** to retrieve a single joke.
    Then, respond with that single joke and offer if the user would like another.
    """,
    tools = [get_dad_joke], # Added the missing comma here!
)