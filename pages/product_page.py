from selenium.webdriver.common.by import By


class ProductPage:

    def __int__(self, browser):
        self.browser = browser

    shopping_cart = (By.CLASS_NAME, 'shopping_cart_link')
    back_pack = (By.ID, "add-to-cart-sauce-labs-backpack")

    def getshopping_cart(self):
        return self.browser.find_element(*ProductPage.shopping_cart)

    def getbackpack(self):
        return self.browser.find_element(*ProductPage.back_pack)

