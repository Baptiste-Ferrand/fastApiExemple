from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.user import UserCreate, UserResponse
from src.controllers.user import create_user, delete_user, get_user, get_all_users, update_user
from src.database import get_db

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=201)
async def create_user_route(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(user, db)

@router.delete("/{user_uuid}", status_code=204)
async def delete_user_route(user_uuid: str, db: AsyncSession = Depends(get_db)):
    await delete_user(user_uuid, db)

@router.get("/{user_uuid}", response_model=UserResponse, status_code=200)
async def get_user_route(user_uuid: str, db: AsyncSession = Depends(get_db)):
    return await get_user(user_uuid, db)

@router.get("/", response_model=List[UserResponse], status_code=200)
async def get_all_users_route(db: AsyncSession = Depends(get_db)):
    return await get_all_users(db)

@router.put("/{user_uuid}", response_model=UserResponse, status_code=200)
async def update_user_route(user_uuid: str, user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await update_user(user_uuid, user, db)