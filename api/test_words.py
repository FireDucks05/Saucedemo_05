import requests
from http import HTTPStatus
import pytest
import jsonschema
from jsonschema import validate


class TestWordsAPI:
    url = 'https://rs-language-api.herokuapp.com/words/'

    def test_get_chunk_of_words(self):
        global counter
        counter = 0
        schema1 = {
            "properties": {
                "id": {
                    "description": "The unique identifier for a user",
                    "type": "string"
                },
            },
            "required": [
                "id",
            ]
        }
        response = requests.get(f'{self.url}')
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        jsonData = response.json()
        try:
            validate(instance=jsonData[0], schema=schema1)
            counter = 1
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            err = "Given JSON data is InValid"

    def test_get_word_with_assets_by_id(self):
        id = '5e9f5ee35eb9e72bc21af4aa'
        schema1 = {
            "properties":
                {
                    "id": {
                        "description": "The unique identifier for a user",
                        "type": "string"
                    },
                },
            "required": [
                "id",
                "group",
                "page",
                "word",
                "image",
                "audio",
                "audioMeaning",
                "audioExample",
                "textMeaning",
                "textExample",
                "transcription",
                "wordTranslate",
                "textMeaningTranslate",
                "textExampleTranslate",
            ]
        }
        response = requests.get(f'{self.url}{id}')
        assert response.status_code == HTTPStatus.OK, 'wrong status code'
        jsonData = response.json()
        try:
            validate(instance=jsonData, schema=schema1)
            counter = 1
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            err = "Given JSON data is InValid"

def test_new():
    response = requests.get('https://reqres.in/api/users')
    assert response.status_code == 200
    print(response.json())
