from sqlalchemy.ext.asyncio import AsyncSession
from src.models.user import User
from src.schemas.user import UserCreate

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
