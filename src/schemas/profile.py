from pydantic import BaseModel
from uuid import UUID

class ProfileCreate(BaseModel):
    firstname: str = "hommer"
    name: str = "simpson"
    age: int = 32
    weight: int = 180
    height: int = 180

class ProfileResponse(BaseModel):
    uuid: UUID
    firstname: str
    name: str
    age: int
    weight: int
    height: int
    user_id: UUID

    class Config:
        orm_mode = True

class ProfileUpdateFristname(BaseModel):
    firstname: str

class ProfileResponseFirstname(BaseModel):
    firstname: str
    uuid: str

class ProfileUpdateName(BaseModel):
    name: str

class ProfileResponseName(BaseModel):
    name: str
    uuid: str

class ProfileUpdateAge(BaseModel):
    age: int

class ProfileResponseAge(BaseModel):
    age: int
    uuid: str

class ProfileUpdateWeight(BaseModel):
    weight: int

class ProfileResponseWeight(BaseModel):
    weight: int
    uuid: str


class ProfileUpdateHeight(BaseModel):
    height: int

class ProfileResponseHeight(BaseModel):
    height: int
    uuid: str
