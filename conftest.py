import pytest
import time
from selenium import webdriver
from pages import login_page
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.headless = False
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return browser

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



