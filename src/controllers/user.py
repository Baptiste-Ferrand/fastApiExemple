from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.user import TokenResponse, UserCreate, UserUpdateEmail, UserResponse
from src.services.user import save_user_to_db, update_email_in_db, get_user_by_id, update_password_in_db, delte_user_in_db
from src.utils.security import hash_password, verify_password
from src.validators.user import validate_passwords, validate_email_format
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from src.models.user import User
from src.utils.jwt_handler import create_access_token


async def create_user(user: UserCreate, db: AsyncSession):

    validate_passwords(user.password, user.confirm_password)
    validate_email_format(user.email)
    
    existing_user = await db.execute(select(User).where(User.email == user.email))
    if existing_user.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already in use."
        )
    
    hashed_password = hash_password(user.password)
    
    try:
        user_data = await save_user_to_db(user.email, hashed_password, db)
        user_data.uuid = str(user_data.uuid)
        token_data = {"sub": user_data.uuid, "email": user_data.email}
        access_token = create_access_token(data=token_data)
        
        return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=user_data
    )
    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already in use."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating user: {str(e)}"
        )

async def update_user_email(user_update: UserUpdateEmail, token: dict, db: AsyncSession):
    user_id = token.get("sub")
    
    validate_email_format(user_update.new_email)

    try:
        updated_user = await update_email_in_db(user_id, user_update.new_email, db)
        token_data = {"sub": str(updated_user.uuid), "email": updated_user.email}
        access_token = create_access_token(data=token_data)
        
        return TokenResponse(
            access_token=access_token,
            token_type="bearer",
            user=UserResponse(
                uuid=str(updated_user.uuid),
                email=updated_user.email
            )
        )
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already in use."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating email: {str(e)}"
        )

async def update_user_password(token: dict, current_password: str, new_password: str, confirm_password: str, db: AsyncSession):
    user_id = token.get("sub")
    validate_passwords(new_password, confirm_password)
    
    user = await get_user_by_id(user_id, db)
    
    if not user or not verify_password(current_password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect."
        )
    
    if verify_password(new_password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New password can't be the actual password"
        )

    hashed_new_password = hash_password(new_password)

    try:
        await update_password_in_db(user_id, hashed_new_password, db) 
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating password: {str(e)}"
        )

async def delete_user(token: dict, current_password: str, db: AsyncSession):
    user_id = token.get("sub")
    
    user = await get_user_by_id(user_id, db)

    if not user or not verify_password(current_password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect."
        )
    
    try:
        await delte_user_in_db(user_id, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating password: {str(e)}"
        ) 