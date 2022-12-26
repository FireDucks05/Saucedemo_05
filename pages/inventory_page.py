from selenium.webdriver.common.by import By


class InventoryPage:

    def __init__(self, browser):
        self.browser = browser

    add_back_pack = (By.ID, 'add-to-cart-sauce-labs-backpack')
    remove_back_pack = (By.ID, 'remove-sauce-labs-backpack')
    shopping_cart = (By.CLASS_NAME, 'shopping_cart_link')
    #shopping_cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')
    shopping_cart_badge = (By.XPATH, "//*[@id='shopping_cart_container']/a/span")
    drop_down_menu = (By.CLASS_NAME, 'product_sort_container')
    #all_products = (By.CLASS_NAME, 'inventory_item_name')
    all_products = (By.XPATH, "//div[@class = 'inventory_item_name']")
    all_products_list = (By.XPATH,"//div[@class = 'inventory_item']")
    add_button = (By.XPATH, "//button[@class = 'btn btn_primary btn_small btn_inventory']")
    back_pack_description = (By.CLASS_NAME, 'inventory_item_desc')
    item_desc = (By.XPATH, '//div[@class = "inventory_item_desc"]')

    def getbackpack(self):
        self.browser.find_element(*InventoryPage.add_back_pack).click()

    def getbackpack_button_text(self):
        add_to_cart = self.browser.find_element(*InventoryPage.add_back_pack)
        add_to_cart_text = add_to_cart.text
        return add_to_cart_text

    def getremove_button(self):
        self.browser.find_element(*InventoryPage.remove_back_pack).click()

    def getremove_button_text(self):
        remove_text = self.browser.find_element(*InventoryPage.remove_back_pack)
        text = remove_text.text
        return text

    def getshopping_cart(self):
        self.browser.find_element(*InventoryPage.shopping_cart).click()

    def getshopping_cart_badge(self):
        count_element = self.browser.find_element(*InventoryPage.shopping_cart_badge)
        count = count_element.text
        return count

    def getdrop_down_menu(self):
        return self.browser.find_element(*InventoryPage.drop_down_menu)

    def getall_products(self):
        return self.browser.find_elements(*InventoryPage.all_products)

    def get_all_products_text(self):
        text = self.browser.find_element(*InventoryPage.all_products)
        productName_text = text
        return productName_text

    def getproduct_description(self):
        description = self.browser.find_element(*InventoryPage.back_pack_description)
        description_text = description.text
        return description_text

    def get_allproduct_list(self):
        return self.browser.find_elements(*InventoryPage.all_products_list)

    def get_add_products(self):
        self.browser.find_element(*InventoryPage.add_button).click()

    def get_item_description(self):
        return self.browser.find_elements(*InventoryPage.item_desc)




