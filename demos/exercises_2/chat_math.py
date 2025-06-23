import sys
import os
import json
import time
import requests
from openai import OpenAI

USER_AGENT = "ChatWithMathAPI"
API_BASE = "http://127.0.0.1:8000"  # FastAPI kalkulator lokalnie

# Wczytywanie API key z pliku demo.key podobnie jak w Twoim przykładzie
key_path = os.path.join(os.path.dirname(__file__), "..", "chat", "demo.key")
with open(key_path, "r") as f:
    api_key: str = f.read().strip()

tools = [
    {
        "type": "function",
        "name": "math_operation",
        "description": "Perform basic math operations (add, subtract, multiply, divide, power).",
        "parameters": {
            "type": "object",
            "properties": {
                "operation": {"type": "string", "description": "add, subtract, multiply, divide, power"},
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required": ["operation", "a", "b"],
            "additionalProperties": False
        }
    }
]

log: list[dict] = []
client = OpenAI(api_key=api_key)

def call_math_api(operation: str, a: float, b: float) -> str:
    try:
        resp = requests.get(
            f"{API_BASE}/{operation}",
            params={"a": a, "b": b},
            headers={"User-Agent": USER_AGENT}
        )
        resp.raise_for_status()
        return str(resp.json().get("result"))
    except Exception as e:
        return f"Error calling math API: {e}"

if __name__ == "__main__":
    print("Chat with math API ready.")
    skip_input = False

    while True:
        if not skip_input:
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

        for o in response.output:
            log.append(o)

            if o.type == "message":
                print(o.content[0].text)
                skip_input = False

            elif o.type == "function_call":
                args = json.loads(o.arguments)
                if o.name == "math_operation":
                    skip_input = True
                    result = call_math_api(args["operation"], args["a"], args["b"])
                    log.append({
                        "type": "function_call_output",
                        "call_id": o.call_id,
                        "output": result
                    })
                    print(f"🧮 Math result: {result}")
                    continue
                else:
                    print(f"Unknown function: {o.name}")
                    skip_input = False

    print("End.")
