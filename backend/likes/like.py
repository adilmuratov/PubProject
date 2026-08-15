from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from users.user import User
    from posts.post import Post
    from comments.comment import Comment

from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship
)
from sqlalchemy import (
    ForeignKey, 
    UniqueConstraint,
    CheckConstraint
)

from infrastructure.db.base import Base


class Like(Base):
    __tablename__ = "likes"
    
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    post_id: Mapped[int] = mapped_column(
        ForeignKey("posts.id"),
        nullable=True
    )
    
    comment_id: Mapped[int] = mapped_column(
        ForeignKey("comments.id"),
        nullable=True
    )

    user: Mapped["User"] = relationship(
        back_populates="likes"
    )

    post: Mapped["Post | None"] = relationship(
        back_populates="likes"
    )

    comment: Mapped["Comment | None"] = relationship(
        back_populates="likes"
    )

    __table_args__ = (
        UniqueConstraint("user_id", "post_id"),
        UniqueConstraint("user_id", "comment_id"),
        CheckConstraint(
            "(post_id IS NOT NULL AND comment_id IS NULL) OR "
            "(post_id IS NULL AND comment_id IS NOT NULL)",
            name="check_like_target",
        )
    )