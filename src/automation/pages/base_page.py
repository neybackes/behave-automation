import time
from typing import Any

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from automation.services.cep_service import CepService

fake = Faker('pt_BR')
Locator = tuple[Any, str]


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url: str) -> None:
        self.driver.get(url)
        print(f'OK: acessando a pagina: {url}')

    def wait_page_load(self, timeout: int = 10) -> None:
        WebDriverWait(self.driver, timeout).until(
            lambda driver: (
                driver.execute_script('return document.readyState')
                == 'complete'
            )
        )
        print('OK: pagina carregada')

    def get_title(self, expected_title: str) -> None:
        actual_title = self.driver.title
        if expected_title and expected_title != actual_title:
            raise AssertionError(
                f"Titulo esperado '{expected_title}' nao corresponde ao "
                f"titulo atual '{actual_title}'"
            )
        print(f'OK: titulo validado: {actual_title}')

    def wait_element_visible(
        self, locator_tuple: Locator, timeout: int = 10
    ) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        print(
            f'OK: aguardando elemento visivel: {locator_tuple} '
            f'(timeout: {timeout}s)'
        )
        locator = wait.until(ec.visibility_of_element_located(locator_tuple))
        print(f'OK: elemento visivel: {locator}')
        return locator

    # Useful for hidden or late elements, such as file upload inputs.
    def wait_element_present(
        self, locator_tuple: Locator, timeout: int = 10
    ) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        print(
            f'OK: aguardando elemento presente: {locator_tuple} '
            f'(timeout: {timeout}s)'
        )
        element = wait.until(ec.presence_of_element_located(locator_tuple))
        print(f'OK: elemento presente: {element}')
        return element

    def get_text(
        self, selector: Any, locator: str, expected_text: str
    ) -> None:
        element = self.wait_element_visible((selector, locator))
        actual_text = element.text
        assert expected_text in actual_text, (
            f"Texto esperado '{expected_text}' nao encontrado. "
            f"Texto atual: '{actual_text}'"
        )
        print(f'OK: texto validado: {actual_text}')

    @staticmethod
    def validate_multiples_text(table, elements) -> None:
        assert table is not None, 'Tabela de validacao nao fornecida'
        messages = [element.text.strip() for element in elements]
        print(f'OK: encontrados {len(elements)} elementos na pagina.')
        print(f'Textos encontrados: {messages}')

        for row in table:
            field = row['campo']
            expected_message = row['mensagem']
            assert expected_message in messages, (
                f'Texto esperado para "{field}" nao encontrado.\n'
                f'Esperado: {expected_message}\n'
                f'Encontrado: {messages}'
            )

    def find_element(self, selector: Any, locator: str) -> WebElement:
        element = self.wait_element_visible((selector, locator))
        print(f'OK: elemento encontrado: {locator}')
        return element

    def click(self, locator_tuple: Locator) -> None:
        element = self.wait_element_visible(locator_tuple)
        element.click()
        print(f'OK: elemento clicado: {locator_tuple}')

    def check_load_time(self, max_time: int = 3) -> None:
        start_time = self.driver.execute_script(
            'return performance.timing.navigationStart'
        )
        load_time = (
            self.driver.execute_script(
                'return performance.timing.loadEventEnd'
            )
            - start_time
        ) / 1000
        assert load_time <= max_time, (
            f'Tempo de carregamento {load_time:.2f}s excede o limite de '
            f'{max_time}s'
        )
        print(f'OK: tempo de carregamento: {load_time:.2f}s')

    def check_resources_loaded(self) -> None:
        resources = self.driver.execute_script(
            "return window.performance.getEntriesByType('resource');"
        )
        http_error = 400
        failed_resources = [
            resource
            for resource in resources
            if resource.get('status', 200) >= http_error
        ]
        assert not failed_resources, (
            f'Recursos com falha de carregamento: {failed_resources}'
        )
        print('OK: todos os recursos carregados corretamente')

    def validate_address(self, cep: str) -> None:
        time.sleep(3)
        street = self.find_element(By.NAME, 'address').get_attribute('value')
        district = self.find_element(By.NAME, 'district').get_attribute(
            'value'
        )
        city_uf = self.find_element(By.NAME, 'city-uf').get_attribute('value')

        address = CepService.get_valid_cep(cep)
        print(
            f'Endereco no formulario: {street}, {district}, {city_uf} '
            f'com CEP: {cep}'
        )

        assert street == address['logradouro']
        assert district == address['bairro']
        assert city_uf == f'{address["localidade"]}/{address["uf"]}'
        print('OK: endereco validado com sucesso')

    def fill_basic_data_input(self, table) -> str:
        if table is None:
            raise ValueError('A tabela de dados pessoais esta ausente.')

        data = {row['campo']: row['valor'] for row in table}
        fields = {
            'Nome completo': (By.NAME, 'name'),
            'CPF': (By.NAME, 'cpf'),
            'E-mail': (By.NAME, 'email'),
            'Whatsapp': (By.NAME, 'whatsapp'),
            'CEP': (By.NAME, 'postalcode'),
        }

        cep = '04823-050'
        for field, value in data.items():
            send_value = value
            if value == '<random>':
                if field == 'Nome completo':
                    send_value = fake.name()
                elif field == 'CPF':
                    send_value = fake.cpf().replace('.', '').replace('-', '')
                elif field == 'E-mail':
                    send_value = fake.email()
                elif field == 'Whatsapp':
                    send_value = fake.msisdn()
                elif field == 'CEP':
                    send_value = cep

            if field in fields:
                self.find_element(*fields[field]).send_keys(send_value)

        return cep
