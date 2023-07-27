import allure
from jsonschema.validators import validate
from utils.helper import load_json_schema


class TestReqresApi:

    @allure.tag('api')
    @allure.title('Создание пользователя')
    def test_create_user(self, reqres):
        response = reqres.post("/api/users", {"name": "Oleg", "job": "Technical-writer"})

        assert response.status_code == 201
        validate(instance=response.json(), schema=load_json_schema('user_create.json'))
        assert response.json()["name"] == "Oleg"
        assert response.json()["job"] == "Technical-writer"

    @allure.tag('api')
    @allure.title('Обновление данных пользователя PUT')
    def test_update_user_by_put(self, reqres):
        response = reqres.put("/api/users/2", {"name": "Ivan", "job": "Qa"})

        assert response.status_code == 200
        validate(instance=response.json(), schema=load_json_schema('user_update.json'))
        assert response.json()["name"] == "Ivan"
        assert response.json()["job"] == "Qa"

    @allure.tag('api')
    @allure.title('Обновление данных пользователя PATCH')
    def test_update_user_by_patch(self, reqres):
        response = reqres.patch("/api/users/2", {"name": "Vladimir", "job": "AQA"})

        assert response.status_code == 200
        validate(instance=response.json(), schema=load_json_schema('user_update.json'))
        assert response.json()["name"] == "Vladimir"
        assert response.json()["job"] == "AQA"

    @allure.tag('api')
    @allure.title('Удаление пользователя')
    def test_delete_user(self, reqres):
        delete_user = reqres.delete("/api/users/2")

        assert delete_user.status_code == 204

    @allure.tag('api')
    @allure.title('Регистрация пользователя')
    def test_register_success(self, reqres):
        data = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = reqres.post(url=f'/api/register', data=data)

        assert response.status_code == 200
        validate(instance=response.json(), schema=load_json_schema('post_register.json'))

    @allure.tag('api')
    @allure.title('Регистрация с ошибкой')
    def test_register_failed(self, reqres):
        response = reqres.post("/api/register", {"email": "neverexisting@email.com"})

        assert response.status_code == 400
        validate(instance=response.json(), schema=load_json_schema('login_failed.json'))
        assert response.json()['error'] == 'Missing password'

    @allure.tag('api')
    @allure.title('Авторизация пользователя')
    def test_login_successful(self, reqres):
        data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = reqres.post(f'/api/login', data=data)

        assert response.status_code == 200
        validate(instance=response.json(), schema=load_json_schema('login_success.json'))

    @allure.tag('api')
    @allure.title('Авторизация с ошибкой')
    def test_login_failed(self, reqres):
        response = reqres.post("/api/login", {"email": "neverexisting@email.com"})

        assert response.status_code == 400
        validate(instance=response.json(), schema=load_json_schema('login_failed.json'))
        assert response.json()['error'] == 'Missing password'
