from Pages.form_page import FormPage
import time


class TestFormPage:
    def test_form(self, driver):
        form_page = FormPage(driver, 'https://www.saucedemo.com/')
        form_page.open()
        # username, password = form_page.fill_field_and_submit()
        # result = form_page.form_result()
        # assert f'{username}{password}' == result[0], 'the form has net been filled'
        # print(username, password)
        time.sleep(5)













