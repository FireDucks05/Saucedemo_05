from selenium.webdriver import Keys
from Pages.base_page import BasePage
from Pages.form_page_locators import FormPageLocators as Locators
import time


class FormPage(BasePage):

    def fill_field_and_submit(self):
        username = "standard_user"
        password = "secret_sauce"
        self.element_is_visible(Locators.USER_NAME).send_keys(username)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.LOGIN).click()
        return username, password

    def form_result(self):
        result_list = self.element_are_visible(Locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]
        return result_text
