from requests import get, post


class BaseAPI(object):
    def __init__(self, url='', data={}, params={}):
        self.url = url
        self.data = data
        self.params = params
        self.response = None

    def get(self):
        self.response = get(url=self.url, data=self.data, params=self.params)

    def post(self):
        self.response = post(url=self.url, data=self.data, params=self.params)

    def is_request_successful(self):
        return self.response.status_code == 200

    def get_status_code(self):
        return self.response.status_code
