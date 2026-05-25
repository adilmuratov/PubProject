from sqlalchemy.orm import (
    Mapped,
    mapped_collumn,
    relationship
)

from infrastructure.db.base import Base
from users.models import User
from posts.models import Post
from likes.models import Like


class Comment(Base):
    id: Mapped[int] = mapped_collumn(
        primary_key=True
    )

    body: Mapped[str] = mapped_collumn(
        String(1000)
    )

    user_id: Mapped[int] = mapped_collumn(
        Foreignkey("user.id"),
        unique=True 
    )

    post_id: Mapped[int] = mapped_collumn(
        ForeignKey("user.id"),
        unique=True
    )

    parent_comment_id: Mapped[int | None] = mapped_column(
        ForeignKey("comments.id"),
        nullable=True
    )

    like_id: Mapped[int] = mapped_collumn(
        ForeignKey("user.id"),
        unique=True 
    )

    user: Mapped["User"] = relationship(
        back_populates="posts"
    )

    post: Mapped["Post"] = relationship(
        back_populates="posts"
    )

    parent_comment: Mapped["Comment | None"] = relationship(
        remote_side=[id],
        back_populates="replies"
    )

    replies: Mapped[list["Comment"]] = relationship(
        back_populates="parent_comment",
        cascade="all, delete-orphan"
    )

    likes: Mapped[list["Like"]] = relationship(
        back_populates="posts"
    )

