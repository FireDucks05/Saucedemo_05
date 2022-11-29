import requests
from http import HTTPStatus
import pytest
import jsonschema
from jsonschema import validate


class TestStoreAPi:
    url = 'https://petstore.swagger.io/v2/store/'

    def test_get_inventory(self):
        global counter
        counter = 0
        schema1 = {
            "title": "User",
            "description": "A user request json",
            "type": "object",
            "properties": {
                "totvs": {
                    "description": "The unique identifier for a user",
                    "type": "integer"
                },
                "sold": {
                    "description": "Name of the user",
                    "type": "integer"
                },
                "1": {
                    "type": "integer"
                }
            },
            "required": [
                "available",
                "unavailable",
            ]
        }

        response = requests.get(f'{self.url}inventory')
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        jsonData = response.json()
        # assert validate(instance=jsonData, schema=schema1)
        try:
            validate(instance=jsonData, schema=schema1)
            counter = 1
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            err = "Given JSON data is InValid"
        assert counter #TODO: crutch remake