import logging
import os

from colorama import Fore, Style, init
from dotenv import load_dotenv

init(autoreset=True)
load_dotenv()


class ColorFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: Fore.BLUE,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
    }

    def format(self, record) -> str:
        color = self.COLORS.get(record.levelno, Fore.WHITE)
        message = super().format(record)
        return f'{color}{message}{Style.RESET_ALL}'


class OkMessageFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        show_ok = os.getenv('SHOW_OK_LOGS', 'false').strip().lower()
        if show_ok in {'1', 'true', 'yes'}:
            return True
        message = record.getMessage()
        return not message.startswith('OK:')


def setup_logger(
    name: str = 'QA',
    level: int = logging.DEBUG,
    silence_external: bool = True,
) -> logging.Logger:
    if silence_external:
        logging.getLogger().setLevel(logging.WARNING)
        for noisy in ('faker', 'selenium', 'urllib3', 'behave', 'behavex'):
            logging.getLogger(noisy).setLevel(logging.WARNING)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    formatter = ColorFormatter('%(asctime)s - %(levelname)s - %(message)s')
    ok_filter = OkMessageFilter()

    if logger.handlers:
        for handler in logger.handlers:
            if isinstance(handler, logging.StreamHandler):
                handler.setFormatter(formatter)
                handler.setLevel(level)
                handler.terminator = '\n\n'
                if not any(
                    isinstance(existing, OkMessageFilter)
                    for existing in handler.filters
                ):
                    handler.addFilter(ok_filter)
        return logger

    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(formatter)
    handler.terminator = '\n\n'
    handler.addFilter(ok_filter)
    logger.addHandler(handler)

    return logger
