import sys

from loguru import logger

LEVEL_ABBR = {
    "TRACE": "TRC",
    "DEBUG": "DBG",
    "INFO": "INF",
    "SUCCESS": "SUC",
    "WARNING": "WRN",
    "ERROR": "ERR",
    "CRITICAL": "CRT",
}


def stderr_format(record):
    """Return a compact format string for stderr logging.

    Injects a 3-letter level abbreviation into ``record["extra"]``
    and returns a format string that drops milliseconds and uses
    pipe separators throughout.
    """
    record["extra"]["abbr"] = LEVEL_ABBR.get(
        record["level"].name, record["level"].name[:3]
    )
    return (
        "{time:YYYY-MM-DD HH:mm:ss} | {extra[abbr]} | "
        "{name}:{function}:{line} | {message}\n{exception}"
    )


def configure_logging():
    """Configure loguru for console and file logging.

    Removes the default handler and sets up:
    - stderr handler at LOG_LEVEL (default: INFO) with compact format
    - File handler at DEBUG level writing to LOG_FILE (default: app.log)

    The stderr format uses 3-letter level abbreviations, no milliseconds,
    and pipe separators throughout.  The file handler keeps the default
    verbose loguru format.
    """
    import os

    log_level = os.environ.get("LOG_LEVEL", "INFO")
    log_file = os.environ.get("LOG_FILE", "app.log")
    logger.remove()
    logger.add(sys.stderr, level=log_level, format=stderr_format)
    logger.add(log_file, level="DEBUG", rotation="50 KB", retention=1)


@logger.catch
def main():
    """Run the application.

    Configures logging and prints a greeting to verify the setup works.
    """
    configure_logging()
    logger.info("Hello from second_brain!")
