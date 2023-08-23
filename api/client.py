import logging
from urllib.parse import urljoin

import allure
import requests

from config import base_config

logger = logging.getLogger(__name__)


class Client:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_full_url(self, path):
        return urljoin(self.base_url, path)

    @allure.step("Do GET request to '{path}'")
    def get(self, path=None, params=None, **kwargs):
        url = self.get_full_url(path)
        logger.info(f"Get request to {url}")
        return requests.get(self.get_full_url(path), params, **kwargs)

    @allure.step("Do POST request to '{path}'")
    def post(self, path=None, data=None, json=None, **kwargs):
        url = self.get_full_url(path)
        logger.info(f"POST request to {url}")
        return requests.post(url, data, json, **kwargs)


def get_client(base_url=base_config.base_url):
    return Client(base_url)
