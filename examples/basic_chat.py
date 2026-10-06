import os

from anthropic import Anthropic

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
model = os.environ["ANTHROPIC_MODEL"]

message = client.messages.create(
    model=model,
    max_tokens=300,
    messages=[
        {"role": "user", "content": "Explain recursion in one short paragraph."}
    ],
)

print(message.content[0].text)
