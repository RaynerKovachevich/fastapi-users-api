from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    is_activate: Optional[bool] = True

class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int

    class config:
        orm_mode = True    