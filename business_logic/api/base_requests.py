import requests
from pydantic import BaseModel

URL="http://127.0.0.1:8000/"

class Token(BaseModel):
    refresh_token: str = ""
    access_token: str = ""
    token_type: str = ""

class User(BaseModel):
    username: str
    password: str

def login(url):
    user= User(username="bob", password="pwd123")
    r = requests.post(URL+url, data=user.model_dump())
    # print(r.text)
    tokens = Token(**r.json())
    return tokens

def get(url, access_token, data={}):
    headers = {"Authorization": f"Bearer {access_token}"}
    r = requests.get(URL+url, headers=headers, params=data)
    return r.text

def post(url, access_token, data):
    headers = {"Authorization": f"Bearer {access_token}"}
    r = requests.post(URL+url, headers=headers, json=data)
    return r.text

class ApiRequests:
    def __init__(self, api_url: str, tokens: Token=None):
        self.api_url = api_url

        if tokens:
            self.tokens = tokens
        else:
            self.tokens = Token()

    def login(self, user: User):
        response = requests.post(self._get_url("login/token"), data=user.model_dump())
        
        if response.status_code == 200:
            self.tokens = Token(**response.json())
            print(self.tokens.refresh_token)
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
            return True
        return False

    def get_token_list(self):
        return self.post("login/get", json={"refresh_token": self.tokens.refresh_token})

    def _get_headers(self):
        return {"Authorization": f"Bearer {self.tokens.access_token}"}

    def _get_url(self, url):
        return f"{self.api_url}{url}"

class QtApi: # Выкидывает пользователя на Login.page, еcли не получилось отправить запрос
    def __init__(self, navigator):
        self._api = ApiRequests("")
        self._navigator = navigator

    def login(self):
        return self._api.login()

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
            self._navigator.navigate("Home")
        elif result == None:
            self._navigator.navigate("Lost connection !!!") # Отвалился интернет
        return True

if __name__ == "__main__":
    t = Token(refresh_token="")
    api = ApiRequests(URL, t)

    user= User(username="bob", password="pwd123")
    api.login(user)
    print(api.get("user"))
    print(api.get_token_list())
    print(api.post("login/delete", json={"tokens": [167, 168]}))

    # tokens = login("login/token")
    # print(tokens.access_token)

    # token = tokens.access_token
    # # token = ""
    # result = get("user", token)
    # print(result)

    # r = post("login/get", token, {"refresh_token": tokens.refresh_token})
    # print(r)

    # result = post("login/delete", token, {"tokens": [149, 151, 158]})
    # print(result)