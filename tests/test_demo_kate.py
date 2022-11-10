from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.headless = True
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.maximize_window()


def test_kate_first():
    browser.get('https://www.selenium.dev/downloads')
    browser.find_element(By.XPATH, "//a[contains(@href,'https://github.com/SeleniumHQ/')]").click()
    browser.quit()
    assert True
