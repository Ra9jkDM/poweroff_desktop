from Config import Config
from business_logic.api.base_requests import ApiRequests
from database.tables.settings import Settings

from business_logic.api.model import Token

import pages.Login

class QtLoginController: # Выкидывает пользователя на Login.page, еcли не получилось отправить запрос  
    def __init__(self, config: Config, navigator):
        self._config = config
        self._navigator = navigator
        self._settings = Settings()

    def _save_tokens(self, refresh_token, access_token):
        print("Save ...")
        self._settings.refresh_token = refresh_token
        self._settings.access_token = access_token

    def is_logged_in(self):
        tokens = Token(refresh_token=self._settings.refresh_token, access_token=self._settings.access_token)
        self._api = ApiRequests(self._config.url, lambda x, y: self._save_tokens(x, y), tokens=tokens)
        return self._api.get("user/") != False

    def login(self, *args, **kwargs):
        self._api = ApiRequests(self._config.url, lambda x, y: self._save_tokens(x, y))
        return self._api.login(*args, **kwargs)

    def get(self, *args, **kwargs):
        result = self._api.get(*args, **kwargs)
        self._is_loggin_or_logout(result)

        return result

    def post(self, *args, **kwargs):
        result = self._api.post(*args, **kwargs)
        self._is_loggin_or_logout(result)

        return result

    def _is_loggin_or_logout(self, result):
        if result == False:
            self._navigator.navigate(Login())
        # elif result == None:
        #     self._navigator.navigate("Lost connection !!!") # Отвалился интернет
        return True

class Request:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = QtLoginController(*args, *kwargs)
        return cls._instance

# make navigator.class static