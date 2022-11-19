from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    FINISH_BUTTON = (By.ID, "finish")

    def finish_order(self):
        self.wait_until_clickable(self.FINISH_BUTTON).click()

    def successfully_message_is_present(self):
        assert self.wait_for_url_to_be(
            'https://www.saucedemo.com/checkout-complete.html'
        )
