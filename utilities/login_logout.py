import pytest
from pages.login_logout_page import LoginPage

class LoginLogout(LoginPage):
    @pytest.fixture(scope = 'function')
    def login_logout(self):
        loginpage = LoginPage(self.browser)
        loginpage.getlogin()


