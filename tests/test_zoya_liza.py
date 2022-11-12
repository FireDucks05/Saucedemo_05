from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

HOME_LINK = "https://www.saucedemo.com/"
INVENTORY_LINK = 'https://www.saucedemo.com/inventory.html'
login_txt = 'standard_user'
password_txt = 'secret_sauce'

HOME_LINK_2 = "https://www.saucedemo.com/"
INVENTORY_LINK_2 = 'https://www.saucedemo.com/inventory.html'
login_txt_2 = 'standard_user'
password_txt_2 = 'secret_sauce'

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.saucedemo.com/")
time.sleep(5)

