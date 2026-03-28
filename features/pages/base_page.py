import time

import requests
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

fake = Faker('pt_BR')


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url: str) -> None:
        self.driver.get(url)
        print(f'✓ Acessando a página: {url}')

    def wait_page_load(self, timeout: int = 10) -> None:
        WebDriverWait(self.driver, timeout).until(
            lambda driver: (
                driver.execute_script('return document.readyState')
                == 'complete'
            )
        )
        print('✓ Página carregada')

    def get_title(self, expected_title: str) -> None:
        actual_title = self.driver.title
        if expected_title and expected_title != actual_title:
            raise AssertionError(
                f"Título esperado '{expected_title}' não corresponde ao "
                f"título atual '{actual_title}'"
            )
        print(f'✓ Título validado: {actual_title}')

    def wait_element_visible(
        self, locator_tuple: tuple, timeout: int = 10
    ) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        print(
            f'✓ Aguardando elemento visível: {locator_tuple} '
            f'(timeout: {timeout}s)'
        )
        locator = wait.until(EC.visibility_of_element_located(locator_tuple))
        print(f'✓ Elemento visível: {locator}')
        return locator

    # Metodo para elementos ocultos ou que demoram a aparecer,
    # como o input de upload de arquivo
    def wait_element_present(
        self, locator_tuple: tuple, timeout: int = 10
    ) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        print(
            f'✓ Aguardando elemento presente: {locator_tuple} '
            f'(timeout: {timeout}s)'
        )
        element = wait.until(EC.presence_of_element_located(locator_tuple))
        print(f'✓ Elemento presente: {element}')
        return element

    def get_text(
        self, selector: str, locator: str, expected_text: str
    ) -> None:
        element = self.wait_element_visible((selector, locator))
        actual_text = element.text
        assert expected_text in actual_text, (
            f"Texto esperado '{expected_text}' não encontrado. "
            f"Texto atual: '{actual_text}'"
        )
        print(f'✓ Texto validado: {actual_text}')

    @staticmethod
    def validate_multiples_text(tabela, elementos) -> None:
        assert tabela is not None, 'Tabela de validação não fornecida'
        mensagens = [element.text.strip() for element in elementos]
        print(f'✓ Encontrados {len(elementos)} elementos página.')
        print(f'Textos: {mensagens}')

        for row in tabela:
            campo = row['campo']
            mensagem_esperada = row['mensagem']

            assert mensagem_esperada in mensagens, (
                f'Texto esperado para "{campo}" não encontrada.\n'
                f'Esperado: {mensagem_esperada}\n'
                f'Encontrado: {mensagens}'
            )

    def find_element(self, selector: str, locator: str) -> WebElement:
        element = self.wait_element_visible((selector, locator))
        print(f'✓ Elemento encontrado: {locator}')
        return element

    def click(self, locator_tuple: tuple) -> None:
        element = self.wait_element_visible(locator_tuple)
        element.click()
        print(f'✓ Elemento clicado: {locator_tuple}')

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
        print(f'✓ Tempo de carregamento: {load_time:.2f}s')

    def check_resources_loaded(self) -> None:
        resources = self.driver.execute_script(
            "return window.performance.getEntriesByType('resource');"
        )
        HTTP_ERROR = 400
        failed_resources = [
            res for res in resources if res.get('status', 200) >= HTTP_ERROR
        ]
        assert not failed_resources, (
            f'Recursos com falha de carregamento: {failed_resources}'
        )
        print('✓ Todos os recursos carregados corretamente')

    @staticmethod
    def get_valid_cep(cep: str) -> dict:
        while True:
            response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            data = response.json()
            if 'erro' not in data:
                return data

    def validate_address(self, cep: str) -> None:
        time.sleep(3)  # Aguarda o preenchimento automático
        rua = self.find_element(By.NAME, 'address').get_attribute('value')
        bairro = self.find_element(By.NAME, 'district').get_attribute('value')
        cidade_uf = self.find_element(By.NAME, 'city-uf').get_attribute(
            'value'
        )
        endereco = self.get_valid_cep(cep)
        print(
            f'Endereço no formulário: {rua}, {bairro}, {cidade_uf} '
            f'com CEP: {cep}'
        )
        assert rua == endereco['logradouro']
        assert bairro == endereco['bairro']
        assert cidade_uf == f'{endereco["localidade"]}/{endereco["uf"]}'
        print('✓ Endereço validado com sucesso')

    def fill_basic_data_input(self, table) -> str:
        if table is None:
            raise ValueError(
                'A tabela de dados pessoais está ausente no cenário.'
            )
        dados = {row['campo']: row['valor'] for row in table}
        campos = {
            'Nome completo': (By.NAME, 'name'),
            'CPF': (By.NAME, 'cpf'),
            'E-mail': (By.NAME, 'email'),
            'Whatsapp': (By.NAME, 'whatsapp'),
            'CEP': (By.NAME, 'postalcode'),
        }
        cep = '04823-050'
        for campo, valor in dados.items():
            # Gera valor random se placeholder
            if valor == '<random>':
                if campo == 'Nome completo':
                    send_value = fake.name()
                elif campo == 'CPF':
                    send_value = fake.cpf().replace('.', '').replace('-', '')
                elif campo == 'E-mail':
                    send_value = fake.email()
                elif campo == 'Whatsapp':
                    send_value = fake.msisdn()
                elif campo == 'CEP':
                    send_value = cep
            if campo in campos:
                self.find_element(*campos[campo]).send_keys(send_value)
        # Retorna o CEP e os dados do endereço
        # (logradouro, bairro, cidade, etc)
        return cep
        # Retorna o CEP e os dados do endereço
        # (logradouro, bairro, cidade, etc)
