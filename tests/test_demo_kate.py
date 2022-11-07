from selenium.webdriver.common.by import By
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_login_standart():
    options = webdriver.ChromeOptions()
    options.headless = True
    # browser = webdriver.Firefox()
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # browser = webdriver.Chrome('/Users/sweed/PycharmProjects/SweedScripts/venv/lib/python3.10/site-packages/chromedriver_py/chromedriver_mac_arm64')
    browser.get('https://www.saucedemo.com/')
    browser.maximize_window()
    browser.find_element(By.ID, "user-name").send_keys('standard_user')
    browser.find_element(By.ID, "password").send_keys('secret_sauce')
    browser.find_element(By.ID, "login-button").send_keys('secret_sauce')
    browser.quit()
