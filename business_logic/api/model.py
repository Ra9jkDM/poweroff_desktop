from pydantic import BaseModel

class Token(BaseModel):
    refresh_token: str|None = ""
    access_token: str|None = ""
    token_type: str|None = ""

class User(BaseModel):
    username: str
    password: str