from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--headless")


@pytest.fixture(autouse=True)
def driver():
    driver_service = Service(ChromeDriverManager().install(), options=options)
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def url():
    url = "https://www.saucedemo.com/"
    if not url:
        raise Exception("Wrong environment")
    return url
