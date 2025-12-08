"""
Steps de exemplo para teste
"""

from behave import given, when, then


@given("que acesso a aplicação")
def step_access_application(context):
    """Acessa a URL base da aplicação"""
    context.driver.get(context.base_url)
    print(f"Acessando: {context.base_url}")


@when("a página carrega")
def step_page_loads(context):
    """Aguarda a página carregar"""
    import time

    time.sleep(2)  # Aguarda 2 segundos para a página carregar
    print("Página carregada")


@then("devo ver a página inicial")
def step_see_homepage(context):
    """Verifica se a página inicial está visível"""
    assert context.driver.title, "Página não tem título"
    print(f"Título da página: {context.driver.title}")
