from fastapi import HTTPException, status
from uuid import UUID

def validate_user_data(user_data):
    errors = []
    if user_data.age < 0:
        errors.append("age can't be negative.")
    if user_data.weight < 0:
        errors.append("weight can't be negative.")
    if not user_data.firstname:
        errors.append("firstname is required.")
    if not user_data.name:
        errors.append("name is required.")

    if errors:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="; ".join(errors)
        )

def validate_uuid(user_uuid: str):
    try:
        UUID(user_uuid)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid UUID format"
        )