import allure
import pytest

from constants import POSITIVE_LOGIN_CREDENTIALS
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestCartClass:

    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.login_page = LoginPage(browser, url)
        self.login_page.open_page()
        self.inventory_page = InventoryPage(browser, url + 'inventory.html')


    @allure.epic('US_002.00')
    @allure.story('TC_002.00.02')
    @allure.title("Change bage when adding")
    def test_change_bage_when_adding(self, browser, url):
        with allure.step('step1 login'):
            self.login_page.login_ui(POSITIVE_LOGIN_CREDENTIALS[0][0], POSITIVE_LOGIN_CREDENTIALS[0][1])
        with allure.step('step2 add to cart'):
            self.inventory_page.add_to_cart()
        with allure.step('step3 changes'):
            self.inventory_page.bage_has_changed()

    @allure.story('US_002.00')
    @allure.step('TC_002.00.02')
    @allure.title("Change button text")
    def test_change_add_button_text(self, browser, url):
        self.login_page.login_ui(POSITIVE_LOGIN_CREDENTIALS[0][0], POSITIVE_LOGIN_CREDENTIALS[0][1])

        self.inventory_page.button_text_before_adding()
        self.inventory_page.add_to_cart()
        self.inventory_page.button_text_after_adding()
