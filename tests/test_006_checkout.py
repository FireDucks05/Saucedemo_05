import pytest
import time
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestInventory:
    @pytest.fixture(scope="function")
    def login(self):
        self.browser.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.browser.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.browser.find_element(By.ID, 'login-button').click()
        yield

        self.browser.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(2)
        self.browser.find_element(By.ID, "logout_sidebar_link").click()

    def test_006_checkout_item(self,login):
        self.browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.browser.find_element(By.ID, "shopping_cart_container").click()
        self.browser.find_element(By.ID, "checkout").click()
        self.browser.find_element(By.ID, "first-name").send_keys("Vasya")
        self.browser.find_element(By.ID, "last-name").send_keys("Ivanov")
        self.browser.find_element(By.ID, "postal-code").send_keys("95117")
        self.browser.find_element(By.ID, "continue").click()
        self.browser.find_element(By.ID, "finish").click()
        message = self.browser.find_element(By.CLASS_NAME, "complete-header").text
        assert "THANK YOU FOR YOUR ORDER" in message



