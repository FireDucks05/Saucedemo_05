import time
from webbrowser import BaseBrowser
from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.saucedemo.com/")
time.sleep(5)

