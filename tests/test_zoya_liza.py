from selenium.webdriver.common.by import By
import pytest
import time
from webbrowser import BaseBrowser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

HOME_LINK = "https://www.saucedemo.com/"
INVENTORY_LINK = 'https://www.saucedemo.com/inventory.html'
login_txt = 'standard_user'
password_txt = 'secret_sauce'

HOME_LINK__ = "https://www.saucedemo.com/"
INVENTORY_LINK__ = 'https://www.saucedemo.com/inventory.html'
login_txt__ = 'standard_user'
password_txt__ = 'secret_sauce'

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.saucedemo.com/")
time.sleep(5)


def test_login():
    driver.get(HOME_LINK)
    driver.find_element(By.ID, 'user-name').send_keys(login_txt)
    driver.find_element(By.ID, 'password').send_keys(password_txt)
    driver.find_element(By.ID, 'login-button').click()
    assert driver.current_url == INVENTORY_LINK
