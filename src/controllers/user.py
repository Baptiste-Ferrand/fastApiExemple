from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.user import UserCreate
from src.services.user import save_user_to_db
from src.utils.security import hash_password
from src.validators.user import validate_passwords, validate_email_format
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from src.models.user import User


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
        return user_data
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