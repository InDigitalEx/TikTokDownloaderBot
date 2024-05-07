import asyncio
import logging
from pathlib import Path

from sqlalchemy import log as sqlalchemy_log

from app import run_bot
from data import config
from utils import get_root_dir


def init_logger() -> None:
    # Patch to avoid duplicate sqlalchemy logging
    sqlalchemy_log._add_default_handler = lambda x: None

    # Create /logs dir if not exist
    log_dir = get_root_dir() + '/logs'
    Path(log_dir).mkdir(parents=True, exist_ok=True)

    # Init Logger
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')

    # Write logs to file (logs.log)
    file_handler = logging.FileHandler(log_dir + '/logs.log', 'a')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Write logs to console out
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.setLevel(logging.DEBUG if config.debug else logging.INFO)


def main() -> None:
    init_logger()
    asyncio.run(run_bot())


if __name__ == "__main__":
    main()
