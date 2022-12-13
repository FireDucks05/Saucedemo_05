import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global browser
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        s = Service("/Users/abloha/selenium/chromedriver")
        browser = webdriver.Chrome(service=s)

    elif browser_name == "firefox":
        s = Service("/Users/abloha/selenium/geckodriver")
        browser = webdriver.Firefox(service=s)

    browser.get("https://www.saucedemo.com/")
    browser.maximize_window()
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
