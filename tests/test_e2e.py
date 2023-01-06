import allure
import pytest
from utilities.BaseClass import BaseClass
from pages.inventory_page import InventoryPage
from pages.shopping_cart_page import ShoppingCartPage
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class TestLoginPage(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        inventory_page = InventoryPage(self.browser)
        cart_page = ShoppingCartPage(self.browser)

        log.info("sorting inventory Z to A")
        dropdown = Select(inventory_page.getdrop_down_menu())
        dropdown.select_by_visible_text("Name (Z to A)")
        ALL_PRODUCTS = inventory_page.getall_products()
        sorted_list = []
        for option in ALL_PRODUCTS:
            sorted_list.append(option.text)
        log.info("Adding backpack into cart")
        inventory_page.getbackpack()
        inventory_page.getshopping_cart()

        cart_page.get_checkout_button()

        log.info("Entering customer's information")
        cart_page.customer_fist_name().send_keys("Anton")
        cart_page.customer_last_name().send_keys("Vasya")
        cart_page.customer_zip_code().send_keys("95117")

        cart_page.get_continue_button()
        cart_page.get_finish_button()
        log.info("Verifying that order was submitted successfully")
        assert cart_page.get_thank_you_note() == "THANK YOU FOR YOUR ORDER"