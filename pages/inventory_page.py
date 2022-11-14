from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bike-light")
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-bike-light")
    CART_BUTTON = (By.ID, 'shopping_cart_container')
    CART_BAGE = (By.CLASS_NAME, 'shopping_cart_badge')

    def add_to_cart(self):
        self.wait_until_clickable(self.ADD_BUTTON).click()

    def button_text_before_adding(self):
        assert 'ADD TO CART' in self.wait_until_visible(
            self.ADD_BUTTON).text, \
            "Incorrect text"

    def button_text_after_adding(self):
        assert 'REMOVE' in self.wait_until_visible(
            self.REMOVE_BUTTON).text, \
            "Incorrect text"

    def go_to_cart(self):
        self.wait_until_clickable(self.CART_BUTTON).click()

    def bage_has_changed(self):
        assert '1' in self.wait_until_visible(
            self.CART_BAGE).text, \
            "Incorrect count"