from sqlalchemy.ext.asyncio import AsyncSession
from src.models.profile import Profile
from src.schemas.profile import ProfileCreate
from src.services.user import get_user_by_id
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from uuid import UUID



async def create_profile_for_user_from_db(user_id: str, profile_data: ProfileCreate, db: AsyncSession):
    print("firstame", profile_data.firstname)
    new_profile  = Profile(
        firstname=profile_data.firstname,
        name=profile_data.name,
        age=profile_data.age,
        weight=profile_data.weight,
        user_id=user_id
    )
    db.add(new_profile )
    await db.commit()
    await db.refresh(new_profile )
    return new_profile 

# async def delete_user_from_db(user_uuid: str, db: AsyncSession):
#     result = await db.execute(select(User).where(User.uuid == UUID(user_uuid)))
#     user = result.scalars().first()
#     if not user:
#         raise NoResultFound("User not found")
    
#     await db.delete(user)
#     await db.commit()

# async def fetch_user_from_db(user_uuid: str, db: AsyncSession):
#     result = await db.execute(select(User).where(User.uuid == UUID(user_uuid)))
#     user = result.scalars().first()
#     if not user:
#         raise NoResultFound("User not found")
#     return user

# async def fetch_all_users(db: AsyncSession):
#     result = await db.execute(select(User))
#     return result.scalars().all()

# async def update_user_in_db(user_uuid: str, user_data: ProfileCreate, db: AsyncSession):
#     result = await db.execute(select(User).where(User.uuid == UUID(user_uuid)))
#     user = result.scalars().first()
    
#     if not user:
#         raise NoResultFound("User not found")
    
#     user.firstname = user_data.firstname
#     user.name = user_data.name
#     user.age = user_data.age
#     user.weight = user_data.weight
    
#     db.add(user)
#     await db.commit()
#     await db.refresh(user)
#     return user

async def update_firstname_profile_in_db(user_id: str, firstname: str, db: AsyncSession):
    user_profile = await get_profil_by_user_id(user_id, db)
    if not user_profile:
        raise Exception("the profile doesn't existe.")
    
    user_profile.firstname = firstname
    await db.commit()
    await db.refresh(user_profile)
    return user_profile

async def get_profil_by_user_id(user_id: str, db: AsyncSession):
    result= await db.execute(select(Profile).where(user_id == user_id))
    return result.scalars().first()