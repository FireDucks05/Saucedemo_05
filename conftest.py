import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def set_chrome_options():
    # options.add_argument("--headless")
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-setuid-sandbox")
    return options


@pytest.fixture(scope="function")
def driver_init(set_chrome_options):
    options = set_chrome_options
    chrome_driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    # browser.maximize_window()
    yield chrome_driver
    chrome_driver.quit()
