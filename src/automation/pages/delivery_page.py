from pathlib import Path

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from automation.pages.base_page import BasePage
from automation.services.cep_service import CepService
from automation.utils.logger import get_logger

fake = Faker('pt_BR')
logger = get_logger()


class DeliveryPage(BasePage):
    FORM = (By.XPATH, '//*[@id="page-deliver"]/form')
    BUSCAR_CEP = (By.XPATH, "//*[@value='Buscar CEP']")
    INPUT_ADDRESS = (By.NAME, 'address')
    INPUT_DISTRICT = (By.NAME, 'district')
    INPUT_CITY_UF = (By.NAME, 'city-uf')
    INPUT_ADDRESS_NUMBER = (By.NAME, 'address-number')
    INPUT_ADDRESS_DETAILS = (By.NAME, 'address-details')
    INPUT_CPF = (By.NAME, 'cpf')
    INPUT_FILE = (By.XPATH, "//input[@type='file']")
    BTN_SUBMIT = (By.CLASS_NAME, 'button-success')
    DIALOG = (By.XPATH, "//*[@role='dialog']")
    DIALOG_TITLE = (By.ID, 'swal2-title')
    DIALOG_TEXT = (By.ID, 'swal2-html-container')
    ALERT_ERROR = (By.CLASS_NAME, 'alert-error')
    BTN_OK = (By.XPATH, "//*[@class='swal2-confirm swal2-styled']")
    CPF_INVALIDO = (
        By.XPATH,
        "//*[@id='page-deliver']/form/fieldset[1]/div[1]/div[2]/span",
    )
    LINK_HOME = (By.XPATH, "//a[contains(text(), 'Voltar para home')]")

    @property
    def path(self) -> str:
        return '/deliver'

    def assert_form_visible(self) -> None:
        self.wait_element_visible(self.FORM)

    def click_buscar_cep(self) -> None:
        self.click(self.BUSCAR_CEP)

    def validate_address(self, cep: str) -> None:
        address = CepService.get_valid_cep(cep)
        expected_street = address['logradouro']
        expected_district = address['bairro']
        expected_city_uf = f'{address["localidade"]}/{address["uf"]}'

        def fields_filled(driver) -> bool:
            street = driver.find_element(*self.INPUT_ADDRESS).get_attribute(
                'value'
            )
            district = driver.find_element(*self.INPUT_DISTRICT).get_attribute(
                'value'
            )
            city_uf = driver.find_element(*self.INPUT_CITY_UF).get_attribute(
                'value'
            )
            return (
                street == expected_street
                and district == expected_district
                and city_uf == expected_city_uf
            )

        WebDriverWait(self.driver, 10).until(fields_filled)
        logger.debug(
            f'Address in form: {expected_street}, '
            f'{expected_district}, {expected_city_uf} with CEP: {cep}'
        )
        logger.info('OK: address validated successfully')

    def fill_basic_data_input(self, table) -> str:
        if table is None:
            raise ValueError('Personal data table is missing.')

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

    def preencher_numero_endereco(self, numero: str) -> None:
        self.find_element(*self.INPUT_ADDRESS_NUMBER).send_keys(numero)

    def preencher_complemento(self, complemento: str) -> None:
        self.find_element(*self.INPUT_ADDRESS_DETAILS).send_keys(complemento)

    def selecionar_metodo_entrega(self, metodo: str) -> None:
        locator_tuple = (By.XPATH, f"//*[@alt='{metodo}']")
        self.click(locator_tuple)

    def upload_cnh(self) -> None:
        project_root = Path(__file__).resolve().parents[3]
        cnh_path = project_root / 'resources' / 'assets' / 'cnh_model.png'
        assert cnh_path.exists(), f'File not found: {cnh_path}'
        input_file = self.wait_element_present(self.INPUT_FILE, timeout=10)
        input_file.send_keys(str(cnh_path))

    def submit_form(self) -> None:
        self.click(self.BTN_SUBMIT)

    def preencher_cpf(self, cpf: str) -> None:
        campo = self.find_element(*self.INPUT_CPF)
        campo.clear()
        campo.send_keys(cpf)

    def assert_mensagem_sucesso(
        self, expected_title: str, expected_text: str
    ) -> None:
        self.wait_element_present(self.DIALOG, timeout=10)
        self.get_text(
            self.DIALOG_TITLE[0],
            self.DIALOG_TITLE[1],
            expected_title,
        )
        self.get_text(
            self.DIALOG_TEXT[0],
            self.DIALOG_TEXT[1],
            expected_text,
        )

    def validar_mensagens_erro(self, table) -> None:
        elementos = self.driver.find_elements(*self.ALERT_ERROR)
        self.validate_multiples_text(table, elementos)

    def confirmar_sucesso(self) -> None:
        self.click(self.BTN_OK)
        self.wait_page_load()

    def assert_cpf_invalido(self, expected_text: str) -> None:
        self.wait_element_present(self.ALERT_ERROR, timeout=20)
        self.get_text(
            self.CPF_INVALIDO[0],
            self.CPF_INVALIDO[1],
            expected_text,
        )

    def voltar_home(self, expected_text: str) -> None:
        self.get_text(By.TAG_NAME, 'a', expected_text)
        self.click(self.LINK_HOME)
