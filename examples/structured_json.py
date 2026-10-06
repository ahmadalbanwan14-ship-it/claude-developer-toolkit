import json
import os

from anthropic import Anthropic

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
model = os.environ["ANTHROPIC_MODEL"]

prompt = """Return ONLY valid JSON with this exact shape:
{"summary": "string", "difficulty": "easy|medium|hard"}

Topic: dependency injection
"""

message = client.messages.create(
    model=model,
    max_tokens=250,
    messages=[{"role": "user", "content": prompt}],
)

raw = message.content[0].text
data = json.loads(raw)
print(json.dumps(data, indent=2))
