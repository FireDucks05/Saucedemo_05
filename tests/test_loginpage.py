import time
import pytest
from selenium.webdriver.common.by import By


# class LoggingIn:
#     def __init__(self, browser):
#         self.browser = browser
#
#     def logging_in(self):
#         self.browser.find_element(By.ID, "user-name").send_keys("standard_user")
#         self.browser.find_element(By.ID, "password").send_keys("secret_sauce")
#         self.browser.find_element(By.ID, "login-button").click()
#         user_logged_in = self.browser
#         return user_logged_in
#
#
# class TestLogin(LoggingIn):
#     @pytest.mark.smoke  # TC.001.00.01
#     def test_success_login(self, logging_in):
#         self.logging_in = logging_in
#         time.sleep(2)
#         assert 'inventory' in self.browser.current_url, 'wrong url'

@pytest.mark.smoke
def test_success_login(browser):
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    time.sleep(2)
    assert 'inventory' in browser.current_url, 'wrong url'


@pytest.mark.negative
def test_login_invalid_username(browser):
    browser.find_element(By.ID, "user-name").send_keys("standard_user1")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    error_message = browser.find_element(By.XPATH, "//*[@data-test='error']")
    time.sleep(2)
    assert error_message
