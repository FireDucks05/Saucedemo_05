import time

import allure
import pytest

from constants import INFORMATION_DATA
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By


class TestCheckoutClass:

    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.inventory_page = InventoryPage(browser, url + 'inventory.html')
        self.cart_page = CartPage(browser, url + 'cart.html')
        self.checkout_page = CheckoutStepOnePage(browser, url + 'checkout-step-one.html')
        self.checkout_page2 = CheckoutStepTwoPage(browser, url + 'checkout-step-two.html')


    @allure.epic('UC_006.00')
    @allure.story('TC_006.00.01')
    @allure.title("Successfully purchase")
    def test_purchase(self, browser, url):
        with allure.step('step1 add to cart'):
            self.inventory_page.add_to_cart()
        with allure.step('step2 go to cart'):
            self.inventory_page.go_to_cart()

        with allure.step('step3 go chekout'):
            self.cart_page.checkout()

        with allure.step('step4 fill information'):
            self.checkout_page.input_your_informarion(
                INFORMATION_DATA["first_name"], INFORMATION_DATA["last_name"], INFORMATION_DATA["zip"])

        with allure.step('step5 click finish'):
            self.checkout_page2.finish_order()
        with allure.step('step6 order confirmed'):
            self.checkout_page2.successfully_message()

    @allure.epic('UC_007.00')
    @allure.story('TC_007.00.01')
    @allure.title("Invalid message on checkout step")
    def test_error_message(self, browser, url):
        with allure.step('step1 add to cart'):
            self.inventory_page.add_to_cart()
        with allure.step('step2 go to cart'):
            self.inventory_page.go_to_cart()

        with allure.step('step3 go chekout'):
            self.cart_page.checkout()

        with allure.step('step4 fill information without first name'):
            self.checkout_page.input_your_informarion('', INFORMATION_DATA["last_name"], INFORMATION_DATA["zip"])

        self.checkout_page.error_when_empty_required_fied()


    @allure.epic('UC_007.00')
    @allure.story('TC_007.00.02')
    @allure.title("Invalid message on checkout step ZIP missed")
    def test_error_message(self, browser, url):
        with allure.step('step1 add to cart'):
            self.inventory_page.add_to_cart()
        with allure.step('step2 go to cart'):
            self.inventory_page.go_to_cart()

        with allure.step('step3 go chekout'):
            self.cart_page.checkout()

        with allure.step('step4 fill information without first name'):
            self.checkout_page.input_your_informarion(INFORMATION_DATA["first_name"], INFORMATION_DATA["last_name"],'' )