# README - Automação de Testes com Behave e Selenium

## Descrição do Projeto

Projeto de automação de testes web para a aplicação **Buger Eats** utilizando:
- **Behave**: Framework BDD (Behavior Driven Development)
- **Selenium**: Automação de navegador web
- **Python**: Linguagem de programação

## Estrutura do Projeto

```
behave_automation/
├── features/                    # Cenários de teste (Gherkin)
│   ├── steps/                   # Implementação dos steps
│   │   └── steps_exemplo.py
│   ├── pages/                   # Page Object Model
│   │   └── base_page.py
│   ├── environment.py           # Hooks do Behave
│   └── exemplo.feature          # Features de exemplo
│
├── support/                     # Suporte e utilitários
│   ├── drivers/                 # Gerenciamento de drivers
│   │   └── driver_manager.py
│   └── utils/                   # Funções utilitárias
│       └── env_config.py
│
├── reports/                     # Relatórios de execução
│
├── anotacoes/                   # Anotações de estudo (ignorado no git)
│
├── .env                         # Variáveis de ambiente (ignorado no git)
├── .env.example                 # Template de variáveis
├── .gitignore                   # Arquivos ignorados pelo git
├── behave.ini                   # Configuração do Behave
├── requirements.txt             # Dependências Python
└── README.md                    # Este arquivo
```

## Instalação e Configuração

### 1. Criar Ambiente Virtual

```bash
python -m venv .venv
```

### 2. Ativar Ambiente Virtual

**Windows (CMD):**
```cmd
.venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

Copie o arquivo `.env.example` para `.env` e configure:

```bash
cp .env.example .env
```

Edite o arquivo `.env` com seus dados:
```
BASE_URL=https://buger-eats.vercel.app/
USERNAME=seu_usuario
PASSWORD=sua_senha
HEADLESS=false
TIMEOUT=10
```

## Executar Testes

### Executar Todos os Testes

```bash
behave
```

### Executar com Formatação Específica

```bash
behave --format pretty
```

### Executar Feature Específica

```bash
behave features/exemplo.feature
```

### Executar com Tags

```bash
behave --tags=@importante
```

### Modo Headless (sem interface)

Edite o `.env` e configure:
```
HEADLESS=true
```

## Page Object Model (POM)

### Por que usar POM?

- **Manutenção**: Alterações em localizadores em um único lugar
- **Reutilização**: Métodos de página podem ser reutilizados
- **Legibilidade**: Código mais limpo e organizado

### Exemplo de Página

```python
from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class LoginPage(BasePage):
    # Localizadores
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-btn")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-msg")

    # Métodos
    def fill_username(self, username):
        self.fill_input(self.USERNAME_INPUT, username)

    def fill_password(self, password):
        self.fill_input(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
```

## Estrutura de um Cenário Behave

### Feature File (`.feature`)

```gherkin
# language: pt
Funcionalidade: Login na aplicação
  Como usuário
  Desejo fazer login
  Para acessar minha conta

  Cenário: Login com credenciais válidas
    Dado que estou na página de login
    Quando preencho usuário "usuario@test.com"
    E preencho senha "senha123"
    E clico no botão entrar
    Então devo ser redirecionado para o dashboard
```

### Implementation (`.py`)

```python
from behave import given, when, then
from features.pages.login_page import LoginPage

@given("que estou na página de login")
def step_goto_login(context):
    context.driver.get(f"{context.base_url}/login")
    context.login_page = LoginPage(context.driver)

@when('preencho usuário "{username}"')
def step_fill_username(context, username):
    context.login_page.fill_username(username)

@when('preencho senha "{password}"')
def step_fill_password(context, password):
    context.login_page.fill_password(password)

@when("clico no botão entrar")
def step_click_login(context):
    context.login_page.click_login()

@then("devo ser redirecionado para o dashboard")
def step_verify_dashboard(context):
    assert "/dashboard" in context.driver.current_url
```

## Variáveis de Ambiente

### Carregando Variáveis

```python
from support.utils.env_config import EnvConfig

env = EnvConfig()
base_url = env.get_base_url()
username = env.get_username()
password = env.get_password()
```

## Boas Práticas

### ✅ FAÇA

- ✓ Use Page Object Model para organizar elementos
- ✓ Crie steps reutilizáveis e independentes
- ✓ Use nomes descritivos para features e cenários
- ✓ Isolado os dados de teste (use fixtures/dados)
- ✓ Capture screenshots em caso de falha
- ✓ Use waits explícitos em vez de sleep
- ✓ Organize seus localizadores em constantes

### ❌ EVITE

- ✗ Hard-code de URLs e credenciais
- ✗ Steps muito longas e complexas
- ✗ Dependências entre cenários
- ✗ Usar sleep em lugar de waits
- ✗ Testes frágeis com seletores instáveis
- ✗ Muita lógica em steps (deve estar em pages)

## Troubleshooting

### ChromeDriver não encontrado

Baixe o ChromeDriver compatível com sua versão do Chrome:
https://chromedriver.chromium.org/

### Elemento não encontrado

- Aumente o tempo de espera no `.env`
- Verifique o seletor CSS/XPath
- Use waits explícitos na base page

### Teste falha aleatoriamente

- Aumente os timeouts
- Use waits explícitos em vez de implícitos
- Verifique se a página está completamente carregada

## Próximos Passos

1. Criar mais page objects conforme necessário
2. Implementar testes de login
3. Adicionar reportes com Allure
4. Configurar CI/CD (GitHub Actions, Jenkins, etc)
5. Implementar Page Factory Pattern

## Referências

- [Behave Documentation](https://behave.readthedocs.io/)
- [Selenium Python Documentation](https://selenium.dev/documentation/webdriver/)
- [Gherkin Syntax](https://cucumber.io/docs/gherkin/)
