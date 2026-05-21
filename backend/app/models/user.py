from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy import (
    UUID,
    Boolean,
    DateTime,
    String,
    UniqueConstraint,
    ForeignKey,
    Enum as ENUM,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.core.database import Base
from enum import Enum

"""
 UNIQUE constraints create indexes in PostgreSQL
"""


class OAuthProvider(str, Enum):
    GOOGLE = "google"
    GITHUB = "github"


class User(Base):
    __tablename__ = "user"
    __table_args__ = (
        UniqueConstraint("email", name="uq_user_email"),
        UniqueConstraint("username", name="uq_user_username"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(1024), nullable=False)

    email: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, server_default="true"
    )

    oauth_accounts: Mapped[list["OAuthAccount"]] = relationship(
        "OAuthAccount", back_populates="user", cascade="all, delete-orphan"
    )


class OAuthAccount(Base):
    __tablename__ = "oauth_account"
    __table_args__ = (
        UniqueConstraint(
            "provider", "provider_user_id", name="uq_oauth_provider_user_id"
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("user.id"), nullable=False, index=True
    )

    provider: Mapped[OAuthProvider] = mapped_column(ENUM(OAuthProvider), nullable=False)
    provider_user_id: Mapped[str] = mapped_column(String(100), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    user: Mapped["User"] = relationship("User", back_populates="oauth_accounts")
