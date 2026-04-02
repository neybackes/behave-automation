import behave
import behave.runner

from automation.pages.delivery_page import DeliveryPage
from automation.pages.home_page import HomePage


@behave.given('que estou na pagina inicial do Buger Eats')
@behave.when('acesso a pagina inicial')
@behave.given('que estou na pagina inicial')
def step_acessar_pagina_inicial(context: behave.runner.Context) -> None:
    context.page = HomePage(context.driver)
    context.page.open(context.base_url)


@behave.then('devo ver a pagina inicial')
@behave.then('devo ser redirecionado para a pagina inicial "/"')
def step_ver_pagina_inicial(context: behave.runner.Context) -> None:
    context.page.wait_page_load()


@behave.then('devo ver o logo "Buger Eats"')
def step_ver_logo(context: behave.runner.Context) -> None:
    expected_title = 'Buger Eats'
    context.page.assert_logo(expected_title)


@behave.then('devo ver o título "Seja um parceiro entregador pela Buger Eats"')
def step_ver_titulo(context: behave.runner.Context) -> None:
    expected_text = 'Seja um parceiro entregador pela Buger Eats'
    context.page.assert_title(expected_text)


@behave.then(
    (
        'devo ver o texto "Em vez de oportunidades tradicionais de entrega de '
        'refeições em horários pouco flexíveis, seja seu próprio chefe."'
    )
)
def step_ver_texto(context: behave.runner.Context) -> None:
    expected_text = (
        'Em vez de oportunidades tradicionais de entrega de refeições em '
        'horários pouco flexíveis, seja seu próprio chefe.'
    )
    context.page.assert_text(expected_text)


@behave.then('devo ver o botão "Cadastre-se para fazer entregas"')
def step_ver_botao(context: behave.runner.Context) -> None:
    expected_text = 'Cadastre-se para fazer entregas'
    context.page.assert_button(expected_text)


@behave.when('clico em "Cadastre-se para fazer entregas"')
@behave.when('clico no botão "Cadastre-se para fazer entregas"')
def step_clicar_botao(context: behave.runner.Context) -> None:
    expected_text = 'Cadastre-se para fazer entregas'
    context.page.click_cadastrar(expected_text)
    context.page = DeliveryPage(context.driver)


@behave.then('devo ser direcionado para a pagina de cadastro')
@behave.then('devo ser redirecionado para "/deliver"')
def step_redirecionado_deliver(context: behave.runner.Context) -> None:
    context.page.assert_on_page()


@behave.then('devo ver o formulário de cadastro')
def step_ver_formulario(context: behave.runner.Context) -> None:
    context.page.assert_form_visible()


@behave.given('que estou na pagina de cadastro')
@behave.when('acesso a pagina de cadastro diretamente')
def step_estou_na_pagina_cadastro(context: behave.runner.Context) -> None:
    context.page = DeliveryPage(context.driver)
    context.page.open(context.base_url)


@behave.when('clico no link "Voltar para home"')
def step_clicar_voltar_home(context: behave.runner.Context) -> None:
    expected_text = 'Voltar para home'
    context.page.voltar_home(expected_text)
    context.page = HomePage(context.driver)


@behave.then('a pagina deve carregar em menos de 3 segundos')
def step_verificar_tempo_carregamento(context: behave.runner.Context) -> None:
    context.page.check_load_time(max_time=3)


@behave.then('todos os recursos devem ser carregados corretamente')
def step_verificar_recursos_carregados(context: behave.runner.Context) -> None:
    context.page.check_resources_loaded()
