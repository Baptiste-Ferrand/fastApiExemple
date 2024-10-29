from sqlalchemy.ext.asyncio import AsyncSession
from src.models.user import User

async def save_user_to_db(email: str, hashed_password: str, db: AsyncSession):
    new_user = User(email=email, password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
