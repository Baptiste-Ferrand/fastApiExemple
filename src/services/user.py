from sqlalchemy.ext.asyncio import AsyncSession
from src.models.user import User
from src.schemas.user import UserCreate
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from uuid import UUID


import logging
logging.basicConfig(level=logging.INFO)

async def save_user_to_db(user_data: UserCreate, db: AsyncSession):
    new_user = User(
        firstname=user_data.firstname,
        name=user_data.name,
        age=user_data.age,
        weight=user_data.weight
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def delete_user_from_db(user_uuid: str, db: AsyncSession):
    result = await db.execute(select(User).where(User.uuid == UUID(user_uuid)))
    user = result.scalars().first()
    if not user:
        raise NoResultFound("User not found")
    
    await db.delete(user)
    await db.commit()

async def fetch_user_from_db(user_uuid: str, db: AsyncSession):
    result = await db.execute(select(User).where(User.uuid == UUID(user_uuid)))
    return result.scalars().first()

async def fetch_all_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()