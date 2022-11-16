# TC_008.00.01,02,03 | Checkout page > Cancel Checkout

import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')

driver_service = Service(ChromeDriverManager().install(), options=options)
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()

link = "https://www.saucedemo.com/"
browser.get(link)

login = "standard_user"
password = "secret_sauce"


@pytest.fixture(scope="function")
def login_cred():
    browser.find_element(By.ID, 'user-name').send_keys(login)
    browser.find_element(By.ID, 'password').send_keys(password)
    browser.find_element(By.ID, 'login-button').click()


@pytest.fixture(scope="function")
def product_selection():
    time.sleep(5)
    browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    browser.find_element(By.ID, "checkout").click()
    assert browser.current_url == "https://www.saucedemo.com/checkout-step-one.html"


@pytest.fixture(scope="function")
def customer_name():
    browser.find_element(By.ID, "first-name").send_keys("Vasya")
    browser.find_element(By.ID, "last-name").send_keys("Ivanov")
    browser.find_element(By.ID, "postal-code").send_keys("94939")
    

def test_ckeckout_form_stepone_cancel():
    first_name = driver.find_element(By.ID, 'first-name')
    first_name.send_keys('Elena')

    last_name = driver.find_element(By.ID, 'last-name')
    last_name.send_keys('Smith')

    postal_code = driver.find_element(By.ID, 'postal-code')
    postal_code.send_keys('692522')

    button_cancel = driver.find_element(By.ID, 'cancel')
    button_cancel.click()
    assert driver.current_url == 'https://www.saucedemo.com/cart.html', 'You reached to another page'


def test_008_00_01_dont_fill_form(login_cred, product_selection):
    browser.find_element(By.ID, "cancel").click()
    assert browser.current_url == "https://www.saucedemo.com/cart.html"
    browser.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(2)
    browser.find_element(By.ID, "logout_sidebar_link").click()


def test_008_00_02_fill_form(login_cred, product_selection, customer_name):
    browser.find_element(By.ID, "continue").click()
    browser.find_element(By.ID, "cancel").click()
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"
    
driver.quit()
