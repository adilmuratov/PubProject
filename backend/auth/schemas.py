from pydantic import BaseModel


class TokenInfo(BaseModel):
    acces_token: str
    token_type: str


class UserData(BaseModel):
    username: str
    password: bytes 