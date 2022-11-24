import pytest
from selenium.webdriver.common.by import By

from pages import login_page
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLoginPage:
    @pytest.fixture(scope="function")
    def login(self):
        self.browser.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.browser.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.browser.find_element(By.ID, 'login-button').click()


    def test_login(self,login):
        page = "https://www.saucedemo.com/inventory.html"
        assert page == 'https://www.saucedemo.com/inventory.html'

    def test_logout(self):



