import logging
import os

from dotenv import load_dotenv

load_dotenv()


class EnvConfig:
    @staticmethod
    def is_headless() -> bool:
        return os.getenv('HEADLESS', 'false').lower() == 'true'

    @staticmethod
    def get_timeout() -> int:
        return int(os.getenv('TIMEOUT', '10'))

    @staticmethod
    def get_base_url() -> str | None:
        return os.getenv('BASE_URL')

    @staticmethod
    def get_log_level() -> int:
        value = os.getenv('LOG_LEVEL', 'DEBUG').strip().upper()
        if value.isdigit():
            return int(value)
        return getattr(logging, value, logging.DEBUG)

    @staticmethod
    def show_ok_logs() -> bool:
        return os.getenv('SHOW_OK_LOGS', 'false').lower() == 'true'

    @staticmethod
    def silence_external_logs() -> bool:
        return os.getenv('SILENCE_EXTERNAL', 'true').lower() == 'true'
