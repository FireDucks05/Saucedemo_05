import pytest

from constants import POSITIVE_LOGIN_CREDENTIALS
from pages.login_page import LoginPage


# @pytest.fixture(autouse=True)
# def login_standart(browser, url):
#     login_page = LoginPage(browser, url)
#     login_page.open_page()
#     login_page.login_ui(
#         POSITIVE_LOGIN_CREDENTIALS[0][0], POSITIVE_LOGIN_CREDENTIALS[0][1]
#     )
