# behave_automation

Suite de automacao E2E com Behave + Selenium, organizada em arquitetura por camadas (`config`, `core`, `pages`, `services`).

## Requisitos
- Python 3.10+
- Poetry
- Google Chrome instalado

## Setup
```bash
git clone <url-do-repo>
cd behave_automation
python -m venv .venv
source .venv/Scripts/activate  # Windows
poetry install
```

Configure o `.env` na raiz (base em `.env.example`):
```env
BASE_URL=https://buger-eats.vercel.app/
HEADLESS=false
TIMEOUT=10
```

## Execucao
```bash
poetry run behavex
```

Relatorios gerados em `output/report.html` e `output/report.json`.

## Estrutura
```text
behave_automation/
├── src/
│   └── automation/
│       ├── config/
│       ├── core/
│       ├── pages/
│       └── services/
│
├── resources/
│   ├── assets/
│   └── data/
│
├── features/
│   ├── environment.py
│   ├── navigation.feature
│   ├── delivery_driver_reg.feature
│   └── steps/
│
├── output/
├── pyproject.toml
├── behave.ini
└── README.md
```

## Exemplo rapido
```python
from automation.core.driver_manager import DriverManager
from automation.pages.base_page import BasePage

driver = DriverManager.create_chrome_driver()
page = BasePage(driver)
page.open('https://buger-eats.vercel.app/')
DriverManager.close_driver(driver)
```
