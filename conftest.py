import pytest

from constants import VALID_BROWSERS, COMMAND_EXECUTOR


# @pytest.fixture(autouse=True)
# def browser(request):
#     browser = request.config.getoption("--browser")
#     if browser == "firefox":
#         options = webdriver.FirefoxOptions()
#         options.add_argument("--window-size=1600,1080")
#         options.headless = True
#
#         browser = webdriver.Firefox(
#             service=FirefoxService(GeckoDriverManager().install()), options=options
#         )
#         yield browser
#         browser.quit()
#     else:
#         options = webdriver.ChromeOptions()
#         options.add_argument("--window-size=1600,1080")
#         options.headless = False
#         browser = webdriver.Chrome(
#             service=Service(ChromeDriverManager().install()), options=options
#         )
#         yield browser
#         browser.quit()


@pytest.fixture(autouse=True)
def url():
    url = "https://www.saucedemo.com/"
    if not url:
        raise Exception("Wrong environment")
    return url


def pytest_addoption(parser):
    parser.addoption("--launch", default="firefox", choices=["chrome", "firefox", "ci"])


@pytest.fixture(autouse=True)
def browser(request):
    launch = request.config.getoption("--launch")
    if launch == 'ci':
        browser = VALID_BROWSERS["remote"](command_executor=COMMAND_EXECUTOR["ci"])
    else:
        browser = VALID_BROWSERS[launch]()
        browser.maximize_window()
    yield browser
    browser.quit()
