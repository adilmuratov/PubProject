from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from users.user import User

from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship
)
from sqlalchemy import String, ForeignKey

from infrastructure.db.base import Base


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        unique=True
    )

    user: Mapped["User"] = relationship(
        back_populates="profile"
    )

    description: Mapped[str] = mapped_column(
        String(200)
    )
