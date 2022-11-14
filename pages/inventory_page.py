from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bike-light")

    def add_to_cart(self):
        self.wait_until_clickable(self.ADD_BUTTON).click()

    def button_text_before_adding(self):
        assert 'ADD TO CART' in self.wait_until_visible(
            self.ADD_BUTTON).text, \
            "Incorrect text"

    def button_text_after_adding(self):
        assert 'REMOVE' in self.wait_until_visible(
            self.ADD_BUTTON).text, \
            "Incorrect text"