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

    def test_003_remove_items_cart(self,login):
        self.browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.browser.find_element(By.ID, "shopping_cart_container").click()
        self.browser.find_element(By.ID, "remove-sauce-labs-backpack").click()
        count = self.browser.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        assert count in "1"



