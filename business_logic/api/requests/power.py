from ..qt_login_controller import Request

class User:
    def __init__(self):
        self._request = Request()

    def delete(self, list):
        self._request.get("user/get")