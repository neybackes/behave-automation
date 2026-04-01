import os

from dotenv import load_dotenv


class EnvConfig:
    def __init__(self) -> None:
        load_dotenv()

    @staticmethod
    def is_headless() -> bool:
        return os.getenv('HEADLESS', 'false').lower() == 'true'

    @staticmethod
    def get_timeout() -> int:
        return int(os.getenv('TIMEOUT', '10'))

    @staticmethod
    def get_base_url() -> str | None:
        return os.getenv('BASE_URL')
