import pytest
import time
from selenium.webdriver.common.by import By
from conftest import *


@pytest.mark.usefixtures("setup")
@pytest.fixture(scope="function")
def login(setup):
    browser.find_element(By.ID, 'user-name').send_keys('standard_user')
    browser.find_element(By.ID, 'password').send_keys('secret_sauce')
    browser.find_element(By.ID, 'login-button').click()


@pytest.fixture(scope="function")
def logout(setup):
    browser.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(2)
    browser.find_element(By.ID, "logout_sidebar_link").click()
