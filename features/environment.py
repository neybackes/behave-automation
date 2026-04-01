
import sys
from pathlib import Path

import behave.model
import behave.runner

from automation.config.env_config import EnvConfig  
from automation.core.driver_manager import DriverManager  

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / 'src'
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))


def before_all(context: behave.runner.Context) -> None:
    print('\n=== Iniciando testes de automacao ===\n')


def before_scenario(
    context: behave.runner.Context, scenario: behave.model.Scenario
) -> None:
    print(f'\nExecutando: {scenario.name}')

    env = EnvConfig()
    context.base_url = env.get_base_url()
    context.driver = DriverManager.create_chrome_driver(
        headless=env.is_headless(),
        implicit_wait=env.get_timeout(),
    )


def after_scenario(
    context: behave.runner.Context, scenario: behave.model.Scenario
) -> None:
    if scenario.status == 'failed':
        print(f'\nScenario FALHOU: {scenario.name}')
    else:
        print(f'\nScenario PASSOU: {scenario.name}')

    if hasattr(context, 'driver'):
        DriverManager.close_driver(context.driver)


def after_all(context: behave.runner.Context) -> None:
    print('\n=== Testes finalizados ===\n')
