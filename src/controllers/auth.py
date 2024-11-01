from fastapi import HTTPException, status
from src.schemas.auth import LoginUser, TokenResponse, LoginResponse
from src.services.auth import authenticate_user
from src.utils.security import verify_password
from src.utils.jwt_handler import create_access_token
from sqlalchemy.ext.asyncio import AsyncSession

async def login_user(user_credentials: LoginUser, db: AsyncSession) -> TokenResponse:
    user = await authenticate_user(user_credentials.email, db)
    if not user or not verify_password(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    token_data = {"sub": str(user.uuid), "email": user.email}
    access_token = create_access_token(data=token_data)
    
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=LoginResponse(uuid=str(user.uuid), email=user.email)
    )
