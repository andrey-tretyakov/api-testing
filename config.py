import configparser
import pathlib


def read_config(config_file="settings.ini"):
    path = pathlib.Path(__file__).parent.absolute() / config_file
    config = configparser.ConfigParser()
    config.read(path)
    return config


class AppConfig:

    @property
    def base_url(self):
        return read_config().get("API", "base_url")


base_config = AppConfig()
