import time

import allure
import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


class TestCartClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.inventory_page = InventoryPage(browser, url + 'inventory.html')
        self.cart_page = CartPage(browser, url + 'cart.html')

    @allure.epic('US_002.00')
    @allure.story('TC_002.00.01')
    @allure.title("Bage change when adding")
    def test_change_bage_when_adding(self, browser, url):
        self.inventory_page.login_with_cookie()
        with allure.step('step1 add to cart'):
            self.inventory_page.add_to_cart()
        with allure.step('step2 watch changes'):
            self.inventory_page.bage_has_changed()

    @allure.epic('US_002.00')
    @allure.story('TC_002.00.02')
    @allure.title("Button text after remove")
    def test_change_add_button_text(self, browser, url):
        self.inventory_page.login_with_cookie()
        with allure.step('step1 text before adding'):
            self.inventory_page.button_text_before_adding()
        with allure.step('step2 click on button'):
            self.inventory_page.add_to_cart()
        with allure.step('step3 text after adding'):
            self.inventory_page.button_text_after_adding()

    @allure.epic('US_002.00')
    @allure.story('TC_002.00.03')
    @allure.title("Remove from cart")
    def test_remove_from_cart(self, browser, url):
        self.inventory_page.login_with_cookie()
        with allure.step('step1 click on add button'):
            self.inventory_page.add_to_cart()
        with allure.step('step3 text after adding'):
            self.inventory_page.go_to_cart()
        with allure.step('step4 go to cart'):
            self.cart_page.continue_shopping()
        with allure.step('step4 check page'):
            self.inventory_page.page_is_open(url)

    def test_go_to_facebook(self, browser, url):
        self.inventory_page.login_with_cookie()
        self.inventory_page.go_to_footer_facebook()
        browser.switch_to_window(browser.window_handles[1])
        browser.current_url= 'https://www.facebook.com/saucelabs'
