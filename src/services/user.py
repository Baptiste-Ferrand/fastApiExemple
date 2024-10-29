from sqlalchemy.ext.asyncio import AsyncSession
from src.models.user import User
from sqlalchemy.future import select

async def save_user_to_db(email: str, hashed_password: str, db: AsyncSession):
    new_user = User(email=email, password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def update_email_in_db(user_id: str, new_email: str, db: AsyncSession):
    result = await db.execute(select(User).where(User.uuid == user_id))
    user = result.scalars().first()
    
    if not user:
        raise Exception("User not found.")
    
    user.email = new_email
    await db.commit()
    await db.refresh(user)
    return user
