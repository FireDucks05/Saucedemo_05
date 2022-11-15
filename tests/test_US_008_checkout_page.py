# TC_008.00.02 | Checkout page > Cancel Checkout > Fill form

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()
driver.get("https://www.saucedemo.com/checkout-step-one.html")

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


driver.quit()
