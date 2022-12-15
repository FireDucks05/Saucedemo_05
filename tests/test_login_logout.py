import pytest
from conftest import homepage
from pages.login_logout_page import LoginPage
from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class TestLoginPage(BaseClass):

    def test_login(self):
        log = self.getLogger()
        loginpage = LoginPage(self.browser)
        log.info("logging in")
        loginpage.getlogin()
        page = "https://www.saucedemo.com/inventory.html"
        assert page == "https://www.saucedemo.com/inventory.html"


    def test_logout(self):
        log = self.getLogger()
        loginpage = LoginPage(self.browser)
        log.info("logging out")
        loginpage.getlogin()
        loginpage.getlogout()
        assert homepage == "https://www.saucedemo.com/"
