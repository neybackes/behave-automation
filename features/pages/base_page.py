"""
Página base para Page Object Model (POM)
Contém métodos comuns reutilizáveis
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    """Classe base para todas as páginas"""

    def __init__(self, driver):
        """
        Inicializa a página

        Args:
            driver (WebDriver): Instância do WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    def open(self, url):
        """
        Abre uma URL

        Args:
            url (str): URL a ser aberta
        """
        self.driver.get(url)
    

    def wait_page_load(self, timeout=10):
        """
        Aguarda a página carregar completamente

        Args:
            timeout (int): Tempo máximo de espera
        """
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def get_title(self):
        """
        Obtém o título da página

        Returns:
            str: Título da página
        """
        return self.driver.title
    
    def wait_element_visible(self, locator, timeout=10):
        """
        Aguarda um elemento ficar visível

        Args:
            locator (tuple): Tupla (By.*, valor) do localizador
            timeout (int): Tempo máximo de espera em segundos

        Returns:
            WebElement: Elemento encontrado
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    # def wait_element_clickable(self, locator, timeout=10):
    #     """
    #     Aguarda um elemento ficar clicável

    #     Args:
    #         locator (tuple): Tupla (By.*, valor) do localizador
    #         timeout (int): Tempo máximo de espera em segundos

    #     Returns:
    #         WebElement: Elemento encontrado
    #     """
    #     wait = WebDriverWait(self.driver, timeout)
    #     return wait.until(EC.element_to_be_clickable(locator))

    # def find_element(self, locator):
    #     """
    #     Encontra um elemento na página

    #     Args:
    #         locator (tuple): Tupla (By.*, valor) do localizador

    #     Returns:
    #         WebElement: Elemento encontrado
    #     """
    #     return self.driver.find_element(*locator)

    # def click(self, locator):
    #     """
    #     Clica em um elemento

    #     Args:
    #         locator (tuple): Tupla (By.*, valor) do localizador
    #     """
    #     element = self.wait_element_clickable(locator)
    #     element.click()

    # def fill_input(self, locator, text):
    #     """
    #     Preenche um campo de entrada

    #     Args:
    #         locator (tuple): Tupla (By.*, valor) do localizador
    #         text (str): Texto a ser digitado
    #     """
    #     element = self.wait_element_visible(locator)
    #     element.clear()
    #     element.send_keys(text)

    # def get_text(self, locator):
    #     """
    #     Obtém o texto de um elemento

    #     Args:
    #         locator (tuple): Tupla (By.*, valor) do localizador

    #     Returns:
    #         str: Texto do elemento
    #     """
    #     element = self.wait_element_visible(locator)
    #     return element.text

    # def is_element_visible(self, locator, timeout=5):
    #     """
    #     Verifica se um elemento está visível

    #     Args:
    #         locator (tuple): Tupla (By.*, valor) do localizador
    #         timeout (int): Tempo máximo de espera em segundos

    #     Returns:
    #         bool: True se visível, False caso contrário
    #     """
    #     try:
    #         WebDriverWait(self.driver, timeout).until(
    #             EC.visibility_of_element_located(locator)
    #         )
    #         return True
    #     except:
    #         return False
