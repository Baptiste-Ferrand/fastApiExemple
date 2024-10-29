from pydantic import BaseModel, EmailStr

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
