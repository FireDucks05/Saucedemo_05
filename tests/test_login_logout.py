import pytest
from conftest import url
from pages.login_page import HomePage
from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class TestLoginPage(BaseClass):

    def test_login(self):
        log = self.getLogger()
        loginpage = HomePage(self.driver)
        log.info("logging in")
        loginpage.getlogin()
        page = "https://www.saucedemo.com/inventory.html"
        assert page == "https://www.saucedemo.com/inventory.html"


    def test_logout(self):
        log = self.getLogger()
        loginpage = HomePage(self.driver)
        log.info("logging out")
        loginpage.getlogin()
        loginpage.getlogout()
        assert url == "https://www.saucedemo.com/"
