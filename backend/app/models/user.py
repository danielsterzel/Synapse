from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy import UUID, Boolean, DateTime, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship

from app.core.database import Base

class User(Base):
    __tablename__ = "user"
    __table_args__ = (
        UniqueConstraint("email", name="uq_user_email"),
        UniqueConstraint("username", name="uq_user_username")
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
        )
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    

    oauth_accounts: Mapped[list["OAuthAccount"]] = relationship("OAuthAccount", back_populates="user")

class OAuthAccount(Base):
    __tablename__ = "oauth_account"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True))
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="oauth_accounts")