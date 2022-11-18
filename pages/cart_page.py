from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def checkout(self):
        self.wait_until_clickable(self.CHECKOUT_BUTTON).click()

