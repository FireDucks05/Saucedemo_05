
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from constants import VALID_BROWSERS


# @pytest.fixture(autouse=True)
# def browser(request):
#     browser = request.config.getoption("--browser")
#     if browser == "firefox":
#         options = webdriver.FirefoxOptions()
#         options.add_argument("--window-size=1600,1080")
#         options.headless = True
#
#         browser = webdriver.Firefox(
#             service=FirefoxService(GeckoDriverManager().install()), options=options
#         )
#         yield browser
#         browser.quit()
#     else:
#         options = webdriver.ChromeOptions()
#         options.add_argument("--window-size=1600,1080")
#         options.headless = False
#         browser = webdriver.Chrome(
#             service=Service(ChromeDriverManager().install()), options=options
#         )
#         yield browser
#         browser.quit()


@pytest.fixture(autouse=True)
def url():
    url = "https://www.saucedemo.com/"
    if not url:
        raise Exception("Wrong environment")
    return url


def pytest_addoption(parser):
    parser.addoption("--launch", default="chrome", choices=["chrome", "firefox"])


@pytest.fixture(autouse=True)
def browser(request):
    launch = request.config.getoption("--launch")
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = True
    browser = VALID_BROWSERS[launch]()
    # browser = webdriver.Chrome(
    # service=Service(ChromeDriverManager().install()), options=options)
    yield browser
    # browser = VALID_BROWSERS[browser]()
    # browser.maximize_window()
    # yield browser
    browser.quit()
