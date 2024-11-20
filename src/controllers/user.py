from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.profile import ProfileCreate
from src.schemas.user import TokenResponse, UserCreate, UserUpdateEmail, UserResponse
from src.services.user import (
    save_user_to_db,
    update_email_in_db,
    get_user_by_id,
    update_password_in_db,
    delte_user_in_db,
)
from src.services.profile import create_profile_for_user_from_db
from src.utils.security import hash_password
from src.validators.user import validate_passwords, validate_email_format
from sqlalchemy.future import select
from src.models.user import User
from src.utils.jwt_handler import create_access_token
from src.utils.exception_handle import (
    handle_exception,
    handle_current_password,
    handle_new_password,
    handle_new_email,
    handle_user_not_found,
)


async def create_user(user: UserCreate, db: AsyncSession):

    validate_passwords(user.password, user.confirm_password)
    validate_email_format(user.email)

    existing_user = await db.execute(select(User).where(User.email == user.email))
    if existing_user.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already in use."
        )

    hashed_password = hash_password(user.password)

    try:
        user_data = await save_user_to_db(user.email, hashed_password, db)
        user_data.uuid = str(user_data.uuid)

        profile_data = ProfileCreate()
        await create_profile_for_user_from_db(user_data.uuid, profile_data, db)

        token_data = {"sub": user_data.uuid, "email": user_data.email, "role": user_data.role}
        access_token = create_access_token(data=token_data)

        return TokenResponse(
            access_token=access_token, token_type="bearer", user=user_data
        )

    except Exception as e:
        handle_exception(e, "Error when create user")


async def update_user_email(
    user_update: UserUpdateEmail, token: dict, db: AsyncSession
):
    user_id = token.get("sub")
    role= token.get("role")

    validate_email_format(user_update.new_email)

    user = await get_user_by_id(user_id, db)
    handle_user_not_found(user)
    handle_new_email(user, user_update.new_email)

    try:
        updated_user = await update_email_in_db(user_id, user_update.new_email, db)
        token_data = {
            "sub": str(updated_user.uuid),
            "email": updated_user.email,
            "role": role,
        }
        access_token = create_access_token(data=token_data)

        return TokenResponse(
            access_token=access_token,
            token_type="bearer",
            user=UserResponse(uuid=str(updated_user.uuid), email=updated_user.email, role= role),
        )
    except Exception as e:
        handle_exception(e, "Error when update email")


async def update_user_password(
    token: dict,
    current_password: str,
    new_password: str,
    confirm_password: str,
    db: AsyncSession,
):
    user_id = token.get("sub")
    validate_passwords(new_password, confirm_password)

    user = await get_user_by_id(user_id, db)

    handle_current_password(user, current_password)

    handle_new_password(user, new_password)

    hashed_new_password = hash_password(new_password)

    try:
        await update_password_in_db(user_id, hashed_new_password, db)
    except Exception as e:
        handle_exception(e, "Error when update password")


async def delete_user(token: dict, current_password: str, db: AsyncSession):
    user_id = token.get("sub")

    user = await get_user_by_id(user_id, db)

    handle_current_password(user, current_password)

    try:
        await delte_user_in_db(user_id, db)
    except Exception as e:
        handle_exception(e, "Error when delete user")
