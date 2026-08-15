from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from posts.post import Post
    from users.user import User
    from comments.comment import Comment

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from comments.schemas import CommentRead
from comments.schemas import CommentCreate

from likes import service as like_service

from comments import repository as comment_repository
from posts import post as post_repository


async def get_comments_by_post(
    session: AsyncSession,
    post_id: int
) -> list[CommentRead]:
    comments: list[Comment] = await comment_repository.get_comments_by_post(
        session=session,
        post_id=post_id
    )

    comments_read = []

    for comment in comments:
        replies = [CommentRead.model_validate(reply) for reply in comment.replies]

        likes_count = like_service.get_count_likes_by_comment(
            session=session,
            comment_id=comment.id
        )

        comments_read.append(
            CommentRead(
                body=comment.body,
                created_at=comment.created_at,
                updated_at=comment.updated_at,
                repleis=replies,
                likes_count=likes_count
            )
        )
    
    return comments_read


async def get_comment_by_id(
    session: AsyncSession,
    comment_id: int
) -> CommentRead:
    comment = await comment_repository.get_comment_by_id(
        session=session,
        comment_id=comment_id
    )

    replies = [CommentRead.model_validate(reply) for reply in comment.replies]

    likes_count = like_service.get_count_likes_by_comment(
        session=session,
        comment_id=comment_id
    )

    return CommentRead(
        body=comment.body,
        created_at=comment.created_at,
        updated_at=comment.updated_at,
        repleis=replies,
        likes_count=likes_count
    )


async def create_comment_to_post(
    session: AsyncSession,
    comment_create: CommentCreate,
    user: User,
    post_id: int
) -> CommentRead:
    post = post_repository.get_post_by_id(
        session=session,
        post_id=post_id
    )
    
    comment = await comment_repository.create_comment(
        session=session,
        comment_create=comment_create,
        user=user,
        post=post,
        parent_comment=None
    )

    return CommentRead(
        body=comment.body,
        created_at=comment.created_at,
        updated_at=comment.updated_at,
        replies=[],
        likes_count=0
    )


async def create_comment_to_comment(
    session: AsyncSession,
    comment_create: CommentCreate,
    user: User,
    parent_comment_id: int
) -> CommentRead:
    parent_comment = comment_repository.get_comment_by_id(
        session=session,
        comment_id=comment_id
    )

    post = parent_comment.post
    
    comment = await comment_repository.create_comment(
        session=session,
        comment_create=comment_create,
        user=user,
        post=post,
        parent_comment=parent_comment
    )
    
    return CommentRead(
        body=comment.body,
        created_at=comment.created_at,
        updated_at=comment.updated_at,
        replies=[],
        likes_count=0
    )


async def update_comment(
    session: AsyncSession,
    comment_id: int,
    comment_update: CommentUpdate,
    user: User
) -> CommentRead:
    comment = await comment_repository.get_comment_by_id(
        session=session,
        comment_id=comment_id
    )
    
    if comment.user != user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    updated_comment = await comment_repository.update_comment(
        session=session,
        comment=comment,
        comment_update=comment_update
    )

    replies = [CommentRead.model_validate(reply) for reply in comment.replies]

    likes_count = like_service.get_count_likes_by_comment(
        session=session,
        comment_id=comment_id
    )

    return CommentRead(
        body=updated_comment.body,
        created_at=updated_comment.created_at,
        updated_at=updated_comment.updated_at,
        repleis=replies,
        likes_count=likes_count
    )


async def delete_comment(
    session: AsyncSession,
    user: User,
    comment_id: int
):
    comment = await comment_repository.get_comment_by_id(
        session=session,
        comment_id=comment_id
    )

    if comment.user != user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    await comment_repository.delete_comment(
        session=session,
        comment=comment
    )
