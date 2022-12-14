import pytest
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage
from pages.login_logout_page import LoginPage
from utilities.BaseClass import BaseClass
from utilities.login_logout import LoginLogout
from conftest import url


@pytest.mark.usefixtures("setup")
class TestInventory(BaseClass):

    def test_add_items_to_cart(self):
        log = self.getLogger()
        loginpage = LoginLogout(self.browser)
        loginpage.login_logout_wrapper()
        inventorypage = InventoryPage(self.browser)
        log.info("adding item to cart")

        inventorypage.getbackpack()
        assert "1" in inventorypage.get_shopping_cart_badge()

        assert url == "https://www.saucedemo.com/"

    def test_002_add_button_changed_to_remove(self, browser):
        browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        count = browser.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        assert count in "1"
        remove_button = browser.find_element(By.ID, "remove-sauce-labs-backpack").text
        assert "REMOVE" in remove_button

# class ProductPage:
#
#     def __int__(self, browser):
#         self.browser = browser
#
#     shopping_cart = (By.CLASS_NAME, 'shopping_cart_link')
#
#     def getshopping_cart(self):
#         return self.browser.find_element(*ProductPage.shopping_cart)
