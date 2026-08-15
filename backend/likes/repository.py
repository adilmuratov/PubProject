from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from likes.like import Like
    from posts.post import Post
    from comments.comment import Comment

from sqlalchemy import select, func
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


async def get_count_likes_by_post(
    session: AsyncSession,
    post_id: int
) -> int:
    stmt = select(func.count(Like.id)).join(Post).where(Post.id == post_id)
    result: Result = await session.execute(stmt)
    count_likes = result.scalars()
    return count_likes


async def get_likes_by_post(
    session: AsyncSession,
    post_id: int
) -> list[Like]:
    stmt = select(Like).join(Post).where(Post.id == post_id).order_by(Like.id)
    result: Result = await session.execute(stmt)
    likes = result.scalars().all()
    return likes


async def get_count_likes_by_comment(
    session: AsyncSession,
    comment_id: int
) -> int:
    stmt = select(func.count(Like.id)).join(Comment).where(Comment.id == comment_id)
    result: Result = await session.execute(stmt)
    count_likes = result.scalars()
    return count_likes


async def get_likes_by_comment(
    session: AsyncSession,
    comment_id: int
) -> list[Like]:
    stmt = select(Like).join(Comment).where(Comment.id == comment_id).order_by(Like.id)
    result: Result = await session.execute(stmt)
    likes = result.scalars().all()
    return likes


async def get_like_by_post_and_user(
    session: AsyncSession,
    post_id: int,
    user_id: int
) -> Optional[Like]:
    stmt = select(Like).where(Like.post_id == post_id, Like.user_id == user_id)
    result: Result = await session.execute(stmt)
    like = result.scalars().all()


async def get_like_by_comment_and_user(
    session: AsyncSession,
    comment_id: int,
    user_id: int
) -> Optional[Like]:
    stmt = select(Like).where(Like.comment_id == comment_id, Like.user_id == user_id)
    result: Result = await session.execute(stmt)
    like = result.scalars().all()
    

async def create_like_to_post(
    session: AsyncSession,
    post_id: int,
    user_id: int
):
    like = Like(
        post_id=post_id,
        user_id=user_id
    )
    session.add(like)
    await session.commit()


async def create_like_to_comment(
    session: AsyncSession,
    comment_id: int,
    user_id: int
):
    like = Like(
        comment_id=comment_id,
        user_id=user_id
    )
    session.add(like)
    await session.commit()


async def delete_like_to_post(
    session: AsyncSession,
    like: Like
):
    await session.delete(like)
    await session.commit()


async def delete_like_to_comment(
    session: AsyncSession,
    like: Like
):
    await session.delete(like)
    await session.commit()


async def delete_all_likes_of_user(
    session: AsyncSession,
    user: User
):
    await session.delete(Like).where(Like.user == user)
    await session.commit()
