from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.profile import (
    ProfileUpdateFristname,
    ProfileResponseFirstname,
    ProfileResponseName,
    ProfileUpdateName,
    ProfileUpdateAge,
    ProfileResponseAge,
    ProfileUpdateWeight,
    ProfileResponseWeight,
    ProfileResponseHeight,
    ProfileUpdateHeight,
)
from src.services.profile import (
    update_firstname_profile_in_db,
    update_name_profile_in_db,
    update_age_profile_in_db,
    update_weight_profile_in_db,
    update_height_profile_in_db,
)
from src.utils.exception_handle import handle_exception


async def update_firstname_profile(
    token: dict, ProfileUpdate: ProfileUpdateFristname, db: AsyncSession
):
    user_id = token.get("sub")

    try:
        update_profile = await update_firstname_profile_in_db(
            user_id, ProfileUpdate.firstname, db
        )
        return ProfileResponseFirstname(
            firstname=update_profile.firstname, uuid=str(update_profile.uuid)
        )

    except Exception as e:
        handle_exception(e, "Error when udpate firstname")


async def update_name_profile(
    token: dict, ProfileUpdate: ProfileUpdateName, db: AsyncSession
):
    user_id = token.get("sub")

    try:
        update_profile = await update_name_profile_in_db(
            user_id, ProfileUpdate.name, db
        )
        return ProfileResponseName(
            name=update_profile.name, uuid=str(update_profile.uuid)
        )

    except Exception as e:
        handle_exception(e, "Error when udpate name")
    


async def update_age_profile(
    token: dict, ProfileUpdate: ProfileUpdateAge, db: AsyncSession
):
    user_id = token.get("sub")

    try:
        update_profile = await update_age_profile_in_db(user_id, ProfileUpdate.age, db)
        return ProfileResponseAge(age=update_profile.age, uuid=str(update_profile.uuid))

    except Exception as e:
        handle_exception(e, "Error when udpate age")


async def update_weight_profile(
    token: dict, ProfileUpdate: ProfileUpdateWeight, db: AsyncSession
):
    user_id = token.get("sub")

    try:
        update_profile = await update_weight_profile_in_db(
            user_id, ProfileUpdate.weight, db
        )
        return ProfileResponseWeight(
            weight=update_profile.weight, uuid=str(update_profile.uuid)
        )

    except Exception as e:
        handle_exception(e, "Error when udpate weight")


async def update_height_profile(
    token: dict, ProfileUpdate: ProfileUpdateHeight, db: AsyncSession
):
    user_id = token.get("sub")

    try:
        update_profile = await update_height_profile_in_db(
            user_id, ProfileUpdate.height, db
        )
        return ProfileResponseHeight(
            height=update_profile.height, uuid=str(update_profile.uuid)
        )

    except Exception as e:
        handle_exception(e, "Error when udpate height")
