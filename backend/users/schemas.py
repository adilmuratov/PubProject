from pydantic import BaseModel


class UserBase(BaseModel):  
    username: str
    password_hash: bytes


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass