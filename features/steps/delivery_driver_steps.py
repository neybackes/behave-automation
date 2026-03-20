

import os
import behave #type: ignore
import behave.runner #type: ignore
from selenium.webdriver.common.by import By
@behave.when('preencho os dados pessoais')
def step_preencho_dados_pessoais(context: behave.runner.Context) -> None:
    context.endereco_cep = context.page.fill_basic_data_input(context.table)
     

@behave.when('clico em "Buscar CEP"')
def step_clico_buscar_cep(context: behave.runner.Context) -> None:
    locator_tuple = (By.XPATH, "//*[@value='Buscar CEP']") 
    context.page.click(locator_tuple)
    
@behave.when('aguardo o preenchimento automático do endereço')
def step_aguardo_preenchimento_automatico(context: behave.runner.Context) -> None:  
    context.endereco_cep
    context.page.validate_address(context.endereco_cep)

@behave.when('preencho o número "500"')
def step_preencho_numero(context: behave.runner.Context) -> None:
    context.page.find_element(By.NAME, "address-number").send_keys("500")

@behave.when('preencho o complemento "Apto 101"')
def step_preencho_complemento(context: behave.runner.Context) -> None:
    context.page.find_element(By.NAME, "address-details").send_keys("Apto 101")

@behave.when('seleciono o método de entrega "Moto"')
def step_seleciono_metodo_entrega_moto(context: behave.runner.Context) -> None:
    locator_tuple = (By.XPATH, "//*[@alt='Moto']")
    context.page.click(locator_tuple)

@behave.when('seleciono o método de entrega "Bicicleta"')
def step_seleciono_metodo_entrega_bicicleta(context: behave.runner.Context) -> None:
    locator_tuple = (By.XPATH, "//*[@alt='Bicicleta']")
    context.page.click(locator_tuple)

@behave.when('seleciono o método de entrega "Van/Carro"')
def step_seleciono_metodo_entrega_van_carro(context: behave.runner.Context) -> None:
    locator_tuple = (By.XPATH, "//*[@alt='Van/Carro']")
    context.page.click(locator_tuple)   

@behave.when('faço upload da foto da CNH')
def step_faço_upload_cnh(context: behave.runner.Context) -> None:
    # Caminho relativo ao diretório raiz do projeto
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    cnh_path = os.path.join(project_root, 'support', 'assets', 'cnh_model.png')
    assert os.path.exists(cnh_path), f"Arquivo não encontrado: {cnh_path}"
    input_file = context.page.wait_element_present((By.XPATH, "//input[@type='file']"), timeout=10)
    input_file.send_keys(cnh_path)
    
@behave.when('clico em "Cadastre-se para fazer entregas" no formulário')
def step_clico_cadastrar_formulario(context: behave.runner.Context) -> None:
    locator_tuple = (By.CLASS_NAME, "button-success")
    context.page.click(locator_tuple)

@behave.then('devo ver a mensagem de sucesso')
def step_ver_mensagem_sucesso(context: behave.runner.Context) -> None:
    context.page.wait_element_present((By.XPATH, "//*[@role='dialog']"), timeout=10)
    context.page.get_text(By.ID, "swal2-title", "Aí Sim...")
    context.page.get_text(By.ID, "swal2-html-container", "Recebemos os seus dados. Fique de olho na sua caixa de email, pois e em breve retornamos o contato.")

@behave.then('quando clicar em "OK" na mensagem de sucesso, devo ser redirecionado para a página inicial')
def step_clicar_ok_redirecionar_inicial(context: behave.runner.Context) -> None:
    locator_tuple = (By.XPATH, "//*[@class='swal2-confirm swal2-styled']")
    context.page.click(locator_tuple)
    context.page.wait_page_load()
    expected_title = "Buger Eats"
    context.page.get_title(expected_title)
    expected_text = "Seja um parceiro entregador pela Buger Eats"
    context.page.get_text("tag name", "h1", expected_text)
    expected_text = "Em vez de oportunidades tradicionais de entrega de refeições em horários pouco flexíveis, seja seu próprio chefe."
    context.page.get_text("tag name", "p", expected_text)