from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

user_name = 'standard_user'
password = 'secret_sauce'


def setUp(self):
    service = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    self.driver = webdriver.Chrome(service=service, options=chrome_options)
    self.driver.get('https://www.saucedemo.com/')


def tearDown(self):
    self.driver.quit()


def test_TC_001(self):
    self.driver.find_element(By.ID, 'user-name').send_keys(user_name)
    self.driver.find_element(By.ID, 'password').send_keys(password)
    self.driver.find_element(By.ID, 'login-button').click()

    assert 'https://www.saucedemo.com/inventory.html' == self.driver.current_url
