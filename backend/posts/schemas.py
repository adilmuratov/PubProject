from pydantic import BaseModel


class PostBase(BaseModel):
    body: str