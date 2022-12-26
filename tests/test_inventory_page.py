import time
import pytest
from pages.inventory_page import InventoryPage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select
from utilities.inventory import sorted_Z_to_A, sorted_A_to_Z, sorted_low_to_high, sorted_high_to_low




@pytest.mark.usefixtures("setup")
class TestInventory(BaseClass):

    def test_add_items_to_cart(self):
        log = self.getLogger()
        inventory_page = InventoryPage(self.browser)
        log.info("adding item to cart")
        inventory_page.getbackpack()
        assert "1" in inventory_page.getshopping_cart_badge()
        inventory_page.getremove_button()


    def test_add_button_changed_to_remove(self):
        log = self.getLogger()
        inventory_page = InventoryPage(self.browser)
        log.info("adding item to cart")
        inventory_page.getbackpack()
        log.info("checking if quantity change cart badge")
        assert "1" in inventory_page.getshopping_cart_badge()
        inventory_page.getremove_button_text()
        log.info("checking if add button changed to remove")
        assert "REMOVE" in inventory_page.getremove_button_text()
        inventory_page.getremove_button()

    def test_remove_items_from_cart(self):
        log = self.getLogger()
        inventory_page = InventoryPage(self.browser)
        log.info("adding item to cart")
        inventory_page.getbackpack()
        time.sleep(2)
        log.info("checking if quantity change cart badge")
        assert "1" in inventory_page.getshopping_cart_badge()
        inventory_page.getremove_button()
        log.info("checking if remove button changed to 'ADD TO CART'")
        assert "ADD TO CART" in inventory_page.getbackpack_button_text()


    def test_sorting_inventory_sorting_Z_to_A(self):
        log = self.getLogger()
        inventory_page = InventoryPage(self.browser)
        log.info("sorting inventory Z to A")
        dropdown = Select(inventory_page.getdrop_down_menu())
        dropdown.select_by_visible_text("Name (Z to A)")
        ALL_PRODUCTS = inventory_page.getall_products()
        sorted_list = []
        for option in ALL_PRODUCTS:
            sorted_list.append(option.text)

        log.info("Verifying that inventory sorted to Z to A")
        assert sorted_list == sorted_Z_to_A

    def test_sorting_inventory_low_to_high(self):
        log = self.getLogger()
        inventory_page = InventoryPage(self.browser)
        log.info("sorting inventory low to high")
        dropdown = Select(inventory_page.getdrop_down_menu())
        dropdown.select_by_visible_text("Price (low to high)")
        ALL_PRODUCTS = inventory_page.getall_products()
        sorted_list = []
        for option in ALL_PRODUCTS:
            sorted_list.append(option.text)

        log.info("Verifying that inventory sorted low to high")
        assert sorted_list == sorted_low_to_high

    def test_sorting_inventory_high_to_low(self):
        log = self.getLogger()
        inventory_page = InventoryPage(self.browser)
        log.info("sorting inventory high to low")
        dropdown = Select(inventory_page.getdrop_down_menu())
        dropdown.select_by_visible_text("Price (high to low)")
        ALL_PRODUCTS = inventory_page.getall_products()
        sorted_list = []
        for option in ALL_PRODUCTS:
            sorted_list.append(option.text)

        log.info("Verifying that inventory sorted high to low")
        assert sorted_list == sorted_high_to_low

    def test_verification_desc(self):
        log = self.getLogger()
        inventory_page = InventoryPage(self.browser)
        log.info("adding inventory description into list")
        products = inventory_page.getall_products()
        for product in products:
            productName = inventory_page.get_all_products_text()

            if productName == "Sauce Labs Backpack":
                product.inventorypage.get_add_products()
        lst = []
        pr = inventory_page.get_item_description()
        for itemss in pr:
            lst.append(itemss.text)
        print(lst)






