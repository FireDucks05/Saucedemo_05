from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    HEADER_LOGO = (By.CLASS_NAME, "app_logo")

    def login_ui(self, user: str, password: str) -> None:
        self.wait_until_clickable(self.LOGIN_FIELD).send_keys(user)
        self.wait_until_clickable(self.PASSWORD_FIELD).send_keys(password)
        self.wait_until_clickable(self.LOGIN_BUTTON).click()

    def check_user_is_authorized(self):
        assert self.element_is_present(self.HEADER_LOGO), "Logo is missing"
