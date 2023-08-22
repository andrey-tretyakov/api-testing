import allure

from constants.api_params import APIParams
from constants.api_paths import APIPaths
from framework.client import get_client
from models.posts_models import PostRequest


@allure.step("Get posts by user_id = '{user_id}'")
def get_posts_by_user_id(user_id):
    client = get_client()
    return client.get(f"{APIPaths.POSTS}", params={f"{APIParams.USER_ID}": user_id})


@allure.step("Make post")
def make_post(post: PostRequest):
    client = get_client()
    return client.post(f"{APIPaths.POSTS}", data=post.to_json())
