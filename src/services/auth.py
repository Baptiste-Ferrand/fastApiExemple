from src.models.user import User
from src.models.role import Role
from src.schemas.auth import LoginResponse
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload


async def authenticate_user(email: str, db: AsyncSession) -> User:
    # Don't forget to eager load your wanted relationships in async mode, because lazy loading is not supported
    user_query = select(User).where(User.email == email).options(selectinload(User.roles))
    user = (await db.execute(user_query)).scalars().first()

    print([role.name for role in user.roles], "mon user loging")
    return user
