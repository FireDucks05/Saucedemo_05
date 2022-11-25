import allure
import pytest

from constants import SOTRING_AZ, SOTRING_ZA, SOTRING_PRICE_ASC, SOTRING_PRICE_DESC
from pages.inventory_page import InventoryPage


class TestCartClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.inventory_page = InventoryPage(browser, url + 'inventory.html')

    @allure.story('US_004.00 | Home Page > Filter > User is able to sort items by different metrics')
    @allure.title("Sort products A-Z")
    def test_sorting_az(self, browser, url):
        self.inventory_page.login_with_cookie()
        with allure.step('step1 add to cart'):
            self.inventory_page.sort_by_AZ()
        with allure.step('step2 check sotring'):
            assert self.inventory_page.show_sorted_elements() == SOTRING_AZ

    @allure.story('US_004.00 | Home Page > Filter > User is able to sort items by different metrics')
    @allure.title("Sort products Z-A")
    def test_sorting_za(self, browser, url):
        self.inventory_page.login_with_cookie()
        with allure.step('step1 add to cart'):
            self.inventory_page.sort_by_ZA()
        with allure.step('step2 check sotring'):
            assert self.inventory_page.show_sorted_elements() == SOTRING_ZA

    @allure.story('US_004.00 | Home Page > Filter > User is able to sort items by different metrics')
    @allure.title("Sort products ASC price")
    def test_sorting_asc(self, browser, url):
        self.inventory_page.login_with_cookie()
        with allure.step('step1 add to cart'):
            self.inventory_page.sort_by_ASC()
        with allure.step('step2 check sotring'):
            assert self.inventory_page.show_sorted_elements() == SOTRING_PRICE_ASC

    @allure.story('US_004.00 | Home Page > Filter > User is able to sort items by different metrics')
    @allure.title("Sort products DESC price")
    def test_sorting_desc(self, browser, url):
        self.inventory_page.login_with_cookie()
        with allure.step('step1 add to cart'):
            self.inventory_page.sort_by_DESC()
        with allure.step('step2 check sotring'):
            assert self.inventory_page.show_sorted_elements() == SOTRING_PRICE_DESC
