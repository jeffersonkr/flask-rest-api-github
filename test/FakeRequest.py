import json


class FakeRequest:
    def __init__(self, data="", status_code=200):
        self._status_code = status_code
        self._data = data

    @property
    def status_code(self):
        return self._status_code

    @property
    def data(self):
        return self._data

    def json(self):
        return self._data
