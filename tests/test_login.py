import allure
import pytest

from constants import POSITIVE_LOGIN_CREDENTIALS, NEGATIVE_LOGIN_CREDENTIALS
from pages.login_page import LoginPage


class TestAuthorizationClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.login_page = LoginPage(browser, url)
        self.login_page.open_page()

    @pytest.mark.parametrize(

        "user, password",
        POSITIVE_LOGIN_CREDENTIALS,
        ids=["standart_user", "problem_user", "performance_glitch_user"],
    )
    @allure.story('US_001.00 | Login Page')
    @allure.title("Registered user is able to login with valid credentials")
    def test_login_positive(self, user, password):
        self.login_page.login_ui(user, password)
        assert self.login_page.page_is_open(
            url="https://www.saucedemo.com/inventory.html"
        )


    @allure.story('US_001.00 | Login Page')
    @allure.title("Lockout login")
    @pytest.mark.xfail()
    def test_login_lockout_use(self):
        self.login_page.login_ui(
            NEGATIVE_LOGIN_CREDENTIALS["user"], NEGATIVE_LOGIN_CREDENTIALS["password"]
        )
        assert self.login_page.page_is_open(
            url="https://www.saucedemo.com/inventory.html"
        )

    @allure.story('US_001.00 | Login Page')
    @allure.title("Login without password impossible")
    @pytest.mark.negative
    def test_login_WO_pass(self):
        self.login_page.login_ui(
            POSITIVE_LOGIN_CREDENTIALS[0][0], ''
        )
        self.login_page.impossibility_auth()

    @allure.story('US_001.00 | Login Page')
    @allure.title("Login without user_name impossible")
    @pytest.mark.negative
    def test_login_WO_login(self):
        self.login_page.login_ui(
            '', POSITIVE_LOGIN_CREDENTIALS[0][1]
        )
        self.login_page.impossibility_auth()

    @allure.story('US_001.00 | Login Page')
    @allure.title("Purpose to fail case")
    @pytest.mark.positive
    def test_for_fail(self):
        self.login_page.login_ui(
            POSITIVE_LOGIN_CREDENTIALS[0][0], POSITIVE_LOGIN_CREDENTIALS[0][1]
        )
        self.login_page.burger_menu()
        self.login_page.logout()
        assert self.login_page.page_is_open(url="https://www.saucedemo.com/inventory.html")
