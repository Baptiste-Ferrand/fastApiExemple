from pydantic import BaseModel
from uuid import UUID

class UserCreate(BaseModel):
    firstname: str
    name: str
    age: int
    weight: int

class UserResponse(BaseModel):
    uuid: UUID
    firstname: str
    name: str
    age: int
    weight: int

    class Config:
        orm_mode = True  # Permet à Pydantic de lire les objets SQLAlchemy
