from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy import UUID, Boolean, DateTime, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship

from backend.app.core.database import Base

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
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(1024), nullable=False)

    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    created_at: Mapped[datetime] = mapped_column(DateTime())


    oauth_accounts: Mapped[list["OAuthAccount"]] = relationship("OAuthAccount", back_populates="user")

class OAuthAccount(Base):
    __tablename__ = "oauth_account"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="oauth_accounts")