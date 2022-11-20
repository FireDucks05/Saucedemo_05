import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

'''Initializing browser'''
@pytest.fixture(autouse=True)
def browser(request):
    browser = request.config.getoption("--browser")
    options = webdriver.FirefoxOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = True
    browser = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()), options=options
    )
    yield browser
    browser.quit()

'''Add URL'''
@pytest.fixture(autouse=True)
def url():
    url = "https://www.saucedemo.com/"
    if not url:
        raise Exception("Wrong environment")
    return url

'''Opportunity to launch background mode'''
def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="headless mode on or off, --headless")


'''System fixture for string parsing'''
@pytest.fixture(scope='class')
def headless(request):
    return request.config.getoption("--headless")
