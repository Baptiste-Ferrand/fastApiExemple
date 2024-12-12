from src.schemas.auth import LoginUser, TokenResponse, LoginResponse
from src.services.auth import authenticate_user
from src.utils.exception_handle import handle_auth_veryfication
from src.utils.jwt_handler import create_access_token
from sqlalchemy.ext.asyncio import AsyncSession


async def login_user(user_credentials: LoginUser, db: AsyncSession) -> TokenResponse:
    user = await authenticate_user(user_credentials.email, db)
    handle_auth_veryfication(user, user_credentials.password)

    roles_names = [role.name for role in user.roles]
    token_data = {"sub": str(user.uuid), "email": user.email, "roles": roles_names}
    access_token = create_access_token(data=token_data)

    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=LoginResponse(uuid=str(user.uuid), email=user.email, roles=roles_names),
    )
