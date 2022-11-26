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
        self.browser.find_element(By.ID, "remove-sauce-labs-backpack").click()
        self.browser.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(2)
        self.browser.find_element(By.ID, "logout_sidebar_link").click()

    def test_002_001_add_items_to_cart(self,login):
        self.browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        count = self.browser.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        assert count in "1"

    def test_002_add_button_changed_to_remove(self,login):
        self.browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        count = self.browser.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        assert count in "1"
        remove_button = self.browser.find_element(By.ID,"remove-sauce-labs-backpack").text
        assert "REMOVE" in remove_button

    def test_003_add_button_changed(self, login):
        item  = self.broweser.find_element(By.ID, "")


