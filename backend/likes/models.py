from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship
)

from infrastructure.db.base import Base


class Like(Base):
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        unique=True
    )

    post_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        unique=True
    )

    user: Mapped["User"] = mapped_column(
        back_populates="likes"
    )

    post: Mapped["User"] = mapped_column(
        back_populates="likes"
    )