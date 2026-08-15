from typing import TYPE_CHECKING

from datetime import datetime, UTC

if TYPE_CHECKING:
    from users.models import User
    from posts.models import Post
    from likes.models import Like

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from sqlalchemy import (
    ForeignKey,
    String,
    DateTime
)

from infrastructure.db.base import Base


class Comment(Base):
    __tablename__ = "comments"
    
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    body: Mapped[str] = mapped_column(
        String(1000)
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC)
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    post_id: Mapped[int] = mapped_column(
        ForeignKey("posts.id")
    )

    parent_comment_id: Mapped[int | None] = mapped_column(
        ForeignKey("comments.id"),
        nullable=True
    )

    user: Mapped["User"] = relationship(
        back_populates="comments"
    )

    post: Mapped["Post"] = relationship(
        back_populates="comments"
    )

    parent_comment: Mapped["Comment | None"] = relationship(
        remote_side=[id],
        back_populates="replies",
        foreign_keys=[parent_comment_id]
    )

    replies: Mapped[list["Comment"]] = relationship(
        back_populates="parent_comment",
        foreign_keys=[parent_comment_id],
        cascade="all, delete-orphan"
    )

    likes: Mapped[list["Like"]] = relationship(
        back_populates="comment"
    )

