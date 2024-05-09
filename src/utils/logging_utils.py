import logging


def setup_logger(logger: logging.Logger) -> None:
    """
    1. Set the formatter (add more info to your logs)
    2. Set the handler (output)
    """
    formatter: logging.Formatter = logging.Formatter(
        "%(asctime)s - %(funcName)s - %(levelname)s - %(message)s"
    )
    handler: logging.FileHandler = logging.FileHandler("logs/logs.txt")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
