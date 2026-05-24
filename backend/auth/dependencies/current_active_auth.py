from jwt.exceptions import InvalidTokenError

from fastapi import (
    status,
    HTTPException,
    Depends
)

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.db.db_helper import db_helper
from schemas import UserData
import utils as auth_utils
from users import repository


http_bearer = HTTPBearer()
 

def get_current_token_payload(
    credentials: HTTPAuthorizationCredentials = Depends(http_bearer)
) -> dict:
    token = credentials.credentials
    try:
        payload = auth_utils.decode_jwt(
            token=token
        )
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid username or password"
        )
    return payload


async def get_current_active_auth(
    session: AsyncSession = Depends(db_helper.session_dependency),
    payload: dict = Depends(get_current_token_payload)
) -> UserData:
    username: str | None = payload.get("sub")
    
    user = await repository.get_user_by_username(
        session=session,
        username=username
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="user not found"
        )

    return user
    
