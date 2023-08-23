from http import HTTPStatus

import allure

from api.endpoints.posts_api import get_posts_by_user_id, make_post
from models.posts_models import Post, PostRequest
from utils.assertions import check_status_code
from utils.random_utils import generate_number_in_range
from utils.schema import validate_schema

user_id = generate_number_in_range()


@allure.feature("Posts")
@allure.story("Posts API")
class TestPostsApi:

    @allure.title("Get posts by user_id")
    def test_get_posts_by_user_id(self):
        response = get_posts_by_user_id(user_id)
        check_status_code(response.status_code, HTTPStatus.OK)
        for post in response.json():
            validate_schema(post, Post.json_schema())

    @allure.title("Make post")
    def test_make_post(self):
        post = PostRequest(userId=user_id, title="Some", body="some")
        response = make_post(post)
        check_status_code(response.status_code, HTTPStatus.CREATED)
