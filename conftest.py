import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    # s = Service("/Users/abloha/selenium/chromedriver")
    # driver = webdriver.Chrome(service=s)

    driver.get("https://www.saucedemo.com/")
    #driver.maximize_window()
    driver.implicitly_wait(5)

    request.cls.driver = driver

    #yield
    #driver.close()















# @pytest.fixture(autouse=True)
# def login(browser):
#     browser.get("https://www.saucedemo.com/")
#     browser.find_element(By.ID, 'user-name').send_keys('standard_user')
#     browser.find_element(By.ID, 'password').send_keys('secret_sauce')
#     browser.find_element(By.ID, 'login-button').click()
#     yield browser
#     browser.find_element(By.ID, "react-burger-menu-btn").click()
#     time.sleep(2)
#     browser.find_element(By.ID, "logout_sidebar_link").click()
#     browser.quit()



    # options = webdriver.ChromeOptions()
    # options.headless = False
    # browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # return browser
