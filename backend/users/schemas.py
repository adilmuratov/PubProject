from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict

from profiles.schemas import ProfileBase


class UserBase(BaseModel):  
    username: str = Field(min_length=3, max_length=20)


class UserCreate(UserBase):
    password: str = Field(min_length=8)


class UserUpdate(UserBase):
    pass


class ChangePassword(BaseModel):
    old_password: str
    new_password: str


class UserRead(UserBase):
    created_at: datetime


class UserWithProfile(UserBase):
    pass


class UserWithPosts(UserBase):
    pass