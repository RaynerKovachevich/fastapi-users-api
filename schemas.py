from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True   

class UserOut(UserResponse):
    pass         

class Token(BaseModel):
    access_token: str
    token_type: str        