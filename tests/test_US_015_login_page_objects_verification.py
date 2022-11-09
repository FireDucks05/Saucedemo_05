from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
options.add_argument("--headless")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

link = "https://www.saucedemo.com/"
browser.get(link)


def test_015_username_field_present(browser):
    login_field = browser.find_element(By.XPATH, "//div[@class = 'form_group'][1]")
    assert login_field


def test_015_password_field_present(browser):
    password_field = browser.find_element(By.XPATH, "//div[@class = 'form_group'][2]")
    assert password_field


def test_015_login_button_present(browser):
    login_button = browser.find_element(By.XPATH, "//input[@id = 'login-button']")
    assert login_button



