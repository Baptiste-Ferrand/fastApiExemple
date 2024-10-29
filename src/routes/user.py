from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.user import UserCreate, UserResponse
from src.controllers.user import create_user
from src.database import get_db

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=201)
async def create_user_route(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(user, db)