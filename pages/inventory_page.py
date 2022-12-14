from selenium.webdriver.common.by import By


class InventoryPage:

    def __init__(self, browser):
        self.browser = browser

    back_pack = (By.ID, "add-to-cart-sauce-labs-backpack")
    shopping_cart = (By.CLASS_NAME, 'shopping_cart_link')
    shopping_cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')


    def getbackpack(self):
        self.browser.find_element(*InventoryPage.back_pack).click()

    def getshopping_cart(self):
        self.browser.find_element(*InventoryPage.shopping_cart)

    def get_shopping_cart_badge(self):
        count_element = self.browser.find_element(*InventoryPage.shopping_cart_badge)
        count = count_element.text
        return count



