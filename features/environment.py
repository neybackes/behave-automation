import sys
from pathlib import Path

import behave.model
import behave.runner

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / 'src'
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from automation.config.env_config import EnvConfig 

from automation.core.driver_manager import DriverManager

from automation.utils.logger import setup_logger

logger = setup_logger()


def before_all(context: behave.runner.Context) -> None:
    logger.debug('=== Iniciando testes de automacao ===')


def before_scenario(
    context: behave.runner.Context, scenario: behave.model.Scenario
) -> None:
    logger.debug(f'Executando: {scenario.name}')

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
        logger.error(f'Scenario FALHOU: {scenario.name}')
    else:
        logger.info(f'Scenario PASSOU: {scenario.name}')

    if hasattr(context, 'driver'):
        DriverManager.close_driver(context.driver)


def after_all(context: behave.runner.Context) -> None:
    logger.debug('=== Testes finalizados ===')
