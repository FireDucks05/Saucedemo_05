import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


'''Initializing browser'''
@pytest.fixture(autouse=True)
def browser(request, headless):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = headless
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    yield browser
    browser.quit()

'''Add URL'''
# @pytest.fixture(autouse=True)
# def url():
#     url = "https://www.saucedemo.com/"
#     if not url:
#         raise Exception("Wrong environment")
#     return url

'''Opportunity to launch background mode'''
def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="headless mode on or off, --headless")


'''System fixture for string parsing'''
@pytest.fixture()
def headless(request):
    return request.config.getoption("--headless")
