import logging
from typing import Tuple

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    LOGGER = logging.getLogger(__name__)
    CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')
    BURGER_MENU = (By.ID, 'react-burger-menu-btn')
    ALL_ITEMS = (By.ID, 'inventory_sidebar_link')
    ABOUT = (By.ID, 'about_sidebar_link')
    LOGOUT = (By.ID, 'logout_sidebar_link')
    RESET_APP_STATE = (By.ID, 'logout_sidebar_link')

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(self.url)

    def wait_for_url_to_be(self, url: str, timeout: int = 5) -> bool:
        return WebDriverWait(self.browser, timeout).until(ec.url_to_be(url))

    def page_title_is(self, title: str, timeout: int = 5) -> bool:
        return WebDriverWait(self.browser, timeout).until(ec.title_is(title))

    def wait_until_clickable(self, locator: Tuple, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self.browser, timeout).until(
                ec.element_to_be_clickable(locator)
            )
        except NoSuchElementException as e:
            self.LOGGER.error(f"NoSuchElementException: {e}")


    def wait_until_present(self, locator: Tuple, timeout: int = 5) -> WebElement:
        return WebDriverWait(self.browser, timeout).until(
            ec.presence_of_element_located(locator)
        )

    def wait_until_not_present(self, locator: Tuple, timeout=5) -> WebElement:
        return WebDriverWait(self.browser, timeout).until_not(
            ec.presence_of_element_located(locator)
        )

    def wait_until_visible(self, locator: Tuple, timeout: int = 5) -> WebElement:
        return WebDriverWait(self.browser, timeout).until(
            ec.visibility_of_element_located(locator)
        )

    def element_is_present(self, locator: Tuple, timeout: int = 5) -> bool:
        try:
            self.wait_until_visible(locator, timeout)
            return True
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def page_is_open(self, url):
        try:
            self.wait_for_url_to_be(url)
            return True
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")
            return False

    def elements_are_present(self, locator, timeout: int = 5):
        return WebDriverWait(self.browser, timeout).until(
            ec.presence_of_all_elements_located(locator)
        )

    def go_to_cart(self):
        self.wait_until_clickable(self.CART_BUTTON).click()

    def burger_menu(self):
        self.wait_until_clickable(self.BURGER_MENU).click()

    def logout(self):
        self.wait_until_clickable(self.LOGOUT).click()
