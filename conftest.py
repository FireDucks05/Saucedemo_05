import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
browser = None
url = "https://www.saucedemo.com/"

@pytest.fixture(scope="class")
def setup(request):
    global browser

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    browser =webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = "https://www.saucedemo.com/"
    browser.get(url)
    browser.implicitly_wait(5)
    request.cls.browser = browser
    yield
    browser.close()















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
