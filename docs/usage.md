# Usage

## Installation

Clone the repository and install dependencies:

```bash
uv sync
```

## Running

Via the CLI entrypoint:

```bash
uv run second_brain                          # production defaults
uv run --env-file .env second_brain          # dev settings
```

Or as a Python module:

```bash
uv run python -m second_brain
```

## Environment Variables

| Variable    | Default    | Description                          |
|-------------|------------|--------------------------------------|
| `LOG_LEVEL` | `INFO`     | Console log level (DEBUG, INFO, …)   |
| `LOG_FILE`  | `app.log`  | Path to the log file                 |

Copy `.env.example` to `.env` for development defaults, then run with `uv run --env-file .env`.

## Logging

stderr uses a compact format with 3-letter level abbreviations, no milliseconds,
and pipe separators:

```
2026-04-05 20:52:59 | INF | second_brain.app:main:29 | Hello from second_brain!
```

| Full name  | Abbreviation |
|------------|-------------|
| TRACE      | TRC         |
| DEBUG      | DBG         |
| INFO       | INF         |
| SUCCESS    | SUC         |
| WARNING    | WRN         |
| ERROR      | ERR         |
| CRITICAL   | CRT         |

The file handler (`app.log`) keeps the default verbose loguru format with
milliseconds and full level names.
