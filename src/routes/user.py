from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.user import UserCreate, TokenResponse, UserUpdateEmail
from src.controllers.user import create_user, update_user_email
from src.database import get_db
from src.utils.jwt_handler import verify_access_token

router = APIRouter()

@router.post("/", response_model=TokenResponse, status_code=201)
async def create_user_route(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(user, db)

@router.put("/email", response_model=TokenResponse, status_code=200)
async def update_user_email_route(
    user_update: UserUpdateEmail, 
    token: dict = Depends(verify_access_token), 
    db: AsyncSession = Depends(get_db)
):
    return await update_user_email(user_update, token, db)