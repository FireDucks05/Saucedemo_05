from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    HEADER_LOGO = (By.CLASS_NAME, "app_logo")
    ERROR_BTN = (By.CLASS_NAME, 'error-button')

    def login_ui(self, user: str, password: str) -> None:
        self.wait_until_clickable(self.LOGIN_FIELD).send_keys(user)
        self.wait_until_clickable(self.PASSWORD_FIELD).send_keys(password)
        self.wait_until_clickable(self.LOGIN_BUTTON).click()

    def check_user_is_authorized(self):
        assert self.element_is_present(self.HEADER_LOGO), "Logo is missing"

    def user_successfully_authorized(self):
        assert self.browser.page_is_open(url="https://www.saucedemo.com/inventory.html")

    def impossibility_auth(self):
        assert self.element_is_present(self.ERROR_BTN), 'Auth successful'
