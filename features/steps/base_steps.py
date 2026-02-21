import behave #type: ignore
import behave.runner #type: ignore
import pages.base_page #type: ignore
from selenium.webdriver.common.by import By

#primeiro cenário

@behave.when("acesso a pagina inicial")
@behave.when('acesso a página inicial')
@behave.given('que estou na página inicial')
def step_acessar_pagina_inicial(context: behave.runner.Context) -> None:
    context.page = pages.base_page.BasePage(context.driver)
    context.page.open(context.base_url)  


@behave.then("devo ver a página inicial")
@behave.then('devo ser redirecionado para a página inicial "/"') 
def step_ver_pagina_inicial(context: behave.runner.Context) -> None:
    context.page.wait_page_load()

@behave.then("devo ver o logo \"Buger Eats\"")
def step_ver_logo(context: behave.runner.Context)-> None:
    expected_title = "Buger Eats"
    context.page.get_title(expected_title)   

@behave.then("devo ver o título \"Seja um parceiro entregador pela Buger Eats\"")
@behave.then('devo ver o título "Seja um parceiro entregador pela Buger Eats"')
def step_ver_titulo(context: behave.runner.Context)-> None:
    expected_text = "Seja um parceiro entregador pela Buger Eats"
    context.page.get_text("tag name", "h1", expected_text)
    

@behave.then("devo ver o texto \"Em vez de oportunidades tradicionais de entrega de refeições em horários pouco flexíveis, seja seu próprio chefe.\"")
def step_ver_texto(context: behave.runner.Context)-> None:
    expected_text = "Em vez de oportunidades tradicionais de entrega de refeições em horários pouco flexíveis, seja seu próprio chefe."
    context.page.get_text("tag name", "p", expected_text)
    

@behave.then("devo ver o botão \"Cadastre-se para fazer entregas\"")
def step_ver_botão(context: behave.runner.Context)-> None:    
    expected_text = "Cadastre-se para fazer entregas"
    context.page.get_text("tag name", "strong", expected_text)

#segundo cenário
@behave.when('clico no botão "Cadastre-se para fazer entregas"')
@behave.when('clico no botão "Cadastre-se para fazer entregas"')
def step_clicar_botao(context: behave.runner.Context) -> None:
    expected_text = "Cadastre-se para fazer entregas"
    context.page.get_text("tag name", "strong", expected_text)
    locator_tuple = (By.XPATH, f"//a[.//strong[text()='{expected_text}']]")
    context.page.click(locator_tuple)

@behave.then('devo ser redirecionado para "/deliver"')
def step_redirecionado_deliver(context: behave.runner.Context) -> None:
    assert "/deliver" in context.driver.current_url
    print(f"✓ Redirecionado para: {context.driver.current_url}")

@behave.then('devo ver o formulário de cadastro')
def step_ver_formulario(context: behave.runner.Context) -> None:
   context.page.find_element("xpath", '//*[@id="page-deliver"]/form')
   

#terceiro cenário
@behave.given('que estou na página de cadastro "/deliver"')
@behave.when('acesso a página de cadastro diretamente')
def step_estou_na_pagina_cadastro(context: behave.runner.Context) -> None:
    context.page = pages.base_page.BasePage(context.driver)
    context.page.open(context.base_url + "/deliver")   

@behave.when('clico no link "Voltar para home"')
def step_clicar_voltar_home(context: behave.runner.Context) -> None:
    expected_text = "Voltar para home"
    context.page.get_text("tag name", "a", expected_text)
    locator_tuple = (By.XPATH, f"//a[contains(text(), '{expected_text}')]")
    context.page.click(locator_tuple)  

@behave.then('a página deve carregar em menos de 3 segundos')
@behave.then('a página deve carregar em menos de 3 segundos')
def step_verificar_tempo_carregamento(context: behave.runner.Context) -> None:
    context.page.check_load_time(max_time=3)

@behave.then('todos os recursos devem ser carregados corretamente')
@behave.then('todos os recursos devem ser carregados corretamente')
def step_verificar_recursos_carregados(context: behave.runner.Context) -> None:
    context.page.check_resources_loaded()