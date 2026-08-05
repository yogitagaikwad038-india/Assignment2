import logging


def get_logger():

    logger = logging.getLogger(
        "RumorBuster"
    )

    logger.setLevel(logging.INFO)

    console = logging.StreamHandler()

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s %(message)s",
        "%m/%d/%y %H:%M:%S"
    )

    console.setFormatter(
        formatter
    )

    if not logger.handlers:
        logger.addHandler(
            console
        )

    return logger