from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    FIRST_NAME_BUTTON = (By.ID, "first-name")
    LAST_NAME_BUTTON = (By.ID, "last-name")
    POSTAL_CODE_BUTTON = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MSG = (By.XPATH, "//h3")


    def input_your_informarion(self, first_name: str, last_name: str, zip: str):
        self.wait_until_clickable(self.FIRST_NAME_BUTTON).send_keys(first_name)
        self.wait_until_clickable(self.LAST_NAME_BUTTON).send_keys(last_name)
        self.wait_until_clickable(self.POSTAL_CODE_BUTTON).send_keys(zip)
        self.wait_until_clickable(self.CONTINUE_BUTTON).click()

    def error_when_empty_required_fied(self):
        assert not self.element_is_present(self.ERROR_MSG)

    def check_post_is_deleted(self, title):
        assert "Error: reFirst Name is required" == self.wait_until_visible(
            self.ERROR_MSG).text, "Error message hasn't been displayed"
        assert not self.element_is_present((
        By.XPATH, "//*[contains(text(), 'Error')]")), "Error message hasn been displayed"
