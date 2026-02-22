
# behave_automation

Bem-vindo(a) ao **projeto behave_automation**! Este projeto implementa uma suíte de E2E em linguagem natural, utilizando Behave e Selenium, com arquitetura desacoplada baseada no padrão Page Object.

## Sobre o projeto
Este repositório foi pensado para aproximar os requisitos de negócio da implementação técnica, utilizando o Behave como facilitador. Os cenários de teste são escritos em linguagem natural (Gherkin), permitindo que a lógica seja baseada no comportamento real e tornando os testes compreensíveis para pessoas não técnicas, como analistas de negócios, POs (Product Owners) e stakeholders.

### Behavex
O projeto utiliza o Behavex, uma extensão do Behave que traz recursos avançados para relatórios, organização e customização dos testes orientados ao comportamento. Com o Behavex, é possível gerar relatórios HTML detalhados, capturar imagens e desacoplar ainda mais as responsabilidades, além de facilitar a integração de novas funcionalidades e a manutenção do projeto.

Principais benefícios do Behavex:
- Relatórios customizados e interativos
- Extensões para hooks, tags e filtros
- Melhor desacoplamento entre steps, pages e suporte
- Facilidade para integração com pipelines e CI/CD


## Requisitos
- Python 3.8+ (recomenda-se versão mais recente)
- Behave
- Selenium
- Acesso o página: `https://buger-eats.vercel.app/`
- (Em breve) Poetry para gerenciamento de dependências

## Como começar
Clone o repositório:
```bash
git clone <url-do-repo>
cd behave_automation
```
Crie e ative o ambiente virtual:
```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows
```
Instale as dependências:
```bash
pip install -r requirements.txt
```
**Configure as variáveis de ambiente:**
	Crie um arquivo `.env` na raiz (um exemplo já está presente):
	```env
	BASE_URL=https://buger-eats.vercel.app/
	```

(Em breve: migração para Poetry)

## Rodando os testes
Execute os testes BDD:
```bash
behavex
```
Os relatórios são gerados em output/report.html e output/report.json.

## Estrutura do projeto
features/           # Cenários BDD e steps
	nav.feature       # Exemplo de feature
	environment.py    # Configuração Behave
	pages/            # Page Objects
		base_page.py    # Base para páginas
	steps/            # Steps definitions
		base_steps.py   # Base para steps
support/            # Suporte e drivers
	drivers/          # Gerenciamento de drivers Selenium
		driver_manager.py
	utils/            # Utilitários e configs
		env_config.py
output/             # Relatórios e logs
requirements.txt    # Dependências atuais
behave.ini          # Configuração Behave
README.md           # Este guia

## Exemplo prático
```python
from features.pages.base_page import BasePage
from support.drivers.driver_manager import DriverManager

driver = DriverManager().get_driver()
page = BasePage(driver)
page.navigate_to('https://exemplo.com')
```

## Integração Contínua
(Ainda a ser implementado) Workflow automatizado com GitHub Actions para rodar testes e checar estilo a cada push/pull request.

## Convenções e estilo
- Estrutura desacoplada e reutilizável
- Page Object para organização
- Steps claros e objetivos
- Tageamento @smoke, @perfomance...
- Relatórios HTML e JSON
- (Em breve) Poetry para dependências

### Pontos pendentes
- Implementação dos fluxos de formulário
- Migração para Poetry
- CI/CD com GitHub Actions

## Bora contribuir?
Pull requests são super bem-vindos! Ideias, sugestões ou dúvidas, abra uma issue.

## Licença
MIT.
