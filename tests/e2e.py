import pytest
import time
from selenium import webdriver
from pages import login_logout_page
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s = Service ("/Users/abloha/selenium/chromedriver")
browser=webdriver.Chrome(service =s)
browser.get("https://www.saucedemo.com/")

browser.find_element(By.ID, 'user-name').send_keys('standard_user')
browser.find_element(By.ID, 'password').send_keys('secret_sauce')
browser.find_element(By.ID, 'login-button').click()

products = browser.find_elements(By.LINK_TEXT,'/html/body/div/div/div/div[2]/div/div/div')

for product in products:
    productName = product.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div').text
    if productName == "Sauce Labs Bike Light":
        product.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div").click()
        print(product)

