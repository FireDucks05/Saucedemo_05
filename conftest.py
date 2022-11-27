import pytest
from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.headless = False
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    return browser


    #request.cls.browser = browser



@pytest.fixture(autouse=True)
def login(browser):
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, 'user-name').send_keys('standard_user')
    browser.find_element(By.ID, 'password').send_keys('secret_sauce')
    browser.find_element(By.ID, 'login-button').click()
    yield browser
    browser.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(2)
    browser.find_element(By.ID, "logout_sidebar_link").click()
    browser.quit()