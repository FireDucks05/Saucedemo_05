from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(ChromeDriverManager().install())
HOME_LINK = "https://www.saucedemo.com/"
INVENTORY_LINK = 'https://www.saucedemo.com/inventory.html'
# USERNAME_FIELD = By.ID, 'user-name'
# PASSWORD_FIELD = By.ID, 'password'
# LOGIN_BTN = By.ID, 'login-button'
login_txt = 'standard_user'
password_txt = 'secret_sauce'


def test_login():
    driver.get(HOME_LINK)
    # el = WebDriverWait(driver, 7).until(element_to_be_selected(USERNAME_FIELD))
    driver.find_element(By.ID, 'user-name').send_keys(login_txt)
    driver.find_element(By.ID, 'password').send_keys(password_txt)
    driver.find_element(By.ID, 'login-button').click()
    assert driver.current_url == INVENTORY_LINK
