from sqlalchemy.ext.asyncio import AsyncSession
from src.models.profile import Profile
from src.schemas.profile import ProfileCreate
from sqlalchemy.future import select


async def create_profile_for_user_from_db(
    user_id: str, profile_data: ProfileCreate, db: AsyncSession
):
    print("firstame", profile_data.firstname)
    new_profile = Profile(
        firstname=profile_data.firstname,
        name=profile_data.name,
        age=profile_data.age,
        weight=profile_data.weight,
        height=profile_data.height,
        user_id=user_id,
    )
    db.add(new_profile)
    await db.commit()
    await db.refresh(new_profile)
    return new_profile


async def get_profil_by_user_id(user_id: str, db: AsyncSession):
    result = await db.execute(select(Profile).where(Profile.user_id == user_id))
    profile =  result.scalars().first()
    return profile


async def update_firstname_profile_in_db(
    user_id: str, firstname: str, db: AsyncSession
):
    user_profile = await get_profil_by_user_id(user_id, db)
    if not user_profile:
        raise Exception("the profile doesn't existe.")

    user_profile.firstname = firstname
    await db.commit()
    await db.refresh(user_profile)
    return user_profile


async def update_name_profile_in_db(user_id: str, name: str, db: AsyncSession):
    user_profile = await get_profil_by_user_id(user_id, db)
    if not user_profile:
        raise Exception("the profile doesn't existe.")

    user_profile.name = name
    await db.commit()
    await db.refresh(user_profile)
    return user_profile


async def update_age_profile_in_db(user_id: str, age: int, db: AsyncSession):
    user_profile = await get_profil_by_user_id(user_id, db)
    if not user_profile:
        raise Exception("the profile doesn't existe.")

    user_profile.age = age
    await db.commit()
    await db.refresh(user_profile)
    return user_profile


async def update_weight_profile_in_db(user_id: str, weight: int, db: AsyncSession):
    user_profile = await get_profil_by_user_id(user_id, db)
    if not user_profile:
        raise Exception("the profile doesn't existe.")

    user_profile.weight = weight
    await db.commit()
    await db.refresh(user_profile)
    return user_profile


async def update_height_profile_in_db(user_id: str, height: int, db: AsyncSession):
    user_profile = await get_profil_by_user_id(user_id, db)
    if not user_profile:
        raise Exception("the profile doesn't existe.")

    user_profile.height = height
    await db.commit()
    await db.refresh(user_profile)
    return user_profile
