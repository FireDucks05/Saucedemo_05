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



