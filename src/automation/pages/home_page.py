from selenium.webdriver.common.by import By

from automation.pages.base_page import BasePage


class HomePage(BasePage):
    @property
    def path(self) -> str:
        return '/'

    def assert_logo(self, expected_title: str) -> None:
        self.get_title(expected_title)

    def assert_title(self, expected_text: str) -> None:
        self.get_text(By.TAG_NAME, 'h1', expected_text)

    def assert_text(self, expected_text: str) -> None:
        self.get_text(By.TAG_NAME, 'p', expected_text)

    def assert_button(self, expected_text: str) -> None:
        self.get_text(By.TAG_NAME, 'strong', expected_text)

    def click_cadastrar(self, expected_text: str) -> None:
        self.assert_button(expected_text)
        locator_tuple = (
            By.XPATH,
            f"//a[.//strong[text()='{expected_text}']]",
        )
        self.click(locator_tuple)
