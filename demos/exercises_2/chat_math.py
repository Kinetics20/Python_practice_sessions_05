import os
import json
import requests
import math
from openai import OpenAI

key_path = os.path.join(os.path.dirname(__file__), "..", "chat", "demo.key")
with open(key_path, "r") as f:
    api_key: str = f.read().strip()

client = OpenAI(api_key=api_key)
API_BASE = "http://127.0.0.1:8000"
USER_AGENT = "ChatWithFullMathAPI"

tools = [
    {"type": "function", "name": "add", "description": "Add two numbers",
     "parameters": {"type": "object",
                    "properties": {"a": {"type": "number"}, "b": {"type": "number"}},
                    "required": ["a", "b"], "additionalProperties": False}},
    {"type": "function", "name": "subtract", "description": "Subtract b from a",
     "parameters": {"type": "object",
                    "properties": {"a": {"type": "number"}, "b": {"type": "number"}},
                    "required": ["a", "b"], "additionalProperties": False}},
    {"type": "function", "name": "multiply", "description": "Multiply two numbers",
     "parameters": {"type": "object",
                    "properties": {"a": {"type": "number"}, "b": {"type": "number"}},
                    "required": ["a", "b"], "additionalProperties": False}},
    {"type": "function", "name": "divide", "description": "Divide a by b",
     "parameters": {"type": "object",
                    "properties": {"a": {"type": "number"}, "b": {"type": "number"}},
                    "required": ["a", "b"], "additionalProperties": False}},
    {"type": "function", "name": "power", "description": "Raise a to the power of b",
     "parameters": {"type": "object",
                    "properties": {"base": {"type": "number"}, "exponent": {"type": "number"}},
                    "required": ["base", "exponent"], "additionalProperties": False}},
    {"type": "function", "name": "sin", "description": "Calculate sine (radians)",
     "parameters": {"type": "object",
                    "properties": {"x": {"type": "number"}},
                    "required": ["x"], "additionalProperties": False}},
    {"type": "function", "name": "cos", "description": "Calculate cosine (radians)",
     "parameters": {"type": "object",
                    "properties": {"x": {"type": "number"}},
                    "required": ["x"], "additionalProperties": False}},
]

def call_math_api(name: str, args: dict) -> str:
    """Execute the local FastAPI for exact operation."""
    try:
        url = f"{API_BASE}/{name}"
        resp = requests.get(url, params=args, headers={"User-Agent": USER_AGENT})
        resp.raise_for_status()
        return str(resp.json().get("result", "no result"))
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Chat with full math API ready.")
    log = []

    while True:
        try:
            user_input = input("? ")
        except (EOFError, KeyboardInterrupt):
            break
        log.append({"role": "user", "content": user_input})

        response = client.responses.create(
            model="gpt-4.1-nano",
            input=log,
            tools=tools,
        )

        skip_input = False
        for o in response.output:
            log.append(o)

            if o.type == "message":
                print(o.content[0].text)
            elif o.type == "function_call":
                func = o.name
                args = json.loads(o.arguments)
                result = call_math_api(func, args)
                log.append({"type": "function_call_output", "call_id": o.call_id, "output": result})
                print(f"🧮 {func} result: {result}")
            skip_input = False

    print("End.")

if __name__ == "__main__":
    main()
