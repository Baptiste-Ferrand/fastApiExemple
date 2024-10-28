from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.user import UserCreate
from src.services.user import save_user_to_db


async def create_user(user: UserCreate, db: AsyncSession):
    if user.age < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="L'âge ne peut pas être négatif."
        )

    if user.weight < 0: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="le poids ne peux pas être négatif."
        )

    if not user.firstname or not user.name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Le prénom et le nom sont requis."
        )

    try:
        return await save_user_to_db(user, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la création de l'utilisateur : {str(e)}"
        )
