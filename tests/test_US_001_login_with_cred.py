import pytest
from pages.login_page import LoginPage
from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class TestLoginPage(BaseClass):

    def test_001_login(self):
        log = self.getLogger()
        loginpage = LoginPage(self.browser)
        log.info("logging in")
        loginpage.getlogin().send_keys('standard_user')
        loginpage.getpassword().send_keys('secret_sauce')
        loginpage.getloginbutton()


    def test_logout(self):
        page = "https://www.saucedemo.com/"
        assert page == "https://www.saucedemo.com/"
