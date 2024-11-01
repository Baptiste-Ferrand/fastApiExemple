from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.profile import ProfileUpdateFristname, ProfileResponseFirstname
from src.services.profile import update_firstname_profile_in_db
from sqlalchemy.exc import NoResultFound
from src.validators.profile import validate_user_data, validate_uuid
from sqlalchemy.exc import IntegrityError



# async def create_user(user: UserCreate, db: AsyncSession):
#     validate_user_data(user)
#     try:
#         return await save_user_to_db(user, db)
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"error when creating user : {str(e)}"
#         )

# async def delete_user(user_uuid: str, db: AsyncSession):
#     validate_uuid(user_uuid)
#     try:
#         await delete_user_from_db(user_uuid, db)
#     except NoResultFound:
#         raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail="User not found"
#             )
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"error when deleting user : {str(e)}"
#         )


# async def get_user(user_uuid: str, db: AsyncSession):
#     validate_uuid(user_uuid)
#     try:
#         user = await fetch_user_from_db(user_uuid, db)
#     except NoResultFound:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User not found"
#         )
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"error when getting user : {str(e)}"
#         )
#     return user

# async def get_all_users(db: AsyncSession):
#     try:
#         users = await fetch_all_users(db)
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"error when getting users: {str(e)}"
#         )
#     return users

# async def update_user(user_uuid: str, user_data: UserCreate, db: AsyncSession):
#     validate_user_data(user_data)
#     validate_uuid(user_uuid)
#     try:
#         return await update_user_in_db(user_uuid, user_data, db)
#     except NoResultFound:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User not found"
#         )
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"Error updating user: {str(e)}"
#         )

async def update_firstname_profile(token: dict, ProfileUpdateFristname: ProfileUpdateFristname, db: AsyncSession):
    user_id= token.get("sub")

    try: 
        update_profile = await update_firstname_profile_in_db(user_id, ProfileUpdateFristname.firstname, db)
        return ProfileResponseFirstname(
            firstname= update_profile.firstname,
            uuid= str(update_profile.uuid)
        )
            
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't be the same"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating email: {str(e)}"
        )