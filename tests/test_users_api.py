from http import HTTPStatus

import allure

from framework.api.users_api import get_user_by_id
from models.users_models import User
from utils.assertions import check_status_code
from utils.schema import validate_schema


@allure.feature("Users")
@allure.story("Users API")
class TestUsersApi:

    @allure.title("Get user by id")
    def test_get_user_by_id(self):
        response = get_user_by_id(5)
        check_status_code(response.status_code, HTTPStatus.OK)
        validate_schema(response.json(), User.json_schema())
        print(response.json()["email"])
