from selenium.webdriver.common.by import By

from pages.product_page import ProductPage


class TestInventory:

    def test_002_001_add_items_to_cart(self):
        productpage = ProductPage()
        productpage.getbackpack().click
        count = productpage.getshopping_cart().text
        assert count in "1"

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