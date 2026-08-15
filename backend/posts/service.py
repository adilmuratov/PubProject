from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from posts.post import Post
    from users.user import User

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from posts.schemas import PostRead, PostCreate, PostUpdate

from posts import repository as post_repository
from likes import service as like_service


# async def get_posts_by_user(        
#     session: AsyncSession
# ) -> list[PostRead]:
#     posts: list[Post] = await repository.get_posts(
#         session=session
#     )

#     return [PostRead.model_validate(post) for post in posts]


async def get_post_by_id(
    session: AsyncSession,
    post_id: int
) -> PostRead:
    post = await repository.get_post_by_id(
        session=session,
        post_id=post_id
    )

    likes_count = await like_service.get_count_likes_by_post(
        session=session,
        post_id=post_id
    )

    return PostRead(
        body=post.body,
        created_at=post.created_at,
        updated_at=post.updated_at,
        likes_count=likes_count
    )


async def create_post(
    session: AsyncSession,
    user: User,
    post_create: PostCreate
) -> PostRead:
    post = await repository.create_post(
        session=session,
        user=user,
        post_create=post_create
    )

    likes_count = await like_service.get_count_likes_by_post(
        session=session,
        post_id=post_id
    )

    return PostRead(
        body=post.body,
        created_at=post.created_at,
        updated_at=post.updated_at,
        likes_count=likes_count
    )


async def update_post(
    session: AsyncSession,
    user: User,
    post_id: int,
    post_update: PostUpdate
) -> PostRead:
    user_post = await repository.get_post_by_id(
        session=session,
        post_id=post_id
    )
    
    if user_post.user != user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    post = await repository.update_post(
        session=session,
        post=user_post,
        post_update=post_update
    )

    likes_count = await like_service.get_count_likes_by_post(
        session=session,
        post_id=post_id
    )

    return PostRead(
        body=post.body,
        created_at=post.created_at,
        updated_at=post.updated_at,
        likes_count=likes_count
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
    
    await repository.delete_post(
        session=session,
        post=post
    )


async def create_like_to_post(
    session: AsyncSession,
    user: User,
    post_id: int
):
    like_service.create_like_to_post(
        session=session,
        user=user,
        post_id=post_id
    )


async def delete_like_to_post(
    session: AsyncSession,
    user: User,
    post_id: int
):
    like_service.delete_like_to_post(
        session=session,
        user=user,
        post_id=post_id
    )
