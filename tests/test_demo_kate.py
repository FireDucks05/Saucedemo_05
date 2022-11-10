from selenium.webdriver.common.by import By
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_kate_first_add():
    options = webdriver.ChromeOptions()
    options.headless = True
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.maximize_window()
    browser.get('https://www.selenium.dev/downloads')
    browser.find_element(By.XPATH, "//a[contains(@href,'https://github.com/SeleniumHQ/')]").click()
    assert True
    browser.quit()


