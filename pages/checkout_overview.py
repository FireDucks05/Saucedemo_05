from selenium.webdriver.common.by import By


class CheckOutOverviewPage:

    def __int__(self, browser):
        self.browser = browser

    finish_button = (By.ID, "finish")
    cancel_button = (By.ID, "")