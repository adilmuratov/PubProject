from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from likes import repository


async def get_count_likes_by_post(
    session: AsyncSession,
    post_id: int,
) -> int:
    return repository.get_count_likes_by_post(
        session=session,
        post_id=post_id
    )


async def get_count_likes_by_comment(
    session: AsyncSession,
    comment_id: int,
) -> int:
    return repository.get_count_likes_by_comment(
        session=session,
        comment_id=comment_id_id
    )


async def create_like_to_post(
    session: AsyncSession,
    post_id: int,
    user: User
):
    await repository.create_like_to_post(
        session=session,
        post_id=post_id,
        user_id=user.id
    )


async def create_like_to_comment(
    session: AsyncSession,
    comment_id: int,
    user: User
):
    await repository.create_like_to_comment(
        session=session,
        comment_id=comment_id,
        user_id=user.id
    )


async def delete_like_to_post(
    session: AsyncSession,
    post_id: int,
    user: User
):
    like = await repository.get_like_by_post_and_user(
        session=session,
        post_id=post_id,
        user_id=user.id
    )

    await repository.delete_like_to_post(
        like=like
    )


async def delete_like_to_comment(
    session: AsyncSession,
    comment_id: int,
    user: User
):
    like = await repository.get_like_by_comment_and_user(
        session=session,
        comment_id=comment_id,
        user_id=user.id
    )

    await repository.delete_like_to_comment(
        like=like
    )
