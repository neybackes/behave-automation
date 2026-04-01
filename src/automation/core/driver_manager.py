from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverManager:

    @staticmethod
    def create_chrome_driver(
        headless: bool = False, implicit_wait: int = 10
    ) -> webdriver.Chrome:
        options = Options()
        if headless:
            options.add_argument('--headless')

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--log-level=3')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option(
            'excludeSwitches',
            ['enable-automation', 'enable-logging'],
        )
        options.add_experimental_option('useAutomationExtension', False)

        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(implicit_wait)
        driver.maximize_window()
        return driver

    @staticmethod
    def close_driver(driver: webdriver.Chrome) -> None:
        if driver:
            driver.quit()
