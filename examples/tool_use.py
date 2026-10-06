import os

from anthropic import Anthropic

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
model = os.environ["ANTHROPIC_MODEL"]

tools = [
    {
        "name": "get_temperature",
        "description": "Get a demo temperature for a city.",
        "input_schema": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    }
]

response = client.messages.create(
    model=model,
    max_tokens=300,
    tools=tools,
    messages=[
        {"role": "user", "content": "What is the temperature in Kuwait City?"}
    ],
)

for block in response.content:
    if block.type == "tool_use":
        city = block.input["city"]
        demo_result = {"Kuwait City": "31 C", "London": "16 C"}.get(city, "Unknown")
        print(f"{block.name}({city!r}) -> {demo_result}")
