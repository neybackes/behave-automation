"""
Configuração do WebDriver para Selenium
Gerencia a criação e fechamento do navegador
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options



class DriverManager:
    """Gerencia instâncias do WebDriver"""

    @staticmethod
    def create_chrome_driver(headless: bool = False, implicit_wait: int = 10) -> webdriver.Chrome:
        """
        Cria uma instância do Chrome WebDriver

        Args:
            headless (bool): Se True, executa sem interface gráfica
            implicit_wait (int): Tempo de espera implícita em segundos

        Returns:
            WebDriver: Instância configurada do WebDriver
        """
        options = Options()

        if headless:
            options.add_argument("--headless")

        # Opções para suprimir logs e warnings
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--log-level=3")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(implicit_wait)
        driver.maximize_window()

        return driver

    @staticmethod
    def close_driver(driver: webdriver.Chrome) -> None:
        """
        Fecha a instância do WebDriver

        Args:
            driver (WebDriver): Instância a ser fechada
        """
        if driver:
            driver.quit()
