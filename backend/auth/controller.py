from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.ext.asyncio import AsyncSession

from users.user import User
from auth import utils as auth_utils
from auth.schemas import TokenInfo
from auth.dependencies.validate_auth import validate_auth_user
from auth.dependencies.get_current_user import get_current_user


router = APIRouter()


@router.post("/login/", response_model=TokenInfo)
async def auth_user(
    user: User = Depends(validate_auth_user)
):
    jwt_payload = {
        "sub": user.username,
        "username": user.username
    }

    token = auth_utils.encode_jwt(jwt_payload)

    return TokenInfo(
        acces_token=token,
        token_type="Bearer"
    )


@router.get("/users/me/")
def auth_user_check_self_info(
    user: User = Depends(get_current_user)
):
    return {
        "username": user.username
    }