from selenium.webdriver.common.by import By

class TestInventory:

    def test_007_002_checkout_item_skip_zipcode(self, browser):
        browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        browser.find_element(By.ID, "shopping_cart_container").click()
        browser.find_element(By.ID, "checkout").click()
        browser.find_element(By.ID, "first-name").send_keys("Vasya")
        browser.find_element(By.ID, "last-name").send_keys("Ivanov")
        browser.find_element(By.ID, "continue").click()
        error_message = browser.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        assert "Error: Postal Code is required" in error_message


    def test_007_003_checkout_item_skip_lastname(self, browser):
        browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        browser.find_element(By.ID, "shopping_cart_container").click()
        browser.find_element(By.ID, "checkout").click()
        browser.find_element(By.ID, "first-name").send_keys("Vasya")
        browser.find_element(By.ID, "postal-code").send_keys("95117")
        browser.find_element(By.ID, "continue").click()
        error_message = browser.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        assert "Error: Last Name is required" in error_message


