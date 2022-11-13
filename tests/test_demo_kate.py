import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_kate():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1200,800")
    options.headless = True
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.get('https://www.saucedemo.com/')
    browser.quit()
