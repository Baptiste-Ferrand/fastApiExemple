from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.user import UserCreate
from src.services.user import save_user_to_db, delete_user_from_db, fetch_all_users, fetch_user_from_db
from sqlalchemy.exc import NoResultFound


async def create_user(user: UserCreate, db: AsyncSession):
    if user.age < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="age is require."
        )

    if user.weight < 0: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="weight can't be negatif."
        )

    if not user.firstname or not user.name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="name or first name are require."
        )

    try:
        return await save_user_to_db(user, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"error when creating user : {str(e)}"
        )

async def delete_user(user_uuid: str, db: AsyncSession):
    try:
        await delete_user_from_db(user_uuid, db)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid UUID format"
        )
    except NoResultFound:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"error when deleting user : {str(e)}"
        )


async def get_user(user_uuid: str, db: AsyncSession):
    try:
        user = await fetch_user_from_db(user_uuid, db)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid UUID format"
        )
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"error when getting user : {str(e)}"
        )
    return user

async def get_all_users(db: AsyncSession):
    try:
        users = await fetch_all_users(db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"error when getting users: {str(e)}"
        )
    return users