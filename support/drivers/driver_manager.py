"""
Configuração do WebDriver para Selenium
Gerencia a criação e fechamento do navegador
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os


class DriverManager:
    """Gerencia instâncias do WebDriver"""

    @staticmethod
    def create_chrome_driver(headless=False, implicit_wait=10):
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

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(implicit_wait)
        driver.maximize_window()

        return driver

    @staticmethod
    def close_driver(driver):
        """
        Fecha a instância do WebDriver

        Args:
            driver (WebDriver): Instância a ser fechada
        """
        if driver:
            driver.quit()
