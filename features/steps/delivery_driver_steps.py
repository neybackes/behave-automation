from pathlib import Path

import behave
import behave.runner
from selenium.webdriver.common.by import By


@behave.when('preencho os dados pessoais:')
def step_preencho_dados_pessoais(context: behave.runner.Context) -> None:
    context.endereco_cep = context.page.fill_basic_data_input(context.table)


@behave.when('clico em "Buscar CEP"')
def step_clico_buscar_cep(context: behave.runner.Context) -> None:
    locator_tuple = (By.XPATH, "//*[@value='Buscar CEP']")
    context.page.click(locator_tuple)


@behave.when('aguardo o preenchimento automático do endereço')
def step_aguardo_preenchimento_automatico(
    context: behave.runner.Context,
) -> None:
    context.page.validate_address(context.endereco_cep)


@behave.when('preencho o número "500"')
def step_preencho_numero(context: behave.runner.Context) -> None:
    context.page.find_element(By.NAME, 'address-number').send_keys('500')


@behave.when('preencho o complemento "Apto 101"')
def step_preencho_complemento(context: behave.runner.Context) -> None:
    context.page.find_element(By.NAME, 'address-details').send_keys('Apto 101')


@behave.when('seleciono o método de entrega "Moto"')
def step_seleciono_metodo_entrega_moto(context: behave.runner.Context) -> None:
    locator_tuple = (By.XPATH, "//*[@alt='Moto']")
    context.page.click(locator_tuple)


@behave.when('seleciono o método de entrega "Bicicleta"')
def step_seleciono_metodo_entrega_bicicleta(
    context: behave.runner.Context,
) -> None:
    locator_tuple = (By.XPATH, "//*[@alt='Bicicleta']")
    context.page.click(locator_tuple)


@behave.when('seleciono o método de entrega "Van/Carro"')
def step_seleciono_metodo_entrega_van_carro(
    context: behave.runner.Context,
) -> None:
    locator_tuple = (By.XPATH, "//*[@alt='Van/Carro']")
    context.page.click(locator_tuple)


@behave.when('faço upload da foto da CNH')
def step_faco_upload_cnh(context: behave.runner.Context) -> None:
    # Caminho relativo ao diretório raiz do projeto
    project_root = Path(__file__).resolve().parents[2]
    cnh_path = project_root / 'resources' / 'assets' / 'cnh_model.png'
    assert cnh_path.exists(), f'Arquivo não encontrado: {cnh_path}'
    input_file = context.page.wait_element_present(
        (By.XPATH, "//input[@type='file']"), timeout=10
    )
    input_file.send_keys(str(cnh_path))


@behave.when('clico em "Cadastre-se para fazer entregas" no formulário')
def step_clico_cadastrar_formulario(context: behave.runner.Context) -> None:
    locator_tuple = (By.CLASS_NAME, 'button-success')
    context.page.click(locator_tuple)


@behave.when(
    'clico em "Cadastre-se para fazer entregas" sem preencher nenhum campo'
)
def step_clico_cadastrar_sem_preencher(context: behave.runner.Context) -> None:
    locator_tuple = (By.CLASS_NAME, 'button-success')
    context.page.click(locator_tuple)


@behave.when('preencho o CPF com "{cpf_invalido}"')
def step_preencho_cpf_alfanumerico(
    context: behave.runner.Context, cpf_invalido: str
) -> None:
    campo = context.page.find_element(By.NAME, 'cpf')
    campo.clear()
    campo.send_keys(cpf_invalido)


@behave.then('devo ver a mensagem de sucesso')
def step_ver_mensagem_sucesso(context: behave.runner.Context) -> None:
    context.page.wait_element_present(
        (By.XPATH, "//*[@role='dialog']"), timeout=10
    )
    context.page.get_text(By.ID, 'swal2-title', 'Aí Sim...')
    context.page.get_text(
        By.ID,
        'swal2-html-container',
        (
            'Recebemos os seus dados. Fique de olho na sua caixa de email, '
            'pois e em breve retornamos o contato.'
        ),
    )


@behave.then('devo ver mensagens de erro nos campos obrigatórios')
def step_ver_mensagens_erro(context: behave.runner.Context) -> None:
    elementos = context.page.driver.find_elements(By.CLASS_NAME, 'alert-error')
    context.page.validate_multiples_text(context.table, elementos)


@behave.then(
    (
        'quando clicar em "OK" na mensagem de sucesso, '
        'devo ser redirecionado para a pagina inicial'
    )
)
def step_clicar_ok_redirecionar_inicial(
    context: behave.runner.Context,
) -> None:
    locator_tuple = (By.XPATH, "//*[@class='swal2-confirm swal2-styled']")
    context.page.click(locator_tuple)
    context.page.wait_page_load()
    expected_title = 'Buger Eats'
    context.page.get_title(expected_title)
    expected_text = 'Seja um parceiro entregador pela Buger Eats'
    context.page.get_text('tag name', 'h1', expected_text)
    expected_text = (
        'Em vez de oportunidades tradicionais de entrega de refeições em '
        'horários pouco flexíveis, seja seu próprio chefe.'
    )
    context.page.get_text('tag name', 'p', expected_text)


@behave.then('devo ver a mensagem "Oops! CPF inválido"')
def step_ver_mensagem_cpf_invalido(context: behave.runner.Context) -> None:
    context.page.wait_element_present(
        (By.CLASS_NAME, 'alert-error'), timeout=20
    )
    context.page.get_text(
        By.XPATH,
        "//*[@id='page-deliver']/form/fieldset[1]/div[1]/div[2]/span",
        'Oops! CPF inválido',
    )
