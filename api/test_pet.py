import requests
from json import JSONDecodeError
from typing import Dict, Union
from http import HTTPStatus


class TestUserAPi:
    url = 'https://petstore.swagger.io/v2/'

    def test_create_new_user(self):
        user_data = {
            "id": 121,
            "username": "KateFox1",
            "firstName": "KAte1",
            "lastName": "Fox1",
            "email": "test@test.test1",
            "password": "Qwerty12341",
            "phone": "+188888888",
            "userStatus": 0
        }
        response = requests.post(f'{self.url}user', json=user_data)
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        print(response.raise_for_status())

    def test_login_user(self):
        login_data = {
            "username": "KateFox",
            "password": "Qwerty1234",
        }
        response = requests.get(f'{self.url}user/login', json=login_data)
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        print(response.raise_for_status())

    def test_logout_user(self):
        response = requests.get(f'{self.url}user/logout')
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        print(response.raise_for_status())

    def test_update_user(self):
        update_data = {
            "id": 121,
            "username": "KateFox1",
            "firstName": "KAte1",
            "lastName": "Fox1",
            "email": "test@test.test1",
            "password": "Qwerty12341",
            "phone": "+188888888",
            "userStatus": 0
        }
        response = requests.put(f'{self.url}user/KateFox', json=update_data)
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        print(response.raise_for_status())

    def test_delete_user(self):
        response = requests.delete(f'{self.url}user/KateFox')
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        print(response.raise_for_status())
