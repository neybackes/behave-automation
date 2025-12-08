"""
Environment setup para Behave
Configura driver, contexto e hooks
"""

from support.drivers.driver_manager import DriverManager
from support.utils.env_config import EnvConfig


def before_all(context):
    """Executa antes de todos os cenários"""
    print("\n=== Iniciando Testes de Automação ===\n")


def before_scenario(context, scenario):
    """Executa antes de cada cenário"""
    print(f"\nExecutando: {scenario.name}")

    # Carrega configurações de ambiente
    env = EnvConfig()
    context.base_url = env.get_base_url()
    context.username = env.get_username()
    context.password = env.get_password()

    # Cria instância do driver
    context.driver = DriverManager.create_chrome_driver(
        headless=env.is_headless(), implicit_wait=env.get_timeout()
    )


def after_scenario(context, scenario):
    """Executa depois de cada cenário"""
    if scenario.status == "failed":
        print(f"\n❌ Cenário FALHOU: {scenario.name}")
        # Aqui você pode capturar screenshots se necessário
    else:
        print(f"\n✅ Cenário PASSOU: {scenario.name}")

    # Fecha o driver
    if hasattr(context, "driver"):
        DriverManager.close_driver(context.driver)


def after_all(context):
    """Executa depois de todos os cenários"""
    print("\n=== Testes Finalizados ===\n")
