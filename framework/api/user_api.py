import allure

from constants.api_paths import APIPaths
from framework.client import get_client


@allure.step("Get user by id = '{user_id}'")
def get_user_by_id(user_id):
    client = get_client()
    return client.get(f"{APIPaths.USERS}/{user_id}")
