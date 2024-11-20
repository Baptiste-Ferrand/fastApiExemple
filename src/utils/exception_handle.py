from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from src.utils.security import verify_password


def handle_exception(e: Exception, context: str):
    if isinstance(e, IntegrityError):
        detail = "Contrainte d'intégrité violée. " + (f"Contexte: {context}")
        if "email" in str(e.orig):
            detail = "Email already used"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )
    elif isinstance(e, ValueError): 
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Error of validation : {str(e)}"
        )
    elif isinstance(e, KeyError):  
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erreur forgoten key : {str(e)}"
        )
    elif isinstance(e, PermissionError):  
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"No authorization : {str(e)}"
        )
    else:  
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{context} : {str(e)}"
        )

def handle_current_password(user, current_password):
      if not user or not verify_password(current_password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect."
        )

def handle_new_password(user, new_password):
    if verify_password(new_password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New password can't be the actual password"
        )

def handle_new_email(user, new_email):
    if user.email == new_email :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current email is already the same"
        )

def handle_auth_veryfication(user, password):
    if not user or not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

def handle_role_verification(token: dict, allowed_roles: list[str]):
    user_roles = token.get("roles", [])  
    if not any(role in allowed_roles for role in user_roles):
        raise HTTPException(status_code=403, detail="Not authorized for this action.")
    

def handle_user_not_found(user):
     if not user:
        raise HTTPException(status_code=404, detail="User not found.")