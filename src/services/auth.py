from src.models.user import User
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

async def authenticate_user(email: str, db: AsyncSession):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalars().first()
    return user  
