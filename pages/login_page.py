from selenium.webdriver.common.by import By


class LoginPage:

    def __int__(self, browser):
        self.browser = browser

    username_field = (By.ID, 'user-name')
    password_field = (By.ID, 'password')
    login_button = (By.ID, 'login-button')

    def getlogin(self):
        return self.browser.find_element(*LoginPage.username_field)

    def getpassword(self):
        return self.browser.find_element(*LoginPage.password_field)

    def getfield(self):
        return self.browser.find_element(*LoginPage.login_button)


