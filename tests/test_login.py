import pytest
import time

import allure

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
    @allure.title("Positive login")
    def test_login_positive(self, user, password):
        self.login_page.login_ui(user, password)
        assert self.login_page.page_is_open(
            url="https://www.saucedemo.com/inventory.html"
        )

    @allure.title("Negative login")
    def test_login_negative(self):
        self.login_page.login_ui(
            NEGATIVE_LOGIN_CREDENTIALS["user"], NEGATIVE_LOGIN_CREDENTIALS["password"]
        )
        assert not self.login_page.page_is_open(
            url="https://www.saucedemo.com/inventory.html"
        )