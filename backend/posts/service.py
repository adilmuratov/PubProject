from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from posts.schemas import PostCreate, PostUpdate
from posts.post import Post

from posts import repository


async def get_posts(
    session: AsyncSession
) -> list[Post]:
    return await repository.get_posts(
        session=session
    )


async def get_post_by_id(
    session: AsyncSession,
    post_id: int
) -> Optional[Post]:
    return await repository.get_post_by_id(
        session=session,
        post_id=post_id
    )


async def create_post(
    session: AsyncSession,
    user: User,
    post_create: PostCreate
) -> Post:
    return await repository.create_post(
        session=session,
        user=user,
        post_create=post_create
    )


async def update_post(
    session: AsyncSession,
    user: User,
    post_id: int,
    post_update: PostUpdate
) -> Post:
    post = await repository.get_post_by_id(
        session=session,
        post_id=post_id
    )
    
    if post.user != user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    return await repository.update_post(
        session=session,
        post=post,
        post_update=post_update
    )


async def delete_post(
    session: AsyncSession,
    user: User,
    post_id: int
):
    post = await repository.get_post_by_id(
        session=session,
        post_id=post_id
    )

    if post.user != user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    return await repository.delete_post(
        session=session,
        post=post
    )
