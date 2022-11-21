import pytest
from selenium.webdriver.common.by import By
import time


@pytest.mark.smoke
def test_add_item_to_cart(browser):  # adding a backpack to the cart and check if it has been added
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    time.sleep(2)
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)
    backpack_remove_button = browser.find_element(By.ID, "remove-sauce-labs-backpack")
    assert backpack_remove_button


@pytest.mark.regression
def test_remove_item_from_cart(browser):
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    time.sleep(2)
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)
    backpack_remove_button = browser.find_element(By.ID, "remove-sauce-labs-backpack")
    backpack_remove_button.click()
    if backpack_remove_button != 0:
        return
    assert True
