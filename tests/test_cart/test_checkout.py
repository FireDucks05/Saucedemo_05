import allure
import pytest

from constants import INFORMATION_DATA
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.inventory_page import InventoryPage


class TestCheckoutClass:

    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.inventory_page = InventoryPage(browser, url + 'inventory.html')
        self.cart_page = CartPage(browser, url + 'cart.html')
        self.chekout_page = CheckoutStepOnePage(browser, url + 'checkout-step-one.html')


    @allure.epic('UC_006.00.01.00')
    @allure.story('TC_006.00.01')
    @allure.title("Successfully purchase")
    def test_purchase(self, browser, url):
        with allure.step('step1 add to cart'):
            self.inventory_page.add_to_cart()
            self.inventory_page.go_to_cart()

            self.cart_page.checkout()

            self.chekout_page.input_your_informarion(
                INFORMATION_DATA["first_name"], INFORMATION_DATA["last_name"], INFORMATION_DATA["zip"])
