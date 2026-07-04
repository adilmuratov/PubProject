from pydantic import BaseModel, Field


class ProfileBase(BaseModel):
    description: str = Field(max_length=200)


class ProfileUpdate(ProfileBase):
    pass

class ProfileRead(ProfileBase):
    pass