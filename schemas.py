from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(UserBase):
    id: int
    username: str

    model_config = {
        "from_attributes": True
    }

class UserOut(UserResponse):
    pass         

class Token(BaseModel):
    access_token: str
    token_type: str        