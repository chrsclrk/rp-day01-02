# second-brain

## Installation

Clone the repository and install dependencies:

```bash
git clone <repo-url>
cd second-brain
uv sync
```

## Usage

Via the CLI entrypoint:

```bash
uv run second_brain                          # production defaults
uv run --env-file .env second_brain          # dev settings
```

Via Python module:

```bash
uv run python -m second_brain
```

## Environment Variables

`.env.example` is the template — copy it to `.env` for development:

```bash
cp .env.example .env
```

| Variable    | Default    | Description                                      |
|-------------|------------|--------------------------------------------------|
| `LOG_LEVEL` | `INFO`     | Console log level (set to DEBUG in `.env` for verbose output) |
| `LOG_FILE`  | `app.log`  | Path to the log file                             |

Run with `uv run --env-file .env second_brain` to load dev environment (no auto-loading).

## Testing

Run tests:

```bash
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov
```

## Documentation

Preview docs locally:

```bash
uv run python scripts/serve_docs.py
```

Build static docs:

```bash
uv run mkdocs build
```
