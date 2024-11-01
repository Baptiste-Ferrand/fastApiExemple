from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.user import UserCreate, TokenResponse, UserUpdateEmail, UserUpdatePassword, UserDeleted
from src.controllers.user import create_user, update_user_email, update_user_password, delete_user
from src.database import get_db
from src.utils.jwt_handler import verify_access_token

router = APIRouter()

@router.post("/", response_model=TokenResponse, status_code=201)
async def create_user_route(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(user, db)

@router.patch("/email", response_model=TokenResponse, status_code=200)
async def update_user_email_route(
    user_update: UserUpdateEmail, 
    token: dict = Depends(verify_access_token), 
    db: AsyncSession = Depends(get_db)
):
    return await update_user_email(user_update, token, db)

@router.patch("/password", status_code=204)
async def update_user_password_route(
    user_update: UserUpdatePassword, 
    token: dict = Depends(verify_access_token), 
    db: AsyncSession = Depends(get_db)
):
    await update_user_password(token, user_update.current_password, user_update.new_password, user_update.confirm_password, db)

@router.post("/delete", status_code=204)
async def delete_user_route(
    user_update: UserDeleted,
    token: dict = Depends(verify_access_token), 
    db: AsyncSession = Depends(get_db)
):
    await delete_user(token, user_update.current_password, db)
