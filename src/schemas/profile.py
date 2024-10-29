from pydantic import BaseModel
from uuid import UUID

class ProfileCreate(BaseModel):
    firstname: str
    name: str
    age: int
    weight: int

class ProfileResponse(BaseModel):
    uuid: UUID
    firstname: str
    name: str
    age: int
    weight: int
    user_id: UUID

    class Config:
        orm_mode = True
