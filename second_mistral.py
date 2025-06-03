from dotenv import load_dotenv
import os
import time
from openai import OpenAI
import requests

# Load environment variables
load_dotenv()
API_KEY = os.getenv("MISTRAL_KEY")

# Define the function to get weather
def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    return response.text

# Available tools
available_tools = {
    "get_weather": get_weather
}

# System prompt
SYSTEM_PROMPT = """
You are a helpful AI assistant specialized in resolving user queries. You work in a start, plan, action, observe mode.

For a given user query and available tools, plan the step-by-step execution:
- First, start and understand the query.
- Once the query is understood, comprehend it thoroughly.
- Plan the step-by-step execution.
- Based on planning, select the relevant tool from the available tools.
- Based on tool selection, perform an action.
- Wait for the observation and, based on the observation from the tool call, resolve the user query.

Rules:
- Follow the output JSON format.
- Always perform one step at a time and wait for the next input.
- Observe whether the step is performed correctly or not.
- Carefully analyze the user query.

Output JSON Format:
{
    "step": "string",
    "content": "string",
    "function": "The name of the function if the step is action",
    "input": "The input parameter for the function"
}

Available Tools:
- "get_weather": Takes a city name as input and returns the current weather for the city.
"""

# Initialize messages
messages = [{"role": "system", "content": SYSTEM_PROMPT}]

# Initialize the OpenAI client
client = OpenAI(api_key=API_KEY, base_url="https://api.mistral.ai/v1")

def make_api_call_with_retry(messages):
    max_retries = 5
    retry_delay = 1  # Initial delay in seconds
#MISTRAL_KEY="BGj1La66UJtvXtOINHMemIHWc76Lr85B"
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="mistral-small-latest",
                messages=messages
            )
            return response
        except Exception as e:
            if isinstance(e, OpenAI.RateLimitError):
                print(f"Rate limit exceeded. Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff
            else:
                raise e
    raise Exception("Max retries exceeded")

while True:
    try:
        query = input("> ")
        messages.append({"role": "user", "content": query})

        response = make_api_call_with_retry(messages)
        response_message = response.choices[0].message
        messages.append(response_message)

        print(response_message.content)

        # Check if the response includes a function call
        if hasattr(response_message, 'function_call') and response_message.function_call:
            function_name = response_message.function_call.name
            function_args = eval(response_message.function_call.arguments)

            if function_name in available_tools:
                function_response = available_tools[function_name](**function_args)
                messages.append({
                    "role": "function",
                    "name": function_name,
                    "content": function_response
                })

    except Exception as e:
        print(f"An error occurred: {e}")
