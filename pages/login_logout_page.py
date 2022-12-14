from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    username_field = (By.ID, 'user-name')
    password_field = (By.ID, 'password')
    login_button = (By.ID, 'login-button')
    burger_menu = (By.ID, 'react-burger-menu-btn')
    logout_button = (By.ID, 'logout_sidebar_link')

    def getlogin(self):
        self.browser.find_element(*LoginPage.username_field).send_keys('standard_user')
        self.browser.find_element(*LoginPage.password_field).send_keys('secret_sauce')
        self.browser.find_element(*LoginPage.login_button).click()

    def getlogout(self):
        self.browser.find_element(*LoginPage.burger_menu).click()
        self.browser.find_element(*LoginPage.logout_button).click()


