import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture
def get_chrome_options():
    options = ChromeOptions()
    options.add_argument("--window-size=1200,800")
    options.headless = False
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    return driver


@pytest.fixture(scope='function', autouse=True)
def browser(request, get_webdriver):
    print('\nstart browser...')
    driver = get_webdriver
    url = 'https://www.saucedemo.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    print('\nquit browser...')
    driver.quit()
