from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_login_standart():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=800,600")
    options.headless = True
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.get('https://www.selenium.dev/downloads')
    browser.find_element(By.XPATH, "//a[contains(@href,'https://github.com/SeleniumHQ/')]").click()
    assert True
    browser.quit()
