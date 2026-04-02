from abc import ABC, abstractmethod
from typing import Any

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from automation.utils.logger import get_logger

Locator = tuple[Any, str]
logger = get_logger()


class BasePage(ABC):
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    @abstractmethod
    def path(self) -> str:
        raise NotImplementedError

    def open(self, base_url: str) -> None:
        base_url = base_url.rstrip('/')
        url = f'{base_url}{self.path}'
        self.driver.get(url)
        logger.info(f'OK: opening page: {url}')

    def wait_page_load(self, timeout: int = 10) -> None:
        WebDriverWait(self.driver, timeout).until(
            lambda driver: (
                driver.execute_script('return document.readyState')
                == 'complete'
            )
        )
        logger.info('OK: page loaded')

    def get_title(self, expected_title: str) -> None:
        actual_title = self.driver.title
        if expected_title and expected_title != actual_title:
            raise AssertionError(
                f"Expected title '{expected_title}' does not match current "
                f"title '{actual_title}'"
            )
        logger.info(f'OK: title validated: {actual_title}')

    def wait_element_visible(
        self, locator_tuple: Locator, timeout: int = 10
    ) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        logger.debug(
            f'OK: waiting for visible element: {locator_tuple} '
            f'(timeout: {timeout}s)'
        )
        locator = wait.until(ec.visibility_of_element_located(locator_tuple))
        logger.info(f'OK: visible element: {locator}')
        return locator

    def wait_element_present(
        self, locator_tuple: Locator, timeout: int = 10
    ) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        logger.debug(
            f'OK: waiting for element present: {locator_tuple} '
            f'(timeout: {timeout}s)'
        )
        element = wait.until(ec.presence_of_element_located(locator_tuple))
        logger.info(f'OK: element present: {element}')
        return element

    def get_text(
        self, selector: Any, locator: str, expected_text: str
    ) -> None:
        element = self.wait_element_visible((selector, locator))
        actual_text = element.text
        assert expected_text in actual_text, (
            f"Expected text '{expected_text}' not found. "
            f"Current text: '{actual_text}'"
        )
        logger.info(f'OK: text validated: {actual_text}')

    @staticmethod
    def validate_multiples_text(table, elements) -> None:
        assert table is not None, 'Validation table not provided'
        messages = [element.text.strip() for element in elements]
        logger.info(f'OK: found {len(elements)} elements on page.')
        logger.debug(f'Texts found: {messages}')

        for row in table:
            field = row['campo']
            expected_message = row['mensagem']
            assert expected_message in messages, (
                f'Expected message for "{field}" not found. '
                f'Expected: {expected_message}. '
                f'Found: {messages}'
            )

    def find_element(self, selector: Any, locator: str) -> WebElement:
        element = self.wait_element_visible((selector, locator))
        logger.info(f'OK: element found: {locator}')
        return element

    def click(self, locator_tuple: Locator) -> None:
        element = self.wait_element_visible(locator_tuple)
        element.click()
        logger.info(f'OK: element clicked: {locator_tuple}')

    def check_load_time(self, max_time: int = 3) -> None:
        start_time = self.driver.execute_script(
            'return performance.timing.navigationStart'
        )
        load_time = (
            self.driver.execute_script(
                'return performance.timing.loadEventEnd'
            )
            - start_time
        ) / 1000
        assert load_time <= max_time, (
            f'Load time {load_time:.2f}s exceeds limit of {max_time}s'
        )
        logger.info(f'OK: load time: {load_time:.2f}s')

    def check_resources_loaded(self) -> None:
        resources = self.driver.execute_script(
            "return window.performance.getEntriesByType('resource');"
        )
        http_error = 400
        failed_resources = [
            resource
            for resource in resources
            if resource.get('status', 200) >= http_error
        ]
        assert not failed_resources, (
            f'Resources failed to load: {failed_resources}'
        )
        logger.info('OK: all resources loaded successfully')

    def assert_on_page(self) -> None:
        assert self.path in self.driver.current_url
        logger.info(f'OK: on expected page: {self.driver.current_url}')
