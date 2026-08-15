from jwt.exceptions import InvalidTokenError

from fastapi import Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession

from users.user import User
from users.dependencies import get_user_by_id, check_existing_user_by_username
from users.schemas import UserUpdate

from users import repository as user_repository
from userstyles import repository as userstyle_repository
from profiles import repository as profile_repository
from posts import repository as post_repository
from likes import repository as like_repository
from comments import repository as comment_repository

from auth import utils as auth_utils


async def get_users(
    session: AsyncSession
):
    return await user_repository.get_users(session=session)


async def create_user(
    user_in: UserCreate,
    session: AsyncSession
):
    await check_existing_user_by_username(
        session=session,
        username=user_in.username
    )

    user = await user_repository.create_user(
        session=session,
        user_in=user_in
    )

    userstyle = await userstyle_repository.create_userstyle(
        session=session,
        user=user
    )


async def get_user(
    session: AsyncSession,
    user_id: int
):
    return await get_user_by_id(
        session=session,
        user_id=user_id
    )


async def update_user(
    session: AsyncSession,
    user_update: UserUpdate,
    user: User
): 
    return await user_repository.update_user(
        session=session,
        user=user,
        user_update=user_update
    )


async def change_password(
    session: AsyncSession,
    old_password: str,
    new_password: str,
    user: User
):
    if not auth_utils.validate_password(
        old_password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid username or password"
        )
    
    if auth_utils.validate_password(
        new_password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="new password can't be similar to old password"
        )

    user_update = {
        password_hash: new_password
    }
    
    await user_repository.update_user(
        session=session,
        user=user,
        user_update=user_update
    )


async def delete_user(
    session: AsyncSession,
    user: User
):
    await userstyle_repository.delete_userstyle(
        session=session,
        userstyle=user.userstyle
    )

    await profile_repository.delete_profile(
        session=session,
        profile=user.profile
    )

    await user_repository.delete_user(
        session=session,
        user=user
    )

    await post_repository.delete_all_posts_of_user(
        session=session,
        user=user
    )

    await like_repository.delete_all_likes_of_user(
        session=session,
        user=user
    )

    await comment_repository.delete_all_comments_of_user(
        session=session,
        user=user
    )

