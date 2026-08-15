from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    body: str


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class PostRead(PostBase):
    created_at: datetime
    updated_at: datetime
    likes_count: int

    model_config = ConfigDict(from_attributes=True)