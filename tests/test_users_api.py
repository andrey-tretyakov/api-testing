from http import HTTPStatus

import allure

from api.endpoints.users_api import get_user_by_id
from models.users_models import User
from utils.assertions import check_status_code
from utils.random_utils import generate_number_in_range
from utils.schema import validate_schema


@allure.feature("Users")
@allure.story("Users API")
class TestUsersApi:

    @allure.title("Get user by id")
    def test_get_user_by_id(self):
        random_user_id = generate_number_in_range()
        response = get_user_by_id(random_user_id)
        check_status_code(response.status_code, HTTPStatus.OK)
        validate_schema(response.json(), User.json_schema())
        print(response.json()["email"])
