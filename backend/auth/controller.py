from jwt.exceptions import InvalidTokenError

from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.ext.asyncio import AsyncSession

from users.schemas import UserData
import utils as auth_utils
from dependencies.validate_auth import validate_auth_user
from dependencies.current_active_auth import get_current_active_auth


router = APIRouter()


@router.post("/login/", response_model=TokenInfo)
async def auth_user(
    user: UserData = Depends(validate_auth_user)
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


@jwt_router.get("/users/me/")
def auth_user_check_self_info(
    user: UserSchema = Depends(get_current_active_auth)
):
    return {
        "username": user.username
    }