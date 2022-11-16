import allure
import pytest

from pages.inventory_page import InventoryPage


class TestCartClass:

    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.inventory_page = InventoryPage(browser, url + 'inventory.html')


    @allure.epic('US_002.00')
    @allure.story('TC_002.00.01')
    @allure.title("Bage change when adding")
    def test_change_bage_when_adding(self, browser, url):
        with allure.step('step1 add to cart'):
            self.inventory_page.add_to_cart()
        with allure.step('step2 watch changes'):
            self.inventory_page.bage_has_changed()

    @allure.epic('US_002.00')
    @allure.story('TC_002.00.02')
    @allure.title("Button text after remove")
    def test_change_add_button_text(self, browser, url):
        with allure.step('step1 text before adding'):
            self.inventory_page.button_text_before_adding()
        with allure.step('step2 click on button'):
            self.inventory_page.add_to_cart()
        with allure.step('step3 text after adding'):
            self.inventory_page.button_text_after_adding()
