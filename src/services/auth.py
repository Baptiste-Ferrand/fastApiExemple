from src.models.user import User
from src.models.role import Role
from src.schemas.auth import LoginResponse
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

async def authenticate_user(email: str, db: AsyncSession):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalars().first()
    
    role_result = await db.execute(
        select(Role).where(Role.id == user.role_id)
    )
    user_role = role_result.scalars().first()

    print(user_role.name, "mon user loging")
    return user, user_role
