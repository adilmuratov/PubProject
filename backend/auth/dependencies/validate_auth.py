from fastapi import (
    status,
    HTTPException,
    Depends
)
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.db.db_helper import db_helper
from users import repository 


async def validate_auth_user(
    username: str,
    password: str,
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid username or password"
    )

    user = await repository.get_user_by_username(
        session=session,
        username=username
    )
    
    if not user:
        raise unauthed_exc

    if not auth_utils.validate_password(
        password=password,
        hashed_password=user.password
    ):
        raise unauthed_exc

    return user
