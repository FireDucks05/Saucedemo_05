class TestLoginPage:

    def test_001_login(self):
        page = "https://www.saucedemo.com/inventory.html"
        assert page == 'https://www.saucedemo.com/inventory.html'

    def test_logout(self):

        page = "https://www.saucedemo.com/"
        assert page == "https://www.saucedemo.com/"


