from pydantic import BaseModel

class LoginUser(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    uuid: str
    email: str

    class Config:
        orm_mode = True
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: LoginResponse
