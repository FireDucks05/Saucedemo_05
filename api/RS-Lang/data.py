base_url = 'https://rs-language-api.herokuapp.com/'
users = 'users'
signin = 'signin'

schema_new_user = {
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
data_new_user = {
    "name": "testeKatetstest",
    "email": "testKate@test1.test",
    "password": "test@test1.test"
}

schema_sign_in = {
    "required": [
        "message",
        "token",
        "name",
        "userId",
    ]
}
data_sign_in = {
    "email": "nimive3050@probdd.com",
    "password": "nimive3050@probdd.com"
}
