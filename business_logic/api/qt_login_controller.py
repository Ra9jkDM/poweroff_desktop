from Config import Config
from business_logic.api.base_requests import ApiRequests
from database.tables.settings import Settings
from pages.message import show_error_msg

from business_logic.api.model import Token

class QtLoginController: # Выкидывает пользователя на Login.page, еcли не получилось отправить запрос  
    _api = None
    
    def __init__(self, config: Config):
        self._config = config
        self._settings = Settings()

    def set_login_page(self, login):
        self._login = login

    def _save_tokens(self, refresh_token, access_token):
        print("Save ...")
        self._settings.refresh_token = refresh_token
        self._settings.access_token = access_token

    def is_logged_in(self):
        self._get_api()
        return self._api.get("user/") != False

    def logout(self):
        self._save_tokens("", "")

    def login(self, *args, **kwargs):
        self._api = ApiRequests(self._config.url, lambda x, y: self._save_tokens(x, y))
        return self._api.login(*args, **kwargs)

    def get(self, *args, **kwargs):
        if not self._api:
            self._get_api()

        result = self._api.get(*args, **kwargs)
        self._is_loggin_or_logout(result)

        return result

    def post(self, *args, **kwargs):
        if not self._api:
            self._get_api()
            
        result = self._api.post(*args, **kwargs)
        self._is_loggin_or_logout(result)

        return result

    def _is_loggin_or_logout(self, result):
        if result == False:
            self._login()
        elif result == None:
            show_error_msg("Соединение с сервером потеряно!")
        return True

    def _get_api(self):
        tokens = Token(refresh_token=self._settings.refresh_token, access_token=self._settings.access_token)
        self._api = ApiRequests(self._config.url, lambda x, y: self._save_tokens(x, y), tokens=tokens)

