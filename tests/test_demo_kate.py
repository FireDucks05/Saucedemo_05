from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_kate():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1200,800")
    options.headless = True
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.get('https://www.saucedemo.com/')


user_name = 'standard_user'
password = 'secret_sauce'


def test_TC_001():
    service = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.headless = True
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, 'user-name').send_keys(user_name)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-button').click()
    assert 'https://www.saucedemo.com/inventory.html' == driver.current_url
    driver.quit()
