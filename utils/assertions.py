from http import HTTPStatus

import allure
from hamcrest import assert_that, equal_to


@allure.step("Check status code")
def check_status_code(actual, expected: HTTPStatus):
    assert_that(actual, equal_to(expected), "Bad status code")
