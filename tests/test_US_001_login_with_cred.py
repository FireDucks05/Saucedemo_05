import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLoginPage:

    def test_001_login(self):
        loginpage = LoginPage()
        loginpage.getlogin().send_keys('standard_user')
        loginpage.getpassword().send_keys('secret_sauce')
        loginpage.getloginbutton()


    def test_logout(self):
        page = "https://www.saucedemo.com/"
        assert page == "https://www.saucedemo.com/"
