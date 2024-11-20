from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.role_service import create_role, update_role, delete_role, get_roles
from src.schemas.role import RoleCreate, RoleUpdate
from src.utils.exception_handle import handle_role_verification

async def create_role(token: dict, db: AsyncSession, role: RoleCreate):

    handle_role_verification(token)
    return await create_role(db, role)

async def update_role(db: AsyncSession, role_id: int, role: RoleUpdate):
    updated_role = await update_role(db, role_id, role)
    if not updated_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return updated_role

async def delete_role(db: AsyncSession, role_id: int):
    deleted_role = await delete_role(db, role_id)
    if not deleted_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return deleted_role

async def get_roles(db: AsyncSession):
    return await get_roles(db)

async def get_one_role(db: AsyncSession):
    return await get_one_role(db)