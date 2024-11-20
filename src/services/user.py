from sqlalchemy.ext.asyncio import AsyncSession
from src.models.user import User
from src.models.role import Role
from sqlalchemy.future import select
from src.schemas.user import UserResponse


async def save_user_to_db(email: str, hashed_password: str, db: AsyncSession):
    user_role_result = await db.execute(
        select(Role).filter_by(name="user")
    )
    user_role = user_role_result.scalar()
    
    new_user = User(
        email=email,
        password=hashed_password,
        roles= [user_role])
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    for role in new_user.roles:
        print(f"dans service Role: {role.name}")
    return UserResponse(
        uuid= str(new_user.uuid),
        email= new_user.email,
        roles= [role.name for role in new_user.roles]
    )


async def update_email_in_db(user_id: str, new_email: str, db: AsyncSession):
    user = await get_user_by_id(user_id, db)

    if not user:
        raise Exception("User not found.")

    user.email = new_email
    await db.commit()
    await db.refresh(user)
    return user


async def update_password_in_db(user_id: str, hashed_password: str, db: AsyncSession):
    user = await get_user_by_id(user_id, db)
    if not user:
        raise Exception("User not found.")

    user.password = hashed_password
    await db.commit()
    await db.refresh(user)


async def get_user_by_id(user_id: str, db: AsyncSession):
    result = await db.execute(select(User).where(User.uuid == user_id))
    return result.scalars().first()


async def delte_user_in_db(user_id: str, db: AsyncSession):
    user = await get_user_by_id(user_id, db)

    if not user:
        raise Exception(detail="User not found")

    await db.delete(user)
    await db.commit()
