import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_logout_page import LoginPage




browser = None
homepage = "https://www.saucedemo.com/"

@pytest.fixture(scope="class")
def setup(request):
    global browser

    options = webdriver.ChromeOptions()
    options.headless = False
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    url = homepage
    browser.get(url)
    browser.implicitly_wait(5)
    request.cls.browser = browser
    yield
    browser.close()



@pytest.fixture(autouse=True)

def login(setup):

# username_field = (By.ID, 'user-name')
# password_field = (By.ID, 'password')
# login_button = (By.ID, 'login-button')
# burger_menu = (By.ID, 'react-burger-menu-btn')
# logout_button = (By.ID, 'logout_sidebar_link')
    browser.find_element(*LoginPage.username_field).send_keys('standard_user')
    browser.find_element(*LoginPage.password_field).send_keys('secret_sauce')
    browser.find_element(*LoginPage.login_button).click()






# @pytest.fixture(autouse=True)
# def login(browser):
#     browser.get("https://www.saucedemo.com/")
#     browser.find_element(By.ID, 'user-name').send_keys('standard_user')
#     browser.find_element(By.ID, 'password').send_keys('secret_sauce')
#     browser.find_element(By.ID, 'login-button').click()
#     yield browser
#     browser.find_element(By.ID, "react-burger-menu-btn").click()
#     time.sleep(2)
#     browser.find_element(By.ID, "logout_sidebar_link").click()
#     browser.quit()



    # options = webdriver.ChromeOptions()
    # options.headless = False
    # browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # return browser
