import behave
import behave.runner

from automation.pages.home_page import HomePage


@behave.when('preencho os dados pessoais:')
def step_preencho_dados_pessoais(context: behave.runner.Context) -> None:
    context.endereco_cep = context.page.fill_basic_data_input(context.table)


@behave.when('clico em "Buscar CEP"')
def step_clico_buscar_cep(context: behave.runner.Context) -> None:
    context.page.click_buscar_cep()


@behave.when('aguardo o preenchimento automático do endereço')
def step_aguardo_preenchimento_automatico(
    context: behave.runner.Context,
) -> None:
    context.page.validate_address(context.endereco_cep)


@behave.when('preencho o número "500"')
def step_preencho_numero(context: behave.runner.Context) -> None:
    context.page.preencher_numero_endereco('500')


@behave.when('preencho o complemento "Apto 101"')
def step_preencho_complemento(context: behave.runner.Context) -> None:
    context.page.preencher_complemento('Apto 101')


@behave.when('seleciono o método de entrega "Moto"')
def step_seleciono_metodo_entrega_moto(context: behave.runner.Context) -> None:
    context.page.selecionar_metodo_entrega('Moto')


@behave.when('seleciono o método de entrega "Bicicleta"')
def step_seleciono_metodo_entrega_bicicleta(
    context: behave.runner.Context,
) -> None:
    context.page.selecionar_metodo_entrega('Bicicleta')


@behave.when('seleciono o método de entrega "Van/Carro"')
def step_seleciono_metodo_entrega_van_carro(
    context: behave.runner.Context,
) -> None:
    context.page.selecionar_metodo_entrega('Van/Carro')


@behave.when('faço upload da foto da CNH')
def step_faco_upload_cnh(context: behave.runner.Context) -> None:
    context.page.upload_cnh()


@behave.when('clico em "Cadastre-se para fazer entregas" no formulário')
def step_clico_cadastrar_formulario(context: behave.runner.Context) -> None:
    context.page.submit_form()


@behave.when(
    'clico em "Cadastre-se para fazer entregas" sem preencher nenhum campo'
)
def step_clico_cadastrar_sem_preencher(context: behave.runner.Context) -> None:
    context.page.submit_form()


@behave.when('preencho o CPF com "{cpf_invalido}"')
def step_preencho_cpf_alfanumerico(
    context: behave.runner.Context, cpf_invalido: str
) -> None:
    context.page.preencher_cpf(cpf_invalido)


@behave.then('devo ver a mensagem de sucesso')
def step_ver_mensagem_sucesso(context: behave.runner.Context) -> None:
    expected_title = 'Aí Sim...'
    expected_text = (
        'Recebemos os seus dados. Fique de olho na sua caixa de email, '
        'pois e em breve retornamos o contato.'
    )
    context.page.assert_mensagem_sucesso(expected_title, expected_text)


@behave.then('devo ver mensagens de erro nos campos obrigatórios')
def step_ver_mensagens_erro(context: behave.runner.Context) -> None:
    context.page.validar_mensagens_erro(context.table)


@behave.then(
    (
        'quando clicar em "OK" na mensagem de sucesso, '
        'devo ser redirecionado para a pagina inicial'
    )
)
def step_clicar_ok_redirecionar_inicial(
    context: behave.runner.Context,
) -> None:
    context.page.confirmar_sucesso()
    context.page = HomePage(context.driver)
    expected_title = 'Buger Eats'
    context.page.assert_logo(expected_title)
    expected_text = 'Seja um parceiro entregador pela Buger Eats'
    context.page.assert_title(expected_text)
    expected_text = (
        'Em vez de oportunidades tradicionais de entrega de refeições em '
        'horários pouco flexíveis, seja seu próprio chefe.'
    )
    context.page.assert_text(expected_text)


@behave.then('devo ver a mensagem "Oops! CPF inválido"')
def step_ver_mensagem_cpf_invalido(context: behave.runner.Context) -> None:
    expected_text = 'Oops! CPF inválido'
    context.page.assert_cpf_invalido(expected_text)
