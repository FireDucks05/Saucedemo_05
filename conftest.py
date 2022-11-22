import logging

import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(autouse=True)
def browser(request, headless):
    browser = request.config.getoption("--launch")
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = headless
    logging.info('start logs')
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield browser
    logging.info('end logs')
    browser.quit()


@pytest.fixture(autouse=True)
def url():
    url = "https://www.saucedemo.com/"
    if not url:
        raise Exception("Wrong environment")
    return url


def pytest_addoption(parser):
    parser.addoption(
        "--launch",
        default="chrome",
        help="define browser: chrome or firefox, --browser=chrome",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="headless mode on or off, --headless",
    )


@pytest.fixture(scope='class')
def headless(request):
    return request.config.getoption("--headless")
