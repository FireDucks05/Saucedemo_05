import time
import pytest
from pages.inventory_page import InventoryPage
from pages.shopping_cart_page import ShoppingCartPage
from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class TestShoppingCart(BaseClass):
    def test_cart_item_desc_verification(self):
        log = self.getLogger()
        inventory_page = InventoryPage(self.browser)
        cart_page = ShoppingCartPage(self.browser)
        inventory_page.getbackpack()
        inventory_page.getshopping_cart()
        log.info("verifying item description")
        assert cart_page.getitem_inventory_desc() == inventory_page.getproduct_description()

    def test_checkout_button(self):
        log = self.getLogger()
        inventory_page = InventoryPage(self.browser)
        cart_page = ShoppingCartPage(self.browser)
        inventory_page.getbackpack()
        inventory_page.getshopping_cart()
        log.info("verifying checkout button works correctly")
        cart_page.get_checkout_button()
        assert "CHECKOUT: YOUR INFORMATION" == cart_page.get_checkout_info_text()

    def test_customer_information(self):
        log = self.getLogger()
        inventory_page = InventoryPage(self.browser)
        cart_page = ShoppingCartPage(self.browser)
        inventory_page.getbackpack()
        inventory_page.getshopping_cart()
        cart_page.get_checkout_button()
        log.info("Entering customer's information")
        cart_page.customer_fist_name().send_keys("Anton")
        cart_page.customer_last_name().send_keys("Vasya")
        cart_page.customer_zip_code().send_keys("95117")

    def test_complete_check_out(self):
        log = self.getLogger()
        inventory_page = InventoryPage(self.browser)
        cart_page = ShoppingCartPage(self.browser)
        inventory_page.getbackpack()
        inventory_page.getshopping_cart()
        cart_page.get_checkout_button()
        log.info("Entering customer's information")
        cart_page.customer_fist_name().send_keys("Anton")
        cart_page.customer_last_name().send_keys("Vasya")
        cart_page.customer_zip_code().send_keys("95117")
        cart_page.get_continue_button()
        cart_page.get_finish_button()
        assert cart_page.get_thank_you_note() == "THANK YOU FOR YOUR ORDER"












