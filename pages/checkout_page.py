from selenium.webdriver.common.by import By


class CheckOut_Page:

    def __int__(self, browser):
        self.browser = browser

    continue_shopping = (By.ID, 'continue-shopping')
    checkout_button = (By. ID, 'checkout')
