import pytest
from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="class")

def setup(request):
    browser = webdriver.Chrome("/Users/abloha/selenium/chromedriver" )
    browser.get("https://www.saucedemo.com/")
    request.cls.browser = browser
