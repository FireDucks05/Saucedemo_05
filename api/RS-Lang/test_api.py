from typing import List, Union, Dict
from json import JSONDecodeError
import requests
from http import HTTPStatus
import pytest
import jsonschema
from jsonschema import validate

from data import *


def check_jsonschema(func):
    """Декоратор, который проверяет статус ответа и конвертирует ответ в json"""
    def wrapper(self, base_url, **kwargs):
        response = func(self, base_url, **kwargs)
        if response.status_code != HTTPStatus.OK:
            raise Exception("Unsuccessful response")
        try:
            return validate(instance=response.json(), schema=schema_new_user)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            err = "Given JSON data is InValid"
            return None

    return wrapper


class TestAPI:
    base_url = 'https://rs-language-api.herokuapp.com/'
    users = 'users'
    signin = 'signin'

    @check_jsonschema
    def test_create_user_new1(self):
        response = requests.post(f'{base_url}{users}', json=data_new_user)
        # try:
        #     validate(instance=response.json(), schema=schema_new_user)
        # except jsonschema.exceptions.ValidationError as err:
        #     print(err)
        #     err = "Given JSON data is InValid"

    def test_sign_in(self):
        response = requests.post(f'{base_url}{signin}', json=data_sign_in)
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        assert response.json()["name"] == "Kate"
        try:
            validate(instance=response.json(), schema=schema_sign_in)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            err = "Given JSON data is InValid"
