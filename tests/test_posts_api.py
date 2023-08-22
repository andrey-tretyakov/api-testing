from http import HTTPStatus

import allure

from framework.api.posts_api import get_posts_by_user_id, make_post
from models.posts_models import Post, PostRequest
from utils.assertions import check_status_code
from utils.schema import validate_schema

USER_ID = 5


@allure.feature("Posts")
@allure.story("Posts API")
class TestPostsApi:

    @allure.title("Get posts by user_id")
    def test_get_posts_by_user_id(self):
        response = get_posts_by_user_id(USER_ID)
        check_status_code(response.status_code, HTTPStatus.OK)
        for post in response.json():
            validate_schema(post, Post.json_schema())

    @allure.title("Make post")
    def test_make_post(self):
        post = PostRequest(userId=USER_ID, title="Some", body="some")
        response = make_post(post)
        check_status_code(response.status_code, HTTPStatus.CREATED)
