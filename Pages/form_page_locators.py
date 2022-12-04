from selenium.webdriver.common.by import By
from random import randint

class FormPageLocators:
    USER_NAME = (By.CSS_SELECTOR, '#ueser-name')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    LOGIN = (By.CSS_SELECTOR, 'input[id="login-batton"]')

    RESULT_TABLE = (By.XPATH, '//div[@class="login_credentials_wrap-inner"]//br[1]' )