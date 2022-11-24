from selenium.webdriver.common.by import By


class CustomerInfo_Page:

    def __int__(self, browser):
        self.browser = browser

    customer_firstname = (By.ID, "first-name")
    customer_lastname = (By.ID, "last-name")
    customer_zip = (By.ID, "postal-code")