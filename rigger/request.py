import requests
from rigger.settings import api_settings


class SysRequest(object):
    def __init__(self, url=None, data=None):
        """
        :param url: self url path
        :param data: self body data
        """
        if not url:
            raise ValueError("url can not be empty ")

        if data:
            if not isinstance(data, dict):
                raise ValueError("data must be dict type")

        self.url = url
        self.data = data
        self.token = api_settings.ADMIN_AUTHORIZATION

    def patch(self):
        requests.patch(self.url, headers={"token": self.token}, data=self.data)

