import pytest
import time
from selenium.webdriver.common.by import By

class TestInventory:

    def test_006_checkout_item(self,browser):
        browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        browser.find_element(By.ID, "shopping_cart_container").click()
        browser.find_element(By.ID, "checkout").click()
        browser.find_element(By.ID, "first-name").send_keys("Vasya")
        browser.find_element(By.ID, "last-name").send_keys("Ivanov")
        browser.find_element(By.ID, "postal-code").send_keys("95117")
        browser.find_element(By.ID, "continue").click()
        browser.find_element(By.ID, "finish").click()
        message = browser.find_element(By.CLASS_NAME, "complete-header").text
        assert "THANK YOU FOR YOUR ORDER" in message



