import requests
from http import HTTPStatus
import pytest


class TestUserAPi:
    url = 'https://petstore.swagger.io/v2/user/'
    global my_name
    my_name = 'KateFox'

    def test_create_new_user(self):
        user_data = {
            "id": 121,
            "username": f'{my_name}',
            "firstName": "KAte1",
            "lastName": "Fox1",
            "email": "test@test.test1",
            "password": "Qwerty12341",
            "phone": "+188888888",
            "userStatus": 0
        }
        response = requests.post(f'{self.url}', json=user_data)
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        print(response.raise_for_status())

    def test_login_user(self):
        login_data = {
            "username": f'{my_name}',
            "password": "Qwerty1234",
        }
        response = requests.get(f'{self.url}login', json=login_data)
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        print(response.raise_for_status())

    def test_logout_user(self):
        response = requests.get(f'{self.url}logout')
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        print(response.raise_for_status())

    def test_update_user(self):
        update_data = {
            "id": 121,
            "username": f'{my_name}',
            "firstName": "KAte1",
            "lastName": "Fox1",
            "email": "test@test.test1",
            "password": "Qwerty12341",
            "phone": "+188888888",
            "userStatus": 0
        }
        response = requests.put(f'{self.url}{my_name}', json=update_data)
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        print(response.raise_for_status())

    def test_delete_user(self):
        response = requests.delete(f'{self.url}{my_name}')
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        print(response.raise_for_status())


class TestPetUserAPi:
    url = 'https://petstore.swagger.io/v2/pet/'
    global id
    id = 12

    @pytest.mark.parametrize(
        "status", ["available", "pending", "sold"],
    )
    def test_find_status(self, status):
        response = requests.get(f'{self.url}findByStatus?status={status}')
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        print(response.raise_for_status())

    def test_add_new_pet(self):
        # id = '12'
        response = requests.post(f'{self.url}{id}')
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        print(response.raise_for_status())

    @pytest.mark.parametrize(
        "id", [10, 8, id],
    )
    def test_find_by_id(self, id):
        response = requests.get(f'{self.url}{id}')
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        print(response.raise_for_status())

    def test_update_existing_pet(self):
        data = {
            "id": id,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        response = requests.put(f'{self.url}', json=data)
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        print(response.raise_for_status())

    def test_upload_img(self):
        data = {"id": id} #TODO: find how to upload image
        response = requests.get(f'{self.url}{id}/uploadImage', json=data)
        assert response.status_code == HTTPStatus.OK, 'wrong status code'

    def test_delete_pet(self):
        response = requests.delete(f'{self.url}{id}')
        assert response.status_code == HTTPStatus.OK, 'wrong status code'