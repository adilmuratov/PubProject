from datetime import datetime

from pydantic import BaseModel


class PostBase(BaseModel):
    body: str


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class PostRead(PostBase):
    created_at: datetime
    updated_at: datetime