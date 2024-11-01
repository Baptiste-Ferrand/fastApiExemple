from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.profile import ProfileUpdateFristname, ProfileResponseFirstname
from src.controllers.profile import update_firstname_profile
from src.database import get_db
from src.utils.jwt_handler import verify_access_token


router = APIRouter()

# @router.post("/", response_model=UserResponse, status_code=201)
# async def create_user_route(user: UserCreate, db: AsyncSession = Depends(get_db)):
#     return await create_user(user, db)

# @router.delete("/{user_uuid}", status_code=204)
# async def delete_user_route(user_uuid: str, db: AsyncSession = Depends(get_db)):
#     await delete_user(user_uuid, db)

# @router.get("/{user_uuid}", response_model=UserResponse, status_code=200)
# async def get_user_route(user_uuid: str, db: AsyncSession = Depends(get_db)):
#     return await get_user(user_uuid, db)

# @router.get("/", response_model=List[UserResponse], status_code=200)
# async def get_all_users_route(db: AsyncSession = Depends(get_db)):
#     return await get_all_users(db)

# @router.put("/{user_uuid}", response_model=UserResponse, status_code=200)
# async def update_user_route(user_uuid: str, user: UserCreate, db: AsyncSession = Depends(get_db)):
#     return await update_user(user_uuid, user, db)

@router.patch("/firstname", response_model=ProfileResponseFirstname, status_code=200)
async def update_firstname_route(
    profile_update: ProfileUpdateFristname,
    token: dict = Depends(verify_access_token),
    db: AsyncSession = Depends(get_db)
):
   return await update_firstname_profile(token, profile_update, db)