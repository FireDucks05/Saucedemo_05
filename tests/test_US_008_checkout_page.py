import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class Testcheckoutpage:
    def test_title(self):
        self.browser.find_element(By.ID, 'user-name').send_keys("vaysa")

