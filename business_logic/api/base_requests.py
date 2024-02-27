import requests
from .model import Token, User

class ApiRequests:
    def __init__(self, api_url: str, save_tokens=None, tokens: Token=None):
        self.api_url = api_url
        self._saver = save_tokens

        if tokens:
            self.tokens = tokens
        else:
            self.tokens = Token()

    def login(self, user: User):
        response = requests.post(self._get_url("login/token"), data=user.model_dump())
        
        if response.status_code == 200:
            self.tokens = Token(**response.json())
            print(self.tokens.refresh_token)
            self._save_tokens()
            return True
        return False

    def get(self, url, data={}):
        get = lambda: requests.get(self._get_url(url), headers=self._get_headers(), params=data)
        return self._request(get)

    def post(self, url, data={}, json={}):
        post = lambda: requests.post(self._get_url(url), headers=self._get_headers(), data=data, json=json)
        return self._request(post)

    def _request(self, func):
        response = func()
        print(response.status_code, response.text)
        if response.status_code == 200:
            return response
        elif response.status_code == 401: # Unauthorized
            if self.relogin():
                response = func()
                print(response, response.text)
                return response
            return False

    def relogin(self):
        response = requests.post(self._get_url("login/refresh"), json={"refresh_token": self.tokens.refresh_token})
        print(response, response.text)
        if response.status_code == 200:
            self.tokens.access_token = response.json()["access_token"]
            self._save_tokens()
            return True
        return False

    def get_token_list(self):
        return self.post("login/get", json={"refresh_token": self.tokens.refresh_token})

    def _get_headers(self):
        return {"Authorization": f"Bearer {self.tokens.access_token}"}

    def _get_url(self, url):
        return f"{self.api_url}{url}"

    def _save_tokens(self):
        if self._saver:
            self._saver(self.tokens.refresh_token, self.tokens.access_token)


if __name__ == "__main__":
    URL="http://127.0.0.1:8000/"
    t = Token(refresh_token="")
    api = ApiRequests(URL, t)

    user= User(username="bob", password="pwd123")
    api.login(user)
    print(api.get("user"))
    print(api.get_token_list())
    print(api.post("login/delete", json={"tokens": [167, 168]}))