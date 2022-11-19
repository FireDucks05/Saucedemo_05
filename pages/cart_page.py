from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BUTTON = (By.ID, 'remove-sauce-labs-bike-light')
    CONTINUE_SHOPPING_BUTTON = (By.ID, 'continue-shopping')

    def checkout(self):
        self.wait_until_clickable(self.CHECKOUT_BUTTON).click()

    def remove(self):
        self.wait_until_clickable(self.REMOVE_BUTTON)

    def continue_shopping(self):
        self.wait_until_clickable(self.CONTINUE_SHOPPING_BUTTON)
