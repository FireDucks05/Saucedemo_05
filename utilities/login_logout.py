import pytest
from pages.login_logout_page import LoginPage

class LoginLogout(LoginPage):
    @pytest.fixture(scope = 'function')
    def login_logout_general(self):
        loginpage = LoginPage(self.browser)
        loginpage.getlogin()
        yield
        loginpage.getlogin()


