from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from comments.comment import Comment
    from users.user import User
    from posts.post import Post

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from comments.schemas import CommentCreate, CommentUpdate


async def get_comments(
    session: AsyncSession
) -> list[Comment]:
    stmt = select(Comment).order_by(Comment.id)
    result: Result = await session.execute(stmt)
    comments = result.scalar().all()
    return comments

    
async def get_comments_by_post(
    session: AsyncSession,
    post_id: int
) -> list[Comment]:
    stmt = select(Comment).where(Comment.post_id == post.id)
    result: Result = await session.execute(stmt)
    comments = result.scalars().all()
    return comments


async def get_comment_by_id(
    session: AsyncSession,
    comment_id: int
) -> Optional[Comment]:
    return await session.get(Comment, comment_id)


async def create_comment(
    session: AsyncSession,
    comment_create: CommentCreate,
    user: User,
    post: Post,
    parent_comment: Comment
) -> Comment:
    comment = Comment(
        body=comment_create.body,
        user=user,
        post=post,
        parent_comment=parent_comment
    )

    session.add(comment)
    await session.commit()

    return comment


async def update_comment(
    session: AsyncSession,
    comment: Comment,
    comment_update: CommentUpdate
) -> Comment:
    for name, value in comment_update.model_dump(exclude_unset=partial).items():
        setattr(comment, name, value)
    await session.commit()

    return comment


async def delete_comment(
    session: AsyncSession,
    comment: Comment
) -> None:
    await session.delete(comment)
    await session.commit()


async def delete_all_comments_of_user(
    session: AsyncSession,
    user: User
) -> None:
    await session.delete(Comment).where(Comment.user == user)
    await session.commit()