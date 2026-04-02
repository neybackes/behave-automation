import logging

from colorama import Fore, Style, init

from automation.config.env_config import EnvConfig

init(autoreset=True)


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
    def __init__(self, show_ok_logs: bool) -> None:
        self.show_ok_logs = show_ok_logs

    def filter(self, record: logging.LogRecord) -> bool:
        if self.show_ok_logs:
            return True
        message = record.getMessage()
        return not message.startswith('OK:')


def setup_logger(
    name: str = 'QA',
    level: int = logging.DEBUG,
    silence_external: bool = True,
    show_ok_logs: bool = False,
) -> logging.Logger:
    if silence_external:
        logging.getLogger().setLevel(logging.WARNING)
        for noisy in ('faker', 'selenium', 'urllib3', 'behave', 'behavex'):
            logging.getLogger(noisy).setLevel(logging.WARNING)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    formatter = ColorFormatter('%(asctime)s - %(levelname)s - %(message)s')

    if logger.handlers:
        for handler in logger.handlers:
            if isinstance(handler, logging.StreamHandler):
                handler.setFormatter(formatter)
                handler.setLevel(level)
                handler.terminator = '\n\n'
                updated = False
                for existing in handler.filters:
                    if isinstance(existing, OkMessageFilter):
                        existing.show_ok_logs = show_ok_logs
                        updated = True
                if not updated:
                    handler.addFilter(OkMessageFilter(show_ok_logs))
        return logger

    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(formatter)
    handler.terminator = '\n\n'
    handler.addFilter(OkMessageFilter(show_ok_logs))
    logger.addHandler(handler)

    return logger


def get_logger(name: str = 'QA') -> logging.Logger:
    return logging.getLogger(name)


def setup_logger_from_env(name: str = 'QA') -> logging.Logger:
    env = EnvConfig()
    return setup_logger(
        name=name,
        level=env.get_log_level(),
        silence_external=env.silence_external_logs(),
        show_ok_logs=env.show_ok_logs(),
    )
