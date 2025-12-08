"""
Utilitários gerais para testes de automação
"""

import os
from dotenv import load_dotenv


class EnvConfig:
    """Carrega e gerencia variáveis de ambiente"""

    def __init__(self):
        """Inicializa e carrega o arquivo .env"""
        load_dotenv()

    @staticmethod
    def get_base_url():
        """Retorna a URL base da aplicação"""
        return os.getenv("BASE_URL", "https://buger-eats.vercel.app/")

    @staticmethod
    def get_username():
        """Retorna o nome de usuário para testes"""
        return os.getenv("USERNAME", "")

    @staticmethod
    def get_password():
        """Retorna a senha para testes"""
        return os.getenv("PASSWORD", "")

    @staticmethod
    def get_api_key():
        """Retorna a chave de API se configurada"""
        return os.getenv("API_KEY", "")

    @staticmethod
    def is_headless():
        """Retorna se o navegador deve rodar em modo headless"""
        return os.getenv("HEADLESS", "false").lower() == "true"

    @staticmethod
    def get_timeout():
        """Retorna o timeout em segundos"""
        return int(os.getenv("TIMEOUT", "10"))
