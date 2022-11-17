from selenium.webdriver import Firefox, Chrome, Remote

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

SOTRING_AZ = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket',
              'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']

SOTRING_ZA = ['Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Onesie', 'Sauce Labs Fleece Jacket',
              'Sauce Labs Bolt T-Shirt', 'Sauce Labs Bike Light', 'Sauce Labs Backpack']

SOTRING_PRICE_ASC = ['Sauce Labs Onesie', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt',
                     'Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Backpack', 'Sauce Labs Fleece Jacket']

SOTRING_PRICE_DESC = ['Sauce Labs Fleece Jacket', 'Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt',
                      'Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Bike Light', 'Sauce Labs Onesie']
