"""
Environment setup para Behave
Configura driver, contexto e hooks
"""

from support.drivers.driver_manager import DriverManager
from support.utils.env_config import EnvConfig
import behave.runner #type: ignore
import behave.model #type: ignore

def before_all(context: behave.runner.Context) -> None:
    print("\n=== Iniciando Testes de Automação ===\n")


def before_scenario(context: behave.runner.Context, scenario: behave.model.Scenario) -> None:
    print(f"\nExecutando: {scenario.name}")

    # Carrega configurações de ambiente
    env = EnvConfig()
    context.base_url = env.get_base_url()
   

    # Cria instância do driver com opções para suprimir logs
    context.driver = DriverManager.create_chrome_driver(
        headless=env.is_headless(), implicit_wait=env.get_timeout()
    )


def after_scenario(context: behave.runner.Context, scenario: behave.model.Scenario) -> None:
    if scenario.status == "failed":
        print(f"\n❌ Cenário FALHOU: {scenario.name}")
       
    else:
        print(f"\n✅ Cenário PASSOU: {scenario.name}")
   
    if hasattr(context, "driver"):
        DriverManager.close_driver(context.driver)


def after_all(context: behave.runner.Context) -> None:
    
    print("\n=== Testes Finalizados ===\n")
