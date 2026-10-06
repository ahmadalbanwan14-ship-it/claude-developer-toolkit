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

## Install

```bash
git clone https://github.com/ahmadalbanwan14-ship-it/claude-developer-toolkit.git
cd claude-developer-toolkit
python -m venv .venv
pip install -e ".[dev]"
```

Set your API key:

```bash
# macOS/Linux
export ANTHROPIC_API_KEY="your-key"

# PowerShell
$env:ANTHROPIC_API_KEY="your-key"
```

## Examples

```bash
python examples/basic_chat.py
python examples/structured_json.py
python examples/tool_use.py
```

## Run tests

```bash
pytest
```

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
