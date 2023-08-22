from http import HTTPStatus

import allure
from hamcrest import assert_that, is_in

from constants.posts_contants import VALID_POSTS_RANGE
from framework.api.posts_api import get_posts_by_user_id, make_post
from framework.api.users_api import get_user_by_id
from models.posts_models import PostRequest
from utils.assertions import check_status_code

USER_ID = 5


@allure.feature("REST API")
@allure.story("REST API")
class TestRestApi:

    @allure.title("Common test")
    def test_common(self):
        response = get_user_by_id(USER_ID)
        print(response.json()["email"])

        response = get_posts_by_user_id(USER_ID)
        json_response = response.json()
        for post in json_response:
            _check_post_id(post["id"])

        post = PostRequest(userId=USER_ID, title="Some", body="some")
        response = make_post(post)
        check_status_code(response.status_code, HTTPStatus.CREATED)


@allure.step("Check post id - '{post_id}'")
def _check_post_id(post_id):
    assert_that(post_id, is_in(VALID_POSTS_RANGE), "Post ID should be an integer between 1 and 100")
