from selenium.webdriver import Firefox, Chrome, Remote

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

POSITIVE_LOGIN_CREDENTIALS = [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
]

NEGATIVE_LOGIN_CREDENTIALS = {"user": "locked_out_user", "password": "secret_sauce"}

VALID_BROWSERS = {
    "chrome": Chrome,
    "firefox": Firefox,
    "remote": Remote
}

BROWSER_REMOTE_CAPABILITIES = {
    "browserName": "chrome",
    "version": "107.0",
    "enableVNC": True,
}

COMMAND_EXECUTOR = {"ci": "http://selenoid-chrome:4444",
                    "local": "http://localhost:4444/wd/hub"}