from selenium.webdriver.common.by import By


class TestInventory:

    def test_002_001_add_items_to_cart(self, browser):
        browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        count = browser.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        assert count in "1"

    def test_002_add_button_changed_to_remove(self, browser):
        browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        count = browser.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        assert count in "1"
        remove_button = browser.find_element(By.ID, "remove-sauce-labs-backpack").text
        assert "REMOVE" in remove_button
