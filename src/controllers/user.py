from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.user import UserCreate
from src.services.user import save_user_to_db

async def create_user(user: UserCreate, db: AsyncSession):
    return await save_user_to_db(user, db)
