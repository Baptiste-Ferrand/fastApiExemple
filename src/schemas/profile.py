from pydantic import BaseModel
from uuid import UUID

class ProfileCreate(BaseModel):
    firstname: str = "hommer"
    name: str = "simpson"
    age: int = 32
    weight: int = 180

class ProfileResponse(BaseModel):
    uuid: UUID
    firstname: str
    name: str
    age: int
    weight: int
    user_id: UUID

    class Config:
        orm_mode = True

class ProfileUpdateFristname(BaseModel):
    firstname: str

class ProfileResponseFirstname(BaseModel):
    firstname: str
    uuid: str