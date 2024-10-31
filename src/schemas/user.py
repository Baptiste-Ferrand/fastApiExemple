from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
    confirm_password: str

class UserResponse(BaseModel):
    uuid: str
    email: str

    class Config:
        orm_mode = True
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse

class UserUpdateEmail(BaseModel):
    new_email: str

class UserUpdatePassword(BaseModel):
    current_password: str
    new_password: str
    confirm_password: str

class UserDeleted(BaseModel):
    current_password: str