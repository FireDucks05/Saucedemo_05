import pytest
import time
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestLoginPage:
    @pytest.fixture(scope="function")
    def login(self):
        self.browser.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.browser.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.browser.find_element(By.ID, 'login-button').click()
        yield
        self.browser.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(2)
        self.browser.find_element(By.ID, "logout_sidebar_link").click()

    def test_001_login(self, login):
        page = "https://www.saucedemo.com/inventory.html"
        assert page == 'https://www.saucedemo.com/inventory.html'

    def test_logout(self, login):

        page = "https://www.saucedemo.com/"
        assert page == "https://www.saucedemo.com/"


