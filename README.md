# behave_automation

Simple E2E automation suite using Behave + Selenium, organized in layers
(`config`, `core`, `pages`, `services`).

## Requirements
- Python 3.10+
- Poetry
- Google Chrome installed

## Setup
```bash
git clone <repo-url>
cd behave_automation
python -m venv .venv
. .venv/Scripts/activate  # Windows
poetry install
```

## Configuration
Create a `.env` file at the project root (use `.env.example` as a base):
```env
BASE_URL=https://buger-eats.vercel.app/
HEADLESS=false
TIMEOUT=10
```

## Run
```bash
poetry run behavex
```

Reports are generated in `output/report.html` and `output/report.json`.

## Documentation
- Project Docs (PT-BR): https://www.notion.so/30e9a13279ae80018031f525970e6909

## Project Structure
```text
behave_automation/
├── src/
│   └── automation/
│       ├── config/
│       ├── core/
│       ├── pages/
│       ├── services/
│       └── utils/
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

## Quick Example
```python
from automation.core.driver_manager import DriverManager
from automation.pages.base_page import BasePage

driver = DriverManager.create_chrome_driver()
page = BasePage(driver)
page.open('https://buger-eats.vercel.app/')
DriverManager.close_driver(driver)
```
