from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    username_field = (By.ID, 'user-name')
    password_field = (By.ID, 'password')
    login_button = (By.ID, 'login-button')
    burger_menu = (By.ID, 'react-burger-menu-btn')
    logout_button = (By.ID, 'logout_sidebar_link')

    def getlogin(self):
        self.driver.find_element(*HomePage.username_field).send_keys('standard_user')

        self.driver.find_element(*HomePage.password_field).send_keys('secret_sauce')

        self.driver.find_element(*HomePage.login_button).click()

    # def getlogin(self):
    #     return self.driver.find_element(*HomePage.username_field).send_keys('standard_user')
    #
    # def getpassword(self):
    #     return self.driver.find_element(*HomePage.password_field).send_keys('secret_sauce')
    #
    # def getloginbutton(self):
    #     return self.driver.find_element(*HomePage.login_button).click()
    def getlogout(self):
        self.driver.find_element(*HomePage.burger_menu).click()
        self.driver.find_element(*HomePage.logout_button).click()


    print(type(login_button))
    print(type(burger_menu))
