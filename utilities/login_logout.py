
def login():
    def getlogin(self):
        return self.browser.find_element(*LoginPage.login_field)

    def getpassword(self):
        return self.browser.find_element(*LoginPage.password_field)

    def getfield(self):
        return self.browser.find_element(*LoginPage.login_button)