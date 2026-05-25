from pydantic import BaseModel


class UserstyleUpdate(BaseModel):
    font: str
    background_color: str