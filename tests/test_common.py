from http import HTTPStatus

import allure
from hamcrest import assert_that, is_in

from constants.posts_contants import VALID_POSTS_RANGE
from api.endpoints.posts_api import get_posts_by_user_id, make_post
from api.endpoints.users_api import get_user_by_id
from models.posts_models import PostRequest
from utils.assertions import check_status_code
from utils.random_utils import generate_number_in_range

user_id = generate_number_in_range()


@allure.feature("REST API")
@allure.story("REST API")
class TestRestApi:

    @allure.title("Common test")
    def test_common(self):
        response = get_user_by_id(user_id)
        print(response.json()["email"])

        response = get_posts_by_user_id(user_id)
        json_response = response.json()
        for post in json_response:
            _check_post_id(post["id"])

        post = PostRequest(userId=user_id, title="Some", body="some")
        response = make_post(post)
        check_status_code(response.status_code, HTTPStatus.CREATED)


@allure.step("Check post id - '{post_id}'")
def _check_post_id(post_id):
    assert_that(post_id, is_in(VALID_POSTS_RANGE), "Post ID should be an integer between 1 and 100")
