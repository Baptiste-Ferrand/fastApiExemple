from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_db
from src.schemas.user import TokenResponse
from src.schemas.auth import LoginUser
from src.controllers.auth import login_user

router = APIRouter()

@router.post("/login", response_model=TokenResponse, status_code=200)
async def login(
    user_credentials: LoginUser,
    db: AsyncSession = Depends(get_db)
):
    return await login_user(user_credentials, db)
