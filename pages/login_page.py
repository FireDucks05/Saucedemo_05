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

    def getloginbutton(self):
        return self.browser.find_element(*LoginPage.login_button).click()


from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckOutPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.CSS_SELECTOR, 'input[name ="name"]')
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By. ID, "exampleFormControlSelect1")
    submit = (By.XPATH, '//input[@type= "submit"]')
    message = (By.CLASS_NAME, "alert-success")


    def shopItems(self):
       self.driver.find_element(*HomePage.shop).click()
       checkOutPage = CheckOutPage(self.driver)
       return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.message)
