from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.controllers.role import (
    create_role,
    update_role,
    delete_role,
    get_roles,
    get_one_roles,
)
from src.schemas.role import RoleCreate, RoleUpdate, RoleResponse
from src.database import get_db
from src.utils.jwt_handler import verify_access_token

router = APIRouter()

@router.post("/", response_model=RoleResponse, status_code=201)
async def create_role_route(
    role: RoleCreate,
    token: dict = Depends(verify_access_token), 
    db: AsyncSession = Depends(get_db),
):
    return await create_role(token, db, role)

@router.put("/{role_id}", response_model=RoleResponse, status_code=200)
async def update_role_route(
    role: RoleUpdate,
    token: dict = Depends(verify_access_token), 
    db: AsyncSession = Depends(get_db),
):  
    return await update_role(token, db, role)

@router.delete("/{role_id}", status_code=204)
async def delete_role_route(
    token: dict = Depends(verify_access_token), 
    db: AsyncSession = Depends(get_db),
): 
    return await delete_role(token, db)

@router.get("/", response_model=list[RoleResponse], status_code=200)
async def get_role_route(
    token: dict = Depends(verify_access_token), 
    db: AsyncSession = Depends(get_db),
):
    return await get_roles(token, db)

@router.get("/{role_id}", response_model=list[RoleResponse], status_code=200)
async def get_one_roles_route(
    token: dict = Depends(verify_access_token), 
    db: AsyncSession = Depends(get_db),
):
    return await get_one_roles(token, db)