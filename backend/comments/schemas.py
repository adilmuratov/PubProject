from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class CommentBase(BaseModel):
    body: str = Field(ge=1, le=1000)
    


class CommentCreate(CommentBase):
    pass


class CommentUpdate(CommentBase):
    pass


class CommentRead(CommentBase):
    created_at: datetime
    updated_at: datetime
    replies: list[CommentRead] = Field(default_factory=list)
    likes_count: int

    model_config = ConfigDict(from_attributes=True)

CommentRead.model_rebuild()