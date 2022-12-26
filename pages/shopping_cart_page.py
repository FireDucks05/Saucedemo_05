from selenium.webdriver.common.by import By


class ShoppingCartPage:

    def __init__(self, browser):
        self.browser = browser

    item_inventory_desc = (By.CLASS_NAME, 'inventory_item_desc')
    checkout_button = (By.ID, 'checkout')
    finish_button = (By.ID, 'finish')
    continue_button = (By.ID, 'continue')
    your_information = (By.CLASS_NAME, 'title')
    first_name = (By.ID, 'first-name')
    last_name = (By.ID, 'last-name')
    zip_code = (By.ID, 'postal-code')
    thank_you_note = (By.CLASS_NAME, 'complete-header')


    def getitem_inventory_desc(self):
        desc_text = self.browser.find_element(*ShoppingCartPage.item_inventory_desc)
        item_inventory_desc = desc_text.text
        return item_inventory_desc

    def get_checkout_button(self):
        self.browser.find_element(*ShoppingCartPage.checkout_button).click()

    def get_finish_button(self):
        self.browser.find_element(*ShoppingCartPage.finish_button).click()

    def get_checkout_info_text(self):
        checkout_info = self.browser.find_element(*ShoppingCartPage.your_information)
        your_information_checkout = checkout_info.text
        return your_information_checkout

    def customer_fist_name(self):
        return self.browser.find_element(*ShoppingCartPage.first_name)

    def customer_last_name(self):
        return self.browser.find_element(*ShoppingCartPage.last_name)

    def customer_zip_code(self):
        return self.browser.find_element(*ShoppingCartPage.zip_code)

    def get_thank_you_note(self):
        thank_you_note = self.browser.find_element(*ShoppingCartPage.thank_you_note)
        thank_you_note_text = thank_you_note.text
        return thank_you_note_text

    def get_continue_button(self):
        self.browser.find_element(*ShoppingCartPage.continue_button).click()





