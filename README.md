# Claude Developer Toolkit

A small, practical open-source toolkit for developers building with the Claude API.

> This is an independent community project and is not affiliated with or endorsed by Anthropic.

## What is included

- Minimal Python Claude API example
- Structured JSON output example
- Tool-use example with a local function
- Reusable retry helper for transient failures
- Basic tests
- GitHub Actions CI
- Contribution guide

## Requirements

- Python 3.10+
- An Anthropic API key
- A Claude model ID available to your Anthropic account

## Install

```bash
git clone https://github.com/ahmadalbanwan14-ship-it/claude-developer-toolkit.git
cd claude-developer-toolkit
python -m venv .venv
pip install -e ".[dev]"
```

Set your environment variables:

```bash
# macOS/Linux
export ANTHROPIC_API_KEY="your-key"
export ANTHROPIC_MODEL="your-model-id"

# PowerShell
$env:ANTHROPIC_API_KEY="your-key"
$env:ANTHROPIC_MODEL="your-model-id"
```

Keeping the model configurable avoids hard-coding a model name that may later become outdated.

## Examples

```bash
python examples/basic_chat.py
python examples/structured_json.py
python examples/tool_use.py
```

The tool-use example intentionally uses a tiny local demo function so it can show the tool-call pattern without depending on another web service.

## Retry helper

```python
from claude_toolkit import retry

@retry(max_attempts=4, base_delay=0.5)
def do_work():
    ...
```

## Run tests

```bash
pytest
```

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
