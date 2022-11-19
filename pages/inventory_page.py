from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    ADD_BIKE_LIGHT_BUTTON = (By.ID, "add-to-cart-labs-bike-light")
    REMOVE_BIKE_LIGHT_BUTTON = (By.ID, "remove-sauce-labs-bike-light")
    CART_BUTTON = (By.ID, 'shopping_cart_container')
    CART_BAGE = (By.CLASS_NAME, 'shopping_cart_badge')
    ALL_PRODUCTS = (By.CLASS_NAME, 'inventory_item_name')
    AZ_BUTTON = (
        By.XPATH,
        '//*[@id="header_container"]/div[2]/div[2]/span/select/option[1]',
    )
    ZA_BUTTON = (
        By.XPATH,
        '//*[@id="header_container"]/div[2]/div[2]/span/select/option[2]',
    )
    ASC_BUTTON = (
        By.XPATH,
        '//*[@id="header_container"]/div[2]/div[2]/span/select/option[3]',
    )
    DESC_BUTTON = (
        By.XPATH,
        '//*[@id="header_container"]/div[2]/div[2]/span/select/option[4]',
    )

    def add_to_cart(self):
        self.wait_until_clickable(self.ADD_BACKPACK_BUTTON).click()

    def button_text_before_adding(self):
        assert (
            'ADD TO CART' in self.wait_until_visible(self.ADD_BACKPACK_BUTTON).text
        ), "Incorrect text"

    def button_text_after_adding(self):
        assert (
            'REMOVE' in self.wait_until_visible(self.REMOVE_BACKPACK_BUTTON).text
        ), "Incorrect text"

    def bage_has_changed(self):
        assert '1' in self.wait_until_visible(self.CART_BAGE).text, "Incorrect count"

    def sort_by_AZ(self):
        self.wait_until_clickable(self.AZ_BUTTON).click()

    def sort_by_ZA(self):
        self.wait_until_clickable(self.ZA_BUTTON).click()

    def sort_by_ASC(self):
        self.wait_until_clickable(self.ASC_BUTTON).click()

    def sort_by_DESC(self):
        self.wait_until_clickable(self.DESC_BUTTON).click()

    def show_sorted_elements(self):
        sorted_list = []
        for option in self.elements_are_present(self.ALL_PRODUCTS):
            sorted_list.append(option.text)
        return sorted_list
