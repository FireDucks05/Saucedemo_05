import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    FIRST_NAME_BUTTON = (By.ID, "first-name")
    LAST_NAME_BUTTON = (By.ID, "last-name")
    POSTAL_CODE_BUTTON = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")


    def input_your_informarion(self, first_name: str, last_name: str, zip :str):
        self.wait_until_clickable(self.FIRST_NAME_BUTTON).send_keys(first_name)
        time.sleep(3)
        self.wait_until_clickable(self.LAST_NAME_BUTTON).send_keys(last_name)
        time.sleep(3)
        self.wait_until_clickable(self.POSTAL_CODE_BUTTON).send_keys(zip)
        time.sleep(3)
        self.wait_until_clickable(self.CONTINUE_BUTTON).click()


