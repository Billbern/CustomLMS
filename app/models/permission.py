from __future__ import annotations
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class Permission(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    controller: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
    access: Mapped[str] = mapped_column(String(10), nullable=False)
