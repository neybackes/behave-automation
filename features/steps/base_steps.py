from behave import *
from pages.base_page import BasePage

#como acoplar em varios cenarios? 
@given("que acesso a aplicação")
def step_access_application(context):
    """Acessa a URL base da aplicação"""
    context.page = BasePage(context.driver)
    context.page.open(context.base_url)
    print(f"Acessando: {context.base_url}")


@when("a página carrega")
def step_page_loads(context):
    """Aguarda a página carregar"""
    context.page.wait_page_load()
    print("Página carregada")


@then("devo ver a página inicial")
def step_see_homepage(context: object):
    """Verifica se a página inicial está visível"""
    expected_title = "Buger Eats"
    actual_title = context.page.get_title()
    assert expected_title in actual_title, f"Título esperado '{expected_title}' não encontrado. Título atual: '{actual_title}'"
    print(f"✓ Título validado: {actual_title}")
