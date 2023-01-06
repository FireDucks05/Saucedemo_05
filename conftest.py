import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from pages.login_logout_page import LoginPage

browser = None
homepage = "https://www.saucedemo.com/"

@pytest.fixture(scope="class")
def setup(request):

    global browser

    options = webdriver.ChromeOptions()
    options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    url = homepage
    browser.get(url)
    browser.implicitly_wait(5)
    request.cls.browser = browser
    yield
    browser.quit()


@pytest.fixture(autouse=True)
def login(setup):
    browser.find_element(*LoginPage.username_field).send_keys('standard_user')
    browser.find_element(*LoginPage.password_field).send_keys('secret_sauce')
    browser.find_element(*LoginPage.login_button).click()
    yield browser
    browser.find_element(*LoginPage.burger_menu).click()
    time.sleep(2)
    browser.find_element(*LoginPage.logout_button).click()


#
# def pytest_html_report_title(report):
#     report.title = "Tony B"