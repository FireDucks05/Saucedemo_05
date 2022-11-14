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


    def test_add_to_cart(self, browser, url):
        self.login_page.login_ui(POSITIVE_LOGIN_CREDENTIALS[0][0], POSITIVE_LOGIN_CREDENTIALS[0][1])

        self.inventory_page.button_text_before_adding()
        self.inventory_page.add_to_cart()
        self.inventory_page.button_text_after_adding()
