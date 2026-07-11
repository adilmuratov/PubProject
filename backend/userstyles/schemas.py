from pydantic import BaseModel


class UserstyleBase(BaseModel):
    font: str
    background_color: str


class UserstyleUpdate(UserstyleBase):
    pass


class UserstyleRead(UserstyleBase):
    pass
