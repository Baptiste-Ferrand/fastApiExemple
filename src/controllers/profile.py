from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.profile import ProfileUpdateFristname, ProfileResponseFirstname, ProfileResponseName, ProfileUpdateName, ProfileUpdateAge, ProfileResponseAge, ProfileUpdateWeight, ProfileResponseWeight,ProfileResponseHeight, ProfileUpdateHeight 
from src.services.profile import update_firstname_profile_in_db, update_name_profile_in_db, update_age_profile_in_db, update_weight_profile_in_db, update_height_profile_in_db
from sqlalchemy.exc import NoResultFound
from src.validators.profile import validate_user_data, validate_uuid
from sqlalchemy.exc import IntegrityError


async def update_firstname_profile(token: dict, ProfileUpdate: ProfileUpdateFristname, db: AsyncSession):
    user_id= token.get("sub")

    try: 
        update_profile = await update_firstname_profile_in_db(user_id, ProfileUpdate.firstname, db)
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

async def update_name_profile(token: dict, ProfileUpdate: ProfileUpdateName, db: AsyncSession):
    user_id= token.get("sub")

    try: 
        update_profile = await update_name_profile_in_db(user_id, ProfileUpdate.name, db)
        return ProfileResponseName(
            name= update_profile.name,
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

async def update_age_profile(token: dict, ProfileUpdate: ProfileUpdateAge, db: AsyncSession):
    user_id= token.get("sub")

    try: 
        update_profile = await update_age_profile_in_db(user_id, ProfileUpdate.age, db)
        return ProfileResponseAge(
            age= update_profile.age,
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

async def update_weight_profile(token: dict, ProfileUpdate: ProfileUpdateWeight, db: AsyncSession):
    user_id= token.get("sub")

    try: 
        update_profile = await update_weight_profile_in_db(user_id, ProfileUpdate.weight, db)
        return ProfileResponseWeight(
            weight= update_profile.weight,
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


async def update_height_profile(token: dict, ProfileUpdate: ProfileUpdateHeight, db: AsyncSession):
    user_id= token.get("sub")

    try: 
        update_profile = await update_height_profile_in_db(user_id, ProfileUpdate.height, db)
        return ProfileResponseHeight(
            height= update_profile.height,
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