from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.profile import ProfileResponseHeight, ProfileUpdateFristname, ProfileResponseFirstname, ProfileResponseName, ProfileUpdateHeight, ProfileUpdateName, ProfileUpdateAge, ProfileResponseAge, ProfileUpdateWeight, ProfileResponseWeight
from src.controllers.profile import update_firstname_profile, update_name_profile, update_weight_profile, update_age_profile, update_height_profile
from src.database import get_db
from src.utils.jwt_handler import verify_access_token


router = APIRouter()

@router.patch("/firstname", response_model=ProfileResponseFirstname, status_code=200)
async def update_firstname_route(
    profile_update: ProfileUpdateFristname,
    token: dict = Depends(verify_access_token),
    db: AsyncSession = Depends(get_db)
):
   return await update_firstname_profile(token, profile_update, db)

@router.patch("/name", response_model=ProfileResponseName, status_code=200)
async def update_name_route(
   profile_update: ProfileUpdateName,
   token: dict = Depends(verify_access_token),
   db: AsyncSession = Depends(get_db)
):
   return await update_name_profile(token, profile_update, db)

@router.patch("/age", response_model=ProfileResponseAge, status_code=200)
async def update_name_route(
   profile_update: ProfileUpdateAge,
   token: dict = Depends(verify_access_token),
   db: AsyncSession = Depends(get_db)
):
   return await update_age_profile(token, profile_update, db)

@router.patch("/weight", response_model=ProfileResponseWeight, status_code=200)
async def update_name_route(
   profile_update: ProfileUpdateWeight,
   token: dict = Depends(verify_access_token),
   db: AsyncSession = Depends(get_db)
):
   return await update_weight_profile(token, profile_update, db)


@router.patch("/height", response_model=ProfileResponseHeight, status_code=200)
async def update_height_route(
    profile_update: ProfileUpdateHeight,
    token: dict = Depends(verify_access_token),
   db: AsyncSession = Depends(get_db)
):
    return await update_height_profile(token, profile_update, db)